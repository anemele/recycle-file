from os import mkdir
from typing import Tuple

from win32comext.shell import shell, shellcon  # type: ignore


def recycle(filename: str) -> Tuple[int, bool]:
    # (0, False)
    return shell.SHFileOperation(
        (
            0,
            shellcon.FO_DELETE,
            filename,
            None,
            shellcon.FOF_SILENT | shellcon.FOF_ALLOWUNDO | shellcon.FOF_NOCONFIRMATION,
            None,
            None,
        )  # type: ignore
    )


def test():
    EXPECT = (0, False)
    open('0', 'w')
    assert recycle('0') == EXPECT
    mkdir('0')
    assert recycle('0') == EXPECT
