import re
import os

# Read the changelog.md file
with open('CHANGELOG.md', 'r') as file:
    changelog_content = file.read()

# Use regular expressions to extract the string between the first occurrence of square brackets
match = re.search(r'## \[(.*?)\]', changelog_content)
if match:
    extracted_string = match.group(1)
else:
    extracted_string = ""

output_name = "extracted_version"
with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    print(f'{output_name}={extracted_string}', file=fh)
