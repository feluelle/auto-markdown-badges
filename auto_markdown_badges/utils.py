import re
from collections.abc import Generator

from simpleicons.all import icons


def finditer(data: str) -> Generator[tuple[str, str], None, None]:
    """
    Generate replacements/badges from words.

    :param data: The data to process.

    :returns: yields replacements i.e. word & badge.
    """
    for title, link, word in set(
        re.findall(
            # Markdown Links or just Words
            r"\[([^\[\]]*)\]\((.*?)\)|(\w+)",
            data,
        ),
    ):
        if title and link and (icon := icons.get(title)):
            # Replace link with badge incl. link
            color = icon.__dict__["hex"]
            badge = f"[![{title}](https://img.shields.io/badge/{title}-{color}?style=for-the-badge&logo={title}&logoColor=white)]({link})"
            yield f"[{title}]({link})", badge
        elif word and (icon := icons.get(word)):
            # Replace word with badge
            color = icon.__dict__["hex"]
            badge = f"![{word}](https://img.shields.io/badge/{word}-{color}?style=for-the-badge&logo={word}&logoColor=white)"
            yield word, badge
