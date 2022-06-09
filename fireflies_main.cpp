/**
* @file fireflies_main.cpp
* @brief main file
* @project Model using cellular automata (IMS at VUT FIT)
* @author Adam Fabo         <xfaboa00@stud.fit.vutbr.cz>
* @author Stanislav Gabris  <xgabri18@stud.fit.vutbr.cz>
*/


#include "fireflies.h"


using namespace std;

int main(int argc, char *argv[])
{
    std::default_random_engine generator(time(0));
    //std::normal_distribution<double> distributionp(3,0.25);
    std::normal_distribution<double> distributions(0,3);

	const int ROWCOUNT = stoi(argv[1]);
	const int COLUMNCOUNT = stoi(argv[2]);
	const double KOEF = stod(argv[3]);
	const double MI = stod(argv[4]);
	const double SIGMA = stod(argv[5]);

    std::normal_distribution<double> distributionp(MI, SIGMA);

	double order_sin = 0;
	double order_cos = 0;
	double order = 0;

    const int FIREFLYCOUNT = ROWCOUNT*COLUMNCOUNT;
	Firefly fireflies[ROWCOUNT][COLUMNCOUNT];

	for(int i = 0; i < ROWCOUNT; i++){
	    for(int j = 0; j < COLUMNCOUNT; j++){
	        fireflies[i][j].init(distributionp(generator), distributions(generator));
	    }
	}

	ofstream myfile;
	myfile.open ("fire.txt");

	ofstream myfile_order;
	myfile_order.open ("fire_order.txt");

	ofstream myfile_delta;
	myfile_delta.open ("fire_delta.txt");

	ofstream myfile_blik;
	myfile_blik.open ("fire_blik.txt");


    for(int i = 0; i < STEPS*ITERATIONS; i++){
        cout << i << "\n";

        for(int firefly_a = 0; firefly_a < FIREFLYCOUNT; firefly_a++){
            Firefly *current_firefly = &fireflies[int(firefly_a/COLUMNCOUNT)][firefly_a%COLUMNCOUNT];

            if(current_firefly->flashed){ //if flashed influence others
                for(int firefly_b = 0; firefly_b < FIREFLYCOUNT; firefly_b++){
                    Firefly *influenced_firefly = &fireflies[int(firefly_b/COLUMNCOUNT)][firefly_b%COLUMNCOUNT];

                    if(firefly_a == firefly_b){
                        continue;
                    }

                    double koef_proximity = current_firefly->distance_from_firefly_koef(firefly_a,firefly_b,COLUMNCOUNT,FIREFLYCOUNT);
                    influenced_firefly->kuramoto_sum += koef_proximity * sin(current_firefly->step_old - influenced_firefly->step_old);
                    influenced_firefly->num_of_influencers++;
                }
            }
        }


        order_sin = 0;
		order_cos = 0;
		myfile << "\n";
		myfile_delta << "\n";
		myfile_blik << "\n";


        for(int i = 0; i < ROWCOUNT; i++){
	        for(int j = 0; j < COLUMNCOUNT; j++){
                fireflies[i][j].next_step(KOEF, FIREFLYCOUNT); //-> make new sinus

                order_sin += fireflies[i][j].sinus;
				order_cos += cos(fireflies[i][j].step_old);

				myfile << fireflies[i][j].sinus << " ";
				myfile_delta << fireflies[i][j].influenced_delta << " ";
				myfile_delta << 1/fireflies[i][j].frequency << " ";


				//myfile_blik << fireflies[i][j].flashed << " ";

				if(fireflies[i][j].flashed)
					myfile_blik << 1 << " ";
				else
					myfile_blik << 0 << " ";

	        }
			myfile << "\n";
			myfile_delta << "\n";

			myfile_blik << "\n";
	    }
	    order = sqrt(order_sin*order_sin + order_cos*order_cos) / FIREFLYCOUNT;
		myfile_order << order << "\n";


    }

	return 0;
}
