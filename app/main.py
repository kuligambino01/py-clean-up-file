from __future__ import annotations

import os
from inspect import Traceback


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: type, exc_val: BaseException | None, exc_tb: Traceback | None) -> None:
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
