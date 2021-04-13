from requests import get, post, delete

# Корректный запрос
print(get('http://localhost:5000/api/v2/jobs/1').json())
# Корректный запрос
qw = {'team_leader': 1, 'job': 'ghuljvlvcl', 'work_size': 15, 'is_finished': True}
print(post('http://localhost:5000/api/v2/jobs', json=qw).json())
# Корректный запрос
qw = {'team_leader': 1, 'job': 'dsGSG', 'work_size': 17, 'is_finished': False}
print(post('http://localhost:5000/api/v2/jobs', json=qw).json())
# Корректный запрос
print(get('http://localhost:5000/api/v2/jobs').json())
# Корректный запрос
print(delete('http://localhost:5000//api/v2/jobs/2').json())
# Некорректный запрос
print(get('http://localhost:5000/api/v2/jobs/2').json())
# Некорректный запрос
qw = {'team_leader': 1, 'job': 'ghuljvlvcl'}
print(post('http://localhost:5000/api/v2/jobs', json=qw).json())
# Некорректный запрос
print(delete('http://localhost:5000//api/v2/jobs/2').json())
# Корректный запрос
print(get('http://localhost:5000/api/v2/jobs').json())