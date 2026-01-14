
import json
from datetime import datetime
from tracker import create_record

records = [
    create_record("Paris", "Loved the museums", "05-06-2022"),
    create_record("Tokyo", "Amazing food", "12-09-2023"),
    create_record("New York", "Great city vibe", "20-03-2024")
]

for record in records:
    d = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = d.strftime("%B %d, %Y")

json_data = json.dumps(records)
print(json_data)

parsed = json.loads(json_data)
for record in parsed:
    print(record)
