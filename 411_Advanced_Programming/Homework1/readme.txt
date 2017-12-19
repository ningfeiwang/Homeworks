code format：
	UTF－8

language:
	python

file:
	hw1.py: source code
	t_test.dat: the data of critical t-test values in critical possibility 0.05 sorted by the degrees of freedom


date: Sep, 1, 2017

running instructions (in sunlab):
1	go to the path of hw1.py and t_test.dat
2	use instruction:
		python hw1.py

design:
	task1(sample t-test): I calculate the value of on sample t-test, using the list of speed, the previous speed 10000, the variance… Then, I use the degrees of freedom and critical possibility 0.05 to search the critical value in the t_test.dat file and compare them. Finally, depending on the comparing result, I gain the conclusion the new system speed and the previous speed do not have obvious difference.
	task2(pair t-test): The difference from task1 is use pair t-test. Also, the conclusion is that the new system speed and the previous speed do not have obvious difference.

results(running in sunlab):
one sample t-test:
critical possibility 0.05, critical t-value 2.571
the value of t-test: 2.0740572394
the previous speed and the new system speed do not have obvious difference
paired t-test:
critical possibility 0.05, critical t-value 2.571
the value of t-test: 1.29524168983
the previous speed and the new system speed do not have obvious difference
