import numpy as np
import pandas as pd
import time

np.random.seed(2)

n_states = 6    #道路的长度
actions = ['left', 'right']   #可能的行为

epsilon = 0.9   #奖励
alpha = 0.1     #学习率
LAMBDA = 0.9    #折扣因子
max_episodes = 13   #最大游戏次数
fresh_time = 0.3    #单步时间

def build_q_table(n_state, actions):
    table = pd.DataFrame(np.zeros((n_states, len(actions))),columns=actions,)
    print(table)
    return table

def choose_action(state, q_table):
    '''this is how to choose an action'''
    state_action = q_table.iloc[state, :]
    if (np.random.uniform() > epsilon) or (state_action.all() == 0):
        action_name = np.random.choice(actions)
    else:
        action_name = state_action.argmax()
    return action_name

def get_env_feedback(S, A):
    '''this is how agent will interact with the environment'''
    if A == 'right':
        if S == n_states - 2:
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else:
        R = 0
        if S == 0:
            S_ = S  #reach the wall
        else:
            S_ = S - 1
    return S_, R

def update_env(S, episode, step_counter):
    '''this is how environment be update'''
    env_list = ['-'] * (n_states - 1) + ['T']
    if S == 'terminal':
        interaction = 'Episode %s: total_step = %s' % (episode+1, step_counter) 
        time.sleep(0.2)
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction),end='')
        time.sleep(fresh_time)

def train():
    q_table = build_q_table(n_states, actions)
    for episode in range(max_episodes):
        S = 0
        step_counter = 0
        is_terminated = False
        update_env(S, episode, step_counter)
        while not is_terminated:
            A = choose_action(S, q_table)
            S_, R = get_env_feedback(S, A)
            q_predict = q_table.ix[S, A]
            if S_ != 'terminal':
                q_target = R + LAMBDA * q_table.iloc[S_,:].max()
            else:
                q_target = R
                is_terminated = True
            
            q_table.ix[S, A] += alpha * (q_target - q_predict)
            S = S_

            update_env(S, episode, step_counter+1)
            step_counter += 1
    
    return q_table
    
ta = train()
print(ta)