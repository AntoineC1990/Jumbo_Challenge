import gymnasium as gym
from stable_baselines3 import DQN
import custom_grid


models_dir = "models/YourModelTiming" # to modify

env = gym.make("GridWorldEnv-v0", render_mode="human")
env.reset()

model_path = f"{models_dir}/xxxxx.zip"
model = DQN.load(model_path, env=env)

episodes = 5

for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        env.render()
        print(rewards)