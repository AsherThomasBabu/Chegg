def mse_plane(x0, x1, t, w):
    
    summation = 0  #variable to store the summation of differences
    n = len(x0) #finding total number of items in list
    for i in range (0,n):  #looping through each element of the list
    difference = x0[i] - x1[i]  #finding the difference between observed and predicted value
    squared_difference = difference**2  #taking square of the differene 
    summation = summation + squared_difference  #taking a sum of all the differences
    mse = summation/n  #dividing summation by total values to obtain average

    return mse

def dmse_plane(x0, x1, t, w):

    ( ) # Enter the appropriate code here instead.

    #return d_w0, d_w1, d_w2

    return d_w