import os, sys
sys.path.append(os.path.join(sys.path[0],'..'))
sys.path.append(os.path.join(sys.path[0],'../basacommons'))
import configloader

configuration = configloader.load_config('ssm','pro')

print(configuration.sections())