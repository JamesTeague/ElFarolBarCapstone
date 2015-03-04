#author: James Teague II
#date: Spring 2015
#description: Strategy Module - Handles all functions to maintain all Communal Strategies

from random import choice
from statistics import *
from collections import Counter
class Strategy(object):
	"""Class Strategy holds information to evaluate strategies.
    
    This class will represent a strategy we need specifically for
    our El Farol Bar/Minority Game problem. It will have a
    simulated value and a simulated score.
    
    Attributes:
        name: A reference to name of the strategy for the dictionary (key).
        value: The number that is the deciding factor whether to attend the
        	bar or to stay home.
        score: The number that will determine how well the strategy is doing
        	overall. This number is used to evaluate it against other strategies.
    """
	no_inst = 0
	strategies = {}
	strategy_progression = open("stratProgression.rtf", "w")
	def __init__(self, name, value="random", score=0):
		"""Initialize Strategy with a name, value and score. Then add it to the Class Dictionary"""
		# Increment number of instances of Strategy
		Strategy.no_inst += 1
		super().__init__()
		self.name = name
		self.value = value
		self.score = score
		self.add_to_dictionary()

	@staticmethod
	def calculate_strategies(attendance_list, half_of_population):
		"""Create/Revalue all Strategies"""
		try:
			# Raises StatisticsError if it is not unimodal
			Strategy("mode", mode(attendance_list))
		except StatisticsError:
			Strategy("mode",Counter(attendance_list).most_common(1)[0][0])
		finally:
			Strategy("last_week", attendance_list[-1])
			Strategy("two_weeks", attendance_list[-2])
			Strategy("three_weeks", attendance_list[-3])
			Strategy("four_weeks", attendance_list[-4])
			Strategy("min_attendance", min(attendance_list))
			Strategy("min_month_attendance", min(attendance_list[-4:]))
			Strategy("min_two_month", min(attendance_list[-8:-4]))
			Strategy("min_three_month", min(attendance_list[-12:-8]))
			Strategy("three_week_average", int(mean(attendance_list[-3:])))
			Strategy("month_average", int(mean(attendance_list[-4:])))
			Strategy("two_month_average", int(mean(attendance_list[-8:])))
			Strategy("three_month_average", int(mean(attendance_list[-12:])))
			Strategy("total_average", int(mean(attendance_list)))
			Strategy("median", int(median(attendance_list)))
			Strategy("median_high", median_high(attendance_list))
			Strategy("median_low", median_low(attendance_list))
			Strategy("month_trend", Strategy.trend(attendance_list[-4:]))
			Strategy("two_month_trend", Strategy.trend(attendance_list[-8:]))
			Strategy("three_month_trend", Strategy.trend(attendance_list[-12:]))
			Strategy("mirror_last_week", Strategy.get_mirror_image(half_of_population, attendance_list[-1]))
			Strategy("mirror_two_weeks", Strategy.get_mirror_image(half_of_population, attendance_list[-2]))
			Strategy("mirror_three_weeks", Strategy.get_mirror_image(half_of_population, attendance_list[-3]))
			Strategy("mirror_four_weeks", Strategy.get_mirror_image(half_of_population, attendance_list[-4]))
			Strategy("mirror_month_average", Strategy.get_mirror_image(half_of_population, mean(attendance_list[-4:])))
			Strategy("mirror_two_month_average", Strategy.get_mirror_image(half_of_population, mean(attendance_list[-8:-4])))
			Strategy("mirror_three_month_average", Strategy.get_mirror_image(half_of_population, mean(attendance_list[-12:-8])))
			Strategy("random_attendance")

	@staticmethod
	def get_mirror_image(half, att):
		"""Calculate the mirror image around the attendance passed in"""
		mirror = half + (half - att)
		if mirror < 0:
			return 0
		elif mirror > 10:
			return 10
		else:
			return round(mirror)

	@staticmethod
	def get_new_key():
		"""Get a key from the Strategies Dictionary"""
		key = choice(list(Strategy.strategies.keys()))
		return key

	@staticmethod
	def trend(num_list):
		"""Calculate the trend of the given list. Return the attendance with the trend applied"""
		length = len(num_list)
		trend = 0
		old = num_list.pop(0)
		for num in num_list:
			trend += num - old
			old = num
		trend = round(trend/length)
		return num_list[-1] + trend

	def add_to_dictionary(self):
		"""Add Strategy to Strategy Class Dictionary"""
		Strategy.strategies[self.name] = {"value": self.value, "score": self.score}

	@classmethod
	def get_no_of_instances(cls):
		"""Return number of instances of the given class"""
		return cls.no_inst

	@classmethod
	def clear_strategies(cls):
		"""Clear dictionary"""
		if isinstance(cls, Strategy.__class__):
			cls.strategies.clear()
		else:
			pass

	@staticmethod
	def evalScore(attendance):
		"""Evaluate the scores of each strategy based on attendance"""
		for key in Strategy.strategies:
			if Strategy.strategies[key]["value"] == "random":
				pass
			elif int(Strategy.strategies[key]["value"]) < 6 and attendance < 6:
				Strategy.strategies[key]["score"] += 1
			elif int(Strategy.strategies[key]["value"]) >= 6 and attendance >= 6:
				Strategy.strategies[key]["score"] += 1
			else:
				pass
	
	@staticmethod
	def print_strategies():
		""" Print progression to text file. Debugging/Test purposes."""
		for k,v in sorted(Strategy.strategies.items()):
			Strategy.strategy_progression.write(str(k) + " " + str(v) + "\n")
		Strategy.strategy_progression.write("----------END OF STRATEGIES----------"+ "\n")
		Strategy.strategy_progression.write("\n")
#=================== Strategy Test Code =============================