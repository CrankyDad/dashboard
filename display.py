# From https://github.com/yawkat/inkstate
from lib.waveshare_epd import epd4in2
import logging
import time
import atexit
from PIL import Image

epd = epd4in2.EPD()

class DrawTarget:
    def __init__(self):
        self.buffer = Image.new("1", (epd.width, epd.height), 1)
        self._last_full_refresh = -1
        self.width = epd.width
        self.height = epd.height
        epd.init()

    def draw(self, image: Image, x: int = 0, y: int = 0):
        assert image.width + x <= 400
        assert image.height + y <= 300
        self.buffer.paste(image, (x, y))

    def flush(self):
        frame_buffer = epd.get_frame_buffer(self.buffer)
        t = int(time.time() / (30 * 60))
        print(t)
        if t > self._last_full_refresh:
            print("Drawing full frame")
            self._last_full_refresh = t
            epd.display_frame(frame_buffer)
        else:
            print("Drawing partial frame")
            _display_frame_quick(frame_buffer)

def _display_frame_quick(frame_buffer):
    epd.send_command(epd4in2.RESOLUTION_SETTING)
    epd.send_data(epd.width >> 8)
    epd.send_data(epd.width & 0xff)
    epd.send_data(epd.height >> 8)
    epd.send_data(epd.height & 0xff)

    epd.send_command(epd4in2.VCM_DC_SETTING)
    epd.send_data(0x12)

    epd.send_command(epd4in2.VCOM_AND_DATA_INTERVAL_SETTING)
    epd.send_command(0x97)  # VBDF 17|D7 VBDW 97  VBDB 57  VBDF F7  VBDW 77  VBDB 37  VBDR B7

    if frame_buffer is not None:
        epd.send_command(epd4in2.DATA_START_TRANSMISSION_2)
        for i in range(0, epd.width * epd.height // 8):
            epd.send_data(frame_buffer[i])
        epd.delay_ms(2)

    _set_lut_quick()
    epd.send_command(epd4in2.DISPLAY_REFRESH)
    epd.delay_ms(100)
    epd.wait_until_idle()


def _set_lut_quick():
    epd.send_command(epd4in2.LUT_FOR_VCOM)
    # lut_vcom0_quick
    for i in [0x00, 0x0E, 0x00, 0x00, 0x00, 0x01,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]:
        epd.send_data(i)
    epd.send_command(epd4in2.LUT_WHITE_TO_WHITE)
    # lut_ww_quick
    for i in [0xA0, 0x0E, 0x00, 0x00, 0x00, 0x01,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00]:
        epd.send_data(i)
    epd.send_command(epd4in2.LUT_BLACK_TO_WHITE)
    # lut_bw_quick
    for i in [0xA0, 0x0E, 0x00, 0x00, 0x00, 0x01,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00]:
        epd.send_data(i)
    epd.send_command(epd4in2.LUT_WHITE_TO_BLACK)
    # lut_wb_quick
    for i in [0x50, 0x0E, 0x00, 0x00, 0x00, 0x01,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00]:
        epd.send_data(i)
    epd.send_command(epd4in2.LUT_BLACK_TO_BLACK)
    # lut_bb_quick
    for i in [0x50, 0x0E, 0x00, 0x00, 0x00, 0x01,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00]:
        epd.send_data(i)

# Clear screen on exit
def clear_screen():
    image = Image.new("1", (epd.width, epd.height), 255)
    epd.display_frame(epd.get_frame_buffer(image))

atexit.register(clear_screen)