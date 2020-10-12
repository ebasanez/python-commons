#Setups path for scripts in test module
import logging 
import configparser
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

import os, sys
sys.path.append(os.path.join(sys.path[0],'../basacommons'))

configuration = configparser.ConfigParser()
configuration.add_section('global')
configuration.add_section('alert')
configuration.set('global','environment','pre')
configuration.set('alert','source','enrique.basanez@gmail.com')
configuration.set('alert','recipients','enrique.basanez@gmail.com')

