import os



stop = 0
while(!stop):
    cmd = str(raw_input('[C]REATE, [A]DD, or [S]TOP?'))

    if cmd == 'C' or cmd == 'c':
        #WHAT IF FILE ALREADY EXISTS?????
        loc = str(raw_input('Please enter the name & location of the file.'))
        if loc[-4:] != '.xml':
            loc += '.xml'

        bgfile = open(loc, 'w')

        #Start the file contents
        initXML(bgfile, loc)

        #Ask for first file
        gimmeFile = 'Please enter the name & location of the first picture.'
        pic1 = str(raw_input(gimmeFile))
        dur = str(raw_input('How many miliseconds shall it last?'))

        #Add first file
        addPic(bgfile, pic1, dur)

        #End file to prevent stupid
        addEnd(bgfile, pic1, pic1, dur)

        print 'Your file has been created!  Now add more pictures!!!!!!!!!'

        bgfile.close()
        
        
    elif cmd == 'A' or cmd == 'a':
        bgfile = open(loc, 'a+')

    elif cmd == 'S' or cmd == 's':
        stop = 1
        print 'Goodbye!'

    else
        print 'Invalid command.'

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

# Remove the ending for more pics
def remEnd(ofile)
    
    os.remove(temp)
    
