shours = input("Enter Hours: ")
#try:
#    fhours = float(shours)
#    srate = input("Enter Rate: ")
#    try:
#        frate = float(srate)
        #print(fhours, frate)
#        if fhours > 40:
#            print("Overtime")
#            fhoursovertime = fhours - 40
#            xpay = (fhours * frate) + (fhoursovertime * frate * 0.5)
#        else :
#            print("Regular")
#            xpay = fhours*frate
#        print("Pay:", xpay)
#    except:
#        print("You did not enter a number")
#
#except Exception as e:
#    print("You did not enter a number")


#another way to write it limiting the line contained in the try except block is
try:
    fhours = float(shours)
    srate = input ("Enter Rate: ")
    try:
        frate = float(srate)
    except:
        quit()
except:
    print("You did not enter a number")
    quit()
if fhours > 40:
    print("Overtime")
    fhoursovertime = fhours - 40
    xpay = (fhours * frate) + (fhoursovertime * frate * 0.5)
else :
    print("Regular")
    xpay = fhours*frate
print("Pay:", xpay)
