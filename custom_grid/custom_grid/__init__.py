from gymnasium.envs.registration import register


register(
     id="GridWorldEnv-v0",
     entry_point="custom_grid.envs:GridWorldEnv",
     max_episode_steps=300,
)