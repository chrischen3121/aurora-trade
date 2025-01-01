import os

import platformdirs as pd
from dotenv import load_dotenv
from cryptography.fernet import Fernet


class AppContext:
    def __init__(self):
        self.appname = "artrade"
        appdirs = pd.PlatformDirs(appname=self.appname, ensure_exists=True)
        self.config_dir: str = appdirs.user_config_dir
        self.cache_dir: str = appdirs.user_cache_dir
        self.data_dir: str = appdirs.user_data_dir
        self.log_dir: str = appdirs.user_log_dir
        self.envfile: str = os.path.join(self.config_dir, ".env")

    @property
    def secret_key(self) -> bytes:
        load_dotenv(self.envfile)
        secret_key = os.getenv("ARTRADE_SECRET_KEY")
        if secret_key is None:
            secret_key = Fernet.generate_key()
            with open(self.envfile, "a") as f:
                f.write(f"ARTRADE_SECRET_KEY={secret_key.decode()}\n")
        else:
            secret_key = secret_key.encode()
        return secret_key


ctx = AppContext()
