import configparser
import os

if 'CONFIG_PATH' in os.environ.keys():
    config_path = os.environ['CONFIG_PATH']
else:
    config_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'import.ini')

config = configparser.ConfigParser()

config.read(config_path)

server = config["import"]["server"]
secure = config["import"].getboolean("secure")

if secure:
    server_id = "https://{}/".format(server)
    websocket_port = "wss://{}/graphql".format(server)
else:
    server_id = "http://{}/".format(server)
    websocket_port = "ws://{}/graphql".format(server)