class Item:
  def __init__(self, id):
    self.id = id      # Unique ID for item
    self.p = dict()   # List of Parent(s) item(s)
    self.c = dict()   # List of Child(s) item(s)
    self.paths_c = [] # List of paths
    self.paths_p = [] # List of paths

  def get_id(self):
    """ Return id of the current object.
    ID is returned as an INT item.
    """
    return self.id

  def set_id(self, id):
    """ Set new id for the current object.
    """
    self.id = id

  def add_p(self, item):
    """ Add new parent Item.
    Create new entry in parent dictionray.
    Parent can only be present once.
    <ID> is used to distinguish between different items.
    Current object is also set as Child of the new Parent.
    """
    if item.get_id() not in self.p.keys():
      self.p[item.get_id()] = item
      item.add_c(self)

  def add_c(self, item):
    """ Add new child Item.
    Create new entry in child dictionray.
    Child can only be present once.
    <ID> is used to distinguish between different items.
    Current object is also set as Parent of the new Child.
    """
    if item.get_id() not in self.c.keys():
      self.c[item.get_id()] = item
      item.add_p(self)

  def get_path_top_down_c_recursive(self, root, path):
    """ Traverse the entire hierarchy and return all paths.
    This function is recursive and in this implementation there
    are no checks to prevent infinite loops in case of cyclic
    connections. This function is not meant to be used directly from
    user but it is an internal utility function.
    """
    p = path
    p.append(self)
    for i in self.c:
      a = []
      for ii in p:
        a.append(ii)
      self.c[i].get_path_top_down_c_recursive(root, a)
    if len(self.c) == 0:
      root.paths_c.append(p)

  def get_path_top_down_c(self):
    """ User function to get all the possible paths that can be
    reached from the root element.
    """
    self.get_path_top_down_c_recursive(self, [])
    return self.paths_c

  def get_path_top_down_p_recursive(self, root, path):
    """ Traverse the entire hierarchy and return all paths.
    This function is recursive and in this implementation there
    are no checks to prevent infinite loops in case of cyclic
    connections. This function is not meant to be used directly from
    user but it is an internal utility function.
    """
    p = path
    p.append(self)
    for i in self.p:
      a = []
      for ii in p:
        a.append(ii)
      self.p[i].get_path_top_down_p_recursive(root, a)
    if len(self.p) == 0:
      root.paths_p.append(p)

  def get_path_top_down_p(self):
    """ User function to get all the possible paths that can be
    reached from the root element.
    """
    self.get_path_top_down_p_recursive(self, [])
    return self.paths_p


  def print_path(self, p):
    """ Utility function to print a path in a readable format by
    using the <id> of each object.
    """
    s = ""
    for i in p:
      if i.get_id() == p[0].get_id():
        s = str(i.get_id())
      else:
        s = s + " --> " + str(i.get_id())
    print(s)
