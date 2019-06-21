#!/usr/bin/env python

#################################################################################
#Linux JSON Data Generator, v1.0 						#
#Written by Matthew Dinep 							#
#June, 21th, 2019 								#
#################################################################################

import os,sys
import ConfigParser
import random
import string
import getpass

try:
	from Tkinter import *
	import tkMessageBox
	import tkFileDialog
except:
	print("Please install Tkinter on your system")
	sys.exit()

currDir = os.getcwd()
cfg = ConfigParser.ConfigParser()
master = Tk()
master.resizable(width=FALSE, height=FALSE)
master.wm_title("Flat Json Data Generator")

inputFile=inputIntegerFields=inputDoubleFields=inputDateFields=inputBooleanFields=inputPhoneFields=inputMonthFields=inputDayFields=inputYearFields=inputTimeFields=inputLatLonFields=pathCol=outDir=""
outputFile=maxUIDLength=staticValues=ssnDivider=phoneDivider=inputDateTimeFields=inputUniqueIdFields=inputSSNFields=inputLatFields=inputLonFields=isHeader=fieldCol=typeCol=numberToProduce=""

inStr = open(currDir + "/wordList.txt", "r")
readmeFile = open(currDir + "/README.md", "r")
inData = None
outfile = None
outDir = ""
counter = 0
dataSize = 0
strData = inStr.readlines()
inStr.close()
readmeData = readmeFile.readlines()[2:]
readmeFile.close()
rmf=''.join(readmeData)

def setConfig():
	global inputFile
	global pathCol
	global fieldCol
	global typeCol
	global numberToProduce
	global inputIntegerFields
	global inputDoubleFields
	global inputDateFields
	global inputBooleanFields
	global inputPhoneFields
	global inputMonthFields
	global inputDayFields
	global inputYearFields
	global inputTimeFields
	global inputLatLonFields
	global outputFile
	global maxUIDLength
	global staticValues
	global ssnDivider
	global phoneDivider
	global inputDateTimeFields
	global inputUniqueIdFields
	global inputSSNFields
	global inputLatFields
	global inputLonFields
	global isHeader
	global currDir

	configFile = tkFileDialog.askopenfilename(initialdir=currDir, title="Select Config File",filetypes = (("conf files","*.conf"),("all files","*.*")))
	currDir = configFile[0:configFile.rindex("/")]
	setConfig.configure(bg="chartreuse", activebackground="pale green")
	textBox.config(state=NORMAL)
	textBox.delete(1.0,END)
	textBox.insert(END, configFile)
	textBox.config(state=DISABLED)
	runButton.config(state=NORMAL)
	outputButton.config(state=NORMAL)
	cfg.read(configFile)

	inputFile = cfg.get('INPUT', 'file')
	pathCol = cfg.get('INPUT', 'pathColumn')
	fieldCol = cfg.get('INPUT', 'fieldColumn')
	typeCol = cfg.get('INPUT', 'typeColumn')
	inputIntegerFields = cfg.get('INPUT', 'integers').split(",")
	inputDoubleFields = cfg.get('INPUT', 'doubles').split(",")
	inputDateFields = cfg.get('INPUT', 'dates').split(",")
	inputBooleanFields = cfg.get('INPUT', 'booleans').split(",")
	inputPhoneFields = cfg.get('INPUT', 'phone').split(",")
	inputMonthFields = cfg.get('INPUT', 'month').split(",")
	inputDayFields = cfg.get('INPUT', 'day').split(",")
	inputYearFields = cfg.get('INPUT', 'year').split(",")
	inputTimeFields = cfg.get('INPUT', 'time').split(",")
	inputDateTimeFields = cfg.get('INPUT', 'datetime').split(",")
	inputUniqueIdFields = cfg.get('INPUT', 'uid').split(",")
	inputSSNFields = cfg.get('INPUT', 'ssn').split(",")
	inputLatFields = cfg.get('INPUT', 'latitude').split(",")
	inputLonFields = cfg.get('INPUT', 'longitude').split(",")
	inputLatLonFields = cfg.get('INPUT', 'LatLon').split(",")
	inHeader = cfg.get('INPUT', 'header').split(",")

	outputFile = cfg.get('OUTPUT', 'file')
	numberToProduce = cfg.get('OUTPUT','numberToProduce')
	maxUIDLength = cfg.get('OUTPUT', 'maxUIDLength')
	staticValues = eval(cfg.get('OUTPUT', 'staticValues'))
	ssnDivider = cfg.get('OUTPUT', 'ssnDivider').replace("\"","")
	phoneDivider = cfg.get('OUTPUT', 'phoneDivider').replace("\"","")
	pBox.config(state=NORMAL)
	fBox.config(state=NORMAL)
	tBox.config(state=NORMAL)
	nBox.config(state=NORMAL)
	outBox.config(state=NORMAL)
	pBox.delete(1.0,END)
	fBox.delete(1.0,END)
	tBox.delete(1.0,END)
	nBox.delete(1.0,END)
	outBox.delete(1.0,END)
	pBox.insert(END, pathCol)
	fBox.insert(END, fieldCol)
	tBox.insert(END, typeCol)
	nBox.insert(END, numberToProduce)
	outBox.insert(END, currDir + "/" + outputFile)
	pBox.config(state=DISABLED)
	fBox.config(state=DISABLED)
	tBox.config(state=DISABLED)
	nBox.config(state=DISABLED)
	outBox.config(state=DISABLED)

