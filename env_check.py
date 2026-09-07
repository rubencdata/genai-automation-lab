import sys
import os
import json

# CONCEPT 1: Functions (Reusable blocks of code)
def get_system_status():
    """
    Collects basic operating system and Python environment details.
    Returns a Python dictionary (key-value pairs).
    """
    
    # CONCEPT 2: Conditionals & Booleans
    # Checks if your terminal is running inside .venv or global Python
    is_venv_active = sys.prefix != sys.base_prefix
    
    # Checks if a folder named "logs" exists on your disk
    logs_folder_exists = os.path.exists("logs")

    # CONCEPT 3: Python Dictionaries (Data Structures)
    status_data = {
        "python_version": sys.version,
        "operating_system": sys.platform,
        "virtual_env_active": is_venv_active,
        "logs_folder_found": logs_folder_exists
    }

    return status_data


# CONCEPT 4: Entry Point Execution
if __name__ == "__main__":
    # Call the function and store its return value in a variable
    diagnostic_result = get_system_status()

    # Print results to the console using f-strings (formatted text)
    print("--- PYTHON NATIVE DIAGNOSTIC ---")
    print(f"Python Version: {diagnostic_result['python_version']}")
    print(f"Operating System: {diagnostic_result['operating_system']}")
    print(f"Virtual Env Active: {diagnostic_result['virtual_env_active']}")
    print(f"Logs Folder Exists: {diagnostic_result['logs_folder_found']}")

    # CONCEPT 5: File Operations (Saving data to disk)
    with open("system_status.json", "w") as file:
        json.dump(diagnostic_result, file, indent=2)

    print("\n[SUCCESS] Saved status report to system_status.json")