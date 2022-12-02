#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
        if i == ord('q') or i == ord('e'):
                continue
        print("{0:c}".format(i), end="")
# ord receives a char and return asci value integer
