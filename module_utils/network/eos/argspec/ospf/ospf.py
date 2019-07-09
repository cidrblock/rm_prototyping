#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The arg spec for the eos_ospf module
"""


class OspfArgs(object):  # pylint: disable=R0903
    """The arg spec for the eos_ospf module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {'config': {'options': {'processes': {'elements': 'dict',
                                      'options': {'adjacency': {'options': {'exchange_start': {'options': {'threshold': {'type': 'int'}},
                                                                                               'type': 'dict'}},
                                                                'type': 'dict'},
                                                  'areas': {'elements': 'dict',
                                                            'options': {'area': {'type': 'str'},
                                                                        'default_cost': {'type': 'int'},
                                                                        'default_information': {'options': {'metric': {'type': 'int'},
                                                                                                            'metric_type': {'choices': [1,
                                                                                                                                        2],
                                                                                                                            'type': 'int'},
                                                                                                            'nssa_only': {'type': 'bool'},
                                                                                                            'originate': {'type': 'bool'}},
                                                                                                'type': 'dict'},
                                                                        'filters': {'elements': 'str',
                                                                                    'type': 'list'},
                                                                        'no_summary': {'type': 'bool'},
                                                                        'nssa_only': {'type': 'bool'},
                                                                        'ranges': {'elements': 'dict',
                                                                                   'options': {'cost': {'type': 'int'},
                                                                                               'not_advertise': {'type': 'bool'},
                                                                                               'range': {'type': 'str'}},
                                                                                   'type': 'list'},
                                                                        'type': {'type': 'str'}},
                                                            'type': 'list'},
                                                  'auto_cost': {'options': {'reference_bandwidth': {'type': 'int'}},
                                                                'type': 'dict'},
                                                  'bfd': {'options': {'all_interfaces': {'type': 'bool'}},
                                                          'type': 'dict'},
                                                  'compatible': {'options': {'rfc1583': {'type': 'bool'}},
                                                                 'type': 'dict'},
                                                  'id': {'type': 'int'},
                                                  'vrf': {'type': 'str'}},
                                      'type': 'list'}},
            'type': 'dict'},
 'state': {'choices': ['merged', 'replaced', 'overridden', 'deleted'],
           'default': 'merged',
           'type': 'str'}}  # pylint: disable=C0301