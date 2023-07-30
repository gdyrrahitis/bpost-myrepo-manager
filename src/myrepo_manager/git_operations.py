import git
import os
import uuid
import json
from myrepo_manager.utils import cd, send_to_stdout
from myrepo_manager.common import get_logger, GIT_SERVER, GIT_SERVER_PORT
from myrepo_manager.models import MyRepoManagerInput

logger = get_logger(__name__)


class MyRepoGitOperationsManager:
    def __init__(self):
        self.current_working_directory = os.getcwd()
        self.temp_directory = os.path.join(self.current_working_directory, "var")
        self.local_repo_workspace = os.path.join(
            self.temp_directory, str(uuid.uuid4().hex), self.repo_name
        )

    @property
    def repo_url(self):
        return f"ssh://git@{GIT_SERVER}:{GIT_SERVER_PORT}/git-server/repos/myrepo.git"

    @property
    def repo_name(self):
        return "myrepo"

    def __enter__(self):
        logger.debug(f"Cloning repo {self.repo_url}")
        try:
            self.repo = git.Repo.clone_from(self.repo_url, self.local_repo_workspace)
            self._setup_repository()
            return self
        except Exception as e:
            logger.exception(e)

    def __exit__(self, etype, value, traceback):
        self.repo.close()
        logger.info(f"Removing temp destination directory {self.temp_directory}")
        git.rmtree(self.temp_directory)

    def _setup_repository(self) -> None:
        logger.debug(f"Setup configuration for repo {self.repo_name}")
        with self.repo.config_writer() as git_config:
            git_config.set_value("user", "email", os.getenv("GIT_USER_EMAIL"))
            git_config.set_value("user", "name", os.getenv("GIT_USER"))

    def append_content_to_file(self, input: MyRepoManagerInput) -> None:
        logger.info(f"Starting process to update file {input.file}")
        with cd(self.local_repo_workspace):
            logger.debug(
                f"Changed directory to {self.local_repo_workspace} - pwd: {os.getcwd()}"
            )
            with open(input.file, mode="a") as f:
                f.write(f"{input.user}: {input.content}\n")
                logger.debug(f"Wrote to file {f.name} successfully")

            files_updated = self.repo.git.diff(None, name_only=True)
            file_diffs = []
            for update_file in files_updated.split("\n"):
                diff = self.repo.git.diff(update_file)
                logger.info(f"\n\n****\n{diff}\n\n****")
                self.repo.git.add(update_file)
                file_diffs.append({"diff": diff, "file": update_file})

            if input.diff_only:
                logger.debug("Dry run operation, returning diff")
                # print for stdout
                send_to_stdout(json.dumps(file_diffs))
            else:
                self.repo.git.commit("-m", "Updated file.txt")
                logger.info(f"Committed changes {self.repo.head.commit.hexsha}")
                self.repo.git.pull()
                self.repo.git.push()
                # print for stdout
                send_to_stdout(json.dumps({"commit_id": self.repo.head.commit.hexsha}))
        logger.debug(
            f"Changed back to working dir {self.current_working_directory} - pwd: {os.getcwd()}"
        )
