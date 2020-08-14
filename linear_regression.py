import formula_for_linear_regression as f #this module is my custom module for my own formula functions.
x= [1,2,3,4,5]
y= [4,2,3,1,6]
predicted_y=[]
mean_of_x=f.find_mean(x)
mean_of_y=f.find_mean(y)
#The Linear ligression formula is y=mx+c
#so value of m is
m =f.find_m(x,mean_of_x,y,mean_of_y)
#c is calculated using the mean cortinate (mean_of_x,mean_of_y)
#predictedY=mx+c
#mean_of_y=m(mean_of_x)+c
#so,c=mean_of_y - m(mean_of_x)
c =mean_of_y-(m*mean_of_x)
for i in x:
    #applying formula mx+c
    predicted_y.append((m*i)+c)
#Printing the result.
for i in range(len(x)):
    print('The predicted cortinates %d - (%.1f,%.2f)' %(i+1,x[i],predicted_y[i]))
