#!/usr/bin/env python
#-*- coding: utf-8 -*-

import json
import random

pretty = lambda x: json.dumps(x, indent=4, sort_keys=True)

def random_hex(size):
   return ''.join([random.choice('0123456789abcdef') for x in range(size)])
   
def randomID():
    return "{0}.{1}".format(random_hex(7), random_hex(6))



def naked(node):

    stripped, replacements = _naked(node)

    # Final parents and wires replacement
    strjson = json.dumps(stripped)
    for key, value in replacements.iteritems():
        strjson = strjson.replace(key, value)

    return json.loads(strjson)


def _naked(node, replacements=dict()):

    _id = node.get('id')
    if _id:
        if _id in replacements:
            replacement = replacements[_id]
        else:
            replacement = randomID()
            replacements[_id] = replacement
            
        
        node['id'] = replacement

        _nodes = node.get('nodes')
        if _nodes:
            for innernode in _nodes:
                innernode, _replaces = _naked(innernode, replacements)
                replacements.update(_replaces)

    return node, replacements
