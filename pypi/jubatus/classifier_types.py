
#/usr/bin/python
# -*- coding:utf-8 -*-

# This file is auto-generated from TYPES
# *** DO NOT EDIT ***


import sys
import msgpack


class string_rule:

  def __init__(self, key, t, sample_weight, global_weight):
    self.key = key
    self.t = t
    self.sample_weight = sample_weight
    self.global_weight = global_weight

  def to_array(self):
    variables = []
    variables.append(self.key)
    variables.append(self.t)
    variables.append(self.sample_weight)
    variables.append(self.global_weight)

    return variables

class filter_rule:

  def __init__(self, key, t, suffix):
    self.key = key
    self.t = t
    self.suffix = suffix

  def to_array(self):
    variables = []
    variables.append(self.key)
    variables.append(self.t)
    variables.append(self.suffix)

    return variables

class num_rule:

  def __init__(self, key, t):
    self.key = key
    self.t = t

  def to_array(self):
    variables = []
    variables.append(self.key)
    variables.append(self.t)

    return variables

class converter_config:

  def __init__(self, string_filter_types, string_filter_rules, num_filter_types, num_filter_rules, string_types, string_rules, num_types, num_rules):
    self.string_filter_types = string_filter_types
    self.string_filter_rules = string_filter_rules
    self.num_filter_types = num_filter_types
    self.num_filter_rules = num_filter_rules
    self.string_types = string_types
    self.string_rules = string_rules
    self.num_types = num_types
    self.num_rules = num_rules

  def to_array(self):
    variables = []
    variables.append({k : v.to_array() for k,v in self.string_filter_types.items()})
    variables.append([elem.to_array() for elem in self.string_filter_rules])
    variables.append({k : v.to_array() for k,v in self.num_filter_types.items()})
    variables.append([elem.to_array() for elem in self.num_filter_rules])
    variables.append({k : v.to_array() for k,v in self.string_types.items()})
    variables.append([elem.to_array() for elem in self.string_rules])
    variables.append({k : v.to_array() for k,v in self.num_types.items()})
    variables.append([elem.to_array() for elem in self.num_rules])

    return variables

class config_data:

  def __init__(self, method, config):
    self.method = method
    self.config = config

  def to_array(self):
    variables = []
    variables.append(self.method)
    variables.append(self.config.to_array())

    return variables

class datum:

  def __init__(self, sv, nv):
    self.sv = sv
    self.nv = nv

  def to_array(self):
    variables = []
    variables.append([elem.to_array() for elem in self.sv])
    variables.append([elem.to_array() for elem in self.nv])

    return variables

class estimate_result:

  def __init__(self, label, prob):
    self.label = label
    self.prob = prob

  def to_array(self):
    variables = []
    variables.append(self.label)
    variables.append(self.prob)

    return variables


