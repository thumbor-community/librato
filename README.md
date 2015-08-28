# Thumbor Librato Metrics Plugin

Send Thumbor runtime metrics to your Librato account.

## Status

[![Circle CI](https://circleci.com/gh/thumbor-community/librato.svg?style=svg&circle-token=099b759fa4d77b86eef5fba15565d435510062d7)](https://circleci.com/gh/thumbor-community/librato)

## Installation

```bash
# master branch
pip install -e git://github.com/thumbor-community/librato.git@master#egg=tc_librato

# latest stable
pip install tc_librato
```

## Configuration

```python
# thumbor.conf
METRICS = 'tc_librato.metrics.librato_metrics'

LIBRATO_USER = 'username' # Librato api username
LIBRATO_TOKEN = 'token' # Librato api token

# optional with defaults
LIBRATO_NAME_PREFIX = 'thumbor' # Librato metrics prefix
LIBRATO_QUEUE_LENGTH = 1000 # Librato autosubmit queue size
```
