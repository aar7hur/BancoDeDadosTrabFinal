import uuid
from typing import Union


class UUID:
    """docstring for UUID."""

    @staticmethod
    def parseValueUUID(valueUUID: Union[str, uuid.UUID]) -> uuid.UUID:
        if isinstance(valueUUID, str):
            try:
                return uuid.UUID(valueUUID)
            except BaseException:
                raise AttributeError
        elif isinstance(valueUUID, uuid.UUID):
            return valueUUID
        else:
            return uuid.UUID(valueUUID)

    @staticmethod
    def verifyUUID(valueUUID: Union[str, uuid.UUID]) -> bool:
        """
        Verify UUID authenticity

        Args:
            valueUUID (Union[str, uuid.UUID]): uuid value

        Returns:
            bool: return true if uiid is valid. Otherwise returns False
        """
        try:
            UUID.parseValueUUID(valueUUID)
            return True
        except BaseException:
            return False

    @staticmethod
    def generateRandomUUID() -> uuid.UUID:
        return uuid.uuid4()
