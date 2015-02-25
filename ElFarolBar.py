#!/usr/bin/env python3
#author: James Teague II
#date: Spring 2015
#description: ElFarolBar.py - Acts as a driver for the Simulation

from Simulation import Simulation as Sim
from Strategy import Strategy

def set_up_simulation():
	Sim.populate_community()
	Sim.strategize_community()

def run():
	Sim.simulate_weekend()
	Sim.take_attendance()
	print("--------------------")
	print(Sim.past_attendance)
	print(Strategy.strategies)
	Sim.print_people_strategies()

set_up_simulation()
run()