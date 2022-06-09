/**
* @file fireflies.h
* @brief class of firefly
* @project Model using cellular automata (IMS at VUT FIT)
* @author Adam Fabo         <xfaboa00@stud.fit.vutbr.cz>
* @author Stanislav Gabris  <xgabri18@stud.fit.vutbr.cz>
*/

#ifndef KURAMOTO_IMS_FIREFLIES_H
#define KURAMOTO_IMS_FIREFLIES_H

#define _USE_MATH_DEFINES

#include <iostream>
#include <fstream>
#include <string>
#include <random>
#include <cmath>
#include <time.h>
#include <cstddef>
#include <algorithm>
#ifndef M_PI
	#define M_PI 3.14159265358979323846
#endif

#define RESOLUTION 100
#define ITERATIONS 20
const int STEPS = int(2*M_PI * RESOLUTION);

/**
* This class represents a firefly
*/
class Firefly
{
    public:
        double period;		// normal period
        double frequency;	// normal frequency
        double influenced_delta; //delta that moves towards period
        double delta; //this delta is calculated only when influenced
        double kuramoto_sum; // at the end of each step holds the sum of sines from all influencers
        int num_of_influencers; //how many influencers each step

        double step;			// new step
        double step_old;		// old step from which new step is calculated

        int iteration;		// number of times firefly blinked
        bool flashed;


        double sinus;


	public:

		void init(double p, double s);

        /**
        * Function calculates new value for delta that is returning to base frequency
        */
	    void update_influenced_delta(double koef);

        /**
        * Function calculates new value for delta if there were any influences
        */
        void calculate_delta(double koef, int firefly_count);

        ////////////////////////////////////////
        /**
        * Function that updates values of a firefly every step
        */
        void next_step(double koef, int firefly_count);

        /**
        * Function calculates inverse square law
        */
        double distance_from_firefly_koef(int this_firefly, int other_firefly, int coulmn_count, int firefly_count);

};


#endif //KURAMOTO_IMS_FIREFLIES_H
