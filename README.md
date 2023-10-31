# Important:

I would like to thank Christophe R. from Jumbo Mana for proposing this challenge. I am grateful for the time he has given me. Thank you for providing me with the motivation and opportunity to explore machine learning approaches for purposes other than classification.

In one week, it was very difficult for me to balance my work as a molecular biologist, my coursework, my family life, and my rest. I was only able to work in 1-2 hour sessions.

Here is my work, which does not deserve much attention as it is essentially a shell at the moment.

## Remaining work to perform (most important):

- Add obstacles to my environment and restrict their access to the AI agent.
- Add an orientation to the goal.
- Find relevant rewards and punishments (punish/restrict agent access in front of the goal, reward the shortest distance by passing behind the goal).
- Train the AI on more complex environments (random obstacles).
- Modify the Deep Q network hyperparameters.

# Jumbo_Challenge

The purpose of this challenge is to create an AI dedicated to bypassing an enemy player. In a 12x12 matrix, the AI will learn to navigate and bypass a stationary player. The player and AI are randomly placed in the grid. The player remains static, and the AI must find the most efficient path to bypass the player. To solve this problem, we use a Deep Q-Learning AI based on the Stable Baselines 3 framework. The AI is trained to mimic realistic player behavior and arrive behind the player successfully.

# Getting Started

To deploy and reproduce the results of this project, follow these steps:

- Install the packages listed below.
- Clone this repository to your local machine.
- Install the custom environment package as mentioned below.

```bash
pip install -e custom_grid
```

## Project Structure

- setup.py: Contains the package setup information.
- TESTZONE.py: Allows you to visualize the environment.
- model_training.py: Used for training the Deep Q-Network (DQN) model and saving it.
- model_load.py: Used to load a trained DQN model and visualize its performance.

custom_grid/: A package for custom gym environments.

- custom_grid/init.py: Initializes the custom environment package.
- custom_grid/envs/init.py: Initializes the custom environment sub-package.
- custom_grid/envs/grid_world.py: Defines the custom grid world environment using Gym.

## Packages

NumPy: https://numpy.org
Pygame: https://www.pygame.org
Gym: https://gym.openai.com
Setuptools: https://setuptools.readthedocs.io/en/latest/
Stable Baselines3: https://stable-baselines3.readthedocs.io/en/master/

# Usage

Use the provided Python scripts for model training and visualization (model_training.py and model_load.py).
Experiment with the environment using TESTZONE.py.

# Training

While the model trains, we can view the results over time by opening a new terminal and doing: tensorboard --logdir=logs

# Contribution

Help me, I'm struggling so hard with the custom environment and with the rewards/sanctions of the AI.
