# Synchronization of fireflies 

This project is about making simulation of blinking swarm of fireflies, that in a nature, can spontaiously synchronise their blinking even when initial blinking of the swarm was chaotic. To achieve this project combines Kuramoto model and Cellular automata.

## General info
### Files
* fireflies_main.cpp
* fireflies.cpp
* fireflies.h
* Makefile
* README.md
* Documentation.pdf

### Usage
To build use ```make```.
To execute use:
```bash
    fireflies X Y KOEF MI SIGMA
```
Where **X** and **Y** represent the size of 2D plane (number of fireflies=X\*Y), **KOEF** represents the coupling strength of oscillators (fireflies), **MI** and **SIGMA** represent mean and variance parameters for normal distribution of firefly frequency.

### Example
```bash
    fireflies 2 2 0.02 3 0.25
```

### Output
Program outputs to _stdin_ its current step and creates 4 text files:
* fire.txt -- cycles (sines) of all fireflies each step
* fire_blik.txt -- which fireflies flashed each step
* fire_delta.txt -- deltas of all the fireflies each step
* fire_order.txt -- system order for each step

## Background
Fireflies can synchronize their blinking by observing other fireflies blinks and adjusting their rate of blinking accordingly. Whole simualtion is based on a premise that synchronisation of blinking fireflies can be described by Kuramoto model. 

### Kuramoto model
Kuramoto model is a mathematical model used to describe synchronization. Most popular example is [synchronisation of metronomes.](https://www.youtube.com/watch?v=Aaxw4zbULMs&ab_channel=HarvardNaturalSciencesLectureDemonstrations) It is well described in [Veritasium video](https://www.youtube.com/watch?v=t-_VPRCtiUg&ab_channel=Veritasium) or online interactive website called [Kuramotocycle](http://www.complexity-explorables.org/slides/ride-my-kuramotocycle/) which is great way to demonstrate principles of Kuramoto model.

<p align="center">
  <img src="https://github.com/Adam-Fabo/Synchronisation-of-fireflies/blob/main/images/kuramoto.png?raw=true" width = 100% />
</p>
 
In simulation we model fireflies as sine waves with given frequency and phase shift. We also measure orderliness of the system - how much is system synchronized.

### Cellular automata
Fireflies are modeled as 2D array in which every cell is a firefly. Unlike general Kuramoto model fireflies in this simulation dont affect eachother globally - meaning that every firefly has an area of influence (like in a real world). Also fireflies sync up only when they "see" another firefly blink - another difference from Kuramoto model in which synchronization is continuous.

### Randomness in model
As in nature starting conditions of fireflies are random and are described by normal distribution. Starting conditions are frequency of firefly and phase shift.

## Info
Simualtion itself is written in C++

Graphs are made in Python - Matplitlib and Numpy

### Links

Result of simulation - [video](https://youtu.be/UF8tPC8jpdA) demostrating synchronization of fireflies over time.

For detailed info see [documentation](https://github.com/Adam-Fabo/Synchronisation-of-fireflies/blob/main/doc/Documentation.pdf) \[Slovak Language]
