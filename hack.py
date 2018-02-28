from Tkinter import *
from time import time

password = ""
account = ""
def m2():
    def closeWindow(event):
	       master2.destroy()
    master2 = Tk()
    e = Entry(master2)
    e.pack()
    e.focus_set()
    e.bind("<Key>", key)
    e.bind("<Return>", closeWindow)
    e.bind("<Left>", getBypass)
    e.bind("<Right>", getBypass)
    master.destroy()

def steven():
	global password
	global account
	password = "imsteven"
	account = "Steven"
	m2()

def henry():
	global password
	global account
	password = "imhenry"
	account = "Henry"
	m2()

start_time = end_time = 0
master = Tk()

master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)
master.title('Account Chooser')
master.geometry("400x200") #You want the size of the app to be 500x500
master.resizable(1, 0) #Don't allow resizing in the x or y direction

Label(master, text = "Choose an Account").grid(row = 0, column = 0, columnspan=2)
password = Entry(master)
Button(master, text = "Henry", command = henry, height = 1).grid(sticky='NSEW')
Button(master, text = "Steven", command = steven, height = 1).grid(sticky='NSEW')
# Button(master, text = "New", command = steven, height = 1).grid(sticky='NSEW')

keys = []
differences = []


def key(event):
    if event.char == '\r':
        e.unbind("<Key>")
        return

    end_time = time()
    keys.append((event.char, end_time-start_time))

bypass = False
def getBypass(event):
    global bypass
    bypass = True

start_time = time()
mainloop()

imsteven = [(0.02667257143, 0.052087/2), (0.05027261905, 0.084157/2), (0.08000904762, 0.047082/2), (0.09100619048, 0.072332/2), (0.1266666667, 0.071547/2), (0.06206685714, 0.046919/2), (0.0703887619, 0.107189/2)]

imhenry = [(0.065577905, 0.036053), (0.174772333, 0.049049), (0.102860778, 0.06441), (0.058267167, 0.059833), (0.096861222, 0.062056), (0.082386611, 0.044183)]


if bypass == False:
    # name = raw_input("What password would you like?")
    first = True
    for x in range(0, len(keys)):
        if x != len(keys)-1:
            key_differences = (keys[x][0], keys[x+1][0], (keys[x+1][1] - keys[x][1]))
            if first == True:
                differences.append(key_differences)
            else:
                differences[x][2] + key_differences[2]



    rejected = False;
    userInput = ""
    for char in keys:
    	userInput += char[0]

    if userInput != password:
        rejected = True

    if rejected != True:
        for comp in range(0, len(differences)):
            if password == "imhenry":
                if not (differences[comp][2] >= imhenry[comp][0] - imhenry[comp][1] and differences[comp][2] <= imhenry[comp][0] + imhenry[comp][1]):
                    rejected = True
                    break
            elif password == "imsteven":
                if not (differences[comp][2] >= imsteven[comp][0] - imsteven[comp][1] and differences[comp][2] <= imsteven[comp][0] + imsteven[comp][1]):
                    rejected = True
                    break

    if len(keys) == 0:
    	rejected = True

    if rejected == True:
    	if password != userInput:
    		print "Password incorrect. You've been rejected"
       	else:
       		print "Password correct, too much typing speed variance"
    else:
        print "Welcome %s" % (account)

else: #Bypass is True
    print "Welcome %s" % (account)
