import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    self.contents = [k for k,v in kwargs.items() for i in range(v)]
    print(self.contents)
    
  def draw(self, num):
    	if num>=len(self.contents):
    		return self.contents
    	arr =[]
    	for i in range(num):
    	  rand_choice = random.choice(self.contents)
    	  arr.append(rand_choice)
    	  self.contents.remove(rand_choice)
    	  
    	return arr

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	return 'todo'