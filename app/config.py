import pathlib
import os

from dotenv import load_dotenv

load_dotenv()

PACKAGE_FOLDER = pathlib.Path(__file__).parent.parent
TARGETS_FOLDER = pathlib.Path(PACKAGE_FOLDER, 'targets')
PROXIES_FOLDER = pathlib.Path(PACKAGE_FOLDER, 'proxies')

HOST = os.environ['HOST']
PORT = os.environ['PORT']

if not TARGETS_FOLDER.exists():
    os.mkdir(TARGETS_FOLDER)
if not PROXIES_FOLDER.exists():
    os.mkdir(PROXIES_FOLDER)
