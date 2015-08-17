# coding: utf-8
from thumbor.config import Config

Config.define('LIBRATO_USER', None, 'Librato api username', 'Metrics')
Config.define('LIBRATO_TOKEN', None, 'Librato api token', 'Metrics')
Config.define('LIBRATO_NAME_PREFIX', 'thumbor', 'Librato metrics prefix', 'Metrics')
Config.define('LIBRATO_QUEUE_LENGTH', 1000, 'Librato autosubmit queue size', 'Metrics')
