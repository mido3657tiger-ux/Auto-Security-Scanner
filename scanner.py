import os

def security_scan(file_path):
    if not os.path.exists(file_path):
        return "Error: File not found"
    with open(file_path, 'r') as file:
        code = file.read()
    # Logic for scanning
    return f"Scan finished for {file_path}"
