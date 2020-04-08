import configparser

server = "localhost:4000"
secure = False
server_id = "http://{}/".format(server)
websocket_port = "ws://{}/graphql".format(server)


def read_config(_config_path: str):
    config = configparser.ConfigParser()
    config.read(_config_path)

    set_server(config["import"]["server"], config["import"].getboolean("secure"))


def set_server(_server: str, _secure: bool):
    global server
    global secure
    global server_id
    global websocket_port

    server = _server
    secure = _secure

    if _secure:
        server_id = "https://{}/".format(server)
        websocket_port = "wss://{}/graphql".format(server)
    else:
        server_id = "http://{}/".format(server)
        websocket_port = "ws://{}/graphql".format(server)
