#!/usr/bin/env python
from artrade.configs import ctx


def main():
    print(ctx.secret_key)
    # print(appdirs.user_dotenv)


if __name__ == "__main__":
    main()
