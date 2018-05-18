words = "It's thanksgiving day. It's my birthday,too!"
wordsFind = "It's thanksgiving day. It's my birthday,too!".find("day", 18);
wordsReplace = "It's thanksgiving day. It's my birthday,too!".replace("day", "month", 1);
print(wordsReplace)

m = [2,54,-2,7,12,98]
high = max(m)
low = min(m)
print("The Max is {}, and the Min is {}".format(high, low))

firstLast = ["hello",2,54,-2,7,12,98,"world"]
first = firstLast[0]
last = firstLast[-1]
print("The first value is {}, and the last value is {}".format(first, last))

x = [19,2,54,-2,7,12,98,32,10,-3,6]
y = x.sort()
y = sorted(x)
print(y)
length = y[0:5]
end_length = y[5:11]
print(length)
z = [length] + end_length
print(z)
