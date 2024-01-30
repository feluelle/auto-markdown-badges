"""Top-level package for auto-markdown-badges."""

from importlib.metadata import version
from os import getcwd
from os.path import dirname, join, realpath

__app_name__ = "auto-markdown-badges"
__version__ = version(__name__)
__location__ = realpath(join(getcwd(), dirname(__file__)))
