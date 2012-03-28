
import stat_types
import msgpackrpc

class stat:
  def __init__ (self, host, port):
    address = msgpackrpc.Address(host, port)
    self.client = msgpackrpc.Client(address)

  def set_config (self, name, c):
    name = name
    c = c.to_array()

    return self.client.call('set_config', name, c)

  def get_config (self, name):
    name = name

    return self.client.call('get_config', name)

  def push (self, arg0, arg1, arg2):
    arg0 = arg0
    arg1 = arg1
    arg2 = arg2

    return self.client.call('push', arg0, arg1, arg2)

  def sum (self, arg0, arg1):
    arg0 = arg0
    arg1 = arg1

    return self.client.call('sum', arg0, arg1)

  def stddev (self, arg0, arg1):
    arg0 = arg0
    arg1 = arg1

    return self.client.call('stddev', arg0, arg1)

  def max (self, arg0, arg1):
    arg0 = arg0
    arg1 = arg1

    return self.client.call('max', arg0, arg1)

  def min (self, arg0, arg1):
    arg0 = arg0
    arg1 = arg1

    return self.client.call('min', arg0, arg1)

  def entropy (self, arg0, arg1):
    arg0 = arg0
    arg1 = arg1

    return self.client.call('entropy', arg0, arg1)

  def moment (self, arg0, arg1, n, c):
    arg0 = arg0
    arg1 = arg1
    n = n
    c = c

    return self.client.call('moment', arg0, arg1, n, c)

  def save (self, name, arg1):
    name = name
    arg1 = arg1

    return self.client.call('save', name, arg1)

  def load (self, name, arg1):
    name = name
    arg1 = arg1

    return self.client.call('load', name, arg1)

  def get_status (self, name):
    name = name

    return self.client.call('get_status', name)


