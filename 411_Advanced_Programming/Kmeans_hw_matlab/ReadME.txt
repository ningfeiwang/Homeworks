
Email: niw217@lehigh.edu

There are four m files, one fig file and a CSV file. The m file is the codes, the fig file is the GUI layout and the CSV file is the generated data. Also, you can generate the data by click the data generation button in GUI.

To run these codes, you need to import these code in Matlab(I use Matlab 2017b) first. Then, run the ‘Kmeans_GUI.m’, which is the main function. After that, it will show the GUI and you can click the ‘Data Generation’ to generate the data. You can input the number of class—-‘K’. ‘K’ should be from 1 to 5 and must be integer. And you can click ‘classification’. Then you will see the results of classification in the left.

Finally, I will introduce these four m files. ‘Kmeans_GUI.m’ is the main function. It gains some parameters from other functions and control to plot. ‘Kmeans_fun.m’ is K-means algorithm finished by myself. ‘distant.m’ calculates the Euclidean Distance between two points, which will be used in ‘Kmeans_fun.m’ to decide which class does this point belong to. ‘data_generation.m’ is used to generate the data from normal distributions of different mean and standard deviation.