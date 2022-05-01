import os
from json import load
from json import JSONDecodeError


class ConfigError(Exception):
    """ Error that will be raised when there is a problem with the config file """

    def __init__(self, message="Error message was not set"):
        self.message = message

    def __str__(self) -> str:
        return self.message


class Config:

    def __init__(self, filename: str):
        """ Initializes the config object, raises ConfigError if the config file is not valid """
        if filename is None or str(filename).strip() == "":
            raise ConfigError("Filename cannot be empty")
        self.filename = str(filename).strip()

        if not self.__valid_file():
            raise ConfigError("Config file does not exist or is not readable")

        self.__valid_config_data(self.__load_config())

    def __valid_file(self) -> bool:
        """ Checks if the config file exists and is readable """
        return os.path.isfile(self.filename) and os.access(self.filename, os.R_OK)

    def __load_config(self) -> dict:
        try:
            with open(self.filename) as file:
                return load(file)
        except JSONDecodeError:
            raise ConfigError("Config file is not valid JSON")

    def __valid_config_data(self, data: dict) -> bool:
        """ Checks if the config file contains the required data """
