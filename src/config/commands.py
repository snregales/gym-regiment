# -*- coding: utf-8 -*-
"""Click commands."""
import os
import sys
from glob import glob
from subprocess import call  # nosec
from typing import List

import click

from src.app import logging

from .settings import TEST_PATH


@click.command()
@click.option(
    "-c",
    "--cov",
    default=True,
    is_flag=True,
    help="Path or package name to measure during execution (multi-allowed).",
)
def test(cov):
    """Run the tests."""
    try:
        import pytest  # pylint: disable=import-outside-toplevel
    except ImportError as _:
        logging.error(_)
    pytest_args: List = [TEST_PATH, "--verbose"]
    if cov:
        pytest_args.extend(["--cov", "--cov-report=html"])
    exit_code: int = pytest.main(pytest_args)
    sys.exit(exit_code)


@click.command()
@click.option(
    "-f",
    "--fix-imports",
    default=True,
    is_flag=True,
    help="Fix imports using isort, before linting",
)
@click.option(
    "-c",
    "--check",
    default=False,
    is_flag=True,
    help="Don't make any changes to files, \
    just confirm they are formatted correctly",
)
def lint(fix_imports, check):
    """Lint and check code style with black, flake8 and isort."""
    skip = ["node_modules", "requirements", "migrations", "__pycache__", "htmlcov"]
    root_files = glob("*.py")
    root_directories = [
        name for name in next(os.walk("."))[1] if not name.startswith(".")
    ]
    files_and_directories = [
        arg for arg in root_files + root_directories if arg not in skip
    ]

    def execute_tool(description, *args):
        """Execute a checking tool with its arguments."""
        command_line = list(args) + files_and_directories
        click.echo("{}: {}".format(description, " ".join(command_line)))
        return_code = call(command_line)  # nosec
        if return_code != 0:
            sys.exit(return_code)

    isort_args = ["-rc"]
    black_args = []
    if check:
        isort_args.append("-c")
        black_args.append("--check")
    if fix_imports:
        execute_tool("Fixing import order", "isort", *isort_args)
    execute_tool("Formatting style", "black", *black_args)
    execute_tool("Checking code style", "flake8")
