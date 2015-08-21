# Thumbor Librato Metrics Plugin

Send Thumbor runtime metrics to your Librato account.

## Installation

```bash
pip install tc_librato
```

## Configuration

```python
LIBRATO_USER = 'username' # Librato api username
LIBRATO_TOKEN = 'token' # Librato api token

# optional with defaults
LIBRATO_NAME_PREFIX = 'thumbor' # Librato metrics prefix
LIBRATO_QUEUE_LENGTH = 1000 # Librato autosubmit queue size
```
