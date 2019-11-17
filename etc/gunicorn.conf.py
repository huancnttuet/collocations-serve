# file gunicorn.conf.py
# coding=utf-8
# Reference: https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
import multiprocessing
import logging.config

import yaml

# load config for logging
with open('etc/logging.yml', 'r') as f:
    _config = yaml.safe_load(f.read())
    logging.config.dictConfig(_config)
# end load config for logging

bind = '0.0.0.0:5000'
workers = multiprocessing.cpu_count() * 2 + 1

timeout = 3 * 60  # 3 minutes
keepalive = 24 * 60 * 60  # 1 day

capture_output = True
