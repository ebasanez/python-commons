import os, sys
import pytest
import logging 

sys.path.append(os.path.join(sys.path[0],'../'))
from basacommons import configloader
from basacommons.Database import Database, Page

#Load test configuration properties and ddbb
config = configloader.load_config('ssm','test')
subject = Database.ofConfiguration(config)

@pytest.fixture(scope="session", autouse=True)
def pytest_configure():
    """
    Create and destroy tables that will be used in this tests"
    """
    logging.info('Generating test ddbb schema')
    subject.run_query('DROP TABLE IF EXISTS test_table')    
    subject.run_query('CREATE TABLE test_table (`id` INT(10) NULL)')    
    subject.run_query(f"INSERT INTO test_table VALUES {','.join([f'({i})' for i in range(100)])}")    
    yield
    logging.info('Destroying test ddbb schema')
    subject.run_query('DROP TABLE test_table')    
    
def test_pagination():
    # Arrange
    page = Page(10)
    # Act
    results = subject.run_query('SELECT * FROM test_table', page = page)
    # Assert
    assert len(results) == 10

def test_arguments():
    # Act
    results = subject.run_query('SELECT * FROM test_table WHERE id >= %s', (50) )
    # Assert
    assert len(results) == 50

def test_arguments_and_pagination():
    # Arrange
    page = Page(10)
    # Act
    results = subject.run_query('SELECT * FROM test_table where id >= %s',(50), page)
    # Assert
    assert len(results) == 10
    assert results[0]['id'] == 50
    assert results[-1]['id'] == 59

def test_sort():
    # Arrange
    page = Page(sort_field= 'id')
    # Act
    results = subject.run_query('SELECT * FROM test_table',(), page)
    # Assert
    assert results[0]['id'] == 0
    assert results[-1]['id'] == 99
      
def test_sort_desc():
    # Arrange
    page = Page(sort_field = 'id', sort_order_asc = False)
    # Act
    results = subject.run_query('SELECT * FROM test_table ',(), page)
    # Assert
    assert results[0]['id'] == 99
    assert results[-1]['id'] == 0
