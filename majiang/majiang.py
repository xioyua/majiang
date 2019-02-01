# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
import random
import math
# 总牌
# [1 2 3 4 5 6 7 8 9 
# 11 12 13 14 15 16 17 18 19
# 21 22 23 24 25 26 27 28 29 ]


class Majiang():
    def __init__(self):
        super(Majiang, self).__init__()
        self.All_Board = [s + x for s in [0, 10, 20]
                          for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]] * 4
        self.current_board_heap = self.All_Board
        random.shuffle(self.current_board_heap)  # 牌堆为总牌洗牌
        self.remain_board_num = len(self.All_Board)
        self.hand_board = [[], [], [], []]  # east south west north
        self.bump = [[], [], [], []]  # east south west north
        self.bar = [[], [], [], []]  # east south west north
        self.out = [[], [], [], []]  # east south west north
        self.east = 0
        self.south = 1
        self.west = 2
        self.north = 3
        print(self.hand_board)
        self.cursor_loc = self.east  # 当前焦点位置，即出牌者
        self.status = np.array([0, 0, 0, 0])  # bar, top4, bottom4, showReady
        self.act_list1 = np.array([0, 0, 0])  # output, self-get, dark-bar
        self.act_list2 = np.array([0, 0, 0])  # other-get, point-bar, bump
        self.stage = 0
        self.player_done = np.array([0, 0, 0, 0])

    def reset(self,):
        self.cursor_loc = self.east
        self.status = [0, 0, 0, 0]
        self.act_list1 = [0, 0, 0, 0]
        self.act_list2 = [0, 0, 0, 0]
        self.stage = 0
        self.player_done = [0, 0, 0, 0]

        self.current_board_heap = self.All_Board
        random.shuffle(self.current_board_heap)  # 牌堆为总牌洗牌
        self.remain_board_num = len(self.All_Board)
        # 东
        self.hand_board[self.east] = []
        self.bump[self.east] = []
        self.bar[self.east] = []
        self.out[self.east] = []
        # 南
        self.hand_board[self.south] = []
        self.bump[self.south] = []
        self.bar[self.south] = []
        self.out[self.south] = []
        # 西
        self.hand_board[self.west] = []
        self.bump[self.west] = []
        self.bar[self.west] = []
        self.out[self.west] = []
        # 北
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

        # 理牌
        self.hand_board[self.east].sort()
        self.hand_board[self.south].sort()
        self.hand_board[self.west].sort()
        self.hand_board[self.north].sort()

        self.deal_one_board(self.east)  # 开局直接给东方玩家发一张牌
        self.stage = 1  # 第一阶段开始

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
        print('self.current_board_heap', self.current_board_heap)  # 牌堆为总牌洗牌
        print('self.remain_board_num', self.remain_board_num)
        # 东
        print('self.hand_board[self.east]', self.hand_board[self.east])
        print('self.bump[self.east]', self.bump[self.east])
        print('self.bar[self.east]', self.bar[self.east])
        print('self.out[self.east]', self.out[self.east])
        # 南
        print('self.hand_board[self.south]', self.hand_board[self.south])
        print('self.bump[self.south]', self.bump[self.south])
        print('self.bar[self.south]', self.bar[self.south])
        print('self.out[self.south]', self.out[self.south])
        # 西
        print('self.hand_board[self.west]', self.hand_board[self.west])
        print('self.bump[self.west]', self.bump[self.west])
        print('self.bar[self.west]', self.bar[self.west])
        print('self.out[self.west]', self.out[self.west])
        # 北
        print('self.hand_board[self.north]', self.hand_board[self.north])
        print('self.bump[self.north]', self.bump[self.north])
        print('self.bar[self.north]', self.bar[self.north])
        print('self.out[self.north]', self.out[self.north])

    def hit_out(self, hand_loc):
        '''出牌'''
        if len(self.hand_board[self.cursor_loc]) > hand_loc:
            self.new_board = self.hand_board[self.cursor_loc].pop(
                index=hand_loc)
            self.out[self.cursor_loc].append(self.new_board)
        else:
            raise Exception('err1')

    def baring_in_dark(self, hand_loc):
        '''暗杠'''
        if len(self.hand_board[self.cursor_loc]) > hand_loc + 3:
            if (self.hand_board[self.cursor_loc][hand_loc] == self.hand_board[self.cursor_loc][hand_loc + 1] and
                self.hand_board[self.cursor_loc][hand_loc + 1] == self.hand_board[self.cursor_loc][hand_loc + 2] and
                    self.hand_board[self.cursor_loc][hand_loc + 2] == self.hand_board[self.cursor_loc][hand_loc + 3]):
                self.bar[hand_loc].extend(
                    self.hand_board[self.cursor_loc][hand_loc:hand_loc+4])
                del (self.hand_board[self.cursor_loc][hand_loc:hand_loc + 4])
        else:
            raise Exception('err1')

    def baring_ba(self, hand_loc):
        '''巴杠'''
        if (self.hand_board[self.cursor_loc][hand_loc] in self.bump[self.cursor_loc]):
            this_board = self.hand_board[self.cursor_loc].pop(hand_loc)  # 手牌取出
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
        if self.stage == 1:  # 自摸只能在1阶段
            reward = self.calculate_reward(
                self.hand_board[self.cursor_loc], self.bar[self.cursor_loc], self.bump[self.cursor_loc], 1)
            if (reward != 0):
                return reward
        raise Exception("不能自摸")

    def get_hand_win(self, player_loc):
        '''胡牌'''
        if self.stage == 2:  # 胡牌只能在二阶段
            reward = self.calculate_reward(
                self.hand_board[player_loc] + self.out[self.cursor_loc][-1], self.bar[player_loc], self.bump[player_loc], 2)
            if reward != 0:
                return reward
        raise Exception("不能胡牌")

    def calculate_reward(self, hand, bar, bump, type):
        '''奖励计算'''
        if type == 1:  # 自摸
            reward = self.board_cal(hand, bar, bump)
            return reward
        elif type == 2:  # 胡
            reward = self.board_cal(hand, bar, bump)
            if reward == 1:
                return 0
            else:
                return reward
        else:
            raise Exception('牌型计算类型参数不正确')

    def board_cal(self, hand, bar, bump):
        '''牌型计算'''
        rate = 1
        for each in self.status:  # 杠、前四、后四、报叫倍率计算
            if each == 1:
                rate = rate * 2
        
        if self.is_Sanitary_color(hand, bar, bump):
            rate = rate * 2

        drgon = self.is_seven_couple(hand, bar, bump)
        if drgon > 0:
            rate = rate * math.pow(2, drgon)
            return rate

        big_couple = self.is_big_couple(hand, bar, bump)
        if big_couple > 0:
            rate = rate * 2
            return rate

        gold_single = self.is_gold_single(hand, bar, bump)
        if gold_single > 0:
            rate = rate * 4
            return rate
        
        if self.is_normal_hu(hand, bar, bump) > 0:
            return rate
        else:
            return 0

        
        

        

    def judge_board_type(self, board):
        '''判断花型'''
        if board < 10:
            return 1  # 万字
        elif board < 20:
            return 2  # 筒子
        elif board < 30:
            return 3  # 条子
        else:
            raise Exception("花型错误，没有这张牌")

    def is_Sanitary_color(self, hand, bar, bump):
        all = hand + bar + bump
        for each in range(len(all)-1):
            if self.judge_board_type(all[each]) != self.judge_board_type(all[each + 1]):
                break
        else:
            return 1
        return 0

    def is_seven_couple(self, hand, bar, bump):
        '''七对判断，返回１为暗七对，２为龙，３为双龙，以此类推'''
        bar_num = 1
        if (len(hand) == 14):
            for each in set(hand):
                if self._is_couple(hand, each) == 0 and self._is_bar(hand, each) == 0:
                    break
                else:
                    if (self._is_bar(hand, each) == 1):
                        bar_num = bar_num + 1
            else:
                return bar_num
        return 0

    def is_big_couple(self, hand, bar, bump):
        '''是否为大对子'''
        couple_num = 0
        three_num = 0
        for each in set(hand):
            if hand.count(each) == 2:
                couple_num = couple_num + 1
            elif hand.count(each) == 3:
                three_num = three_num + 1
            else:
                break
        else:
            if couple_num == 1:
                return 1

    def is_gold_single(self, hand, bar, bump):
        '''金钩钓'''
        if len(hand) == 2:
            if hand[0] == hand[1]:
                return 1
        return 0

    def is_normal_hu(self, hand, bar, bump):
        '''是否可以正常胡牌'''
        couples = []
        for each in set(hand):
            if hand.count(each) >= 2:
                couples.append(each)

        for couple in couples:
            except_couptle = hand
            except_couptle.remove(couple)
            except_couptle.remove(couple)
            if self.is_all_sectence(except_couptle) == 1:
                return 1
        else:
            return 0

    def is_all_sectence(self, hand):
        '''列表中全是句子'''
        hand_buff = hand
        hand_buff.sort()
        while len(hand) != 0:
            the_one = hand[0]
            if hand.count(the_one) >= 3:
                hand.remove(the_one)
                hand.remove(the_one)
                hand.remove(the_one)
            elif self.get_seq(the_one, 1) in hand and self.get_seq(the_one, 2) in hand and self.get_seq(the_one, 1) != 0 and self.get_seq(the_one, 2):
                hand.remove(the_one)
                hand.remove(self.get_seq(the_one, 1))
                hand.remove(self.get_seq(the_one, 2))
            else:
                return 0
        return 1
    
    def get_seq(self, target, offset):
        '''取得偏移量后的牌'''
        if offset > 8:
            return 0
        
        if (target % 10) > (target + offset) % 10:
            return 0
        
        return target + offset

    def _is_couple(self, hand, target):
        '''检测该牌在手牌中是否有一对'''
        if isinstance(hand, list):
            if hand.count(target) == 2:
                return 1
            else:
                return 0
        else:
            raise Exception("手牌参数输入错误，不是列表")

    def _is_bar(self, hand, target):
        '''检测该牌在手牌中是否有一杠'''
        if isinstance(hand, list):
            if hand.count(target) == 4:
                return 1
            else:
                return 0
        else:
            raise Exception("手牌参数输入错误，不是列表")


mj = Majiang()

mj.reset()
l1 = [1, 1, 1, 2, 3, 7, 7,
      7, 9, 9, 9, 8, 8, 8]
print('七对', mj.is_seven_couple(l1, [], []))
print('清一色', mj.is_Sanitary_color(l1, [], []))
print('大对子', mj.is_big_couple(l1, [], []))
print('普通胡', mj.is_normal_hu(l1, [], []))
