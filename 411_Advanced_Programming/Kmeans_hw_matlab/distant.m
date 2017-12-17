function dist = distant(data, center)
    dist = sqrt(sum((data-center).^2));
end