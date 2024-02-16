from tkinter import *
import tkinter as tk
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

class TkDragAndDropObject():
  def __init__(self, root):
    self.root = root
    self.coord = TkCoords()
    self.coord.set(10, 10, 100, 100)
    self.block = self.root.create_rectangle(
      self.coord.x0, self.coord.y0, self.coord.x1, self.coord.y1, fill = "red")
    self.focus = 0

  def move(self, x, y):
    self.root.move(self.block, x, y)
    self.coord.x0, self.coord.y0, self.coord.x1, self.coord.y1 = self.root.coords(self.block)

class TkWindow():
  def __init__(self, root):
    self.root = root
    self.cfg = TkCfg()
    H = self.cfg.TkWindowW
    W = self.cfg.TkWindowW
    self.canv = tk.Canvas(self.root, width=H, height=H)
    self.canv.pack()
    self.canv.bind("<ButtonPress-1>", self.on_react_press)
    self.canv.bind("<B1-Motion>", self.on_react_move)
    self.canv.bind("<ButtonRelease-1>", self.on_react_release)
    self.example = TkDragAndDropObject(self.canv)
    self.x = 0
    self.y = 0

  def on_react_press(self, event):
    self.x, self.y = event.x, event.y
    self.example.focus = 1
    pass
  def on_react_move(self, event):
    x, y = self.x, self.y
    self.x, self.y = event.x, event.y
    if self.example.focus:
      self.example.move(self.x - x, self.y -y)
    pass
  def on_react_release(self, event):
    self.example.focus = 0
    pass

class TkView():
  def __init__(self):
    self.root = Tk()
    self.window = TkWindow(self.root)
    self.root.mainloop()