import random
import copy
from collections import Counter
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    self.contents = [k for k,v in kwargs.items() for i in range(v)]
    self.cpy_contents = self.contents[:]  
    
  def draw(self, num):
    if num>len(self.contents):
      #print(self.contents)
      return self.cpy_contents
    arr =[]
    for i in range(num):
      rand_choice = random.choice(self.contents)
      arr.append(rand_choice)
      self.contents.remove(rand_choice)
    return arr

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(num_experiments):
    cap = copy.deepcopy(hat)
    draw = cap.draw(num_balls_drawn)
    draw_count = Counter(draw)
    expected = True
    for color in expected_balls:
      try:
        if expected_balls[color] > draw_count[color]:
          #print(draw_count)
          expected = False
      except:
        #print(draw_count)
        expected = False
        
    if expected:
      M +=1
      #print(draw_count, draw_count[color])
  return M/num_experiments