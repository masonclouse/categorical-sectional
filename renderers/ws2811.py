"""
Simple driver of the WS2811/ addressable RGB LED lights.
Based on the AdaFruit code by Tony DiCola
License: Public Domain
"""

from __future__ import division
import lib.local_debug as local_debug
import neopixel
import board


class Ws2811Renderer(object):
    def __init__(self, pixel_count, gpio_port, rgb_order='GRB'):
        """
        Create a new controller for the WS2811 based lights

        Arguments:
            pixel_count {int} -- The total number of neopixels
            gpio_port {string} -- The GPIO port the neopixels are on. Will be eval'd with board module
        """

        self.pixel_count = pixel_count
        self.rgb_order = rgb_order

        if not local_debug.is_debug():
            # Specify a hardware SPI connection on /dev/spidev0.0:
            self.pixels = neopixel.NeoPixel(eval("board.D{}".format(gpio_port)), pixel_count, auto_write=False)

            # Clear all the pixels to turn them off.
            self.pixels.fill((0, 0, 0))
            self.pixels.show()

    def set_led(self, pixel_index, color):
        """
        Sets the given airport to the given color

        Arguments:
            pixel_index {int or int array} -- The index of the pixel to set
            color {int array} -- The RGB (0-255) array of the color we want to set.
        """

        if not local_debug.is_debug():

            if (type(pixel_index) is not list):
                pixel_index = [pixel_index]

            for p in pixel_index:
                if (self.rgb_order == 'GRB'):
                    self.pixels[p] = (color[1], color[0], color[2])
                elif (self.rgb_order is 'RGB'):
                    self.pixels[p] = (color[0], color[1], color[2])

            self.pixels.show()
