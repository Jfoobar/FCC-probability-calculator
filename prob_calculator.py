import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    self.contents = [k for k,v in kwargs.items() for i in range(v)]
    print(self.contents)
    
  def draw(self, num):
      cpy_contents = self.contents.copy()
      if num>=len(self.contents):
    		 return self.contents
      arr =[]
      for i in range(num):
    	  rand_choice = random.choice(cpy_contents)
    	  arr.append(rand_choice)
    	  cpy_contents.remove(rand_choice)
    	  
      return arr

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  for i in range(num_experiments):
    draw = hat.draw(num_balls_drawn)
    print(draw)
    # make dict from draw and then see if mathces expected_balls
    #if not same set flag to false
  
  return 'todo'