def setOutDir():
	global outDir
	outDir = tkFileDialog.askdirectory(initialdir="/home/" + getpass.getuser(), title="OutputDirectory",mustexist=True)
	outDir = outDir.replace("//","")
	outBox.config(state=NORMAL)
	outBox.delete(1.0,END)
	outBox.insert(END, outDir + "/" + outputFile)
	outBox.config(state=DISABLED)

def ioFiles(fileSuff=0):
	global inData
	global outfile
	global dataSize
	global outDir
	global inputFile
	global currDir

	outIterFile = ""
	if "/" in inputFile:
		infile = open(inputFile, "r")
		currDir = inputFile[0:inputFile.rindex("/")]
	else:
		infile = open(currDir + "/" + inputFile, "r")

	if fileSuff != 0:
		outIterFile = outputFile.replace(".","_" + str(fileSuff) + ".")
	else:
		outIterFile = outputFile
	if outDir == "":
		outfile = open(currDir + "/" + outIterFile, "w")
	else:
		outfile = open(outDir + "/" + outIterFile, "w")

	if isHeader == "true":
		inData = infile.readlines()[1:]
	else:
		inData = infile.readlines()
	infile.close()
	outfile.write("{\n")
	dataSize=len(inData)

def generateMonth():
	return str(random.randint(1,12))

def generateDat():
	return str(random.randint(1,28))

def generateYear():
	return str(random.randint(1900,2000))

def generateTime():
	return (str( "%02d" % random.randint(01,23)) + ':' + str( "%02d" % random.randint(01,59)) + ':' + str( "%02d" % random.randint(01,59)) + '.' + str( "%02d" % random.randint(00,99)) + 'Z')

def generatePhone(divider):
	return (str(random.randint(100,999)) + divider + str(random.randint(100,999)) + divider + str(random.randint(1000,9990)))

def generateSSN(divider):
	return (str(random.randint(100,999)) + divider + str(random.randint(10,99)) + divider + str(random.randint(1000,9990)))

def generateRandomString(length):
	return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(int(length)))

def generateRandomLat():
	return (str(random.randint(-89,99)) + "." + str(random.randint(100000,999999)))

def generateRandomLon():
	return (str(random.randint(-179,179)) + "." + str(random.randint(100000,999999)))

def generateRandomBool():
	return random.choice(('true','false'))

def generateRandomInt():
	return str(random.randint(10000,99999))

def generateRandomDouble(lLen, rLen):
	leftVal = ''.join((str(random.randint(0,9))) for _ in range(int(lLen)))
	rightVal = leftVal = ''.join((str(random.randint(1,9))) for _ in range(int(rLen)))
	return leftVal + "." + rightVal

def setIntField(line):
	return "\"" + line + "\": " + generateRandomInt()

def setDoubleField(line, lVal, rVal):
	return "\"" + line + "\": " + generateRandomDouble(str(lVal), str(rVal))

def setBoolField(line):
	return "\"" + line + "\": " + generateRandomBool()

def setMonthField(line):
	return "\"" + line + "\": \"" + generateRandomMonth() + "\""

def setDayField(line):
	return "\"" + line + "\": \"" + generateRandomDay() + "\""

def setYearField(line):
	return "\"" + line + "\": \"" + generateRandomYear() + "\""

