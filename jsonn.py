import json

student = {"name": "Alice", "age": 20, "grade": "A"}

data = json.dumps(student)
print(data)
print(type(data))

student['test'] = True
data = json.dumps(student, indent=2, sort_keys=True)
print(data)