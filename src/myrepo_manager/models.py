from dataclasses import dataclass


@dataclass
class MyRepoManagerInput:
    user: str
    content: str
    diff_only: bool
    file: str
