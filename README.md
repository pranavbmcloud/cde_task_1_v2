# cde_task_1

## Workflow:
#### Ingests the source file
#### Cleans the data
#### Creates a local clean copy
#### Processes from the clean copy
#### Flattens (if required)
#### Writes to final file

  
## Current usage
#### Place the json or txt file to be processed in the ./src directory
#### Execute the main.py file
#### Output file will be in the ./src dir with the name "final - <original file name>"
#### Intermediate cleaned file will be in the ./src dir with the name "cleaned - <original file name>"
  
  
## Tests
#### Project uses the Python unittest testing framework for the tests
#### Tests can be run using "python -m unittest" in the root
  
  
## To Do
#### Test cases for the text cleaning and dictionary flattening methods
#### Get file to parse from command line
  
  
## Thoughts

### Data could Originate from multiple sources:
#### File from local file system
#### File from online url
#### API response
#### NoSQL tables


### There could be multiple cleaning requirements:
#### Malformed json, xml


### Data could be of multiple types:
#### Text files
#### Binaries
#### JSON
#### XML
#### YAML
#### sql

### There could be a need for multiple transformations:
#### JSON to XML



### Data might need to be sent to multiple destinations:
#### Local file system
#### Web endpoints
#### Exposed as a REST API
