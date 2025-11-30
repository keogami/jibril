import os
import sys
from pathlib import Path
from typing import Literal

import typed_settings as ts
import typer
from loguru import logger

from retrain import retrain

# TODO: Add log file with a short retention, and another with compression that
# is retained forever.
# TODO: Add ability to register multiple paths to watch for organizing.


# TODO: validate the values, i dont know if typed-settings is validating
@ts.settings
class Config:
    target: Path = Path.home() / "jibril/"
    # TODO convert this to enum https://typed-settings.readthedocs.io/en/latest/examples.html#the-code
    model_size: Literal["small", "medium", "large", "xlarge"] = "large"
    ignore: list[Path] = []


def load_config() -> Config:
    xdg_config = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))
    config_path = xdg_config / "jibril" / "config.toml"

    return ts.load(
        Config,
        appname="jibril",
        config_files=[config_path, ".jibril.toml"],
        config_file_section=None,
    )


app = typer.Typer()


@app.command()
def daemon():
    """
    Start jibril as a daemon. Run this through a systemd auto start unit.
    """

    logger.remove()
    logger.add(sys.stdout, format="{level} - <level>{message}</level>", level="DEBUG")
    config = load_config()

    logger.info(f"Jibril is starting as a daemon for directory {config.target}")

    # TODO
    # - validate health
    # - if there's no model yet, force a retrain
    # - start a thread with watchdog, sending file paths to a queue
    # - pop things from the queue from another N thread and run yolo on it
    # - setup a cron to pause infering and start a retrain
    # - setup whatever's need for graceful shutdown
    #
    # do whatever is needed to orchestrate all this

    retrain()


@app.command()
def health():
    """
    Check the health of the system setup and configuration.
    """
    # TODO
    # - validate that configuration is sane
    # - check if the target directory has sub-directories with sane characters
    # - check every relevant directory has at least one image
    pass


if __name__ == "__main__":
    app()
