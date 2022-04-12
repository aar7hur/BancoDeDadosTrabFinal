import base64
import datetime
import enum
import json
from uuid import UUID

from jsonschema import Draft7Validator, ValidationError


class JSON:
    """docstring for JSON."""

    @staticmethod
    def decode(value: str):
        return json.loads(value)

    @staticmethod
    def encode(o, **kwargs):
        return json.dumps(o, default=JSON.convert, **kwargs)

    @staticmethod
    def valid(value: str) -> bool:
        try:
            JSON.decode(value)
        except Exception:
            return False
        return True

    @staticmethod
    def convert(o):
        if isinstance(o, datetime.datetime) or isinstance(o, datetime.date):
            return o.isoformat()
        elif issubclass(o.__class__, enum.Enum):
            return o.value
        elif isinstance(o, UUID):
            return str(o) if o.int != 0 else None
        elif isinstance(o, bytes):
            return base64.b64encode(o).decode("utf-8")
        elif hasattr(o, "__dict__") and callable(getattr(o, "__dict__")):
            return o.__dict__()

    @staticmethod
    def decodeWithSchema(value: str, schema: dict) -> dict:
        """https://python-jsonschema.readthedocs.io/en/latest/

        http://json-schema.org/draft-07/schema#
        """
        try:
            d = JSON.decode(value)
            schema = Draft7Validator(schema)
            schema.validate(d)
        except json.decoder.JSONDecodeError as e:
            raise Exception(message=e.__str__())
        except ValidationError as e:
            raise Exception(message=f"{e.json_path} {e.message}. Schema: {e.schema}")
        except Exception:
            raise Exception

        return d
