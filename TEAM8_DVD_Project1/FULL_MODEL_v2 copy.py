#Model to calculate leakage current

#Codes for understanding
rounding_digits = 2
temp = 0      
valim = 1    
vd = 2
vg = 3
vs = 4
vb = 5
Id = 6
Ig = 7
Is = 8
Ib = 9        

def read_text(path):
    arr = [[item for item in line.split()] for line in open(path)]
    return [list(map(float, i)) for i in arr]

def wToi(w):
    
    if(w==1):
        i=0
    elif(w==2):
        i=1
    elif(w==3):
        i=2
    elif(w==4):
        i=3
    elif(w==6):
        i=4
    elif(w==8):
        i=5
    return i


def IsubN(v, w):
    vr = v
    vr = round(vr, rounding_digits)
    vr = abs(vr)
    rowNo = vr/0.01 - 1
    rowNo = round(rowNo)
    rowNo = int(rowNo)

    if(v == 0):
        return 0

    if(w == 1):
        return NMOS_OFF_1u[rowNo][Id]
    elif(w == 2):
        return NMOS_OFF_2u[rowNo][Id]
    elif(w == 3):
        return NMOS_OFF_3u[rowNo][Id]
    elif(w == 4):
        return NMOS_OFF_4u[rowNo][Id]
    elif(w == 6):
        return NMOS_OFF_6u[rowNo][Id]
    elif(w == 8):
        return NMOS_OFF_8u[rowNo][Id]

def IsubP(v, w):
    vr = v
    vr = round(vr, rounding_digits)
    vr = abs(vr)
    rowNo = vr/0.01 - 1
    rowNo = round(rowNo)
    rowNo = int(rowNo)

    if(v == 0):
        return 0

    if(w == 1):
        return PMOS_OFF_1u[rowNo][Id]
    elif(w == 2):
        return PMOS_OFF_2u[rowNo][Id]
    elif(w == 3):
        return PMOS_OFF_3u[rowNo][Id]
    elif(w == 4):
        return PMOS_OFF_4u[rowNo][Id]
    elif(w == 6):
        return PMOS_OFF_6u[rowNo][Id]
    elif(w == 8):
        return PMOS_OFF_8u[rowNo][Id]


def IbodyVDSB(v, w):

    vr = v
    vr = round(vr, rounding_digits)
    vr = abs(vr)
    rowNo = vr/0.01 - 1
    rowNo = round(rowNo)
    rowNo = int(rowNo)

    if(v > 0):
        if(w == 1):
            return NMOS_OFF_1u[rowNo][Ib] 
        elif(w == 2):
            return NMOS_OFF_2u[rowNo][Ib]
        elif(w == 3):
            return NMOS_OFF_3u[rowNo][Ib]
        elif(w == 4):
            return NMOS_OFF_4u[rowNo][Ib]
        elif(w == 6):
            return NMOS_OFF_6u[rowNo][Ib]
        elif(w == 8):
            return NMOS_OFF_8u[rowNo][Ib]

    elif(v<0):
        if(w == 1):
            return PMOS_OFF_1u[rowNo][Ib] 
        elif(w == 2):
            return PMOS_OFF_2u[rowNo][Ib]
        elif(w == 3):
            return PMOS_OFF_3u[rowNo][Ib]
        elif(w == 4):
            return PMOS_OFF_4u[rowNo][Ib]
        elif(w == 6):
            return PMOS_OFF_6u[rowNo][Ib]
        elif(w == 8):
            return PMOS_OFF_8u[rowNo][Ib]

    else:
        return 0

def IbodyVGB(v, w):

    vr = v
    vr = round(vr, rounding_digits)
    vr = abs(vr)
    rowNo = vr/0.01 - 1
    rowNo = round(rowNo)
    rowNo = int(rowNo)

    if(v > 0):
        if(w == 1):
            return NMOS_ON_1u[rowNo][Ib] 
        elif(w == 2):
            return NMOS_ON_2u[rowNo][Ib]
        elif(w == 3):
            return NMOS_ON_3u[rowNo][Ib]
        elif(w == 4):
            return NMOS_ON_4u[rowNo][Ib]
        elif(w == 6):
            return NMOS_ON_6u[rowNo][Ib]
        elif(w == 8):
            return NMOS_ON_8u[rowNo][Ib]

    elif(v<0):
        if(w == 1):
            return PMOS_ON_1u[rowNo][Ib] 
        elif(w == 2):
            return PMOS_ON_2u[rowNo][Ib]
        elif(w == 3):
            return PMOS_ON_3u[rowNo][Ib]
        elif(w == 4):
            return PMOS_ON_4u[rowNo][Ib]
        elif(w == 6):
            return PMOS_ON_6u[rowNo][Ib]
        elif(w == 8):
            return PMOS_ON_8u[rowNo][Ib]

    else:
        return 0

