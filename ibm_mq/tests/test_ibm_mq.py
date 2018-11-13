# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import logging

from six import iteritems

from datadog_checks.ibm_mq import IbmMqCheck

log = logging.getLogger(__file__)

METRICS = [
    'ibm_mq.queue.service_interval',
    'ibm_mq.queue.inhibit_put',
    'ibm_mq.queue.depth_low_limit',
    'ibm_mq.queue.inhibit_get',
    'ibm_mq.queue.harden_get_backout',
    'ibm_mq.queue.service_interval_event',
    'ibm_mq.queue.trigger_control',
    'ibm_mq.queue.usage',
    'ibm_mq.queue.scope',
    'ibm_mq.queue.type',
    'ibm_mq.queue.depth_max',
    'ibm_mq.queue.backout_threshold',
    'ibm_mq.queue.depth_high_event',
    'ibm_mq.queue.depth_low_event',
    'ibm_mq.queue.trigger_message_priority',
    'ibm_mq.queue.depth_current',
    'ibm_mq.queue.depth_max_event',
    'ibm_mq.queue.open_input_count',
    'ibm_mq.queue.persistence',
    'ibm_mq.queue.trigger_depth',
    'ibm_mq.queue.max_message_length',
    'ibm_mq.queue.depth_high_limit',
    'ibm_mq.queue.priority',
    'ibm_mq.queue.input_open_option',
    'ibm_mq.queue.message_delivery_sequence',
    'ibm_mq.queue.retention_interval',
    'ibm_mq.queue.open_output_count',
    'ibm_mq.queue.trigger_type',
    'ibm_mq.queue.depth_percent',
    'ibm_mq.queue_manager.dist_lists',
    'ibm_mq.queue_manager.max_msg_list',
]

OPTIONAL_METRICS = [
    'ibm_mq.queue.max_channels',
    'ibm_mq.channel.batch_size',
    'ibm_mq.channel.batch_interval',
    'ibm_mq.channel.long_retry_count',
    'ibm_mq.channel.long_retry_interval',
    'ibm_mq.channel.max_message_length',
    'ibm_mq.channel.short_retry_count',
]


def test_check(aggregator, instance, spin_up_ibmmq, seed_data):
    check = IbmMqCheck('ibm_mq', {}, {})
    check.check(instance)

    for m, v in iteritems(aggregator._metrics):
        log.warning("{} {}".format(m, v))

    for metric in METRICS:
        aggregator.assert_metric(metric)

    for metric in OPTIONAL_METRICS:
        aggregator.assert_metric(metric, at_least=0)

    aggregator.assert_all_metrics_covered()

    assert False
