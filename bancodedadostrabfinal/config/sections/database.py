from configparser import ConfigParser
from dataclasses import dataclass

from .section import SectionConfig


@dataclass
class DatabaseConfig(SectionConfig):
    """docstring for DatabaseConfig."""

    __sectionName__: str = "DATABASE"

    driver: str = "postgresql"
    minConnection: int = 1
    maxConnection: int = 2
    user: str = "przkhstfjgjtat"
    password: str = (
        "a691af2f94dc98ce6860259f3aa03e31f5f850b96b49271737319ccf7fdf8e46"
    )
    host: str = "ec2-44-195-209-130.compute-1.amazonaws.com"
    port: int = 5432
    database: str = "d2tcnsjttf3ms8"

    def parse(self, section: ConfigParser):
        self.driver = section[self.__sectionName__]["driver"]
        self.minConnection = section[self.__sectionName__].getint(
            "min_connection"
        )
        self.maxConnection = section[self.__sectionName__].getint(
            "max_connection"
        )
        self.user = section[self.__sectionName__]["user"]
        self.password = section[self.__sectionName__]["password"]
        self.host = section[self.__sectionName__]["host"]
        self.port = section[self.__sectionName__].getint("port")
        self.database = section[self.__sectionName__]["database"]
