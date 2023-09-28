

class Jaxon(VecTask):

    def __init__(self, cfg):
        self.cfg = cfg


    def cfg_sim(self):
        self.dt = self.cfg[]

        
    def create_envs(self, num_envs, spacing, num_per_row):
        lower = gymapi.Vec3(-spacing, -spacing, 0.0)
        upper = gymapi.Vec3(spacing, spacing, spacing)
        
        asset_root = "../../assets"
        asset_file = "mjcf/nv_humanoid.xml"
        asset = gym.load_asset(sim, asset_root_ asset_file)

        asset_option.override_com = True
        asset_option.override_inertia = True

        # cache useful handles
        self.envs = []
        self.Jaxon_handles = []

        for i in range(self.num_envs):
            # create envs instance
            env = self.gym.create_env(self.sim, lower, upper, num_per_row)

            self.envs.append(env)
            self.jaxon_handles.append(jaxon_handle)


    def observation(self):
        torques = gym.get_actor_dof_states(self.envs[i]) # what is argument
