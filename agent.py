import torch
import random
import numpy as np
from collections import deque
# TODO from model import Linear_QNet, QTrainer


MAX_MEMORY = 100000
BATCH_SIZE = 1000
LR = 0.001


class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0  # randomness
        self.gamma = 0.9  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)  # popleft()
        # TODO model and trainer

    def get_state(self, game):
        # Extract relevant information from the game object
        player_x, player_y = game.player.position
        enemy_x, enemy_y = game.enemy.position
        power_ups = game.power_ups_available
        obstacles = game.obstacles_present
        game_score = game.score

        # Encode the state information into a suitable format
        state = [player_x, player_y, enemy_x, enemy_y, power_ups, obstacles, game_score]

        # Convert the state into a numpy array or torch tensor
        state = np.array(state)

        return state

    def get_action(self, state):
        # Implement the logic to choose an action based on the current state
        final_move = [0, 0, 0, 0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 3)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1
        return final_move

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))  # popleft if MAX_MEMORY is reached

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)  # list of tuples
        else:
            mini_sample = self.memory
        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)


if __name__ == '__main__':
    agent = Agent()
