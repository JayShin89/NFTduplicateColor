import json
import glob
import os
import natsort

# List of JSON files
json_files = glob.glob('json_file/*.json') #Define Json file location
img_files = glob.glob('img_file/*.png') #Define img file location

# re-sort files with numeric ascend order
json_files = natsort.natsorted(json_files)
img_files = natsort.natsorted(img_files)

#new number after duplicate color file
a = 1

# Iterate through the list of JSON files
for file in json_files:
  # Open the JSON file
  file_name = os.path.basename(file)
  
  #for img_file in img_files:
    #if((file.split("."))[0] == (img_file.split("."))[0]):
      #img_file_name = os.path.basename(img_file)
  with open(file, 'r') as f:        
    # Load the contents of the file into a variable
    data = json.load(f)

      # Check the conditions and print the results
  if data['attributes'][0]['value'] in data['attributes'][1]['value']:
    #print(f'{file} meets the condition')
    print(file_name)
    os.rename('img_file/'+(file_name.split("."))[0]+'.png', 'img_file/' + 'duplicated-' + (file_name.split("."))[0]+'.png')
    os.rename(file, 'json_file/' + 'duplicated-' + file_name)
    
  else:
    print(f'{file} does not meet the condition')
    os.rename('img_file/'+(file_name.split("."))[0]+'.png', 'img_file/' + str(a) + '.png')
    os.rename(file, 'json_file/' + str(a) + '.json')    
    a+=1
    
    
    
