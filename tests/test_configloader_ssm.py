import os, sys
sys.path.append(os.path.join(sys.path[0],'..'))
from basacommons import configloader

def test_ssm_has_sections():
    #Act
    configuration = configloader.load_config('ssm','pro')
    #Assert
    assert len(configuration.sections()) > 0

def test_env():
    #Arrange:
    os.environ["MYPROJECT_TEST_DDBB_HOST"] = 'host_ddbb'

    # Act
    config = configloader.load_config('env','TEST', 'MYPROJECT')

    # Assert
    assert config.get('ddbb','host') == 'host_ddbb'
       