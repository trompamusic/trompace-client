import configparser
import os

config_path = None

config = configparser.ConfigParser()

if not config_path:
	config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'import.ini'))
else: 
	config.read(config_path)

uri = config["import"]["uri"]
server = config["import"]["server"]
