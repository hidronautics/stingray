from os import environ


def get_env(name: str, default):
    if name in environ:
        return environ[name]

    return default
