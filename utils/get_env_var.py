from dotenv import load_dotenv

load_dotenv()  # Load potential .env file

import os


def get_env_var(var_name: str) -> str:
    """Loads and returns the key from the environment"""
    return os.environ.get(var_name)