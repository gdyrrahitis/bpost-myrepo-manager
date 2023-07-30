import sys
from myrepo_manager.utils import get_input_model_from_arguments
from myrepo_manager.common import get_logger
from myrepo_manager.git_operations import MyRepoGitOperationsManager
from typing import List

logger = get_logger(__name__)

def main(cli_args: List[str] = None) -> int:
    try:
        input = get_input_model_from_arguments(cli_args=cli_args)
        with MyRepoGitOperationsManager() as myrepo:
            myrepo.append_content_to_file(input)
    except KeyboardInterrupt as e:
        logger.exception(e)
        print("Aborted manually.", file=sys.stderr)
        return 1
    except Exception as e:
        logger.exception(e)
        return 1

if __name__ == "__main__":
    sys.exit(main())
