# auto-markdown-badges

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/feluelle/auto-markdown-badges/main.svg)](https://results.pre-commit.ci/latest/github/feluelle/auto-markdown-badges/main)
![test workflow](https://github.com/feluelle/auto-markdown-badges/actions/workflows/test.yml/badge.svg)
![codeql-analysis workflow](https://github.com/feluelle/auto-markdown-badges/actions/workflows/codeql-analysis.yml/badge.svg)
[![codecov](https://codecov.io/gh/feluelle/auto-markdown-badges/branch/main/graph/badge.svg?token=J8UEP8IVY4)](https://codecov.io/gh/feluelle/auto-markdown-badges)
[![PyPI version](https://img.shields.io/pypi/v/auto-markdown-badges)](https://pypi.org/project/auto-markdown-badges/)
[![License](https://img.shields.io/pypi/l/auto-markdown-badges)](https://github.com/feluelle/auto-markdown-badges/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/auto-markdown-badges)](https://pypi.org/project/auto-markdown-badges/)
[![PyPI version](https://img.shields.io/pypi/dm/auto-markdown-badges)](https://pypi.org/project/auto-markdown-badges/)

> Auto-generated markdown badges. 🧙🖼

Inspired by [markdown-badges](https://github.com/Ileriayo/markdown-badges), I wanted to have a tool which automatically creates badges for me.

## 🚀 Get started

To install it from [PyPI](https://pypi.org/) run:

```console
pip install auto-markdown-badges
```

Then just call it like this:

```console
Usage: auto-markdown-badges generate [OPTIONS] INPUT_FILE

  Generates badges from a file.

Options:
  INPUT_FILE                      The file to use for generation of badges.
                                  [required]
  -o, --output-file FILE          The file to output to.
  -p, --placement [header|inplace|footer]
                                  Specify where to place the badge.  [default:
                                  Placement.INPLACE]
  -h, --help                      Show this message and exit.
```

_Examples of generated badges can be found in the [examples](examples) directory._

## 🤔 How it Works

1. It reads the given file, line by line
2. It tries to find [simple-icons](https://github.com/simple-icons/simple-icons) for every word
3. It replaces the word with a badge

## ❤️ Contributing

Contributions are very welcome. Please go ahead and raise an issue if you have one or open a PR. Thank you.
