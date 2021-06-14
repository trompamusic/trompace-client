Usage
=====

Configuration
-------------

In order to connect to a CE server you require a configuration file. See the ``trompace.ini`` example file
in the code repository

.. code-block:: text

    [server]
    host = http://localhost:4000

    [auth]
    id = local
    key = PZsG+oEW3K3QOoB5z0f30InzjXdBqM9LMtJa7BTg1xo=
    scopes = *
    # If the server doesn't require auth, set required to no, otherwise it should be yes
    required = yes

    [logging]
    # A python logging level (debug, info, warning, error)
    level = debug

Set ``server.host`` to the URL that your CE is running from. For information about the ``auth.id``, ``auth.key``,
and ``auth.scopes`` values, see the `CE documentation on authentication <https://github.com/trompamusic/ce-api/blob/staging/docs/authentication.md>`_


In order to perform queries you need to load the config file. To do so, use :meth:`trompace.config.config.load` with
the name of the config file:

.. code-block:: python

    from trompace.config import config
    config.load('trompace.ini')

Alternatively, you can set the environment variable ``TROMPACE_CLIENT_CONFIG`` to the path of the config file and
call :meth:`trompace.config.config.load` with no arguments:

.. code-block:: python

    from trompace.config import config
    config.load()

Making requests
---------------

``trompace-client`` is a simple wrapper to send HTTP requests to a graphql endpoint.
The request methods can be used with a manually constructed query, or by using the methods
available in the `Mutations`_ section.

Use :meth:`trompace.connection.submit_query` to send a graphql command to the CE.

.. autofunction:: trompace.connection.submit_query

.. code-block:: python

    from trompace.mutations import person
    from trompace.connection import submit_query
    query = person.mutation_create_person(name="Gustav Mahler", ...)
    submit_query(query, auth_required=True)

