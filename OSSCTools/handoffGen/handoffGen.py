# Scope of project is to expand upon the coundHandoff.ps1 file I use daily.  I want to make this a standalone GUI that will generate a formatted handoff template.

import os, time, platform

def getNum(x):
    y = len(x)
    if x > y:
        return y
    else:
        return x
    #allows user to input tally marks or numerals and get the expected result. NOT_YET_IMPLEMENTED 100%  Currently checks for 0 and non zero, but has to be in tally form otherwise

def calcBreak(x, y):
    from datetime import datetime
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(y, FMT) - datetime.strptime(x, FMT)
    return tdelta
#Currently working on this time calc function, seems to do nothing right now.
def validConv(x):
    if x == '':
        return 0
    else:
        return getNum(x)

shiftDict = {
    'shift': '',
    'date': ''
}
#initializing the numbers being converted with 0 to appease the compiler.
titleDict = {
    'outgoingAnalyst': '',
    'breakStart': '',
    'breakEnd': '',
    'breakTotal': ''
}
certDict = {
    'certCreated': '',
    'certClosed': '',
    'CertEsc': '',
    'CertFollow': '',
    'CertReopen': '',
    'certOther': '',
    'abuseForward': '',
    'emailsFiled': '',
    'other': ''
}
ticketDict = {
    't2Esc': '',
    'tClosed': '',
    'tCreated': '',
    'tEsc': '',
    'tWFR': '',
    'tAppend': '',
    'tFollow': '',
    'msnAcct': ''
}
scardDict = {
    'pinsUnblocked': '',
    'emailFiled': ''
}
nextDict = {
    'activeIR': '',
    'activeRF': '',
    'activePU': '',
    'activeCert': '',
    'numAnalysts': ''
}

shiftDict['shift'] = raw_input('What shift are you on? MS, GS, AS, NS, GNS: \n')
shiftDict['date'] = time.strftime("%d/%m/%Y")

titleDict['outgoingAnalyst'] = raw_input("what is your alias?: \n")
titleDict['breakStart'] = raw_input("When did you go on break?(HH:MM:SS): \n")
titleDict['breakEnd'] = raw_input("When did you get back from break?(HH:MM:SS): \n")
titleDict['breaktotal'] = calcBreak(titleDict['breakStart'], titleDict['breakEnd'])

#test
print(titleDict['breakTotal'])

handler = raw_input('How many certs did you create?: \n')
certDict['certCreated'] = validConv(handler)
handler = raw_input("How many certs did you close: \n")
certDict['certClosed'] = validConv(handler)
handler = raw_input("How many certs did you escalate to SIM? \n")
certDict['CertEsc'] = validConv(handler)
handler = raw_input("How many certs did you follow up on?: \n")
certDict['CertFollow'] = validConv(handler)
handler = raw_input("How many certs did you reopen?: \n")
certDict['CertReopen'] = validConv(handler)
handler = raw_input("How many other did you file?: \n")
certDict['certOther'] = validConv(handler)
handler = raw_input("How many reports did you forward to abuse?: \n")
certDict['abuseForward'] = validConv(handler)
handler = raw_input("How many emails did you file?: \n")
certDict['emailsFiled'] = validConv(handler)
handler = raw_input("How many emails did you file outside of cert case folders?: \n")
certDict['other'] = validConv(handler)

#checking contents of dict to make sure validation is working
#for key, value in certDict.iteritems():
#    print key, value

handler = raw_input("How many times did you contact tier 2?: \n")
ticketDict['t2Esc'] = validConv(handler)
handler = raw_input("How many tickets did you close?: \n")
ticketDict['tClosed'] = validConv(handler)
handler = raw_input("How many tickets did you create?: \n")
ticketDict['tCreated'] = validConv(handler)
handler = raw_input('How many tickets did you escalate? \n')
ticketDict['tEsc'] = validConv(handler)
handler = raw_input('How many tickets did you place in WFR?: \n')
ticketDict['tWFR'] = validConv(handler)
handler = raw_input("How many tickets did you append?: \n")
ticketDict['tAppend'] = validConv(handler)
handler = raw_input("How many tickets did you follow up on?: \n")
ticketDict['tFollow'] = validConv(handler)
handler = raw_input("How many MSNAccounts requests did you work?: \n")
ticketDict['msnAcct'] = validConv(handler)

handler = raw_input("How many smartcards did you unblock?: \n")
scardDict['pinsUnblocked'] = validConv(handler)
handler = raw_input("How many smartcard emails did you file?: \n")
scardDict['emailFiled'] = validConv(handler)

handler = raw_input("How many IR tickets are in the queue?: \n")
nextDict['activeIR'] = validConv(handler)
handler = raw_input("How many RF tickets are in the queue?: \n")
nextDict['activeRF'] = validConv(handler)
handler = raw_input("How many active pin unblocks are there in the inbox?: \n")
nextDict['activePU'] = validConv(handler)
handler = raw_input("How many active certs are in the inbox?: \n")
nextDict['activeCert'] = validConv(handler)
handler = raw_input("How many analysts are coming in next shift?: \n")
nextDict['numAnalysts'] = validConv(handler)

analystAlias = []

for i in range(0, int(nextDict['numAnalysts'])):
    print("What is the alias of analyst #") + str(nextDict['numAnalysts'] + "?: \n")
    handler = raw_input("")
    analystAlias.append(handler)


#test case
#for j in range(0, int(nextDict['numAnalysts'])):
#   print analystAlias[j]



notes = raw_input("Please enter any notes for the next shift: \n")

#fileLoc = os.path.join(os.path.expanduser('~'), 'Desktop') #define default save location
#handoff = open("handoff.html" "w")

