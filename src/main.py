"""Main module that directs the workflow"""
from src.source_type import get_source_type
from src.file_type import get_data_type
from src.ingest import ingesters
from src.clean import cleaners
from src.write import simple_writer, writers
from src.process import processors
from src.flatten import flatteners


input_file = 'file 01.json'
source_type = get_source_type(input_file)
source_data_type = get_data_type(input_file)

cleaned_file_name = "cleaned - " + input_file
final_file_name = "final - " + input_file

ingest = ingesters[source_type]
ingested_data = ingest(input_file)

cleaner = cleaners[source_data_type]
cleaned_data = cleaner(ingested_data)

simple_writer(cleaned_data, cleaned_file_name)

processor = processors[source_data_type]
processed_data = processor(cleaned_file_name)

flattener = flatteners[source_data_type]
flattened_data = []

for data_line in processed_data:
    flattened_data.append(flattener(data_line))

writer = writers[source_data_type]
writer(flattened_data, final_file_name)
