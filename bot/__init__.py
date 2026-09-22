import os
import asyncio
from time import time
from logging import getLogger, FileHandler, StreamHandler, INFO, ERROR, basicConfig

# Disable Pyrogram sync wrapper to fix Python 3.14 import crash
os.environ["PYROGRAM_NO_SYNC"] = "1"

from uvloop import install

# Install uvloop policy and set event loop
install()
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

basicConfig(format="[%(asctime)s] [%(levelname)s] - %(message)s",
            datefmt="%d-%b-%y %I:%M:%S %p",
            handlers=[FileHandler('log.txt'), StreamHandler()],
            level=INFO)

getLogger("aiohttp").setLevel(ERROR)
getLogger("pyrogram").setLevel(ERROR)
getLogger("aiohttp.web").setLevel(ERROR)

LOGGER = getLogger(__name__)
StartTime = time()

__version__ = "1.2.6"
