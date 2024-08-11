import json

def load_job_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)