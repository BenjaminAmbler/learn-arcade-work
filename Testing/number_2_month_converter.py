###########################################################################
# This is a program that was made by Ben Ambler on 2/18/23.
# This program takes in a number, 1 through 12, and puts out
# a month that corresponds with that number.
#
###########################################################################
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
   # months = "012,345,567,8910, etc... 343536"
n = int(input("Enter a month number: "))
if n == 1:
    print(months[0:3])
if n == 2:
    print(months[3:6])
if n == 3:
    print(months[6:9])
if n == 4:
    print(months[9:12])
if n == 5:
    print(months[12:15])
if n == 6:
    print(months[15:18])
if n == 7:
    print(months[18:21])
if n == 8:
    print(months[21:24])
if n == 9:
    print(months[24:27])
if n == 10:
    print(months[27:30])
if n == 11:
    print(months[30:33])
if n == 12:
    print(months[33:36])