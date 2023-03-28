from environs import Env
from os import path, getcwd

# Populate environment variables from file to environment
env = Env()
try:
    env.read_env(path.join(getcwd(), ".env.{}".format(env("env", preprocessor=str.lower, default="local"))))
except FileNotFoundError:
    pass

# Environment variables
TOKEN_BOT = env.str("TOKEN_BOT", default="")
