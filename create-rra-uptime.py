#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
create-rra-uptime.py

creates RRD file with 60 seconds primary step length
four datasources which are counters
three RRA for one day, one week and one mont
"""

import fritzconnection
import rrdtool
import os

from common import read_configuration

def get_uptime():
    fc = fritzconnection.FritzConnection()
    status = fc.call_action('WANIPConnection', 'GetStatusInfo')
    uptime = status['NewUptime']
    return uptime

def main():
    uptime = get_uptime()
    max_uptime = uptime*1.1
    rrdtool.create(prefs['rra_filename_uptime'], '--step', '60',
        'DS:uptime:GAUGE:500:0:'+str(max_uptime),
        'RRA:AVERAGE:0.8:1:1440',
        'RRA:AVERAGE:0.8:10:1008',
        'RRA:AVERAGE:0.8:60:5040' )

if __name__ == '__main__':
    prefs = read_configuration('fritz-speed.ini')
    main()
