import os

from typing import Optional

from dotenv import load_dotenv

from ._appdirs import get_env_filepath


def get_appname() -> str:
    return "artrade"

def load_envfile():
    envfile = get_env_filepath()
    if os.path.isfile(envfile):
        load_dotenv(envfile)

def get_env(key: str) -> Optional[str]:
    envfile = get_env_filepath()
    if os.path.isfile(envfile):
        load_dotenv(envfile)
        return os.getenv(key)
    return None


def set_env(key: str, value: str):
    envfile = get_env_filepath()
    if os.path.isfile(envfile):
