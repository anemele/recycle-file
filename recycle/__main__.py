import argparse
import glob
from itertools import chain

from .log import logger


def get_args():
    parser = argparse.ArgumentParser(__package__, description=__doc__)
    parser.add_argument(
        'file', nargs='+', type=str, help='Files or folders sent to the recycle bin'
    )

    args = parser.parse_args()
    logger.debug(f'{args=}')

    file: list[str] = args.file
    return file


files = chain.from_iterable(map(glob.iglob, get_args()))


# from .recycle import recycle

# for sth in files:
#     logger.info(f'done: {sth}')
#     recycle(sth)

from .send2trash import send2trash

send2trash(files)
