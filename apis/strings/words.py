import re

def words(str):
  return re.split('[^a-zA-Z-]+', str)