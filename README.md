[![iThenticate](http://www.ithenticate.com/Portals/92785/images/iThenticate_Logo.png =75px)](http://www.ithenticate.com/)
[![Turnitin](http://go.turnitin.com/l/45292/2015-07-07/37ty9m/45292/77056/turnitin_logo_primary_rgb.png =100px)](http://turnitin.com/)

# iThenticate API client Python

This package provides an [iThenticate API](https://guides.turnitin.com/iThenticate/iThenticate_API_Guide) Client for Python. You may also use this client for a [Turnitin](http://turnitin.com/) account, which uses the iThenticate API.

[![PyPI version](https://badge.fury.io/py/ithenticate-api-python.svg)](https://badge.fury.io/py/ithenticate-api-python)

## Installation ##

The easiest way to install is with [pip](https://pip.pypa.io).
```
$ pip install ithenticate-api-python
```

## Getting started ##

Requiring the iThenticate API Client.

```python
import iThenticate
```

Initializing the iThenticate API client, and login.

```python
client = iThenticate.API.Client('test_username', 'test_password')
client.login()
```

## License ##
[BSD (Berkeley Software Distribution) License](https://opensource.org/licenses/bsd-license.php).
Copyright (c) 2017, Jorran de Wit.
