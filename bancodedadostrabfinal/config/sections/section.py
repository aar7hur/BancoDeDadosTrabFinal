import inspect
import re
from typing import Any, List, Tuple
from configparser import ConfigParser


class SectionConfig:
    """docstring for AbstractSection."""

    def toJSON(self) -> dict:
        obj = {}
        for attr in self.__getAttributes():
            obj[self.__convertNameParameter(attr[0])] = attr[1]

        return {
            "sectionName": getattr(self, "__sectionName__", "DEFAULT"),
            "config": obj,
        }

    def __dict__(self) -> dict:
        return self.toJSON()

    def __convertNameParameter(self, key: str) -> str:
        return "_".join(
            list(
                map(
                    lambda x: str(x).lower(),
                    re.split("(?=[A-Z])", key),
                )
            )
        )

    def __getAttributes(self) -> List[Tuple[str, Any]]:
        attributes = inspect.getmembers(
            self, lambda a: not (inspect.isroutine(a))
        )
        return [
            a
            for a in attributes
            if not (
                (a[0].startswith("__") and a[0].endswith("__"))
                or a[0].startswith("_")
            )
        ]

    def parse(self, section: ConfigParser):
        raise NotImplementedError()
