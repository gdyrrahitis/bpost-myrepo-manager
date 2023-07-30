import datetime
import json
import re
from myrepo_manager.main import main

pattern = r"(?:diff\s+--git\sa\/file.txt\sb\/file.txt\nindex\s[a-z0-9]+\.{2}[a-z0-9]+\s[a-z0-9]+)\n(?:---\sa\/file.txt\n\+{3}\sb\/file.txt\n@@\s.*@@\n)(?P<previous>\s+[a-zA-Z]+\n)(?P<diff>\+george:\s\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d+\]-exec)"


def test_appending_to_file_in_myrepo_repository(capsys):
    now = datetime.datetime.now()
    cli_args = [
        "--file",
        "file.txt",
        "--user",
        "george",
        "--content",
        f"[{now}]-exec",
        "--diff-only",
    ]
    code = main(cli_args)
    captured = capsys.readouterr()

    # CLI execution was successful
    assert code == 0

    output = json.loads(captured.out)
    assert len(output) == 1

    updated_file = output[0]
    assert updated_file["file"] == "file.txt"
    match = re.search(pattern, updated_file["diff"])
    assert match != None
    diff = match.group("diff")
    assert diff != None
