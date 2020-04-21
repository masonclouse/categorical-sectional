# Illuminates LEDs one at a time

import logging
import time
import configuration
import lib.local_debug as local_debug
import weather
import board
import neopixel
from lib.logger import Logger
from renderers import led, led_pwm, ws2811
from safe_logging import safe_log, safe_log_warning

python_logger = logging.getLogger("check_lights_wiring")
python_logger.setLevel(logging.DEBUG)
LOGGER = Logger(python_logger)

if not local_debug.IS_PI:
    safe_log_warning(LOGGER, "This is only able to run on a Raspberry Pi.")
    exit(0)

airport_render_config = configuration.get_airport_configs()
colors = configuration.get_colors()


def get_test_renderer():
    if configuration.get_mode() == configuration.WS2811:
        pixel_count = configuration.CONFIG["pixel_count"]
        port = configuration.CONFIG["gpio_port"]
        return ws2811.Ws2811Renderer(pixel_count, port)


renderer = get_test_renderer()

if __name__ == '__main__':

    index = 0
    total = int(input("Enter total number of LEDs: "))

    while index < total:
        renderer.set_led(index, colors[weather.GREEN])
        print("LED " + str(index + 1) + " now lit.")
        input("Press Enter to continue...")
        renderer.set_led(index, colors[weather.OFF])
        index += 1