def IgateN(v, w):

    vr = v
    vr = round(vr, rounding_digits)
    vr = abs(vr)
    rowNo = vr/0.01 - 1
    rowNo = round(rowNo)
    rowNo = int(rowNo)

    if(v > 0):
        if(w == 1):
            return NMOS_OFF_1u[rowNo][Ig] 
        elif(w == 2):
            return NMOS_OFF_2u[rowNo][Ig]
        elif(w == 3):
            return NMOS_OFF_3u[rowNo][Ig]
        elif(w == 4):
            return NMOS_OFF_4u[rowNo][Ig]
        elif(w == 6):
            return NMOS_OFF_6u[rowNo][Ig]
        elif(w == 8):
            return NMOS_OFF_8u[rowNo][Ig]

    elif(v < 0):
        if(w == 1):
            return NMOS_ON_1u[rowNo][Id] 
        elif(w == 2):
            return NMOS_ON_2u[rowNo][Id]
        elif(w == 3):
            return NMOS_ON_3u[rowNo][Id]
        elif(w == 4):
            return NMOS_ON_4u[rowNo][Id]
        elif(w == 6):
            return NMOS_ON_6u[rowNo][Id]
        elif(w == 8):
            return NMOS_ON_8u[rowNo][Id]

    else:
        return 0

def IgateP(v, w):

    vr = v
    vr = round(vr, rounding_digits)
    vr = abs(vr)
    rowNo = vr/0.01 - 1
    rowNo = round(rowNo)
    rowNo = int(rowNo)

    if(v>0):
        if(w == 1):
            return PMOS_ON_1u[rowNo][Id] 
        elif(w == 2):
            return PMOS_ON_2u[rowNo][Id]
        elif(w == 3):
            return PMOS_ON_3u[rowNo][Id]
        elif(w == 4):
            return PMOS_ON_4u[rowNo][Id]
        elif(w == 6):
            return PMOS_ON_6u[rowNo][Id]
        elif(w == 8):
            return PMOS_ON_8u[rowNo][Id]

    elif(v<0):
        if(w == 1):
            return PMOS_OFF_1u[rowNo][Ig] 
        elif(w == 2):
            return PMOS_OFF_2u[rowNo][Ig]
        elif(w == 3):
            return PMOS_OFF_3u[rowNo][Ig]
        elif(w == 4):
            return PMOS_OFF_4u[rowNo][Ig]
        elif(w == 6):
            return PMOS_OFF_6u[rowNo][Ig]
        elif(w == 8):
            return PMOS_OFF_8u[rowNo][Ig]

    else:
        return 0
    

NMOS_OFF_1u = read_text(r'Part-1 files/NMOS_OFF_1u.txt')
NMOS_OFF_2u = read_text(r'Part-1 files/NMOS_OFF_2u.txt')
NMOS_OFF_3u = read_text(r'Part-1 files/NMOS_OFF_3u.txt')
NMOS_OFF_4u = read_text(r'Part-1 files/NMOS_OFF_4u.txt')
NMOS_OFF_6u = read_text(r'Part-1 files/NMOS_OFF_6u.txt')
NMOS_OFF_8u = read_text(r'Part-1 files/NMOS_OFF_8u.txt')

NMOS_ON_1u = read_text(r'Part-1 files/NMOS_ON_1u.txt')
NMOS_ON_2u = read_text(r'Part-1 files/NMOS_ON_2u.txt')
NMOS_ON_3u = read_text(r'Part-1 files/NMOS_ON_3u.txt')
NMOS_ON_4u = read_text(r'Part-1 files/NMOS_ON_4u.txt')
NMOS_ON_6u = read_text(r'Part-1 files/NMOS_ON_6u.txt')
NMOS_ON_8u = read_text(r'Part-1 files/NMOS_ON_8u.txt')

PMOS_OFF_1u = read_text(r'Part-1 files/PMOS_OFF_1u.txt')
PMOS_OFF_2u = read_text(r'Part-1 files/PMOS_OFF_2u.txt')
PMOS_OFF_3u = read_text(r'Part-1 files/PMOS_OFF_3u.txt')
PMOS_OFF_4u = read_text(r'Part-1 files/PMOS_OFF_4u.txt')
PMOS_OFF_6u = read_text(r'Part-1 files/PMOS_OFF_6u.txt')
PMOS_OFF_8u = read_text(r'Part-1 files/PMOS_OFF_8u.txt')

PMOS_ON_1u = read_text(r'Part-1 files/PMOS_ON_1u.txt')
PMOS_ON_2u = read_text(r'Part-1 files/PMOS_ON_2u.txt')
PMOS_ON_3u = read_text(r'Part-1 files/PMOS_ON_3u.txt')
PMOS_ON_4u = read_text(r'Part-1 files/PMOS_ON_4u.txt')
PMOS_ON_6u = read_text(r'Part-1 files/PMOS_ON_6u.txt')
PMOS_ON_8u = read_text(r'Part-1 files/PMOS_ON_8u.txt')


