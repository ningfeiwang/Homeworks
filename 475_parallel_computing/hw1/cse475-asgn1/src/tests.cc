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

	    void printer(int k, float v) {
			std::cout<<"<"<<k<<","<<v<<">"<< std::endl;
	}

	void run_custom_tests(config_t& cfg) {
		// Step 1
		// Define a simplemap_t of types <int,float>
		// this map represents a collection of bank accounts:
		// each account has a unique ID of type int;
		// each account has an amount of fund of type float.

		// Step 2
		// Populate the entire map with the 'insert' function
		// Initialize the map in a way the sum of the amounts of
		// all the accounts in the map is 10000

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

		// WHAT IS THE OUTPUT OF this call of "balance"?
		// DOES IT MATCH WHAT YOU EXPECT?
		// WHAT DO YOU EXPECT?
		// WHAT ARE THE OUTCOMES OF ALL THE "balance" CALLS DURING THE EXECUTION?
		// IS THAT WHAT YOU EXPECT?

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

		// Final step: Produce plot
        // I expect each submission to include a plot in which
        // the x-axis is the concurrent threads used {1;2;4;8}
        // the y-axis is the application execution t ime.
        // The performance at 1 thread must be the sequential
        // application without locking

        // You might need the following function to print the entire map.
        // Attention if you use it while multiple threads are operating
        map.apply(printer);

	}

void test_driver(config_t &cfg) {
	run_custom_tests(cfg);
}
