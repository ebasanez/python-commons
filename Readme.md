This project joins some useful scripts designed to speed up project development.

Main scripts are:

## configuration.py
Configuration load from different sources:
### AWS Systems manager parameter store
```python
configuration = load_config('ssm',environment)
```
SSM variable key must have format: 
/$environment/$section 
and value in json format

Key | Value
--- | ---
/pre/ddbb | {"host":"localhost","port":3306,"user":"root","password":"changeit"}
#### Local file
```python
configuration = load_config('file',environment, file_name)
```
File expected in standard INI file structure. 

```
[ddbb]
host=localhost
port=3306
user=root
password=changeit
```
#### Environment variables.
```python
configuration = load_config('env',environment, projectname)
```
Variables should have the following format:
$projectname_$environemnt_$sectionname

```
MYPROJECT_PRO_DDBB_HOST=localhost
MYPROJECT_PRO_DDBB_PORT=3306
MYPROJECT_PRO_DDBB_USER=root
MYPROJECT_PRO_DDBB_PASSWORD=changeit
```
### database.py
Database connection and query execution
```python
database = database(configuration)
```
To execute query, use method *Database.run_query*
```python
records = database.run_query('SELECT * FROM table WHERE mycolumn = %s AND myothercolumn = '%s',('value1', 'value2' ))
```
Pagination is supported using class *database.Page*:
```python
page_number = 1
page_size = 50
page = database.Page(page_number, page_size)
records = database.run_query('SELECT * FROM table WHERE mycolumn = %s AND myothercolumn = '%s', ('value1', 'value2' ), page)
```
### alerts.py
Alert sending, via AWS simple email service.
