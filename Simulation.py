#author: James Teague II (james.teague@drake.edu)
#date: Spring 2015
#description: Simulation Module - Handles functions required to run a
#	proper simulation of the El Farol Bar Problem
from Person import Person
from Strategy import Strategy
class Simulation(object):
	community = {}
	past_attendance = Person.recent_memory[0:]

	@staticmethod
	def populate_community():
		""" Run only at the beginning of the Simulation

			Create instances of the Person for the simulation
		"""
		for i in range(1,4):
			Simulation.community["person"+str(i)] = Person("person"+str(i))

	@staticmethod
	def strategize_community():
		""" Run only at the beginning of the Simulation

			Give all persons strategies
		"""
		Strategy.calculate_strategies(Person.recent_memory, int(Person.get_no_of_instances()/2))
		for person in Simulation.community:
			Simulation.community[person].give_strategies()

	@staticmethod
	def simulate_weekend():
		""" Have people make their decision on stay or go"""
		for person in Simulation.community:
			if Simulation.community[person].has_random:
				Simulation.community[person].get_random_attendance()
			Simulation.community[person].eval_strategies()

	@staticmethod
	def take_attendance():
		""" Count number of people who went to the bar"""
		count = 0
		for person in Simulation.community:
			if Simulation.community[person].went_to_bar():
				count += 1
		print(count)
		Strategy.evalScore(count)
		Simulation.eval_randoms(count)

	@staticmethod
	def eval_randoms(count):
		""" Evaluate each persons random strategy"""
		for person in Simulation.community:
			Simulation.community[person].eval_random_strategy(count)

	@staticmethod
	def add_to_memory(count):
		""" Add week's attendance to Simulation memory and Person memory"""
		Simulation.past_attendance.append(count)
		Person.add_to_memory(count)

	@staticmethod
	def print_people_strategies():
		""" Test Function
			Print Communities strategies along with random if present, what they chose, and if they went
		"""
		for person in Simulation.community:
			print(person+":")
			print(Simulation.community[person].went_to_bar())
			print(Simulation.community[person].strat_chose)
			print(Simulation.community[person].strategies)
			if Simulation.community[person].has_random:
				print(Simulation.community[person].random_dict)
#============== Simulation Test Code ========================
# Simulation.populate_community()
# Simulation.strategize_community()
# Simulation.simulate_weekend()
# Simulation.take_attendance()
# print("--------------------")
# print(Simulation.past_attendance)
# print(Strategy.strategies)
# Simulation.print_people_strategies()


