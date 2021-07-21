H=20
M=23
while 0<=H<=23 and 0<=M<=59:
    if M>=45:
        H=H, M=M-45
        print(H,M)
    else:
        if H>=1:
            H-=1,M+=15
            print(H,M)
        else:
            H=23,M+=15
            print(H,M)