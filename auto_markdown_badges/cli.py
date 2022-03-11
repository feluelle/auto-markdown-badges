"""This module provides the auto-markdown-badges CLI."""
import re
from pathlib import Path
from typing import Optional

from simpleicons.all import icons
from typer import Argument, Exit, Option

from auto_markdown_badges import __app_name__, __version__
from auto_markdown_badges.custom_typer import CustomTyper

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
):
    def process(line: str) -> str:
        """
        Replace links or words by badges.

        :param line: The line to process.
        """
        for title, link, word in re.findall(
            # Markdown Links or just Words
            r"\[([^\[\]]*)\]\((.*?)\)|(\w+)",
            line,
        ):
            if title and link and (icon := icons.get(title)):
                # Replace link with badge incl. link
                color = icon.__dict__["hex"]
                badge = f"[![{title}](https://img.shields.io/badge/{title}-{color}?style=for-the-badge&logo={title}&logoColor=white)]({link})"
                line = line.replace(f"[{title}]({link})", badge, 1)
            elif word and (icon := icons.get(word)):
                # Replace word with badge
                color = icon.__dict__["hex"]
                badge = f"![{word}](https://img.shields.io/badge/{word}-{color}?style=for-the-badge&logo={word}&logoColor=white)"
                line = line.replace(word, badge, 1)
        return line

    lines = []
    with open(input_file, "r") as file:
        for line in file:
            lines.append(process(line))
    with open(output_file or input_file, "w") as file:
        file.writelines(lines)
