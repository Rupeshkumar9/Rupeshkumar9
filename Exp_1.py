# A Python program to display Operating System name, version, and architecture using the platform library

import platform 
# Get OS name
os_name=platform.system()
# Get OS version
os_version=platform.version()
# Get architecture
os_architecture=platform.architecture()

# Display results
print(f"OS Name: {os_name}")
print(f"OS Version: {os_version}")
print(f"OS Architecture: {os_architecture}")