def setDateField(line):
	return "\"" + line + "\": \"" + generateRandomMonth() + "-" + generateRandomDay() + "-" + generateRandomYear() + "\""

def setTimeField(line):
	return "\"" + line + "\": \"" + generateTime() + "\""

def setDateTimeField(line):
	return "\"" + line + "\": \"" + generateRandomMonth() + "-" + generateRandomDay() + "-" + generateRandomYear() + "T" + generateTime() + "\""

def setPhoneField(line):
	return "\"" + line + "\": \"" + generatePhone() + "\""

def setSSNField(line):
	return "\"" + line + "\": \"" + generateSSN(ssnDivider) + "\""

def setUIDField(line):
	return "\"" + line + "\": \"" + generateRandomString(maxUIDLength) + "\""

def setLatField(line):
	return "\"" + line + "\": \"" + generateRandomLat() + "\""

def setLonField(line):
	return "\"" + line + "\": \"" + generateRandomLon() + "\""

def setLatLonField(line):
	return "\"" + line + "\": \"" + generateRandomLat() + "," + generateRandomLon() + "\""

def setCharacterField(line, t):
	charLength = t[t.rindex("(")+1:t.rindex(")")]
	return "\"" + line + "\": \"" + generateRandomString(charLength) + "\""

def setStrField(line):
	global strData
	fieldValue = strData[random.randint(0,len(strData))].strip()
	if len(fieldValue)<5:
		subVal = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
		fieldValue = fieldValue + subVal
	return "\"" + line + "\": \"" + fieldValue + "\""

def setStatic(line, field):
	return "\"" + line + "\": \"" + staticValues[field].strip() + "\""

def processItems(inJLine, inField, dataType):
	if inField in staticValues:
		outLine = setStatic(inJLine,inField)
	elif inField in inputBooleanFields:
		outLine = setBoolField(inJLine)
	elif inField in inputIntegerFields:
		outLine = setIntField(inJLine)
	elif inField in inputDoubleFields:
		outLine = setDoubleField(inJLine,5,2)
	elif inField in inputMonthFields:
		outLine = setMonthField(inJLine)
	elif inField in inputDayFields:
		outLine = setDayField(inJLine)
	elif inField in inputYearFields:
		outLine = setYearField(inJLine)
	elif inField in inputDateFields:
		outLine = setDateField(inJLine)
	elif inField in inputTimeFields:
		outLine = setTimeField(inJLine)
	elif inField in inputDateTimeFields:
		outLine = setDateTimeField(inJLine)
	elif inField in inputPhoneFields:
		outLine = setPhoneField(inJLine)
	elif inField in inputUniqueIdFields:
		outLine = setUIDField(inJLine)
	elif inField in inputSSNFields:
		outLine = setSSNField(inJLine)
	elif inField in inputLatFields:
		outLine = setLatField(inJLine)
	elif inField in inputLonFields:
		outLine = setLonField(inJLine)
	elif inField in inputLatLonFields:
		outLine = setLatLonField(inJLine)
	elif "NUMBER" in dataType:
		intVar = dataType[dataType.rindex("(")+1:dataType.rindex(")")]
		if "," in intVar:
			lVal,rVal = intVar.split(",")
			outLine = setDoubleField(inJLine,lVal.strip(),rVal.strip())
		else:
			outLine = setIntField(inJLine)
	elif dataType.startswith("DATE"):
		outLine = setDateTimeField(inJLine)
	elif dataType.startswith("CHAR"):
		outLine = setCharacterField(inJLine, dataType)
	else:
		outLine = setStrField(inJLine)
	return outLine

def processData():
	global outfile
	global inData
	global counter
	global pathCol
	global fieldCol
	global typeCol

	for inLine in inData:
		counter = counter + 1
		outline = ""
		dataType = "VARCHAR"

		columnSet = inLine.split(",")

		inPath = columnSet[int(pathCol) - 1]
		inField = columnSet[int(fieldCol) - 1]
		if typeCol != "":
			dataType = columnSet[int(typeCol) - 1]
			if not dataType.endswith(")") and "(" in dataType:
				dataType = (dataType + "," + columnSet[int(typeCol)]).lstrip("\"").rstrip("\"")
		inField = inField.strip()
		inJLine = inPath.strip() + "." + inField
		inJLine = inJLine.lstrip(".")
		outLine = processItems(inJLine, inField, dataType)

		if counter != dataSize:
			outfile.write("\t" + outLine.replace("..",".") + ",\n")
		else:
			outfile.write("\t" + outLine.replace("..",".") + "\n")

	outfile.write("}")
	outfile.close()

