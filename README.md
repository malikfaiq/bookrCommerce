# bookrCommerce

### Project setup
```
python3 -m venv env
source ./env/bin/activate
```

### Install Requirements
```
pip install -r requirements.txt
```

### Migrate and Run Django Server
```
python manage.py migrate
python manage.py runserver
```
### Django Admin for data creation
```
http://localhost:8000/admin 
```
###

### Graph QL for query Testing
```
http://localhost:8000/graphql 
```
###
### Run your unit tests
```
pytest -s
```
### Coverage Report
```
coverage report -m
```
### Lints and fixes files
```
black .
```