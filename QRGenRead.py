import qrcode
import cv2
from PIL import Image, ImageDraw

#Generating a QR code image from a given string
ipstr = "Dog ID 1236,Loc Road 9 HIG Phase 1, BHEL, ARV 22-6-22, ABC 10-1-22"
opfile = "Dog1236.jpg"

def myqrgen(ipstring, opfilename):
    img = qrcode.make(ipstring)
    img.save(opfilename)
    print(f'Generated the QR code for {opfilename}\n')
    return 0


#Reading the QR code, from an image
ipfile = "Dog1236.jpg"

def myqrread(ipfilename):
    d = cv2.QRCodeDetector()
    opstring,pts,straight_qrcode  = d.detectAndDecode(cv2.imread(ipfilename))
    print(f'QR Reading complete ! \nThe output string is:  {opstring}')
    return opstring

#Add CRUD Code here
#Create a Database (locally / remotely)
#Create a table in the database (locally/remotely)
#Create funtions to C, R, U and D the DB - ?


#Calling the functions here
myqrgen(ipstr, opfile)

opstr = myqrread(ipfile)

