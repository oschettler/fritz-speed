#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
graph-traffic.py
"""

import os
import datetime

import rrdtool

from common import read_configuration

def main():
    prefs = read_configuration(os.path.join(os.path.dirname(__file__),'fritz-speed.ini'))
    for g in prefs['graphs_uptime']:
        # graph the data for information about parameters see https://oss.oetiker.ch/rrdtool/doc/rrdgraph.en.html
        rrdtool.graph(g['filename'],
            "--watermark", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "--left-axis-formatter", "duration",
            "-t", g['title'],
            "-w", g['graph_width'],
            "-h", g['graph_height'],
            "-s", "end-"+g['interval']+"s",
            "DEF:uptime="+g['rra_filename_uptime']+":uptime:AVERAGE",
            "CDEF:uptime_ms=uptime,1000,*",
            prefs['graph_type_up']+":uptime_ms#"+prefs['graph_color_up']+":Uptime",
            "-v", "Uptime")

if __name__ == '__main__':
    main()
