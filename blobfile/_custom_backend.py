# backends/base.py
from __future__ import annotations

import concurrent.futures
from typing import Iterator, Optional, Protocol

from blobfile._common import DirEntry, Stat

class CustomBackend(Protocol):
    """
    Abstraction layer required by blobfile.Context.
    One instance handles *all* URI schemes listed in ``schemes``.
    """

    def exists(self, path: str) -> bool: ...
    def isdir(self, path: str) -> bool: ...
    def scandir(self, path: str, *, shard_prefix_length: int) -> Iterator[DirEntry]: ...
    def makedirs(self, path: str) -> None: ...
    def remove(self, path: str) -> None: ...
    def rmtree(
        self,
        path: str,
        *,
        parallel: bool,
        parallel_executor: Optional[concurrent.futures.Executor] = None,
    ) -> None: ...

    def stat(self, path: str) -> Stat: ...
    def set_mtime(self, path: str, *, mtime: float, version: Optional[str] = None) -> bool: ...
