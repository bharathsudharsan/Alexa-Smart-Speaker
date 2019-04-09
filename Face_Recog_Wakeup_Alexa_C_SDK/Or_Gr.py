"""
Control pixel ring on ReSpeaker USB Mic Array
"""

import time

from pixel_ring import pixel_ring


if __name__ == '__main__':
    pixel_ring.change_pattern('echo')
    while True:

        try:
            pixel_ring.set_brightness(2)
            pixel_ring.set_color(rgb=None, r=50, g=205, b=50)
            time.sleep(3)
            pixel_ring.off()
            time.sleep(3)
            pixel_ring.set_color(rgb=None, r=255, g=165, b=0)
            time.sleep(3)
        except KeyboardInterrupt:
            break


    pixel_ring.off()
    time.sleep(1)


