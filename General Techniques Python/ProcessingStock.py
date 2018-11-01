#Processing the Stock data can be done in a variety of ways.  
#You MUST take note of the file format.  Notice that each line is 
#                   Open         High   ...       Adj Close   Volume
#Date                                   ...                         
#2017-01-18   829.799988   829.809998   ...      829.020020  1027700

#if we index the line we see that it is consistent acorss everyline
#Simpliest approach is

str = "2017-01-18   829.799988   829.809998   ...      829.020020  1027700"

#if we want the opening price
print(str[13:22])