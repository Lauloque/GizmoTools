# SPDX-License-Identifier: GPL-3.0-or-later

"""
Colored Logger for Blender Scripts and Extensions

A simple, plug-and-play colored logging solution for Blender that automatically
detects script/addon names and provides colorized console output.

Usage:
    from .bl_logger import logger

    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')

Compatible with Blender 4.2+ extensions and traditional addons.
"""

import logging
import os
import inspect
import bpy

# ANSI color codes - using bright colors for better visibility in Blender
COLORS = {
    'DEBUG': '\033[96m',       # Bright Cyan
    'INFO': '\033[92m',        # Bright Green
    'WARNING': '\033[93m',     # Bright Yellow
    'ERROR': '\033[91m',       # Bright Red
    'CRITICAL': '\033[95m'     # Bright Magenta
}
RESET = '\033[0m'


class ColoredFormatter(logging.Formatter):
    """
    Colors entire log lines based on log level.
    """

    def format(self, record):
        """
        Take the LogRecord instance containing log information and            
        returns it with ANSI color codes
        """
        formatted = super().format(record)
        if record.levelname in COLORS:
            return COLORS[record.levelname] + formatted + RESET
        return formatted


def _get_logger_name():
    """
    Returns appropriate logger name for Blender scripts and extensions.
    """
    if __package__:
        return __package__.split('.')[-1]
    basepath = os.path.basename(__file__)
    if basepath == '':
        return "Unnamed Logger"
    return basepath


# Create and configure the logger automatically
logger_name = _get_logger_name()
logger = logging.getLogger(logger_name)

# Only setup if not already configured - prevents duplicate handlers
if not logger.handlers:
    logger.setLevel(logging.CRITICAL + 1)
    handler = logging.StreamHandler()
    formatter = ColoredFormatter(
        "[%(name)s][%(levelname)-8s]  %(message)s (%(filename)s:%(lineno)d)"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False

# Clear any root logger handlers that might interfere
if logging.getLogger().handlers:
    logging.getLogger().handlers.clear()

# Example usage (remove these lines when using as a module)
# if __name__ == "__main__":
#     logger.debug('debug test message')
#     logger.info('info test message')
#     logger.warning('warning test message')
#     logger.error('error test message')
#     logger.critical('critical test message')