input_data = 2
width = 2 #in µm
Vdd = 1.2

########## AND GATE VOLTAGE ################
      #[1µm, 2µm, 3µm, 4µm, 6µm, 8µm]
Va00 = [0.0863, 0.0864, 0.0864, 0.08641, 0.086426, 0.086449]
Va01 = [0.0001740, 0.0001219, 0.0001220, 0.0001221, 0.0001221, 0.0001222]
Va10 = [1.002459, 1.002459, 1.002458, 1.002456, 1.002452, 1.002445]
Va11 = [0.0005923, 0.0005940, 0.0005945, 0.0005947, 0.0005950, 0.0005950]


########## XOR GATE VOLTAGE ################
       #[1µm, 2µm, 3µm, 4µm, 6µm, 8µm]
Va00x = [0.1403495, 0.1407, 0.1408, 0.1408, 0.1408, 0.1408]
Va01x = [1.00217, 1.00217, 1.00217, 1.00217, 1.00217, 1.00217]
Va10x = [0.0001215, 0.0001218, 0.0001219, 0.0001219, 0.0001219, 0.0001219]
Va11x = [0.0004064, 0.0004075, 0.0004079, 0.0004079, 0.0004079, 0.0004079]
Vb00x = [0.6927653, 0.6929, 0.6929, 0.6929, 0.6929, 0.6929]
Vb01x = [1.198743, 1.198743, 1.199214, 1.199214, 1.199214, 1.199214]
Vb10x = [1.198215, 1.1989, 1.1989, 1.1989, 1.1989, 1.1989]
Vb11x = [1.199374, 1.199374, 1.199374, 1.199374, 1.199374, 1.199374]

def AND(inputA, inputB, width, Vdd):
    total_leakage_power = 0
    if((inputA==0) and (inputB==0)):
        total_leakage_power += abs(IsubN(Va00[wToi(width)], width)) + abs(IsubP(-Vdd, width))
        total_leakage_power += 2*abs(IbodyVDSB(Va00[wToi(width)], width)) + abs(IbodyVDSB(Vdd, width)) + 2*abs(IbodyVGB(-Vdd, width)) + abs(IbodyVGB(Vdd, width)) + abs(IbodyVDSB(-Vdd, width))
        total_leakage_power += 4*abs(IgateP(Vdd, width)) + 2*abs(IgateN(Va00[wToi(width)], width)) + abs(IgateN(Vdd, width)) + 2*abs(IgateN(-Vdd, width)) + abs(IgateP(-Vdd, width)) 
    elif((inputA==0) and (inputB==1)):
        total_leakage_power += IsubN(Va01[wToi(width)], width) + IsubP(-Vdd, width)
        total_leakage_power += 2*abs(IbodyVDSB(Va01[wToi(width)], width)) + abs(IbodyVDSB(Vdd, width)) + abs(IbodyVGB(-Vdd, width)) + abs(IbodyVGB(Vdd, width)) + abs(IbodyVDSB(Vdd, width))
        total_leakage_power += 2*abs(IgateP(Vdd, width)) + abs(IgateN(Va01[wToi(width)], width)) + 2*abs(IgateN(-Vdd, width)) + abs(IgateP(-Vdd, width))
    elif((inputA==1) and (inputB==0)):
        total_leakage_power += IsubN(Vdd - Va10[wToi(width)], width) + IsubP(-Vdd, width)
        total_leakage_power += 2*abs(IbodyVDSB(Va10[wToi(width)], width)) + abs(IbodyVDSB(Vdd, width)) + abs(IbodyVGB(Vdd, width)) + abs(IbodyVGB(-Vdd, width)) + abs(IbodyVGB(Vdd, width)) + abs(IbodyVDSB(-Vdd, width))
        total_leakage_power += 2*abs(IgateP(Vdd, width)) + abs(IgateN(Vdd, width)) + abs(IgateN(Va10[wToi(width)], width)) + 2*abs(IgateN(-Vdd, width)) + 2*abs(IgateN(-Vdd, width)) + abs(IgateP(-Vdd, width))
    else:
        total_leakage_power += 2*IsubP(-Vdd, width) + IsubN(Vdd, width)
        total_leakage_power += 2*abs(IbodyVGB(Vdd, width)) + 2*abs(IbodyVDSB(-Vdd, width)) + abs(IbodyVDSB(Vdd, width)) + abs(IbodyVGB(Vdd, width))
        total_leakage_power += 2*abs(IgateP(-Vdd, width)) + 4*abs(IgateN(-Vdd, width)) + 2*abs(IgateP(Vdd, width)) + abs(IgateN(Vdd, width))

    return total_leakage_power


