function [th0,th,mse] = fun_cvx(data, k)
    len = length(data);
    x = [];
    %get x from data which use a sliding windows
    for i = 1 : len - k
       x =  [x ; data(i : i + k - 1)];
    end
    x = fliplr(x);
    %get y
    y = data(1 + k : len);
    M = length(y);
    
    % cvx
    cvx_begin quiet
        variable th0
        variable th(k)
        variables y_hat(M)
        minimize (sum((y' - y_hat).^2)/M)
        subject to
            y_hat == th0 + x * th
    cvx_end
    mse = cvx_optval;

end