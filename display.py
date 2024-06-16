#from waveshare_epd import epd7in5_V2
import epaperdummy

import threading
import logging
from PIL import Image
from config import partial_frame_limit

logger = logging.getLogger(__name__)

#epd = epd4in2.EPD()
#epd = epd7in5_V2.EPD()
epd = epaperdummy.EPD()

class DrawTarget:
    def __init__(self):
        self.lock = threading.Lock()
        self.buffer = Image.new("1", (epd.width, epd.height), 1)
        self.width = epd.width
        self.height = epd.height
        self.partial_frames = 0
        self.partial_frame_limit = partial_frame_limit
        self.insleep = False
        epd.init()
        epd.Clear()

    def draw(self, image: Image, x: int = 0, y: int = 0):
        assert image.width + x <= epd.width
        assert image.height + y <= epd.height
        self.buffer.paste(image, (x, y))

    def flush(self, full = False, tosleep=True):
        logging.debug('Waiting for the lock in display')
# Just return if dislay is used
        if not self.lock.acquire(False):
            logger.debug('Unable to get lock for display. Skipping writing')
            return
        try:
            logger.debug('Got lock for display. Commence flushing')
            frame_buffer = epd.getbuffer(self.buffer)
            if (full == True) or (self.partial_frames >= self.partial_frame_limit):
                logger.debug('Drawing full frame. Status of sleep:' + str(self.insleep) )
                if self.insleep :
                    logger.debug('To wake up from sleep')
                    epd.init()
                    logger.debug('After wake up from sleep')
                    self.insleep = False
      #              epd.Clear()
                epd.display(frame_buffer)
                self.partial_frames = 0
            else:
                #_display_frame_quick(frame_buffer)
                self.partial_frames += 1

#Send display to sleep during normal operation to prolong its life
            if tosleep:
                logger.debug('Sending the display to sleep')
                epd.sleep()
                logger.debug('Sent display to sleep')
                self.insleep = True
 
 #Wrap up after flushing       
        finally:
            logging.debug('Released the lock for the display')
            self.lock.release()
            
    def clear_screen(self):
        if self.insleep :
            logger.debug('Wake up from sleep')
            epd.init()
            self.insleep = False
        epd.Clear()
        epd.sleep()
        self.insleep = True
