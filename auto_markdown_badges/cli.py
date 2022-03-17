"""This module provides the auto-markdown-badges CLI."""
from enum import Enum
from pathlib import Path
from typing import Optional

from typer import Argument, Exit, Option

from auto_markdown_badges import __app_name__, __version__
from auto_markdown_badges.custom_typer import CustomTyper
from auto_markdown_badges.utils import finditer

app = CustomTyper()


def _version_callback(value: bool) -> None:
    if value:
        print(f"{__app_name__} v{__version__}")
        raise Exit()


@app.callback()
def main(
    version: Optional[bool] = Option(  # dead: disable
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
) -> None:
    return


class Placement(str, Enum):
    """Indicator for badge placement."""

    HEADER = "header"
    INPLACE = "inplace"
    FOOTER = "footer"


@app.command(
    help="Generates badges from a file.",
)
def generate(  # dead: disable
    input_file: Path = Argument(
        ...,
        help="The file to use for generation of badges.",
        exists=True,
        dir_okay=False,
    ),
    output_file: Path = Option(
        None,
        "-o",
        "--output-file",
        help="The file to output to.",
        exists=False,
        dir_okay=False,
    ),
    placement: Placement = Option(
        Placement.INPLACE,
        "-p",
        "--placement",
        case_sensitive=False,
        help="Specify where to place the badge.",
    ),
):
    with open(input_file, "r") as file:
        data = file.read()

    if placement is Placement.INPLACE:
        new_data = data
        for string, badge in finditer(data):
            new_data = new_data.replace(string, badge, 1)
    else:
        badges = " ".join(badge for _, badge in finditer(data))
        if placement is Placement.HEADER:
            new_data = f"{badges}\n\n{data}"
        elif placement is Placement.FOOTER:
            new_data = f"{data}\n\n{badges}"

    with open(output_file or input_file, "w") as file:
        file.write(new_data)
