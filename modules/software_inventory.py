import platform
import subprocess

class SoftwareInventoryModule:
    def __init__(self):
        self.operating_system = platform.system()

    def collect_data(self):
        software_inventory = {}

        if self.operating_system == "Linux":
            software_inventory = self.get_linux_software_inventory()
        elif self.operating_system == "Windows":
            software_inventory = self.get_windows_software_inventory()
        elif self.operating_system == "Darwin":
            software_inventory = self.get_mac_software_inventory()

        return software_inventory

    def get_linux_software_inventory(self):
        try:
            command = "dnf list installed"
            output = subprocess.check_output(command, shell=True, text=True)
            lines = output.strip().split("\n")
            software_inventory = []

            for line in lines[1:]:
                package_info = line.split()
                if len(package_info) >= 3:
                    package_name = package_info[0]
                    package_version = package_info[1]
                    software_inventory.append({"package_name": package_name, "package_version": package_version})

        except Exception as e:
            print(f"Fout bij het ophalen van software-inventaris op Linux: {e}")

        return software_inventory

    def get_windows_software_inventory(self):
        software_inventory = {}
        try:
            # Gebruik het juiste commando om de software-inventaris op te vragen op Windows
            command = "wmic product get Name,Version"
            output = subprocess.check_output(command.split()).decode().strip()

            # Verwerk de uitvoer om de software-inventaris te verkrijgen
            lines = output.split('\n')
            for line in lines[2:]:
                line = line.strip()
                if line:
                    package_info = line.split('  ')
                    software_inventory[package_info[0]] = package_info[1]

        except Exception as e:
            print(f"Fout bij het ophalen van software-inventaris op Windows: {e}")

        return software_inventory

    def get_mac_software_inventory(self):
        software_inventory = {}
        try:
            # Gebruik het juiste commando om de software-inventaris op te vragen op Mac
            command = "system_profiler SPApplicationsDataType -xml"
            output = subprocess.check_output(command.split()).decode().strip()

            # Verwerk de uitvoer om de software-inventaris te verkrijgen
            # Implementeer de verwerking van de XML-uitvoer naar een bruikbare software-inventaris

        except Exception as e:
            print(f"Fout bij het ophalen van software-inventaris op Mac: {e}")

        return software_inventory
