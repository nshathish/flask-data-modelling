# Migrating databases using Alembic and Flask-Migrate

```python
pip3 install flask-migrate 
```

To initialize migrations
```python
flask db init
```
once changes are made to models, call the migrate command
```python
flask db migrate
```
To make the changes reflect on the database
```python
flask db upgrade
```

