%%%%ISE 416 Dynamic Programming HW1
%%%%Author: Ningfei Wang
%%%%Date: Sep, 04, 2018

%clean
clear;
clc;

%data
data = [2.000 1.000 -0.500 0.950 0.935 -0.115 0.442 0.705 0.099 0.224 0.481];
len = length(data);

% answer for 1) 2) 3) and print
for k = 1 : 5
    [th0, th, mse] = fun_cvx(data, k);
    disp('**************************');
    fprintf('K = %d \n',k);
    fprintf('th0 = %.4f \n',th0);
    for i = 1 : length(th)
        fprintf('th%i = %.4f \n',i,th(i));
    end
    fprintf('mse = %.4f \n', mse);
end

%%%%%%%%%%%%prediction for question 5)
k = 3;
[th_pre0, th_pre, mse_pre] = fun_cvx(data, k);
disp('**************************');
disp("predictions x(12:21)")
for i = 12 : 21
    len = length(data);
    %predict
    pre =  th_pre0 + fliplr(data(len-2 : len)) * th_pre;
    data = [data, pre];
    fprintf('x(%i) = %.3f \n', i-1, data(i));
end



    
