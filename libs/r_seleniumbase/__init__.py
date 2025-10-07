import collections
import os
import pdb
import sys
from contextlib import suppress
from r_selenium import webdriver
from r_seleniumbase.__version__ import __version__
from r_seleniumbase.common import decorators  # noqa
from r_seleniumbase.common import encryption  # noqa
from r_seleniumbase.core import colored_traceback
from r_seleniumbase.core import sb_cdp  # noqa
from r_seleniumbase.core.browser_launcher import get_driver  # noqa
from r_seleniumbase.fixtures import js_utils  # noqa
from r_seleniumbase.fixtures import page_actions  # noqa
from r_seleniumbase.fixtures import page_utils  # noqa
from r_seleniumbase.fixtures import shared_utils
from r_seleniumbase.fixtures.base_case import BaseCase  # noqa
from r_seleniumbase.masterqa.master_qa import MasterQA  # noqa
from r_seleniumbase.plugins.sb_manager import SB  # noqa
from r_seleniumbase.plugins.driver_manager import Driver  # noqa
from r_seleniumbase.plugins.driver_manager import DriverContext  # noqa
from r_seleniumbase.undetected import cdp_driver  # noqa
from r_seleniumbase import translate  # noqa

with suppress(Exception):
    import colorama

with suppress(Exception):
    import pdbp  # (Pdb+) --- Python Debugger Plus

with suppress(Exception):
    shared_utils.fix_colorama_if_windows()
    colorama.init(autoreset=True)

if sys.version_info[0] < 3 and "pdbp" in locals():
    # With Python3, "import pdbp" is all you need
    for key in pdbp.__dict__.keys():
        # Replace pdb with pdbp
        pdb.__dict__[key] = pdbp.__dict__[key]
    if hasattr(pdb, "DefaultConfig"):
        # Here's how to customize Pdb+ options
        pdb.DefaultConfig.filename_color = pdb.Color.fuchsia
        pdb.DefaultConfig.line_number_color = pdb.Color.turquoise
        pdb.DefaultConfig.truncate_long_lines = False
        pdb.DefaultConfig.sticky_by_default = True
colored_traceback.add_hook()
os.environ["SE_AVOID_STATS"] = "true"  # Disable r_selenium Manager stats
webdriver.TouchActions = None  # Lifeline for past r_selenium-wire versions
if sys.version_info >= (3, 10):
    collections.Callable = collections.abc.Callable  # Lifeline for nosetests
del collections  # Undo "import collections" / Simplify "dir(r_seleniumbase)"
del os  # Undo "import os" / Simplify "dir(r_seleniumbase)"
del sys  # Undo "import sys" / Simplify "dir(r_seleniumbase)"
del webdriver  # Undo "import webdriver" / Simplify "dir(r_seleniumbase)"

version_list = [int(i) for i in __version__.split(".") if i.isdigit()]
version_tuple = tuple(version_list)
version_info = version_tuple  # noqa
