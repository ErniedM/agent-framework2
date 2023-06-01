import git
import os
import json
import time
import shutil

class GitHubConnector:
    def __init__(self, repository_url):
        self.repository_url = repository_url

    def check_for_updates(self):
        try:
            local_directory = "temp_directory"
            print(local_directory)
            repo = git.Repo.clone_from(self.repository_url, local_directory)
            response = None
            config_file_path = os.path.join(local_directory, "config.txt")
            print(config_file_path)
            if os.path.exists(config_file_path):
                with open(config_file_path, "r") as file:
                    response = file.read()
                    print(response)

            repo.close()
            shutil.rmtree(local_directory)

            if response:
                return True
            else:
                return False
        except (git.exc.GitCommandError, FileNotFoundError):
            print("error")
            return False


connector = GitHubConnector("https://github.com/ErniedM/agent-framework2")
print(connector.check_for_updates())