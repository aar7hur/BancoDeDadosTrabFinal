import configparser
import os
from typing import List, Optional

from bancodedadostrabfinal.config.sections import (
    DatabaseConfig,
    SectionConfig,
)


class Config:
    """
    Class used to config application, database and server.
    """

    database: DatabaseConfig = DatabaseConfig()
    _configFile: Optional[str] = os.environ.get("CONFIG_FILE", "config.cfg")
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Since this class is called several times,
        implements singleton to not open and read the config file
        several times
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """
        Call setup in order to set ApplicationConfig, DatabaseConfig and also
        server config
        """
        self._sections: List[SectionConfig] = [
            self.application,
            self.database
        ]
        self.setUp()

    def setUp(self) -> None:
        """
        Configure application, database and server by reading a config file.
        """
        self.config = configparser.ConfigParser()

        # checks the existence of the config.cfg file and also
        # checks the permission to read it
        if os.path.exists(self._configFile) and os.access(
            self._configFile, os.R_OK
        ):
            self.config.read(self._configFile)

            # scan all section in order to populate their attributes
            for section in self._sections:
                section.parse(self.config)

        else:
            # if config.cfg was not found, creates it
            self.handleMissingConfigFile()

    def handleMissingConfigFile(self) -> None:
        """
        If config.cfg could not be found, create it.
        """
        for section in self._sections:
            sectionConfigs = section.toJSON()
            self.config[sectionConfigs["sectionName"]] = sectionConfigs[
                "config"
            ]

        with open(self._configFile, "w") as file_:
            self.config.write(file_)
