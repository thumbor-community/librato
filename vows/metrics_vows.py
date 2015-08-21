#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from pyvows import Vows, expect

from thumbor.context import Context, ServerParameters
from thumbor.importer import Importer
from thumbor.config import Config
import thumbor.metrics
import tc_librato.metrics.librato_metrics


@Vows.batch
class MetricsVows(Vows.Context):

    class CanCreateContextWithLibratoMetrics(Vows.Context):

        def topic(self):
            conf = Config()
            conf.METRICS = 'tc_librato.metrics.librato_metrics'
            conf.LIBRATO_USER = 'test'
            conf.LIBRATO_TOKEN = 'test'
            conf.LIBRATO_NAME_PREFIX = 'test'
            imp = Importer(conf)
            imp.import_modules()
            return Context(None, conf, imp)

        def should_initialize_librato(self, topic):
            expect(topic.metrics).to_be_instance_of(tc_librato.metrics.librato_metrics.Metrics)

        def should_not_fail_on_use(self, topic):
            expect(topic.metrics.incr('test.count')).not_to_be_an_error()
            expect(topic.metrics.incr('test.count', 2)).not_to_be_an_error()
            expect(topic.metrics.timing('test.time', 100)).not_to_be_an_error()
