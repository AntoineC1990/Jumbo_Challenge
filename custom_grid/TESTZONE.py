import numpy as np
import pygame
import gymnasium as gym
from gymnasium import spaces
import custom_grid

# Créez une instance de l'environnement GridWorldEnv
env = gym.make("GridWorldEnv-v0", render_mode="human")

# Réinitialisez l'environnement pour obtenir l'observation initiale
observation, info = env.reset()

# Créez une fenêtre Pygame pour l'affichage
while True:
    env.render()

    # Effectuez une action aléatoire (0, 1, 2 ou 3) pour l'exemple
    action = env.action_space.sample()
    observation, reward, terminated, _ = env.step(action)

    # Si l'épisode est terminé, réinitialisez l'environnement
    if terminated:
        observation, info = env.reset()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.done = True