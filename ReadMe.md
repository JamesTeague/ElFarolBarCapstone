Date: 2015-02-23  
Title: James Teague II  
Published: true  
Type: post  
Excerpt:   

El Farol Bar Simulation
===
> This is being written for the Capstone of James Teague II at Drake University. Spring of 2015.

###Author
* James Teague II (james.teague@drake.edu)

##Background

The El Farol Bar Problem (Minority Game) is an interesting problem in Game Theory. The problem states that there is one bar in the town with a community that must decided on the particular night, whether they will attend the bar or not.

For sake of keeping the math really simple here in this document, we will say the town consists of 100 people. These people must decided whether they will attend the bar or not without talking to anyone else or gaining information from anyone. The bar has a capacity of 60 persons and if a person decides to go and there bar is at capacity or higher (>= 60), the bar will be too crowded and is unenjoyable. The people inside the bar would have been better off staying at home and vice-a-versa. 

Keep in mind a person is not allowed to go scope out the bar and then make a decision. They all must make a decision at the same time, and once a decision is made, it cannot be changed. 

The participants have knowledge of past attendance to a certain time period in the past. They are to employ a strategy to decided whether to go or stay home.

##Simulation
This program is being written to simulate the attendance of the bar with the method discussed above. People will be randomly given a set of strategies to use and evaluate. They will select the best strategy of the ones they have been randomly assigned. They will employ that strategy and then re-evaluate each given strategy for the potential of a new best. The attendance numbers are then calculated and stored and the process is to be run again.