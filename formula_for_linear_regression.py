
def find_mean(x_values):
    total_x=0
    for i in x_values:
        total_x +=i
        mean=total_x/len(x_values)
    return mean
def find_m(x,x_bar,y,y_bar):
    #formula of m =sum of (x-xbar) * (y-ybar)/sum of (x-xbar)**2
    sum_of_x_minus_x_bar_sqrt=0
    sum_of_x_minus_x_bar_MUL_y_minus_y_bar=0
    m=0
    for i in range(len(x)):
        sum_of_x_minus_x_bar_sqrt+=(x[i]-x_bar)**2
        sum_of_x_minus_x_bar_MUL_y_minus_y_bar+=(x[i]-x_bar)*(y[i]-y_bar)
    #apply formula in m variable
    m = sum_of_x_minus_x_bar_MUL_y_minus_y_bar/sum_of_x_minus_x_bar_sqrt
    return m
