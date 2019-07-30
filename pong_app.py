'''
My attempt at using q-learning to play pong.
s u c c 
e s s f u l
'''
import pygame
import player
import ball
import scoreboard
import q_agent
import numpy as np

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class PongApp():
    '''
    Main class which controls the game.
    '''

    def __init__(self):
        '''
        '''

        self.window_size = (1000, 1000)
        self.window = pygame.display.set_mode(self.window_size)

        pygame.init()
        pygame.display.init()
        pygame.font.init()

        self.agent_1_reward = -1
        self.agent_2_reward = -1

        self.running = False

    def run(self):
        '''
        Main loop for running the game/training the agent.
        '''
        self.window.fill(BLACK)        
        self.clock = pygame.time.Clock()

        self.player_1 = player.Player(100, 100, 5, 150, self.window, WHITE, 5)
        self.player_2 = player.Player(900, 100, 5, 150, self.window, WHITE, 5)

        self.pong_ball = ball.Ball(500, 100, 10, 10, self.window, WHITE, -1, 1)

        self.score_board = scoreboard.Scoreboard(500, 10, 
                           str(self.player_1.score) + str(self.player_2.score), 
                           30, self.window)

        self.agent_1 = q_agent.QAgent(self)
        self.agent_2 = q_agent.QAgent(self)

        self.p1_wins = 0
        self.p2_wins = 0
        for i in range(self.agent_1.EPISODES):
            
            if i % self.agent_1.SHOW_EVERY == 0:
                self.render = True
            
            else:
                self.render = False

            self.running = True
            while self.running:
                current_state = self.observe()
                current_discrete_state = self.agent_1.get_discrete_state(current_state)

                agent_1_action = self.agent_1.select_action(current_discrete_state)
                agent_2_action = self.agent_2.select_action(current_discrete_state)

                self.player_1.perform_action(agent_1_action, self.pong_ball.rect.y, self, 'agent_1')
                self.player_2.perform_action(agent_2_action, self.pong_ball.rect.y, self, 'agent_2')

                self.event_handler()
                
                self.pong_ball.move_ball()

                self.check_collision()

                new_state = app.observe()
                new_discrete_state = self.agent_1.get_discrete_state(new_state)

                if self.running:
                    self.agent_1.adjust_table(new_discrete_state, current_discrete_state, 
                                              agent_1_action, self.agent_1_reward)
                    self.agent_2.adjust_table(new_discrete_state, current_discrete_state, 
                                              agent_2_action, self.agent_2_reward)

                if self.render:
                    self.window.fill(BLACK)
                    self.player_1.draw_self()
                    self.player_2.draw_self()
                    self.pong_ball.draw_self()
                    self.score_board.display_scoreboard()

                    pygame.display.update()
            
            print("P1: ", self.p1_wins, "P2: ", self.p2_wins)
            print(i)
            
    def event_handler(self):
        '''
        Handles all pygame events.
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP]:
        #     self.player_1.perform_action(0)
        # if keys[pygame.K_DOWN]:
        #     self.player_1.perform_action(1)

    def check_collision(self):
        '''
        Checks for collision between ball & player, as well as
            ball & wall.
        '''
        if pygame.sprite.collide_rect(self.pong_ball, self.player_2):
            self.pong_ball.x_speed *= -1
            self.agent_2_reward = 1 
        elif pygame.sprite.collide_rect(self.pong_ball, self.player_1):
            self.pong_ball.x_speed *= -1
            self.agent_1_reward = 1
        if self.pong_ball.rect.y < 0 or self.pong_ball.rect.y > 1000:
            self.pong_ball.y_speed *= -1

        if self.pong_ball.rect.x < 0:
            self.player_2.score += 1 
            self.agent_1_reward = -1    
            self.p2_wins += 1      
            self.score_board.message = str(self.player_1.score) + str(self.player_2.score)
            self.pong_ball.reset_ball()
            self.running = False

        elif self.pong_ball.rect.x > 1000:
            self.player_1.score += 1
            self.agent_2_reward = -1
            self.score_board.message = str(self.player_1.score) + str(self.player_2.score)
            self.p1_wins += 1
            self.running = False
            self.pong_ball.reset_ball()

    def observe(self):
        '''
        Returns the current 'state' of the game.
        '''
        player_1_y = self.player_1.rect.y
        player_2_y = self.player_2.rect.y

        ball_y = self.pong_ball.rect.y
        ball_x = self.pong_ball.rect.x

        return np.array([player_1_y, player_2_y, ball_y, ball_x])

    def observe_max(self):
        '''
        Returns the max observation values.
        '''
        return np.array([self.window_size[0] + 50, 
                         self.window_size[0] + 50, 
                         self.window_size[0] + 50,
                         self.window_size[0] + 50])

    def observe_min(self):
        '''
        Returns the minimum observation values.
        '''
        return np.array([-20, -20, -20, -20])



app = PongApp()
app.run()