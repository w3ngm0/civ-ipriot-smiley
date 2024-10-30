from smiley import Smiley
import time
from blinkable import Blinkable


class Angry(Smiley, Blinkable):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws mouth feature on a smiley = angry frown
        """
        mouth = [50, 42, 43, 44, 45, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [9, 10, 18, 13, 14, 21]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.my_complexion
            self.pixels[pixel] = eyes

    def blink(self, delay=0.25):
        """
       Blinks the smiley's eyes once

        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
