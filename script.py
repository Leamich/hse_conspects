import os
import re

vault_path = "."  # Update this to your vault path

def file_has_h1(file_path):
    """Check if a file contains an H1 heading."""
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if re.match(r"^# ", line):  # Matches only H1
                return True
    return False

def update_headings(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    updated_lines = []
    modified = False  # Track changes

    for line in lines:
        match = re.match(r"^(#{1,5}) (.*)", line)
        if match:
            updated_heading = f"#{match[1]} {match[2]}\n"  # Ensure newline is preserved
            if updated_heading != line:  # Check if change is needed
                modified = True
            updated_lines.append(updated_heading)
        else:
            updated_lines.append(line)

    if modified:  # Only write if changes were made
        print(file_name)
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(updated_lines)

for root, _, files in os.walk(vault_path):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            if file_has_h1(file_path):  # Only modify files with H1
                update_headings(file_path)

print("Headings updated in files containing H1!")
