'''
Module for defining the Q Learning Agent.
'''
import numpy as np
import time

class QAgent():
    '''
    Q Learning Agent Class.
    '''

    def __init__(self, app):
        '''
        Parameters:
            app <Object>: The app for the agent to be trained on.
        '''

        self.app = app
       
        self.LEARNING_RATE = 0.1
        self.DISCOUNT = 0.95
        self.EPISODES = 15_000

        self.DISCRETE_OS_SIZE = [2] * len(app.observe())
        self.DISCRETE_OS_WIN_SIZE = (app.observe_max() - app.observe_min()) / self.DISCRETE_OS_SIZE
        
        self.START_EPSILON_DECAYING = 1
        self.END_EPSILON_DECAYING = self.EPISODES // 2
        self.epsilon = 0.05
        self.epsilon_decay_value = self.epsilon / (self.END_EPSILON_DECAYING
                                                   - self.START_EPSILON_DECAYING)

        self.SHOW_EVERY = 50

        self.q_table = []
        self.create_q_table()

    def create_q_table(self):
        '''
        Generates an intial Q Table.
        '''
        self.q_table = np.random.uniform(low=-2, high=1, 
                                         size=(self.DISCRETE_OS_SIZE + [2]))

    def get_discrete_state(self, state):
        '''
        Convertes a continuos state to a discrete one, allowing us
            to find it in our q_table.

        Parameters:
            state <np array>: The current state of the app.
        '''
        discrete_state = (state - self.app.observe_min()) / self.DISCRETE_OS_WIN_SIZE
        return tuple(discrete_state.astype(np.int))

    def select_action(self, current_discrete_state):
        '''
        Determines which action to take based on the q-value, or
            random action depending on epsilon.

        Parameters:
            current_discrete_state <np array>: The current game state.
        '''
        if np.random.random() > self.epsilon:
            action = np.argmax(self.q_table[current_discrete_state])
        else:
            action = np.random.randint(0,1)

        return action

    def adjust_table(self, new_discrete_state, current_discrete_state, action, reward):
        '''
        Adjusts our q_table with new q value based on action/reward.

        Parameters:
            current_discrete_state <np array>: The game state before we took the action.
            new_discrete_state <np array>: The game state after we took the action.
            action <int>: The action we took.
            reward <int>: The reward returned for performing action.
        '''
        max_future_q = np.max(self.q_table[new_discrete_state])

        current_q = self.q_table[current_discrete_state + (action,)]
        new_q = ((1 - self.LEARNING_RATE) * current_q 
                + self.LEARNING_RATE * (reward + self.DISCOUNT * max_future_q))

        self.q_table[current_discrete_state + (action,)] = new_q
