#author: James Teague II (james.teague@drake.edu)
#date: Spring 2015
#description: Simulation Module - Handles functions required to run a
#	proper simulation of the El Farol Bar Problem
from Person import Person
from Strategy import Strategy
import const
class Simulation(object):
	community = {}
	past_attendance = Person.recent_memory[0:]
	simulation_progression = open("simProgression.rtf","w")

	@staticmethod
	def populate_community():
		""" Run only at the beginning of the Simulation

			Create instances of the Person for the simulation
		"""
		for i in range(1,11):
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
		Simulation.add_to_memory(count)

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
		Simulation.simulation_progression.write(str(Person.recent_memory))
		Simulation.simulation_progression.write("\n")

	@staticmethod
	def revalue_strategies():
		""" Call to calulate strategies again for the new results"""
		# Clear old values out
		Strategy.clear_strategies()
		Strategy.calculate_strategies(Person.recent_memory, int(Person.get_no_of_instances()/2))

	@staticmethod
	def print_people_strategies():
		""" Test Function
			Print Communities strategies along with random if present, what they chose, and if they went
		"""
		for person in sorted(Simulation.community):
			Simulation.community[person].print_info()
		Person.person_progression.write("--------------- END OF WEEK ---------------" + "\n")
#============== Simulation Test Code ========================