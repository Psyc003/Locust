import os
import shutil

class Worm:
  def __init__(self, path=None, target_dir_list=None, iteration=None):
    if isinstance(path, type(None)):
      self.path = "/"
    else:
      self.path = path
    
    if isinstance(target_dir_list, type(None)):
      self.target_dir_list = []
    else:
      self.target_dir_list = target_dir_list
    
    if isinstance(target_dir_list, type(None)):
      self.iteration = 2
    else:
      self.iteration = iteration
    
    # finding path
    self.own_path = os.path.realpath(__file__)
    # not complete
    
