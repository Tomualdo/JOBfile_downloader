#!/usr/bin/env python3

import nclib
import sys
import os
from datetime import date

if len(sys.argv)<=1:
    print("No ARGs !! Exiting..")
    print("1st ARG: LINE dir")
    print("2nd ARG: IP (10.210.202.<xxx>)")
    print("3rd ARG: [OPTIONAL] datefolder")
    print("4th ARG: [OPTIONAL] specific JOB file")
    sys.exit()

today = date.today()
d1 = today.strftime("%Y%m%d")

if sys.argv[3:]:
    print ("rewriting date folder from: ",d1," to ",sys.argv[3]) 
    d1 = sys.argv[3]

######################
### DIR name & IP ####
######################
directory=sys.argv[1]
IP=sys.argv[2]

try:
    os.mkdir('/home/tom/Projects/proface/robotFiles/'+directory+'')
except:
    pass
try:
    os.mkdir('/home/tom/Projects/proface/robotFiles/'+directory+'/'+d1)
except:
    pass

def formating(jobNo):

    print("saved ",jobNo)
    # FORMATING ***********************************************************
    # FileNotFoundError: [Errno 2] No such file or directory: '/home/tom/Projects/proface/robotFiles/scr1/20200303/job0000_20200303.txt'

    f = open('/home/tom/Projects/proface/robotFiles/'+directory+'/'+d1+'/job'+jobNo+'_'+d1+'.txt','rb')    
    l = list(f.read())
    l = l[36:]  #remove first 36 elements (header)

    #add extension for old programs
    extension = [0,0,0]
    l = l+extension

    for x in range(20):  # remove UDP separatros
        n=0
        temp_list=list()
        for ch in range(len(l)):
            if n<len(l):        # keep length of the list (index overflow)
                if l[n]==72 and l[n+1]==70 and l[n+2]==1 :
                    temp_list=l[:n] # cut list from beginning to first found HF...
                    l=l[n+12:]      # cut list from end of HF(12).... to files end
                    l=temp_list+l   # concatenante the lists 
                    break
            n=n+1

    # REMOVE UNPRINTABLE CHARS
    n=0
    for ch in range(len(l)):    
        for x in range(126,255):
            if n<len(l):        # keep length of the list (index overflow)
                if l[n]==x:
                    l[n]=0 
        n=n+1 

    n=0
    for ch in range(len(l)):    # check each character in list
        for x in range(1,127):  # check specific pattern with ascii character
            if n<len(l)-6:        # keep length of the list (index overflow)
                if (l[n]==x and l[n+1]==0 and l[n+2]==0 and l[n+3]==0 and l[n-1]==0) :#" 0 ? 0 0 0 "   << specific pattern
                    l[n+2] = 13 # input CR
                    l[n+3] = 10 # input LF
                    l[n] = 0    # remove founded character
                    n=n+3       # jump to next possible 3 pattern
                if (l[n]==x and l[n+1]==0 and l[n+2]==0 and l[n+3]==0 and l[n+4]==32 and l[n+5]==32 and l[n+6]==32 ) :#" ? 0 0 0 _ _ _ "   << specific pattern
                    l[n+2] = 13 # input CR
                    l[n+3] = 10 # input LF
                    l[n] = 0    # remove founded character
                    #n=n-3       # jump to next possible 3 pattern
                if (l[n]==x and l[n+1]==0 and l[n+2]==0 and l[n+3]==0 and l[n+4]==83 ) :#" X 0 0 0 "   << specific pattern
                    l[n+2] = 13 # input CR
                    l[n+3] = 10 # input LF
                    l[n] = 0    # remove founded character
        n=n+1

