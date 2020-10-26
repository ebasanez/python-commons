import pytest,pymysql
import os, sys
import configparser
sys.path.append(os.path.join(sys.path[0],'..'))
from basacommons.Database import Database

def test_not_allowed_query():
    ### Arrange
    configuration = configparser.ConfigParser()
    configuration.add_section('ddbb')
    configuration.set('ddbb','host','localhost')
    configuration.set('ddbb','port','3306')
    configuration.set('ddbb','name','myschema')
    configuration.set('ddbb','username','root')
    configuration.set('ddbb','password','changeit')
    ddbb = Database(configuration)

    ### Act
    with pytest.raises(Exception) as e:
        ddbb.run_query('SHOW TABLES')
    assert str(e.value) == f'Query \'SHOW TABLES\' is not allowed in non-management mode. To allow management mode, set coniguration value ddbb.allow-management = True'