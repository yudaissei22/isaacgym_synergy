from isaccgym import gymutil, gymapi, gymtorch
import numpy as np
import yaml # i dont know where the yaml file loaded in program

class Model:
    def __init__(self, cfg, args):
        self.cfg = cfg

    def create_sim(self, args):
        sim_params = gymapi.SimParams()
        
        """ read from yaml file """
        sim_params.dt = self.dt
        if self.cfg["sim"]["up_axis"] == "z":
            sim_params.up_axis = gymapi_.UP_AXIS_Z
