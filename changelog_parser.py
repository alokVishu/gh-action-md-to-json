import re
import json
import os
import sys

# Get input file paths from environment variables or default values
markdown_file_path = sys.argv[1] if len(sys.argv) > 1 else 'CHANGELOG.md'
output_file_path = sys.argv[2] if len(sys.argv) > 2 else 'changelog.json'

# Open the Markdown file and read its content
with open(markdown_file_path, 'r') as file:
    markdown_data = file.read()

# Regex patterns to extract versions, dates, types, and changes
version_pattern = r'## (v\d+\.\d+\.\d+) \((\d{4}-\d{2}-\d{2})\)'
type_pattern = r'### (\w+)'
change_pattern = r'- (.+)'

# Parse versions
changelog = []
versions = re.split(version_pattern, markdown_data)[1:]

for i in range(0, len(versions), 3):
    version, date, content = versions[i], versions[i + 1], versions[i + 2]
    log_entries = []

    # Parse types and changes within each version
    types = re.split(type_pattern, content)[1:]

    for j in range(0, len(types), 2):
        log_type, changes_content = types[j], types[j + 1]
        changes = re.findall(change_pattern, changes_content)
        log_entries.append({
            'type': log_type,
            'change': changes
        })

    changelog.append({
        'version': version,
        'date': date,
        'log': log_entries
    })

# Convert to JSON
json_output = json.dumps(changelog, indent=2)

# Write the JSON output to a file
with open(output_file_path, 'w') as json_file:
    json_file.write(json_output)

print(f"Changelog has been saved to {output_file_path}")
