# Will create an xml file for a whole folder of pictures (.jpg, .png, and .bmp)

import os

#===========================<Function library>==================================
def initXML(ofile, loc):
    ofile.write('<background>\n\n\t<starttime>\n\t\t<hour>0</hour>')
    ofile.write('\n\t\t<minute>00</minute>\n\t\t<second>01</second>')
    ofile.write('\n\t</starttime>')
    

#Add picture to file
#NEED TO ADD CODE TO REMOVE THEN ADD FINISHING CODE!!!!!
def addPic(ofile, pic, dur):
    ofile.write('\n<static>\n\t<duration>' + str(dur) +'</duration>')
    ofile.write('\n\t<file>' + pic + '</file>')
    ofile.write('\n</static>')

#Add trasition time between pic1 & pic2
def addTrans(ofile, pic1, pic2, dur):
    ofile.write('<transition>\n\t<duration>' + str(dur) + '</duration>')
    ofile.write('\n\t<from>' +pic1 + '</from>')
    ofile.write('\n\t<to>' +pic2+ '</to>\n</transition>')
    
#Add ending transition for after user adds a pic
#This will be used to loop back to beginning of list
def addEnd(ofile, pic1, pic2, dur):
    ofile.write('<transition>\n\t<duration>' + str(dur) + '</duration>')
    ofile.write('\n\t<from>' + pic1 + '</from>')
    ofile.write('\n\t<to>' + pic2 + '</to>\n</transition>\n\n</background>')
#===============================================================================




#WHAT IF FILE ALREADY EXISTS?????
#WHAT IF LOCATION DOESN'T EXIST???

loc = str(raw_input('Please enter the name & location of the file:\n'))
if loc[-4:] != '.xml':
    loc += '.xml'

#Ask for folder location
picDir = str(raw_input('Please enter the picture directory:\n'))
if picDir[-1] != '/':
    picDir += '/'


dur = str(raw_input('How many miliseconds shall each picture last?\n'))

bgfile = open(loc, 'w')        

#Start the file contents
initXML(bgfile, loc)

#Get pics into a list
picL = os.listdir(picDir)

#Get list with only pics
picLN = []

for x in picL:
    if (x[-4:] == '.jpg') or (x[-4:] == '.png') or (x[-4:] == '.bmp'):
        picLN.append(x)

for i in range(len(picLN[:-2])):
    addPic(bgfile, picDir+picLN[i], dur)
    addTrans(bgfile, picDir+picLN[i], picDir+picLN[i+1], 4) 

addPic(bgfile, picDir+picLN[-1], dur)

#End file
addEnd(bgfile, picDir+picLN[-1], picDir+picLN[0], 4)

bgfile.close()
