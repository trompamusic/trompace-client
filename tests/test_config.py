import configparser

import pytest

from trompace import config


class TestConfig:

    def test_set_server_old(self):
        # host and secure flag
        settings = {"server": {"host": "localhost:4000", "secure": "false"}}
        c = config.TrompaConfig()
        c.config = configparser.ConfigParser()
        c.config.read_dict(settings)

        c._set_server()
        assert c.host == "http://localhost:4000"
        assert c.websocket_host == "ws://localhost:4000/graphql"

    def test_set_server_no_secure(self):
        # host with no scheme, and no secure flag
        settings = {"server": {"host": "localhost:4000"}}
        c = config.TrompaConfig()
        c.config = configparser.ConfigParser()
        c.config.read_dict(settings)

        with pytest.raises(ValueError):
            c._set_server()

    def test_set_server_https(self):
        # host with scheme built-in
        settings = {"server": {"host": "https://localhost:4000"}}
        c = config.TrompaConfig()
        c.config = configparser.ConfigParser()
        c.config.read_dict(settings)

        c._set_server()
        assert c.host == "https://localhost:4000"
        assert c.websocket_host == "wss://localhost:4000/graphql"

    def test_set_server_http(self):
        # host with scheme built-in
        settings = {"server": {"host": "http://localhost:4000"}}
        c = config.TrompaConfig()
        c.config = configparser.ConfigParser()
        c.config.read_dict(settings)

        c._set_server()
        assert c.host == "http://localhost:4000"
        assert c.websocket_host == "ws://localhost:4000/graphql"

    def test_set_server_subdir(self):
        # Hosted in a subdirectory
        settings = {"server": {"host": "http://localhost:4000/trompa/"}}
        c = config.TrompaConfig()
        c.config = configparser.ConfigParser()
        c.config.read_dict(settings)

        c._set_server()
        assert c.host == "http://localhost:4000/trompa/"
        assert c.websocket_host == "ws://localhost:4000/trompa/graphql"

