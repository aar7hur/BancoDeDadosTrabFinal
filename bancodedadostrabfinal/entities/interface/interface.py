"""
Implements abstract design pattern
"""

from typing import Any, Dict


class AbstractEntity:
    """
    This class is used as basis to create others entities.
    This is done in order to force all entities to have the same
    methods.
    """

    @property
    def valid(self) -> bool:
        raise NotImplementedError()

    def json(self) -> str:
        raise NotImplementedError()

    def toJSON(self) -> Dict[str, Any]:
        raise NotImplementedError()

    def validation(self) -> bool:
        raise NotImplementedError()

    @classmethod
    def create(cls) -> object:
        raise NotImplementedError()
