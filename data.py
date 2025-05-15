student_data = {'id1': {
    'name': ['Sara'],
    'class': ['V'],
    'subjects': ['Math, Science']
}, 'id2': {
    'name': ['David'],
    'class': ['V'],
    'subjects': ['History, Geography']
}, 'id3': {
    'name': ['Matt'],
    'class': ['V'],
    'subjects': ['Math, Science']
}, 'id4': {
    'name': ['Surya'],
    'class': ['V'],
    'subjects': ['Eco, Commerce']
}}

result = {}

for key, value in student_data.items():
    if value not in result.items():
        result[key] = value


print(result)
