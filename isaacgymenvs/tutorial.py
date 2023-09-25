from isaacgym import gymapi

gym = gymapi.acquire_gym() # I can get all gymapi function. dir(gym) shows all api function.

# create a simulation
sim = gym.create_sim(compute_device_id, graphics_device_id, gymapi.SIM_PHYSX, sim_params)

'''
Simulation Parameters
'''

# get default set of parameters
sim_params = gymapi.SimParams() # what is the contents of params?

# set common parameters
sim_params.dt = 1 / 60
sim_params.substeps = 2 # substeps??
sim_params.up_axis = gymapi.UP_AXIS_Z 
sim_params.gravity = gymapi.Vec3(0.0, 0.0, -9.8)

# set PhysX-specific parameters
sim_params.physx.use_gpu = False
sim_params.physx.solver_type = 1
sim_params.physx.num_position_iterations = 6
sim_params.physx.num_velocity_iterations = 1
sim_params.physx.contact_offset = 0.01
sim_params.physx.rest_offset = 0.0

# set Flex-specific parameters
sim_params.flex.solver_type = 5
sim_params.flex.num_outer_iterations = 4
sim_params.flex.num_inner_iteration = 20
sim_params.flex.relation = 0.8
sim_params.flex.warm_start = 0.5

# create sim with those parameters
sim = gym.create_sim(compute_device_id, graphics_device_id, gymapi.SIM_PHYSX, sim_params)

'''
Creating a Ground Plane
'''

# configure the ground plane
plane_params = gymapi.PlaneParams()
plane_params.normal = gymapi.Vec3(0, 0, 1) # z-up! mainly for robotics research
plane_params.distance = 0
plane_params.static_friction = 1
plane_params.dynamic_friction = 1
plane_params.restitution = 0

# create the ground plane
gym.add_ground(sim, plane_param)

'''
Loading assets, robot body and mesh
'''

asset_root = "../../assets"
asset_file = "urdf/franka_description/robots/franka_panda.urdf" # supported both urdf and mjcf.
asset = gym.load_asset(sim, asset_root, asset_file)

# extra asset importer. Physical and visual model
asset_options = gymapi.AssetOptions()
asset_options.fix_base_link = True
asset_options.armature = 0.01

asset = gym.load_asset(sim, asset_root, asset_file, asset_options)

'''
Environments and Actors
'''
spacing = 2.0
lower = gymapi.Vec3(-spacing, 0.0, -spacing)
upper = gymapi.Vec3(spacing, spacing, spacing)

env = gym.create_env(sim, lower, upper, 8)

pose = gymapi.Transform()
pose.p = gymapi.Vec3(0.0, 1.0, 0.0) # actor position place.
pose.r = gymapi.Quat(-0.707107, 0.0, 0.0, 0.707107) # oriantation quaternion
   """
   pose.r = gymapi.Quat.from_axis_angle(gymapi.Vec3(1, 0, 0), -0.5 * math.pi)
   """ 

actor_handle = gym.create_actor(env, asset, pose, "MyActor", 0, 1)
