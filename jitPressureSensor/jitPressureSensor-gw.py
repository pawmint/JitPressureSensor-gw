#!/usr/bin/env python

import sys

from ubiGATE.ubigate.utils.logger import logger
from ubiGATE.ubigate.communication import mqtt_pusher
from ubiGATE.ubigate.config import conf

from sensors import pressure_signal


def get_signal():
    """
    Read the shell inputs
    """

    return sys.stdin.readline()

def gather_data(signal):
    """
    Call the 'matches' methode in order to analyse the inputs and to write them a standard way
    """

    data = None
    data = pressure_signal.matches(signal)

    return data


logger.info("Starting application")
server, house, username, password = conf.get_options()
logger.info('Server: %s\n'
            'House: %s\n'
            'Username: %s' % (server, house, username))


mqtt = mqtt_pusher.broker_connection("jitPressureSensor-gw_sensors", "127.0.0.1")

stop = 0
topic = "my/topic"

while stop == 0:

    signal = get_signal()
    logger.debug('Signal received: %s' % signal)
    data = gather_data(signal)
    if data is not None:
        print "signal received"
        for digit in ['D0', 'D1','D2', 'D3','D4', 'D5','D6', 'D7']:
            mqtt_pusher.push_data(data[digit], house)
            stop = mqtt_pusher.send(mqtt, topic)

mqtt_pusher.disconnection(mqtt)


