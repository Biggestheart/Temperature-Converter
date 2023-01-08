#Input the number you want to calculate
#The program will calculate your input from Fahrenheit to Celcius & from Celcius to Fahrenheit
import math
x = eval(input())
f_c = (x-32)/1.8
c_f = 1.8*x+32
print("Fahrenheit to Celcius of",x,"is:",math.floor(f_c))
print("Celcius to Fahrenheit of",x,"is:",math.floor(c_f))