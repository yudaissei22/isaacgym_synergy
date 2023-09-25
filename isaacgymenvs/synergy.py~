from isaccgym import gymutil, gymapi, gymtorch
import numpy as np

class Model(Vectask):
    def __init__(self, cfg, args):
        self.cfg = cfg

    def create_sim(self, args):
        sim_params = gymapi.SimParams()
        
        """ read from yaml file is better? """
