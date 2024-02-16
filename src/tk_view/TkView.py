from tkinter import *
import tkinter as tk
import random

class TkCfg():
  def __init__(self):
    self.TkWindowH = 1000
    self.TkWindowW = 1000

class TkCoords():
  def __init__(self):
    self.x0 = 0
    self.y0 = 0
    self.x1 = 0
    self.y1 = 0
  def set(self, x0, y0, x1, y1):
    self.x0 = x0
    self.y0 = y0
    self.x1 = x1
    self.y1 = y1
  def print(self):
    dbg = ""
    dbg = dbg + "[ " + str(self.x0) + " : " + str(self.y0) + " ]"
    dbg = dbg + "[ " + str(self.x1) + " : " + str(self.y1) + " ]"
    print(dbg)

class TkDragAndDrop():
  def __init__(self):
    self.coord = None
    self.root  = None
    self.obj   = None
    self.focus = None
  def move(self, x, y, e):
    self.root.move(self.obj, x, y)
    self.coord.x0, self.coord.y0, self.coord.x1, self.coord.y1 = self.root.coords(self.obj)
  def detect_focus(self, e):
    x0, y0, x1, y1 = self.root.coords(self.obj)
    if e.x > x0 and \
       e.x < x1 and \
       e.y > y0 and \
       e.y < y1 :
      self.focus = 1
    else:
      self.focus = 0
  def clean_focus(self):
    self.focus = 0
class TkConnector(TkDragAndDrop):
  def __init__(self, root, A, B):
    super(TkConnector, self).__init__()
    self.A = A
    self.B = B
    self.root = root
    self.coord = TkCoords()
    self.coord.x0 = A.coord.x0
    self.coord.y0 = A.coord.y0
    self.coord.x1 = A.coord.x1
    self.coord.y1 = A.coord.y1
    self.draw()
  def draw(self):
    self.obj = self.root.create_line(
      self.A.coord.x0 + ((self.A.coord.x1 - self.A.coord.x0) / 2),
      self.A.coord.y0 + ((self.A.coord.y1 - self.A.coord.y0) / 2),
      self.B.coord.x0 + ((self.B.coord.x1 - self.B.coord.x0) / 2),
      self.B.coord.y0 + ((self.B.coord.y1 - self.B.coord.y0) / 2),
      arrow=tk.BOTH,
      width=3,
      fill="black")
    self.root.tag_lower(self.obj)

  def update(self):
    self.root.delete(self.obj)
    self.draw()
    pass

class TkDragAndDropTxt(TkDragAndDrop):
  def __init__(self, root):
    super(TkDragAndDropTxt, self).__init__()
    self.root = root
    self.coord = TkCoords()
    self.coord.set(10, 10, 100, 100)
    self.obj = self.root.create_text(self.coord.x0, self.coord.y0, text = "TEST", fill = "black")
  def move(self, x, y, e):
    self.root.move(self.obj, x, y)
  def set_txt(self, var):
    self.root.delete(self.obj)
    self.obj = self.root.create_text(self.coord.x0, self.coord.y0, text = var, fill = "black")

class TkDragAndDropObject(TkDragAndDrop):
  def __init__(self, root):
    super(TkDragAndDropObject, self).__init__()
    self.root = root
    self.coord = TkCoords()
    self.coord.set(10, 10, 100, 100)
    self.obj = self.root.create_rectangle(
      self.coord.x0, self.coord.y0, self.coord.x1, self.coord.y1, fill = "red")
class GBox():
  def __init__(self, root):
    self.rectangle = TkDragAndDropObject(root)
    self.txt       = TkDragAndDropTxt(root)
  def move(self, x, y, e):
    self.rectangle.move(x, y, e)
    self.txt.move(x, y, e)
    self.txt.coord = self.rectangle.coord
  def get_focus(self):
    return self.rectangle.focus
  def detect_focus(self, e):
    self.rectangle.detect_focus(e)
  def clean_focus(self):
    self.rectangle.clean_focus()


class TkWindow():
  def __init__(self, root):
    self.root = root
    self.cfg = TkCfg()
    H = self.cfg.TkWindowW
    W = self.cfg.TkWindowW
    self.canv = tk.Canvas(self.root, width=H, height=H, bg = 'green')

    self.canv.pack()
    self.canv.bind("<ButtonPress-1>", self.on_react_press)
    self.canv.bind("<B1-Motion>", self.on_react_move)
    self.canv.bind("<ButtonRelease-1>", self.on_react_release)

#    self.knotsA = GBox(self.canv)
#    self.knotsB = GBox(self.canv)
#    self.knotsB.move(200, 200, None)
#    self.connector = TkConnector(self.canv, self.knotsA.rectangle, self.knotsB.rectangle)

    self.all_elem       = dict()
    self.all_connectors = []
#    self.all_elem.append(self.knotsA)
#    self.all_elem.append(self.knotsB)
    #self.all_elem.append(self.txt)
    self.x = 0
    self.y = 0

  def add_gbox(self, id):
    if id not in self.all_elem.keys():
      i = GBox(self.canv)
      self.all_elem[id] = i
    return self.all_elem[id]

  def add_connector(self, a, b):
    i =  TkConnector(self.canv, a.rectangle, b.rectangle)

    self.all_connectors.append(i)
    return i

  def on_react_press(self, event):
    self.x, self.y = event.x, event.y
    for k,e in self.all_elem.items():
      e.detect_focus(event)
      if e.get_focus():
        print("detected focus")
        e.rectangle.coord.print()
        dbg = "E [ " + str(self.x) + " : " + str(self.y) + " ]"
        print(dbg) 
        return
    pass
  def on_react_move(self, event):
    x, y = self.x, self.y
    self.x, self.y = event.x, event.y
    for k,e in self.all_elem.items():
      if e.get_focus() :
        print("detect Movement for object in focus")
        e.move(self.x - x, self.y - y, event)
    for e in self.all_connectors:
      e.update()
    pass
  def on_react_release(self, event):
    for k,e in self.all_elem.items():
      e.clean_focus()
    pass

class TkView():
  def __init__(self):
    self.root = Tk()
    self.window = TkWindow(self.root)

  def run(self):
    for k, e in self.window.all_elem.items():
      a = random.randint(20, 500)
      b = random.randint(20, 500)
      dbg = str(a) + " : " + str(b)
      print(dbg)
      e.move(a, b, None)
    self.root.mainloop()