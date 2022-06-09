/**
* @file fireflies.cpp
* @brief implementation of class firefly
* @project Model using cellular automata (IMS at VUT FIT)
* @author Adam Fabo         <xfaboa00@stud.fit.vutbr.cz>
* @author Stanislav Gabris  <xgabri18@stud.fit.vutbr.cz>
*/

#include "fireflies.h"




void Firefly::init(double p, double s){
	this->period    = p;
	this->frequency = (1/period)*RESOLUTION;
	this->influenced_delta = 1/frequency;
    this->delta = 0.0;
    this->kuramoto_sum = 0.0;
    this->num_of_influencers = 0;


	this->step      = s;
	this->step_old  = s;
	this->iteration = int(step/(2*M_PI)); //how many periods
	this->flashed = false;
	this->sinus = sin(step_old);
}


void Firefly::update_influenced_delta(double koef){
    this->influenced_delta += 0.1 * ((1/this->frequency) - this->influenced_delta) / RESOLUTION;
}


void Firefly::calculate_delta(double koef, int firefly_count){
	this->delta = this->influenced_delta;

    if(num_of_influencers != 0){
        double kuramoto = this->kuramoto_sum * (koef/num_of_influencers/firefly_count);
		this->delta += kuramoto;
    }

	this->num_of_influencers = 0;
	this->kuramoto_sum = 0.0;

	this->influenced_delta = delta;
}


void Firefly::next_step(double koef, int firefly_count){
    calculate_delta(koef,firefly_count);
    update_influenced_delta(koef); //prepare for the next step

	this->step_old = this->step_old + this->delta;

	if(int(step_old/(2*M_PI)) > this->iteration){
	    iteration++;
	    this->flashed = true;
	}else{
	    this->flashed = false;
	}
	this->sinus = sin(step_old);
}

double Firefly::distance_from_firefly_koef(int this_firefly, int other_firefly, int coulmn_count, int firefly_count){
    int a_col = other_firefly%coulmn_count;
    int a_row = int(other_firefly/coulmn_count);
    int b_col = this_firefly%coulmn_count;
    int b_row = int(this_firefly/coulmn_count);

    int col_mid = abs(b_col-a_col);
    int row_mid = abs(b_row-a_row);
    double val =  sqrt(200/(pow(col_mid,2.0)+pow(row_mid,2.0)));
    return val > 1 ? 1 : val;
}
