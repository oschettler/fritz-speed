#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
uptime-monitor.py

querys the Fritz!Box via the TR-064 interface and writes uptime counters
into round robin archive (RRA).
"""
import os

import fritzconnection
import rrdtool

from common import read_configuration

def update_rra (rra_filename, *args):
    data = ":".join(args)
    rrdtool.update(rra_filename, "N:"+data)

def main():
    prefs = read_configuration(os.path.join(os.path.dirname(__file__),'fritz-speed.ini'))
    fc = fritzconnection.FritzConnection()
    status = fc.call_action('WANIPConnection', 'GetStatusInfo')
    uptime =  status['NewUptime']
    update_rra(prefs['rra_filename_uptime'], str(uptime))

if __name__ == '__main__':
    main()
