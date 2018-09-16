// CSE 375/475 Assignment #1
// Fall 2018
//
// Description: This file implements a function 'run_custom_tests' that should be able to use
// the configuration information to drive tests that evaluate the correctness
// and performance of the map_t object.

#include <iostream>
#include <ctime>
#include "config_t.h"
#include "tests.h"

#include "simplemap.h"

#include <stdlib.h> 
#include <thread>
#include <time.h>
#include <sys/time.h>
#include <mutex>
#include <map>
#include <string>

simplemap_t<int, float> *map;
int key_max;
std::mutex locks;
int cfg_iter;
double *cons;
double exe_time;



void printer(int k, float v) {
	std::cout<<"<"<<k<<","<<v<<">"<< std::endl;
}


		// Step 3
		// Define a function "deposit" that selects two random bank accounts
		// and an amount. This amount is subtracted from the amount
		// of the first account and summed to the amount of the second
		// account. In practice, give two accounts B1 and B2, and a value V,
		// the function performs B1-=V and B2+=V.
		// The execution of the whole function should happen atomically:
		// no operation should happen on B1 and B2 (or on the whole map?)
		// while the function is executing.

void deposit(int id)
{
	int acc_1 = (int) (rand() % key_max);
	int acc_2 = (int) (rand() % key_max);
	
	float left = 0.0;

    std::lock_guard<std::mutex> lock(locks);
	// test whether less than 0
	left = map -> lookup(acc_1).first;
	while(left <= 0.0)
	{
		acc_1 = (int) (rand() % (key_max + 1));
		left = map -> lookup(acc_1).first;
	}
		
	float v = ((float) rand() / (float) (RAND_MAX)) * left;
	v = (float)((int) (v*100)) / (float)(100);
	map -> update(acc_1, left - v);
	map -> update(acc_2, map -> lookup(acc_2).first + v);
	// std::cout << "thread " << id << " deposite " << v << "\t" << acc_1 << " to " << acc_2 << std::endl;
}

		// Step 4
		// Define a function "balance" that sums the amount of all the
		// bank accounts in the map. In order to have a consistent result,
		// the execution of this function should happen atomically:
		// no other deposit operations or balance operations should interleave.


void balance(int id)
{
	std::lock_guard<std::mutex> lock(locks);
	float sum_bal = 0.0;
	for( auto i = 0 ; i < key_max ;++ i)
		sum_bal += map -> lookup(i).first;
	// std::cout << "balance: " << sum_bal << std::endl;
	// return sum_bal;
}

		// Step 5
		// Define a function 'do_work', which has a for-loop that
		// iterates for config_t.iters times. Each iteration, the function should
		// call the function 'deposit' with 80% of the probability;
		// otherwise (the rest 20%) the function 'balance' should be called.
		// The function 'do_work' should measure 'exec_time_i', which is the
		// time needed to perform the entire for-loop. This time will be shared with
		// the main thread once the thread executing the 'do_work' joins its execution
		// with the main thread.

void do_work(int id)
{
	struct timeval start;
    gettimeofday(&start, NULL);
	for (auto i = 0 ; i < cfg_iter ;++ i)
		(rand() % 10 < 8)? deposit(id):balance(id);
	struct timeval end;
    gettimeofday(&end, NULL);
	cons[id] = (end.tv_sec - start.tv_sec) * 1000000 + ((int)end.tv_usec - (int)start.tv_usec);;
}


