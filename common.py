# -*- coding: utf-8 -*-

"""
common.py

commong helper functions used by the fritz-speed scripts
"""

import ConfigParser

def read_graphs(cfg, graph_sections):
    graphs = []
    for graph_section in graph_sections:
        graph = dict(cfg.items(graph_section))
        graphs.append(graph)
    return graphs

def read_configuration(filename):
    """
    reads configuration from the configuration file and prepares
    a preferences dict
    """

    cfg = ConfigParser.ConfigParser()
    cfg.read(filename)
    preferences = {}
    for name, value in cfg.items('DEFAULT'):
        preferences[name] = value

    graph_sections = [g for g  in cfg.sections() if g is not 'DEFAULT' and not g.endswith('_uptime')]
    preferences['graphs'] = read_graphs(cfg, graph_sections)

    graph_sections = [g for g  in cfg.sections() if g is not 'DEFAULT' and g.endswith('_uptime')]
    preferences['graphs_uptime'] = read_graphs(cfg, graph_sections)

    return preferences


