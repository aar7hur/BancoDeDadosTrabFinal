import inspect
from typing import Any, Dict, List, Tuple

from bancodedadostrabfinal.entities.interface import AbstractEntity
from util.operator import JSON, Datetime


class Entity(AbstractEntity):
    """
    This class represents an entity by itself.
    """

    def toJSON(self) -> Dict[str, Any]:
        """
        Converts an entity attributes to dict
        json serialized

        Returns:
            Dict: dico with all entity attributes
        """
        obj = {}
        for attr in self.__getAttributes():
            obj[attr[0]] = attr[1]
        return obj

    def __dict__(self) -> dict:
        return self.toJSON()

    @property
    def valid(self) -> bool:
        """
        Return if entity is valid ot not

        Return:
            bool: if true, entity is valid. Otherwise returns False
        """
        try:
            return self.validation()
        except Exception:
            return False

    def json(self) -> str:
        """
        Tries to convert all entity attributes to json

        Returns:
            str: string representation of a json response
        """
        try:
            return JSON.encode(self.toJSON())
        except NotImplementedError:
            obj = {}
            for attr in self.__getAttributes():
                obj[attr[0]] = attr[1]
            return JSON.encode(obj)

    def __getAttributes(self) -> List[Tuple[str, Any]]:
        """
        Get all attributes

        Returns:
            List[Tuple[str, Any]]: Return all atributes
        """
        attributes = inspect.getmembers(
            self,
            lambda a: not (inspect.isroutine(a)),
        )
        return [
            a
            for a in attributes
            if not (
                (a[0].startswith("__") and a[0].endswith("__"))
                or a[0].startswith("_")
                or a[0] == "valid"
            )
        ]

    def setCreatedAtToNow(self):
        self.createdAt = Datetime.now()

    def setUpdatedAtToNow(self):
        self.updatedAt = Datetime.now()

    def __str__(self) -> str:
        """
        Returns all attributes except those private

        Returns:
            str: str object description
        """
        values = {}

        for member in inspect.getmembers(self):
            # Ignores anything starting with underscore
            # (that is, private and protected attributes)
            if not member[0].startswith("_"):
                # Ignores methods
                if not inspect.ismethod(member[1]):
                    values[member[0]] = member[1]

        return JSON.encode(values, indent=4, sort_keys=True)
