from m5stack import *
from m5stack_ui import *
from uiflow import *

import time

class Terminal:
 
  def __init__(self, color=0x00ff00, bg_color=0x000000):
    self.color = color
    self.bg_color = bg_color
    self.lines = []
   
    self.screen = M5Screen()
    self.screen.clean_screen()
    self.screen.set_screen_bg_color(bg_color)
   
    self.line_labels = [
      M5Label('', x=3, y=i * 15, color=self.color, font=FONT_MONT_14, parent=None) for i in range(15)
    ]
 
  def print(self, line):
    self.lines.append(str(line))
    self.update()
   
  def update(self, start_index=None, nb_lines=15):
    start_index = start_index or max(0, len(self.lines) - nb_lines)
   
    lines = self.lines[start_index:start_index + nb_lines]
   
    for i, line in enumerate(lines):
      self.line_labels[i].set_text(str(start_index + i) + ": " + line)
   
 
t = Terminal()

# simulating incoming data
for i in range(20):
  t.print(i ** 2)
  wait_ms(100)