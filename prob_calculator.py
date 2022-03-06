import random
import copy
from collections import Counter

class Hat:
  def __init__(self,**kwargs):
    #make a list from dict argument
    self.contents = [k for k,v in kwargs.items() for i in range(v)] 
    
  def draw(self, num):
    if num>len(self.contents):
      return self.contents
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
      if expected_balls[color] > draw_count[color]:
        #less than expected
        expected = False
    #if all colors in draw are >= to the corresponding colors in expected_balls, add 1 to M  
    if expected:
      M +=1
  return M/num_experiments