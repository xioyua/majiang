# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
import random
#总牌
# ['A1' 'A2' 'A3' 'A4' 'A5' 'A6' 'A7' 'A8' 'A9' 'B1' 'B2' 'B3' 'B4' 'B5' 'B6'
#  'B7' 'B8' 'B9' 'C1' 'C2' 'C3' 'C4' 'C5' 'C6' 'C7' 'C8' 'C9' 'D1' 'D2' 'D3'
#  'D4' 'D5' 'D6' 'D7' 'D8' 'D9']

class Majiang():
    def __init__(self):
        super(Majiang,self).__init__()
        self.All_Board = [s + x for s in 'ABCD' for x in '123456789'] * 4
        self.current_board_heap  = self.All_Board
        random.shuffle(self.current_board_heap)  #牌堆为总牌洗牌
        self.remain_board_num = len(self.All_Board)
        self.hand_board = [[],[],[],[]]   #  east south west north
        self.bump = [[], [], [], []]     #  east south west north
        self.bar = [[], [], [], []]     #  east south west north
        self.out = [[], [], [], []]     #  east south west north
        self.east = 0
        self.south = 1
        self.west = 2
        self.north = 3
        print(self.hand_board)
        self.cursor_loc = self.east  #当前焦点位置，即出牌者
        self.status = np.array([0, 0, 0, 0])  #bar, top4, bottom4, showReady
        self.act_list1 = np.array([0, 0, 0])  #output, self-get, dark-bar
        self.act_list2 = np.array([0, 0, 0])  #other-get, point-bar, bump
        self.stage = 0
        self.player_done = np.array([0,0,0,0])

        
        
    def reset(self,):
        self.cursor_loc = self.east
        self.status = [0,0,0,0]
        self.act_list1 = [0, 0, 0, 0]
        self.act_list2 = [0, 0, 0, 0]
        self.stage = 0
        self.player_done = [0, 0, 0, 0]

        self.current_board_heap  = self.All_Board
        random.shuffle(self.current_board_heap)  #牌堆为总牌洗牌
        self.remain_board_num = len(self.All_Board)
        #东
        self.hand_board[self.east] = []
        self.bump[self.east] = []
        self.bar[self.east] = []
        self.out[self.east] = []
        #南
        self.hand_board[self.south] = []
        self.bump[self.south] = []
        self.bar[self.south] = []
        self.out[self.south] = []
        #西
        self.hand_board[self.west] = []
        self.bump[self.west] = []
        self.bar[self.west] = []
        self.out[self.west] = []
        #北
        self.hand_board[self.north] = []
        self.bump[self.north] = []
        self.bar[self.north] = []
        self.out[self.north] = []

    def get_east_id(self):
        '''获得东方玩家的名号'''
        return self.east

    def get_south_id(self):
        '''获得南方玩家的名号'''
        return self.south

    def get_west_id(self):
        '''获得西方玩家的名号'''
        return self.west

    def get_north_id(self):
        '''获得北方玩家的名号'''
        return self.north

    def distribute_board(self):
        '''开始时给四位玩家发牌'''
        if self.remain_board_num != len(self.All_Board):
            return False
        self.hand_board[self.east].extend(self.current_board_heap[-13:])
        self.current_board_heap = self.current_board_heap[:-13]
        self.hand_board[self.south].extend(self.current_board_heap[-13:])
        self.current_board_heap = self.current_board_heap[:-13]
        self.hand_board[self.west].extend(self.current_board_heap[-13:])
        self.current_board_heap = self.current_board_heap[:-13]
        self.hand_board[self.north].extend(self.current_board_heap[-13:])
        self.current_board_heap = self.current_board_heap[:-13]

        #理牌
        self.hand_board[self.east].sort()
        self.hand_board[self.south].sort()
        self.hand_board[self.west].sort()
        self.hand_board[self.north].sort()

        self.deal_one_board(self.east)  #开局直接给东方玩家发一张牌
        self.stage = 1 #第一阶段开始

        return True

    def deal_one_board(self, loc):
        '''发给特定玩家一张牌'''
        self.hand_board[loc].extend(self.current_board_heap[-1:])
        self.current_board_heap = self.current_board_heap[:-1]


    def player_new_round(self, loc):
        '''根据玩家所坐方位，摸牌'''
        if (self.cursor_loc == loc):
            if self.status == 'normal_get_put':
                pass
            elif self.status == 'bump_ready_put':
                pass
            elif self.status == 'bar_get_put':
                pass 




    def show_battleField(self):
        print('self.current_board_heap', self.current_board_heap)  #牌堆为总牌洗牌
        print('self.remain_board_num', self.remain_board_num)
        #东
        print('self.hand_board[self.east]', self.hand_board[self.east])
        print('self.bump[self.east]', self.bump[self.east])
        print('self.bar[self.east]', self.bar[self.east])
        print('self.out[self.east]', self.out[self.east])
        #南
        print('self.hand_board[self.south]', self.hand_board[self.south])
        print('self.bump[self.south]', self.bump[self.south])
        print('self.bar[self.south]', self.bar[self.south])
        print('self.out[self.south]', self.out[self.south])
        #西
        print('self.hand_board[self.west]', self.hand_board[self.west])
        print('self.bump[self.west]', self.bump[self.west])
        print('self.bar[self.west]', self.bar[self.west])
        print('self.out[self.west]', self.out[self.west])
        #北
        print('self.hand_board[self.north]', self.hand_board[self.north])
        print('self.bump[self.north]', self.bump[self.north])
        print('self.bar[self.north]', self.bar[self.north])
        print('self.out[self.north]', self.out[self.north])

    def hit_out(self, hand_loc):
        '''出牌'''
        if len(self.hand_board[self.cursor_loc]) > hand_loc:
            self.new_board = self.hand_board[self.cursor_loc].pop(index=hand_loc)
            self.out[self.cursor_loc].append(self.new_board)
        else:
            raise Exception('err1')

    def baring_in_dark(self, hand_loc):
        '''暗杠'''
        if len(self.hand_board[self.cursor_loc]) > hand_loc + 3:
            if (self.hand_board[self.cursor_loc][hand_loc] == self.hand_board[self.cursor_loc][hand_loc + 1] and 
                        self.hand_board[self.cursor_loc][hand_loc + 1] == self.hand_board[self.cursor_loc][hand_loc + 2] and
                    self.hand_board[self.cursor_loc][hand_loc + 2] == self.hand_board[self.cursor_loc][hand_loc + 3]):
                self.bar[hand_loc].extend(self.hand_board[self.cursor_loc][hand_loc:hand_loc+4])
                del (self.hand_board[self.cursor_loc][hand_loc:hand_loc + 4])
        else:
            raise Exception('err1')
    
    def baring_ba(self, hand_loc):
        '''巴杠'''
        if (self.hand_board[self.cursor_loc][hand_loc] in self.bump[self.cursor_loc]):
            this_board = self.hand_board[self.cursor_loc].pop(hand_loc)     #手牌取出
            self.bar[self.cursor_loc].append(this_board)  # 杠牌堆新增一张
            self.bump[self.cursor_loc].remove(this_board)  # 碰牌堆减少一张
        else:
            raise Exception("不能巴杠")

    def baring_point(self, player_loc, hand_loc):
        '''点杠'''
        if(self.stage == 2):
            if self.out[self.cursor_loc][-1] == self.hand_board[player_loc][hand_loc] and \
            self.hand_board[player_loc][hand_loc] == self.hand_board[player_loc][hand_loc + 1] and \
            self.hand_board[player_loc][hand_loc + 1] == self.hand_board[player_loc][hand_loc + 2]:
                this_board = self.hand_board[player_loc][hand_loc]
                self.bar[player_loc].append(this_board)
                del (self.hand_board[player_loc][hand_loc:hand_loc + 3])
                return True
        raise Exception("不能点杠")
    
    def bumping(self, player_loc, hand_loc):
        '''碰'''
        if(self.stage == 2):
            if self.out[self.cursor_loc][-1] == self.hand_board[player_loc][hand_loc] and \
                    self.hand_board[player_loc][hand_loc] == self.hand_board[player_loc][hand_loc + 1]:
                this_board = self.hand_board[player_loc][hand_loc]
                self.bump[player_loc].append(this_board)
                del (self.hand_board[player_loc][hand_loc:hand_loc + 2])
                return True
        raise Exception("不能碰")
    
    def self_hand_win(self):
        '''自摸'''
        if self.stage == 1:  #自摸只能在1阶段
            reward = self.calculate_reward(self.hand_board[self.cursor_loc], 1)
            if (reward != 0):
                return reward
        raise Exception("不能自摸")

    def get_hand_win(self, player_loc):
        '''胡牌'''
        if self.stage == 2:  #胡牌只能在二阶段
            reward = self.calculate_reward(self.hand_board[player_loc] + self.out[self.cursor_loc][-1], 2)
            if reward != 0:
                return reward
        raise Exception("不能胡牌")

    def calculate_reward(self, brd, type):
        '''奖励计算'''
        if type == 1:  #自摸
            reward = self.board_cal(brd)
            return reward
        elif type == 2:  #胡
            reward = self.board_cal(brd)
            if reward == 2:
                return 0
            else:
                return reward
        else:
            raise Exception('牌型计算类型参数不正确')

    def board_cal(self, brd):
        '''牌型计算'''
        rate = 1
        for each in self.status:
            if each == 1:
                rate = rate * 2
        

mj = Majiang()

mj.reset()
mj.distribute_board()
mj.show_battleField()
mj.deal_one_board("east")
mj.show_battleField()

