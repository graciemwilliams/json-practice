#!/usr/bin/env python3

import json

# reads in the file as json
with open('../../data/schacon.repos.json', 'r') as file:
    data = json.load(file)


with open('../../data/chacon.repos.csv', 'a') as f:
    # Write up to 5 records
    for d in data[:5]:
        line = f"{d['name']},{d['html_url']},{d['updated_at']},{d['visibility']}\n"
        f.write(line)

