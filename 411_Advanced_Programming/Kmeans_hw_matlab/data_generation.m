function data_set = data_generation()
%     data_set_k = [];
    data_set1 = normrnd(-10,5,[100,2]);
    data_set2 = normrnd(10,3,[100,2]);
    data_set3 = normrnd(0,3,[100,2]);
    data_set4 = normrnd(20,2,[20,2]);
%     for i = 1:K
%        data_set_k = [data_set_k; normrnd(-10+(K-1)*20,1+2*K,[100,2])];
%     end
    data_set = [data_set1; data_set2; data_set3;data_set4];
    csvwrite('data_set.csv',data_set);
%     data_set = data_set_k;
    plot(data_set(:,1),data_set(:,2),'r.')
end
% data_set1 = normrnd(-10,5,[100,2]);
% data_set2 = normrnd(10,3,[100,2]);
% data_set3 = normrnd(0,3,[100,2]);
% % data_set3 = normrnd(-10,2,[100,2]);
% csvwrite('data_set1.csv',data_set1);
% csvwrite('data_set2.csv',data_set2);
% % plot(data_set2,'r*')
% data_set = [data_set1; data_set2;data_set3];
% csvwrite('data_set.csv', data_set);
% plot(data_set(:,1),data_set(:,2),'b.')
% s1 = csvread('data_set1.csv');
% s2 = csvread('data_set2.csv');
% s1_x = zeros(1,100);
% s1_y = zeros(1,100);
% s2_x = zeros(1,100);
% s2_y = zeros(1,100);
% for i = 1:100
%     s1_x(i) = s1(i,1);
%     s1_y(i) = s1(i,2);
%     s2_x(i) = s2(i,1);
%     s2_y(i) = s2(i,2);
% end
% plot(s1_x,s1_y,'r*',s2_x,s2_y,'b.')
% plot(s2_x,s2_y,'b.')