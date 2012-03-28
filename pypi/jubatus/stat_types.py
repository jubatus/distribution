
#/usr/bin/python
# -*- coding:utf-8 -*-

# This file is auto-generated from TYPES
# *** DO NOT EDIT ***


import sys
import msgpack


class config_data:

  def __init__(self, window_size):
    self.window_size = window_size

  def to_array(self):
    variables = []
    variables.append(self.window_size)

    return variables


