import os
from platformdirs import PlatformDirs

appdirs = PlatformDirs(appname="artrade")
setattr(appdirs, "user_dotenv",
        os.path.join(appdirs.user_config_dir, ".local/.env"))