def createDialogue(state):
	if state == "true":
		tkMessageBox.showinfo("SUCCESS", "Successfully processed data")
	else:
		tkMessageBox.showinfo("FAILURE", "Failed to process. Check config and input data.")

def runGen():		
	global counter
	global numberToPoduce
	counter = 0
	try:
		if numToProduce != "":
			for fNum in range(1,int(numberToPoduce)+1):
				ioFiles(fNum)
				processData()
		else:
			ioFiles()
			processData()
		createDialogue("true")
	except:
		createDialogue("false")

def showHelp():
	global currDir
	global rmf
	helpWin = Toplevel()
	helpWin.title("Help")
	helpWin.grid()
	pFrame = Frame(helpWin)
	pFrame.grid(row=0, column=0)
	helpBox = Text(pFrame, height=40, width=160)
	scroll = Scrollbar(pFrame)
	scroll.pack(side=RIGHT, fill=Y)
	helpBox.pack(side=LEFT, fill=Y)
	scroll.config(command=helpBox.yview)
	helpBox.config(yscrollcommand=scroll.set)
	closeButton = Button(helpWin, text="Close", width=20, command=lambda: helpWin.destroy(), bd=3)
	closeButton.grid(row=1, column=0)
	helpContent = "Information on how this tool works:\n\nNOTE: THE CURRENT DIRECTORY FOR THIS TOOL IS %s\n" % currDir
	helpContent = helpContent + rmf

	helpBox.insert(END,helpContent)
	helpBox.config(state=DISABLED)
	helpWin.mainloop()

def exist():
	master.destroy()

top = Frame(master)
bottom = Frame(master, bd=10)
top.grid(row=0, column=0)
bottom.grid(row=1, column=0)
setConfig = Button(master, text="Select Config File", width=30, command=setConfig, bg="orange red", activebackground="tomato", bd=3)
setConfig.pack(in_=top)
textBox = Text(master, height=1, width=40, state=DISABLED)
configLabel = Label(master, text="Config File: ")
configLabel.pack(in_=top)
textBox.pack(in_=top)

colFrame = Frame(bottom, bd=8)
colFrame.pack()
colLabel = Label(master, text="Column Numbers")
colLabel.pack(in_=colFrame)
pLabel = Label(master, text="Path Column")
pLabel.pack(in_=colFrame, side=LEFT)
pBox = Text(master, height=1, width=2, state=DISABLED)
pBox.pack(in_=colFrame, side=LEFT, fill=Y)
fLabel = Label(master, text="Field Column")
fLabel.pack(in_=colFrame, side=LEFT)
fBox = Text(master, height=1, width=2, state=DISABLED)
fBox.pack(in_=colFrame, side=LEFT, fill=Y)
tLabel = Label(master, text="Type Column")
tLabel.pack(in_=colFrame, side=LEFT)
tBox = Text(master, height=1, width=2, state=DISABLED)
tBox.pack(in_=colFrame, side=LEFT, fill=Y)
nLabel = Label(master, text="Num Output Files")
nLabel.pack(in_=colFrame, side=LEFT)
nBox = Text(master, height=1, width=2, state=DISABLED)
nBox.pack(in_=colFrame, side=LEFT, fill=Y)

outputFrame = Frame(bottom, bd=8)
outputFrame.pack()
outLabel = Label(master, text="Output Path")
outLabel.pack(in_=outputFrame)

x_scroll = Scrollbar(master, orient='horizontal')
x_scroll.pack(in_=outputFrame, side='bottom', fill='x')

outBox = Text(master, height=1, width=40, xscrollcommand=x_scroll.set, wrap='none', state=DISABLED)
outBox.pack(in_=outputFrame)
x_scroll.config(command=outBox.xview)

outputButton = Button(master, text="Change Output Dir", width=30, command=setOutDir, state=DISABLED, bd=3)
outputButton.pack(in_=bottom)

runButton = Button(master, text="Generate Data", width=30, command=runGen, state=DISABLED, bd=3)
runButton.pack(in_=bottom)
infoButton = Button(master, text="Help/Info", width=30, command=showHelp, bd=3)
infoButton.pack(in_=bottom)
quitButton = Button(master, text="Exit", width=30, command=exist, bd=3)
quitButton.pack(in_=bottom)

mainloop()


