#Dylan Thiemann
#Daily Programmer - 7-10-18
#https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/

#Sample Data
#00:00
#01:30
#12:05
#14:01
#20:29
#21:00

import sys

if (len(sys.argv) < 2):
    raise ValueError("No file input recieved")

filePath = sys.argv[1]

lines = []
with open(filePath) as f:
    lines = [line.strip() for line in f]

tens = ["oh", "", "twenty", "thirty", "forty", "fifty"]
ones = ["twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

for time in lines:
    timeSplit = time.split(":")
    h = int(timeSplit[0])
    m = int(timeSplit[1])
    ampm = "am" if h < 12 else "pm"

    if m == 0:
        print("It's", ones[h%12], ampm)
    elif m < 10:
        print("It's", ones[h%12], "oh", ones[m], ampm)
    elif m >= 10 and m < 20:
        print("It's", ones[h%12], ones[m], ampm)
    elif m == 20 or m == 30 or m == 40 or m == 50:
        print("It's", ones[h%12], tens[m // 10], ampm)
    else:
        print("It's", ones[h%12], tens[m // 10], ones[m % 10], ampm)
