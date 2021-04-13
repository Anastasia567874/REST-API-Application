from requests import get, post, delete

# Корректный запрос
print(delete('http://localhost:5000//api/v2/users/1').json())
# Корректный запрос
qw = {'name': 'nas', 'surname': 'veche', 'age': 12, 'email': 'ansad@gh', 'hashed_password': 'poityuhjvcsa342'}
print(post('http://localhost:5000/api/v2/users', json=qw).json())
# Корректный запрос
qw = {'name': 'adv', 'surname': 'hdAGrf', 'age': 3, 'email': 'sAFdsgf#fd', 'hashed_password': 'geaew432gfgj'}
print(post('http://localhost:5000/api/v2/users', json=qw).json())
# Корректный запрос
print(get('http://localhost:5000/api/v2/users').json())
# Корректный запрос
print(delete('http://localhost:5000//api/v2/users/2').json())
# Некорректный запрос
print(get('http://localhost:5000/api/v2/users/2').json())
# Некорректный запрос
qw = {'name': 'nasa', 'surname': 'vecher'}
print(post('http://localhost:5000/api/v2/users', json=qw).json())
# Некорректный запрос
print(delete('http://localhost:5000//api/v2/users/2').json())
# Корректный запрос
print(get('http://localhost:5000/api/v2/users').json())