#    n=0
#    for ch in range(len(l)):    # check each character in list
#        for x in range(1,127):  # check specific pattern with ascii character
#            if n<len(l)-4:        # keep length of the list (index overflow)
#                if (l[n]==x and l[n+1]==0 and l[n+2]==0 and l[n+3]==0 and l[n+4]!=0 ) :#" X 0 0 0 "   << specific pattern
#                    l[n+2] = 13 # input CR
#                    l[n+3] = 10 # input LF
#                    l[n] = 0    # remove founded character
#                    #n=n+3       # jump to next possible 3 pattern
#               # if (l[n]==88 and l[n+1]==0 and l[n+2]==0 and l[n+3]==0 ) :#" X 0 0 0 "   << specific pattern
#               #     l[n+2] = 13 # input CR
#               #     l[n+3] = 10 # input LF
#               #     l[n] = 0    # remove founded character
#               # if (l[n]==80 and l[n+1]==0 and l[n+2]==0 and l[n+3]==0 ) :#" P 0 0 0 "   << specific pattern
#               #     l[n+2] = 13 # input CR
#               #     l[n+3] = 10 # input LF
#               #     l[n] = 0    # remove founded character
#               #     #n=n+3       # jump to next possible 3 pattern
#               # if (l[n]==100 and l[n+1]==0 and l[n+2]==0 and l[n+3]==0 ) :#" d 0 0 0 "   << specific pattern
#               #     l[n+2] = 13 # input CR
#               #     l[n+3] = 10 # input LF
#               #     l[n] = 0    # remove founded character
#               #     #n=n+3       # jump to next possible 3 pattern
#               # if (l[n]==84 and l[n+1]==0 and l[n+2]==0 and l[n+3]==0 ) :#" T 0 0 0 "   << specific pattern
#               #     l[n+2] = 13 # input CR
#               #     l[n+3] = 10 # input LF
#               #     l[n] = 0    # remove founded character
#               #     #n=n+3       # jump to next possible 3 pattern
#               # if (l[n]==28 and l[n+1]==0 and l[n+2]==0 and l[n+3]==0 ) :#" FS 0 0 0 "   << specific pattern
#               #     l[n+2] = 13 # input CR
#               #     l[n+3] = 10 # input LF
#               #     l[n] = 0    # remove founded character
#                    #n=n+3       # jump to next possible 3 pattern
#
#        n+=1


    n=0
    for ch in range(len(l)):    # check each character in list
            if n<len(l)-2:        # keep length of the list (index overflow)
                    # Check after " AuxAxis: X? "  << specific pattern
                if (l[n]==65 and l[n+1]==117 and l[n+2]==120 and l[n+3]==65 and l[n+4]==120 and l[n+5]==105 and l[n+6]==115 and l[n+7]==58 and l[n+8]==32 and l[n+10]==x ) :
                    l[n+10] = 13 # input CR
                    l[n+11] = 10 # input LF
                    #n=n-1       # jump to next possible 3 pattern
                if l[n]==69 and l[n+1]==78 and l[n+2]==68 and l[n+3]==0:# END CRLF
                    l[n+3] = 13 # input CR
                    l[n+4] = 10 # input LF
            n=n+1

    n=0
    for ch in range(len(l)*3):
        if n<len(l):
            if l[n]==0: #remove zeros
                l.pop(n)
                n=n-3
        n=n+1

    n=0
    for ch in range(len(l)):    # check each character in list
        if n<len(l)-3:
            if (l[n]==13 and l[n+1]==10 and l[n+2]==13 and l[n+3]==10 ) :# CRLF CRLF   << specific pattern
              #  l[n+1] = 0 # input CR
              #  l[n] = 0    # remove founded character
                l.pop(n+1)
                l.pop(n)
        n=n+1

    l=(''.join(str(chr(e)) for e in l))
    w = open('/home/tom/Projects/proface/robotFiles/'+directory+'/'+d1+'/'+jobNo+'.JOB','w')
    w.write(l)
    w.close()

def jobDownload(jobNo):

    #jobNo = '0600'
#
    
#                   /home/tom/Projects/proface/robotFiles/mainQl02/20200303
    logfile = open('/home/tom/Projects/proface/robotFiles/'+directory+'/'+d1+'/job'+jobNo+'_'+d1+'.txt', 'wb')
    nc = nclib.Netcat(('10.210.202.'+IP+'', 700), udp=True, verbose=0, log_recv=logfile)
    nc.settimeout(0.3)

    #vzor prikazu na poslanie JOBu
    comm = (b'HF\x01\x00 \x00\x00\x00l\x05\x00\x00H \x0c\x00\x14\x00\x00\x01\x00\x10\x01\x07\x08\x00\x00\x000001.JOB\x00\x00\x00\x00ff\x00\x00\x00')
    #print(comm)

    #konverzia na list aby bolo mozne upravit obsah prikazu
    l = list(comm)
    #print(l)

    # n - pozicia kde v prikaze sa nachadza indentifikator JOB suboru
    n=28

    #prepisanie prikazu konverziou jednotilvych znakov z pozadovaneho jobNo
    for ch in jobNo:
     l.pop(n)
     l.insert(n,ord(ch))
     n=n+1

    #print(l)

    #vytvor novy prikaz
    commNew = bytes(l)
    #print(commNew)

    nc.send(commNew)

    rob = nc.recvuntil(str.encode('  END'))
    # IMPORATANT !!!! have to wait for file close !!
    logfile.close()

    #kontrola velkosti suboru - ak je mensi (JOB neexistuje)
    stat = os.stat('/home/tom/Projects/proface/robotFiles/'+directory+'/'+d1+'/job'+jobNo+'_'+d1+'.txt')
    #print(stat.st_size)
    if stat.st_size <= 28:
        os.remove('/home/tom/Projects/proface/robotFiles/'+directory+'/'+d1+'/job'+jobNo+'_'+d1+'.txt')
    else:
        formating(jobNo) # start formatin UDP stream
        # remove original file
        # !!!!!!!!!!!!!!!!!!!!!!!!!!    DEBUGING   !!!!!!!!!!!!!!!!!!!!!!
        # Coment next line
        os.remove('/home/tom/Projects/proface/robotFiles/'+directory+'/'+d1+'/job'+jobNo+'_'+d1+'.txt')

print("Robot: ",directory)
if sys.argv[4:]:
    x=sys.argv[4]
    x=(str(x).zfill(4))
    jobDownload(x)
    sys.exit()

for x in range(100):
    #konverzia int na str so 0000 miestami
    x=(str(x).zfill(4))
    jobDownload(x)

for x in range(100,1000,100):
    for y in range(30):
        z=x+y
        #konverzia int na str so 0000 miestami
        z=(str(z).zfill(4))
        jobDownload(z)

for x in range(1000,10000,1000):
    for y in range(100,1000,100):
        for z in range(11):
            v=x+y+z
            #konverzia int na str so 0000 miestami
            v=(str(v).zfill(4))
            jobDownload(v)

for x in range(9900,10000):
    #konverzia int na str so 0000 miestami
    x=(str(x).zfill(4))
    jobDownload(x)

