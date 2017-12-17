function [data_set, class, err] = kmeans_fun(K)

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
%     clear;
%     clc;
%     K = 6;
%     K = class_num;
    data_set = csvread('data_set.csv');
    [row, line] = size(data_set);
    % init
    center = zeros(K, line);
    max_d = zeros(1,line);
    min_d = zeros(1,line);
    for i = 1:line
        max_d(i) = max(data_set(:,i));
        min_d(i) = min(data_set(:,i));
        for j = 1:K
            center(j,i) = max_d(i)+(min_d(i) - max_d(i))*rand();
        end
    end
    % center =[-10,-10;10,10]
    % k = 0
    while (1)
        class=[];
        %     class2=[];

        pre_cen = center;
        for i = 1:row
            distance = [];
            for j = 1:K
               distance = [distance; distant(data_set(i,:),center(j,:))];
            end
            [val,index]=min(distance);
            class = [class;index];
        %        for j = 1:line
        %         for j = 1:K
        %            dist1 = dist(data_set(row , :),center(1,:));
        %            dist2 = dist(data_set(row , :),center(2,:));
        %            if dist1 < dist2
        %                class1 = [class1;data_set(row , :)];
        %            else
        %                class2 = [class2;data_set(row , :)];
        %            end
        end
        center_sum = zeros(K,line);
        quan = zeros(K,line);
        for i = 1:length(class)
            for j = 1:line
               center_sum(class(i),j) = center_sum(class(i),j) + data_set(i,j);
               quan(class(i),j) = quan(class(i),j) + 1;
            end
        end
        center = center_sum./quan;
        %     center
    %     k = k+1
        err = sqrt(sum(sum((pre_cen - center).^2)));
        if any(isnan(err))
            break
        end
        if err < 0.01
           break; 
        end

    end
end