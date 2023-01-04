import json
import glob
import os
# List of JSON files
json_files = glob.glob('json_file/*.json')

# Iterate through the list of JSON files
for file in json_files:
  # Open the JSON file
  file_name = os.path.basename(file)
  
  
  with open(file, 'r') as f:
    # Load the contents of the file into a variable
    data = json.load(f)

  # Check the conditions and print the results
  if data['attributes'][0]['value'] in data['attributes'][1]['value']:
    print(f'{file} meets the condition')
    os.rename(file, 'json_file/' + 'duplicate-' + file_name)
#   else:
#     print(f'{file} does not meet the condition')