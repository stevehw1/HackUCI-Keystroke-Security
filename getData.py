from Tkinter import *
from time import time

start_time = end_time = 0
master = Tk()
e = Entry(master)
e.pack()
e.focus_set()
keys = []
differences = []

def key(event):
    if event.char == '\r':
        e.unbind("<Key>")
        return

    end_time = time()
    # print "pressed", repr(event.char)
    keys.append((event.char, end_time-start_time))
    # keys.append((event.char, end_time-start_time))
    # print "measured time:", end_time-start_time

e.bind("<Key>", key)

start_time = time()
mainloop()

first = True
for x in range(0, len(keys)):
    if x != len(keys)-1:
        fuck = (keys[x][0], keys[x+1][0], (keys[x+1][1] - keys[x][1]))
        if first == True:
            differences.append(fuck)
        else:
            differences[x][2] + fuck[2]

    # else:
    #     print keys[x]

for dif in differences:
    print "%.6f" % (dif[2])

print()
