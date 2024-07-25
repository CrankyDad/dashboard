#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
from waveshare_epd import epd7in5_V2
import time
import traceback

logging.basicConfig(level=logging.WARNING)

# This scipt is used to clean and put the display to sleep.
# Useful if the program crashes and leaves the display painted and powered.
# Substitute references to epd7in5_V2 to the correct display

try:
    logging.info("epd7in5_V2 init")
    epd = epd7in5_V2.EPD()
    
    logging.info("Before init and Clear")
    epd.init()
    logging.info("Done init")
    epd.Clear()
    logging.info("Done Clear")

    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5_V2.epdconfig.module_exit()
    exit()
