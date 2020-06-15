# Trompa Contributor Environment Python Client

Music Technology Group, Universitat Pompeu Fabra, Barcelona

A python library to read from and write to the Trompa Contributor Environment
(Trompa CE).

## Installation

To install, run

    python setup.py install

to install the package and dependencies

## Using the library

This library connects to an existing Trompa CE instance. For testing on a local
environment the docker containers from https://github.com/trompamusic/ce-api
can be run.

Basic example code for using the library to add an artist to the Trompa CE.

To use the library an existing Trompa Contributor environment

```python
import asyncio
import os
import trompace as ce

from trompace.config import config
from trompace.connection import submit_query
from trompace.mutations.person import mutation_create_artist

async def main():

    qry = mutation_create_artist(
        artist_name="A. J. Fynn",
        publisher="https://www.cpdl.org",
        contributor="https://www.cpdl.org",
        creator="https://www.upf.edu",
        source="https://www.cpdl.org/wiki/index.php/A._J._Fynn",
        language="en",
        formatin="text/html",
        date=datetime.now(),
        birthDate=1860,
        deathDate=1920,
    )

    response = await ce.connection.submit_query(qry)

    print(response)


if __name__ == "__main__":
    config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'import.ini')

    if os.path.exists(config_file):
        config.load(config_file)

    asyncio.run(main())
```

## License

```
Copyright 2019 Music Technology Group, Universitat Pompeu Fabra

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## Development

This package is published on pypi, and has documentation on readthedocs:

 * https://pypi.org/project/trompace-client/
 * https://trompace-client.readthedocs.io/en/latest/
 
To build and publish a new version:
 
    git tag v0.3
    git push --tags
    python setup.py sdist bdist_wheel
    twine upload dist/*
     
To release a version on github after pushing the tag, go to https://github.com/trompamusic/trompa-ce-client/releases/new
and choose the tag that you just pushed.

To build docs, go to https://readthedocs.org/projects/trompace-client/ and click
"Build version".