import random
import string
from datetime import datetime

eventid = datetime.now().strftime('%Y/%S/') 
alpha = ['AB','AC']
nums = random.randint(100,999)

def matric_no():
      alphas = random.choice(alpha)
      # results = random.choice(alpha,nums)
      return f'{eventid}{nums}{alphas}'

