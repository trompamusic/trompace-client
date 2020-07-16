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
import trompace.connection
from trompace.config import config
from trompace.mutations import person

config.load('trompace.ini')

mutation_musicbrainz = person.mutation_create_person(
    creator="https://github.com/trompamusic/trompa-ce-client/tree/v0.1/demo",
    contributor="https://musicbrainz.org",
    source="https://musicbrainz.org/artist/8d610e51-64b4-4654-b8df-064b0fb7a9d9",
    format_="text/html",
    title="Gustav Mahler - MusicBrainz",
    name="Gustav Mahler",
    birth_date="1860-07-07",
    death_date="1911-05-18",
    family_name="Mahler",
    given_name="Gustav",
    gender="male",
    language="en"
)

response = trompace.connection.submit_query(mutation_musicbrainz, auth_required=True)

print(response)
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