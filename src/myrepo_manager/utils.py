import os
import sys
from argparse import ArgumentParser, Namespace
from typing import List
from myrepo_manager.models import MyRepoManagerInput

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def parse_arguments(cli_args: List[str] = None) -> Namespace:
    parser = ArgumentParser(description="Managing files on Git repository 'myrepo'")
    parser.add_argument("--file", type=str, required=True, help="The file path to update, relative to repository root e.g. file.txt")
    parser.add_argument("--content", type=str, required=True, help="Content to add to file")
    parser.add_argument("--user", type=str, required=True, help="User who made the change")
    parser.add_argument("--diff-only", action="store_true", help="Produce only git diff if on, commit otherwise")
    return parser.parse_args(args=cli_args)

def get_input_model_from_arguments(cli_args: List[str]) -> MyRepoManagerInput:
    raw_args = parse_arguments(cli_args=cli_args)
    return MyRepoManagerInput(
        user=raw_args.user,
        content=raw_args.content,
        diff_only=raw_args.diff_only,
        file=raw_args.file
    )

def send_to_stdout(result: str):
    # print for stdout
    print(result, file=sys.stdout)