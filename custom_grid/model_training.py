import gymnasium as gym
import custom_grid
from stable_baselines3 import DQN
import os
import time

models_dir = f"models/{int(time.time())}/"
logdir = f"logs/{int(time.time())}/"

if not os.path.exists(models_dir):
	os.makedirs(models_dir)

if not os.path.exists(logdir):
	os.makedirs(logdir)


env = gym.make("GridWorldEnv-v0", render_mode="human")

model = DQN("MultiInputPolicy", env, verbose=1, tensorboard_log=logdir)


TIMESTEPS = 10000
iters = 0
while True:
	iters += 1
	model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"DQN")
	model.save(f"{models_dir}/{TIMESTEPS*iters}")
	