void run_custom_tests(config_t& cfg) {
	struct timeval start;
    gettimeofday(&start, NULL);

	cfg_iter = cfg.iters;
	cons = new double[cfg.threads];

		// Step 1
		// Define a simplemap_t of types <int,float>
		// this map represents a collection of bank accounts:
		// each account has a unique ID of type int;
		// each account has an amount of fund of type float.
	map = new simplemap_t<int, float>();

		// Step 2
		// Populate the entire map with the 'insert' function
		// Initialize the map in a way the sum of the amounts of
		// all the accounts in the map is 10000

	key_max = cfg.key_max;
	float initial_account = float(10000.0)/float(key_max);
	for (int i = 0 ; i < key_max ;++ i)
	{
		map -> insert(i, initial_account);
	}

		// Step 3
		// Define a function "deposit" that selects two random bank accounts
		// and an amount. This amount is subtracted from the amount
		// of the first account and summed to the amount of the second
		// account. In practice, give two accounts B1 and B2, and a value V,
		// the function performs B1-=V and B2+=V.
		// The execution of the whole function should happen atomically:
		// no operation should happen on B1 and B2 (or on the whole map?)
		// while the function is executing.

		// Step 4
		// Define a function "balance" that sums the amount of all the
		// bank accounts in the map. In order to have a consistent result,
		// the execution of this function should happen atomically:
		// no other deposit operations or balance operations should interleave.

		// Step 5
		// Define a function 'do_work', which has a for-loop that
		// iterates for config_t.iters times. Each iteration, the function should
		// call the function 'deposit' with 80% of the probability;
		// otherwise (the rest 20%) the function 'balance' should be called.
		// The function 'do_work' should measure 'exec_time_i', which is the
		// time needed to perform the entire for-loop. This time will be shared with
		// the main thread once the thread executing the 'do_work' joins its execution
		// with the main thread.

		// Step 6
		// The evaluation should be performed in the following way:
		// - the main thread creates #threads threads (as defined in config_t)
		//   << use std:threds >>
		// - each thread executes the function 'do_work' until completion
		// - the (main) spawning thread waits for all the threads to be executed
		//   << use std::thread::join() >>
		//	 and collect all the 'exec_time_i' from each joining thread
		// - once all the threads have joined, the function "balance" must be called
	std::thread * threads[cfg.threads];
	for (auto i = 0 ; i < cfg.threads ;++ i)
	{
		threads[i] = new std:: thread(do_work, i);
	}
	for ( auto each_th : threads )
	{
		each_th -> join();
	}
		// WHAT IS THE OUTPUT OF this call of "balance"?
		// DOES IT MATCH WHAT YOU EXPECT?
		// WHAT DO YOU EXPECT?
		// WHAT ARE THE OUTCOMES OF ALL THE "balance" CALLS DURING THE EXECUTION?
		// IS THAT WHAT YOU EXPECT?
		// std::cout << 'balance(last): ' << balance(key_max-1) << std::endl;
		// Step 7
		// Now configure your application to perform the same total amount
		// of iterations just executed, but all done by a single thread.
		// Measure the time to perform them and compare with the time
		// previously collected.
		// Which conclusion can you draw?
		// Which optimization can you do to the single-threaded execution in
		// order to improve its performance?

		// Step 8
		// Remove all the items in the map by leveraging the 'remove' function of the map
		// Destroy all the allocated resources (if any)
		// Execution terminates.
		// If you reach this stage happy, then you did a good job!
	// map -> apply(printer);
	for (int i = 0 ; i < key_max ;++ i)
	{
		map -> remove(i);
	}
	struct timeval end;
    gettimeofday(&end, NULL);
	exe_time = (end.tv_sec - start.tv_sec) * 1000000 + ((int)end.tv_usec - (int)start.tv_usec);;
	for (int i = 0 ; i < cfg.threads ;++ i)
	{
		std::cout << "thread" << i << "\t" << cons[i] << "(us)" <<std::endl;
	}
	std::cout << "total exe_time: " << exe_time << std::endl;
		// std:: cout << exe_time <<endl;
		// Final step: Produce plot
        // I expect each submission to include a plot in which
        // the x-axis is the concurrent threads used {1;2;4;8}
        // the y-axis is the application execution t ime.
        // The performance at 1 thread must be the sequential
        // application without locking

        // You might need the following function to print the entire map.
        // Attention if you use it while multiple threads are operating
    map -> apply(printer);

}

void test_driver(config_t &cfg) {
	run_custom_tests(cfg);
}
