
import regression_types
import msgpackrpc

class regression:
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

  def train (self, arg0, arg1):
    arg0 = arg0
    arg1 = [elem.to_array() for elem in arg1]

    return self.client.call('train', arg0, arg1)

  def estimate (self, arg0, arg1):
    arg0 = arg0
    arg1 = [elem.to_array() for elem in arg1]

    return self.client.call('estimate', arg0, arg1)

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


