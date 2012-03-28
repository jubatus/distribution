
import recommender_types
import msgpackrpc

class recommender:
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

  def clear_row (self, name, id):
    name = name
    id = id

    return self.client.call('clear_row', name, id)

  def update_row (self, name, id, arg2):
    name = name
    id = id
    arg2 = arg2.to_array()

    return self.client.call('update_row', name, id, arg2)

  def clear (self, name):
    name = name

    return self.client.call('clear', name)

  def complete_row_from_id (self, name, id):
    name = name
    id = id

    return self.client.call('complete_row_from_id', name, id)

  def complete_row_from_data (self, name, arg1):
    name = name
    arg1 = arg1.to_array()

    return self.client.call('complete_row_from_data', name, arg1)

  def similar_row_from_id (self, name, id, size):
    name = name
    id = id
    size = size

    return self.client.call('similar_row_from_id', name, id, size)

  def similar_row_from_data (self, name, data, size):
    name = name
    data = data.to_array()
    size = size

    return self.client.call('similar_row_from_data', name, data, size)

  def decode_row (self, name, id):
    name = name
    id = id

    return self.client.call('decode_row', name, id)

  def get_all_rows (self, name):
    name = name

    return self.client.call('get_all_rows', name)

  def similarity (self, name, lhs, rhs):
    name = name
    lhs = lhs.to_array()
    rhs = rhs.to_array()

    return self.client.call('similarity', name, lhs, rhs)

  def l2norm (self, name, arg1):
    name = name
    arg1 = arg1.to_array()

    return self.client.call('l2norm', name, arg1)

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


