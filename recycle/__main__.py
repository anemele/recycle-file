import argparse
import glob
from itertools import chain

from .log import logger
from .recycle import recycle

parser = argparse.ArgumentParser(__package__, description=__doc__)
parser.add_argument(
    'file', nargs='+', type=str, help='Files or folders sent to the recycle bin'
)

args = parser.parse_args()
logger.debug(f'{args=}')

file: list[str] = args.file
for sth in chain.from_iterable(map(glob.iglob, file)):
    logger.info(f'done: {sth}')
    recycle(sth)
