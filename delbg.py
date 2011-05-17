# Will create an xml file for a whole folder of pictures (.jpg, .png, and .bmp)

import os

stop = 0
while(!stop):
    if cmd == 'C' or cmd == 'c':
        #WHAT IF FILE ALREADY EXISTS?????
        
        loc = str(raw_input('Please enter the name & location of the file.'))
        if loc[-4:] != '.xml':
            loc += '.xml'

        #Ask for folder location
        picDir = str(raw_input('Please enter the picture directory.'))
        
        dur = str(raw_input('How many miliseconds shall each picture last?'))

        randy = str(raw_input('Randomize? (y/n)'))

        bgfile = open(loc, 'w')        

        #Start the file contents
        initXML(bgfile, loc)

        #Get pics into a list
        
        

        #Add first file
        for x in picL:
            addPic(bgfile, x, dur)

        #End file
        addEnd(bgfile, pic1, pic1, dur)

        bgfile.close()

#===========================<Function library>==================================
def initXML(ofile, loc):
    ofile.write('<background>\n\t<starttime>\n\t\t<hour>0</hour>\n\t\t')
    ofile.write('\n\t\t<minute>00</minute>\n\t\t<second>01</second>)
    ofile.write('\n\t</starttime>')
    

#Add picture to file
#NEED TO ADD CODE TO REMOVE THEN ADD FINISHING CODE!!!!!
def addPic(ofile, loc, dur):
    ofile.write('<static>\n\t<duration>' + dur +'</duration>')
    ofile.write('\n\t<file>' + loc + '</file>')
    ofile.write('\n</static>')

#Add trasition time between pic1 & pic2
def addTrans(ofile, pic1, pic2, dur):
    ofile.write('<transition>\n\t<duration>' + dur + '</duration>')
    ofile.write('\n\t<from>' +picc1 + '</from>')
    ofile.write('\n\t<to>' +pic2+ '</to>\n</transition>')
    
#Add ending for after user adds a pic
def addEnd(ofile, loc1, loc2, dur)
    ofile.write('<transition>\n\t<duration>' + dur + '</duration>')
    ofile.write('\n\t<from>' + loc + '</from>')
    ofile.write('\n\t<to>' + loc2 + '</to>\n</transition>')