def XOR(inputA, inputB, width, Vdd):
    total_leakage_power = 0
    if((inputA==0) and (inputB==0)):
        total_leakage_power += 2*abs(IsubP(Vb00x[wToi(width)] - Vdd, width))
        total_leakage_power += 2*abs(IbodyVGB(Vdd, width)) + 2*abs(IbodyVDSB(-Vdd, width)) + 4*abs(IbodyVDSB(Vb00x[wToi(width)] - Vdd, width)) + 2*abs(IbodyVGB(-Vdd, width))
        total_leakage_power += 4*abs(IgateN(-Vdd, width)) + 2*abs(IgateP(Vb00x[wToi(width)], width)) + 2*abs(IgateP(Vb00x[wToi(width)] - Vdd, width))
    elif((inputA==0) and (inputB==1)):
        total_leakage_power += 2*abs(IsubN(Va01x[wToi(width)], width))
        total_leakage_power += 4*abs(IbodyVDSB(Va01x[wToi(width)], width)) + 2*abs(IbodyVDSB(Vdd, width)) + 2*abs(IbodyVGB(Vdd - Va01x[wToi(width)], width)) + 2*abs(IbodyVGB(-Vdd, width))
        total_leakage_power += 2*abs(IgateN(Va01x[wToi(width)], width)) + 2*abs(IgateN(Va01x[wToi(width)] - Vdd, width)) + 6*abs(IgateP(Vdd, width))
    elif((inputA==1) and (inputB==0)):
        total_leakage_power += 2*abs(IsubN(Vdd - Va10x[wToi(width)], width))
        total_leakage_power += 4*abs(IbodyVDSB(Va10x[wToi(width)], width)) + 2*abs(IbodyVDSB(Vdd, width)) + 2*abs(IbodyVGB(Vdd, width)) + 2*abs(IbodyVGB(-Vdd, width))
        total_leakage_power += 2*abs(IgateN(-Vdd, width)) + 2*abs(IgateN(Va10x[wToi(width)] - Vdd, width)) + 2*abs(IgateN(Va10x[wToi(width)], width)) + 2*abs(IgateN(Vdd, width)) + 4*abs(IgateP(Vdd, width))
    else:
        total_leakage_power += 2*abs(IsubP(-Vb11x[wToi(width)], width))
        total_leakage_power += 2*abs(IbodyVDSB(-Vdd, width)) + 4*abs(IbodyVDSB(Vb11x[wToi(width)] - Vdd, width)) + 2*abs(IbodyVGB(Vdd, width)) + 2*abs(IbodyVGB(-Vdd, width))
        total_leakage_power += 4*abs(IgateN(-Vdd, width)) + 2*abs(IgateP(-Vdd, width)) + 2*abs(IgateP(Vb11x[wToi(width)]-Vdd, width)) + 2*abs(IgateP(Vdd, width))
    
    return total_leakage_power

def MULTIPLIER(inputA1, inputA0, inputB1, inputB0, width, Vdd):

    S0 = inputA0 & inputB0
    I1 = inputA1 & inputB0
    I2 = inputA0 & inputB1
    I3 = inputA1 & inputB1
    C0 = I1 & I2
    S1 = I1 ^ I2
    S2 = C0 ^ I3
    S3 = C0 & I3

    print("The inputs of Multiplier are in order as follows A1, A0, B1, B0:       ", inputA1, inputA0, inputB1, inputB0)
    print("The outputs of Multiplier are in order as follows S3, S2, S1, S0:      ", S3, S2, S1, S0)

    leakage_current = 0
    leakage_current +=  AND(inputA0, inputB0, width, Vdd) #X1-AND GATE
    leakage_current +=  AND(inputA0, inputB1 , width, Vdd) #X2-AND GATE
    leakage_current +=  AND(inputA1, inputB0 , width, Vdd) #X3-AND GATE
    leakage_current +=  AND(inputA1, inputB1, width, Vdd) #X4-AND GATE
    leakage_current +=  AND(I1, I2, width, Vdd) #X6-AND GATE
    leakage_current +=  AND(C0, inputA1&inputB1, width, Vdd) #X7-AND GATE

    leakage_current +=  XOR(I1, I2, width, Vdd) #X5-XOR GATE
    leakage_current +=  XOR(C0, inputA1&inputB1, width, Vdd) #X8-XOR GATE

    return leakage_current

#rint(AND(0, 1, 3, 1.2))
#print(XOR(input_data, width, Vdd))

TOTAL_LEAKAGE_CURRENT = MULTIPLIER(0, 1, 0, 1, 6, 1.2)

print("Total Leakage current in the circuit =", round(TOTAL_LEAKAGE_CURRENT*1000000, 4), "µA") #A1, A0, B1, B0, width, Vdd

