from typer.testing import CliRunner

from auto_markdown_badges import __app_name__, __version__, cli

runner = CliRunner()


def test_version():
    """Test printing version"""
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" == result.stdout


def test_generate():
    """Test end-to-end"""
    result = runner.invoke(
        cli.app,
        [
            "generate",
            "examples/example.md",
            "--output-file",
            "generated/example_badges.md",
        ],
    )
    assert result.exit_code == 0


def test_generate_with_placement_header():
    """Test end-to-end with header placement"""
    result = runner.invoke(
        cli.app,
        [
            "generate",
            "examples/example.md",
            "--output-file",
            "generated/example_badges.md",
            "--placement",
            "header",
        ],
    )
    assert result.exit_code == 0


def test_generate_with_placement_footer():
    """Test end-to-end with footer placement"""
    result = runner.invoke(
        cli.app,
        [
            "generate",
            "examples/example.md",
            "--output-file",
            "generated/example_badges.md",
            "--placement",
            "footer",
        ],
    )
    assert result.exit_code == 0
