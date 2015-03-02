#!/usr/bin/env python3
#author: James Teague II
#date: Spring 2015
#description: ElFarolBar.py - Acts as a driver for the Simulation

from Simulation import Simulation as Sim, Person, Strategy

def set_up_simulation():
	Sim.populate_community()
	Sim.strategize_community()

def run():
	Sim.simulate_weekend()
	Sim.take_attendance()
	Strategy.print_strategies()
	Sim.print_people_strategies()
	Sim.revalue_strategies()

def end():
	Strategy.strategy_progression.close()
	Person.person_progression.close()
	Sim.simulation_progression.close()


set_up_simulation()
for x in range(0,4):
	run()
end()