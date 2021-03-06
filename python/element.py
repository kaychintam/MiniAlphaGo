# -*- coding:utf-8 -*-  

import datetime

#棋子
#class Piece:
#	def __init__(self, color):
#		self.color = color # 'b' or 'w'

#玩家
class Player:
	def __init__(self, name, kind):
		self.name          = name  # 玩家名字
		self.kind          = kind  # 玩家类型（人、AI、网络对手）
		self.own           = 2     # 有多少棋子
		self.turn          = ''    # 先手还是后手
		self.t_step_start  = 0     # 每一步开始的时间戳
		self.t_step_total  = 0     # 每一步总共的耗时
		self.t_total       = 0     # 总共的时间

	def step_start(self):
		self.t_step_start = datetime.datetime.now()

	def step_stop(self):
		self.t_total += self.t_step_total
		self.t_step_total = 0

	def update(self, turn):
		if turn==self.turn:
			self.t_step_total = (datetime.datetime.now()-self.t_step_start).seconds

	# 计算有多少属于自己的棋子
	def count(self, pieces):
		self.own = 0
		for i in range(8):
			for j in range(8):
				if not pieces[i][j]=='n' and pieces[i][j] == self.turn:
					self.own += 1

class Game:
	def __init__(self):
		self.pieces = None
		self.player1 = None
		self.player2 = None
		self.turn = 'b'
		self.unwalkable = 0
		self.is_finished = False
		self.last_move = None

	def players_config(self,name1='Black',name2='White',kind1='Human',kind2='Human'):
		self.player1 = Player(name=name1, kind=kind1)
		self.player2 = Player(name=name2, kind=kind2)

	def start(self):
		# 黑棋先 白棋后
		self.turn = 'b'
		# 如果 = 1则上一个人不能走。 = 2则都不能走 比赛结束
		self.unwalkable = 0
		
		#设置初始棋盘
		self.pieces = [['n' for i in range(8)] for j in range(8)]
		self.pieces[3][3] = 'w'
		self.pieces[3][4] = 'b'
		self.pieces[4][3] = 'b'
		self.pieces[4][4] = 'w'

		self.player1.t_step_total = self.player1.t_total = 0
		self.player2.t_step_total = self.player2.t_total = 0
		self.player1.turn = 'b'
		self.player2.turn = 'w'

		self.is_finished = False

		# 玩家1开始计时
		self.player1.t_step_start = datetime.datetime.now()

	def update(self):
		self.player1.update(self.turn)
		self.player2.update(self.turn)
		self.player1.count(self.pieces)
		self.player2.count(self.pieces)

	def end(self):
		self.is_finished = True
		self.player1.step_stop()
		self.player2.step_stop()