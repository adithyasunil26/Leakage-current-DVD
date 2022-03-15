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
    i = {
        1: 0,
        2: 1,
        3: 2,
        4: 3,
        6: 4,
        8: 5
    }
    return i.get(w)


def IsubN(v, w):
    vr = v
    vr = round(vr, rounding_digits)
    vr = abs(vr)
    rowNo = vr/0.01 - 1
    rowNo = round(rowNo)
    rowNo = int(rowNo)

    l = {
        0: 0,
        1: NMOS_OFF_1u[rowNo][Id],
        2: NMOS_OFF_2u[rowNo][Id],
        3: NMOS_OFF_3u[rowNo][Id],
        4: NMOS_OFF_4u[rowNo][Id],
        6: NMOS_OFF_6u[rowNo][Id],
        8: NMOS_OFF_8u[rowNo][Id]
    }
    return l.get(w)

def IsubP(v, w):
    vr = v
    vr = round(vr, rounding_digits)
    vr = abs(vr)
    rowNo = vr/0.01 - 1
    rowNo = round(rowNo)
    rowNo = int(rowNo)

    l = {
        0: 0,
        1: PMOS_OFF_1u[rowNo][Id],
        2: PMOS_OFF_2u[rowNo][Id],
        3: PMOS_OFF_3u[rowNo][Id],
        4: PMOS_OFF_4u[rowNo][Id],
        6: PMOS_OFF_6u[rowNo][Id],
        8: PMOS_OFF_8u[rowNo][Id]
    }
    return l.get(w)


def IbodyVDSB(v, w):

    vr = v
    vr = round(vr, rounding_digits)
    vr = abs(vr)
    rowNo = vr/0.01 - 1
    rowNo = round(rowNo)
    rowNo = int(rowNo)

    if(v > 0):
        l = {
            1: NMOS_OFF_1u[rowNo][Ib],
            2: NMOS_OFF_2u[rowNo][Ib],
            3: NMOS_OFF_3u[rowNo][Ib],
            4: NMOS_OFF_4u[rowNo][Ib],
            6: NMOS_OFF_6u[rowNo][Ib],
            8: NMOS_OFF_8u[rowNo][Ib]
        }
        return l.get(w)
    elif(v<0):
        l = {
            1: PMOS_OFF_1u[rowNo][Ib],
            2: PMOS_OFF_2u[rowNo][Ib],
            3: PMOS_OFF_3u[rowNo][Ib],
            4: PMOS_OFF_4u[rowNo][Ib],
            6: PMOS_OFF_6u[rowNo][Ib],
            8: PMOS_OFF_8u[rowNo][Ib]
        }
        return l.get(w)
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
        l = {
            1: NMOS_ON_1u[rowNo][Ib],
            2: NMOS_ON_2u[rowNo][Ib],
            3: NMOS_ON_3u[rowNo][Ib],
            4: NMOS_ON_4u[rowNo][Ib],
            6: NMOS_ON_6u[rowNo][Ib],
            8: NMOS_ON_8u[rowNo][Ib]
        }
        return l.get(w)
    elif(v<0):
        l = {
            1: PMOS_ON_1u[rowNo][Ib],
            2: PMOS_ON_2u[rowNo][Ib],
            3: PMOS_ON_3u[rowNo][Ib],
            4: PMOS_ON_4u[rowNo][Ib],
            6: PMOS_ON_6u[rowNo][Ib],
            8: PMOS_ON_8u[rowNo][Ib]
        }
        return l.get(w)
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
        l = {
            1: NMOS_OFF_1u[rowNo][Ig],
            2: NMOS_OFF_2u[rowNo][Ig],
            3: NMOS_OFF_3u[rowNo][Ig],
            4: NMOS_OFF_4u[rowNo][Ig],
            6: NMOS_OFF_6u[rowNo][Ig],
            8: NMOS_OFF_8u[rowNo][Ig]
        }
        return l.get(w)
    elif(v < 0):
        l = {
            1: NMOS_ON_1u[rowNo][Id],
            2: NMOS_ON_2u[rowNo][Id],
            3: NMOS_ON_3u[rowNo][Id],
            4: NMOS_ON_4u[rowNo][Id],
            6: NMOS_ON_6u[rowNo][Id],
            8: NMOS_ON_8u[rowNo][Id]
        }
        return l.get(w)
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
        l = {
            1: PMOS_ON_1u[rowNo][Id],
            2: PMOS_ON_2u[rowNo][Id],
            3: PMOS_ON_3u[rowNo][Id],
            4: PMOS_ON_4u[rowNo][Id],
            6: PMOS_ON_6u[rowNo][Id],
            8: PMOS_ON_8u[rowNo][Id]
        }
        return l.get(w)
    elif(v<0):
        l = {
            1: PMOS_OFF_1u[rowNo][Ig],
            2: PMOS_OFF_2u[rowNo][Ig],
            3: PMOS_OFF_3u[rowNo][Ig],
            4: PMOS_OFF_4u[rowNo][Ig],
            6: PMOS_OFF_6u[rowNo][Ig],
            8: PMOS_OFF_8u[rowNo][Ig]
        }
        return l.get(w)
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
    I_sub = 0
    I_gate = 0
    I_body = 0
    if((inputA==0) and (inputB==0)):
        I_sub += abs(IsubN(Va00[wToi(width)], width)) + abs(IsubP(-Vdd, width))
        I_body += 2*abs(IbodyVDSB(Va00[wToi(width)], width)) + abs(IbodyVDSB(Vdd, width)) + 2*abs(IbodyVGB(-Vdd, width)) + abs(IbodyVGB(Vdd, width)) + abs(IbodyVDSB(-Vdd, width))
        I_gate += 4*abs(IgateP(Vdd, width)) + 2*abs(IgateN(Va00[wToi(width)], width)) + abs(IgateN(Vdd, width)) + 2*abs(IgateN(-Vdd, width)) + abs(IgateP(-Vdd, width))
        total_leakage_power = I_sub + I_body + I_gate 
    elif((inputA==0) and (inputB==1)):
        I_sub += IsubN(Va01[wToi(width)], width) + IsubP(-Vdd, width)
        I_body += 2*abs(IbodyVDSB(Va01[wToi(width)], width)) + abs(IbodyVDSB(Vdd, width)) + abs(IbodyVGB(-Vdd, width)) + abs(IbodyVGB(Vdd, width)) + abs(IbodyVDSB(Vdd, width))
        I_gate += 2*abs(IgateP(Vdd, width)) + abs(IgateN(Va01[wToi(width)], width)) + 2*abs(IgateN(-Vdd, width)) + abs(IgateP(-Vdd, width))
        total_leakage_power = I_sub + I_body + I_gate
    elif((inputA==1) and (inputB==0)):
        I_sub += IsubN(Vdd - Va10[wToi(width)], width) + IsubP(-Vdd, width)
        I_body += 2*abs(IbodyVDSB(Va10[wToi(width)], width)) + abs(IbodyVDSB(Vdd, width)) + abs(IbodyVGB(Vdd, width)) + abs(IbodyVGB(-Vdd, width)) + abs(IbodyVGB(Vdd, width)) + abs(IbodyVDSB(-Vdd, width))
        I_gate += 2*abs(IgateP(Vdd, width)) + abs(IgateN(Vdd, width)) + abs(IgateN(Va10[wToi(width)], width)) + 2*abs(IgateN(-Vdd, width)) + 2*abs(IgateN(-Vdd, width)) + abs(IgateP(-Vdd, width))
        total_leakage_power = I_sub + I_body + I_gate
    else:
        I_sub += 2*IsubP(-Vdd, width) + IsubN(Vdd, width)
        I_body += 2*abs(IbodyVGB(Vdd, width)) + 2*abs(IbodyVDSB(-Vdd, width)) + abs(IbodyVDSB(Vdd, width)) + abs(IbodyVGB(Vdd, width))
        I_gate += 2*abs(IgateP(-Vdd, width)) + 4*abs(IgateN(-Vdd, width)) + 2*abs(IgateP(Vdd, width)) + abs(IgateN(Vdd, width))
        total_leakage_power = I_sub + I_body + I_gate
    return total_leakage_power , I_sub  ,I_body , I_gate


def XOR(inputA, inputB, width, Vdd):
    total_leakage_power = 0
    I_sub = 0
    I_gate = 0
    I_body = 0
    if((inputA==0) and (inputB==0)):
        I_sub += 2*abs(IsubP(Vb00x[wToi(width)] - Vdd, width))
        I_body += 2*abs(IbodyVGB(Vdd, width)) + 2*abs(IbodyVDSB(-Vdd, width)) + 4*abs(IbodyVDSB(Vb00x[wToi(width)] - Vdd, width)) + 2*abs(IbodyVGB(-Vdd, width))
        I_gate += 4*abs(IgateN(-Vdd, width)) + 2*abs(IgateP(Vb00x[wToi(width)], width)) + 2*abs(IgateP(Vb00x[wToi(width)] - Vdd, width))
        total_leakage_power = I_sub + I_body + I_gate
    elif((inputA==0) and (inputB==1)):
        I_sub += 2*abs(IsubN(Va01x[wToi(width)], width))
        I_body += 4*abs(IbodyVDSB(Va01x[wToi(width)], width)) + 2*abs(IbodyVDSB(Vdd, width)) + 2*abs(IbodyVGB(Vdd - Va01x[wToi(width)], width)) + 2*abs(IbodyVGB(-Vdd, width))
        I_gate += 2*abs(IgateN(Va01x[wToi(width)], width)) + 2*abs(IgateN(Va01x[wToi(width)] - Vdd, width)) + 6*abs(IgateP(Vdd, width))
        total_leakage_power = I_sub + I_body + I_gate
    elif((inputA==1) and (inputB==0)):
        I_sub += 2*abs(IsubN(Vdd - Va10x[wToi(width)], width))
        I_body += 4*abs(IbodyVDSB(Va10x[wToi(width)], width)) + 2*abs(IbodyVDSB(Vdd, width)) + 2*abs(IbodyVGB(Vdd, width)) + 2*abs(IbodyVGB(-Vdd, width))
        I_gate += 2*abs(IgateN(-Vdd, width)) + 2*abs(IgateN(Va10x[wToi(width)] - Vdd, width)) + 2*abs(IgateN(Va10x[wToi(width)], width)) + 2*abs(IgateN(Vdd, width)) + 4*abs(IgateP(Vdd, width))
        total_leakage_power = I_sub + I_body + I_gate
    else:
        I_sub += 2*abs(IsubP(-Vb11x[wToi(width)], width))
        I_body += 2*abs(IbodyVDSB(-Vdd, width)) + 4*abs(IbodyVDSB(Vb11x[wToi(width)] - Vdd, width)) + 2*abs(IbodyVGB(Vdd, width)) + 2*abs(IbodyVGB(-Vdd, width))
        I_gate += 4*abs(IgateN(-Vdd, width)) + 2*abs(IgateP(-Vdd, width)) + 2*abs(IgateP(Vb11x[wToi(width)]-Vdd, width)) + 2*abs(IgateP(Vdd, width))
        total_leakage_power = I_sub + I_body + I_gate
    return total_leakage_power, I_sub, I_body, I_gate

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

    I_sub = 0
    I_body = 0
    I_gate = 0
    total_leak = 0
    total_leak_k, I_sub_k, I_body_k, I_gate_k =  AND(inputA0, inputB0, width, Vdd) #X1-AND GATE
    I_sub += I_sub_k
    I_body += I_body_k
    I_gate += I_gate_k
    total_leak += total_leak_k
    total_leak_k, I_sub_k, I_body_k, I_gate_k =  AND(inputA0, inputB1 , width, Vdd) #X2-AND GATE
    I_sub += I_sub_k
    I_body += I_body_k
    I_gate += I_gate_k
    total_leak += total_leak_k
    total_leak_k, I_sub_k, I_body_k, I_gate_k =  AND(inputA1, inputB0 , width, Vdd) #X3-AND GATE
    I_sub += I_sub_k
    I_body += I_body_k
    I_gate += I_gate_k
    total_leak += total_leak_k
    total_leak_k, I_sub_k, I_body_k, I_gate_k =  AND(inputA1, inputB1, width, Vdd) #X4-AND GATE
    I_sub += I_sub_k
    I_body += I_body_k
    I_gate += I_gate_k
    total_leak += total_leak_k
    total_leak_k, I_sub_k, I_body_k, I_gate_k =  AND(I1, I2, width, Vdd) #X6-AND GATE
    I_sub += I_sub_k
    I_body += I_body_k
    I_gate += I_gate_k
    total_leak += total_leak_k
    total_leak_k, I_sub_k, I_body_k, I_gate_k =  AND(C0, inputA1&inputB1, width, Vdd) #X7-AND GATE
    I_sub += I_sub_k
    I_body += I_body_k
    I_gate += I_gate_k
    total_leak += total_leak_k
    total_leak_k, I_sub_k, I_body_k, I_gate_k =  XOR(I1, I2, width, Vdd) #X5-XOR GATE
    I_sub += I_sub_k
    I_body += I_body_k
    I_gate += I_gate_k
    total_leak += total_leak_k
    total_leak_k, I_sub_k, I_body_k, I_gate_k =  XOR(C0, inputA1&inputB1, width, Vdd) #X8-XOR GATE
    I_sub += I_sub_k
    I_body += I_body_k
    I_gate += I_gate_k
    total_leak += total_leak_k

    return total_leak, I_sub, I_body, I_gate

#rint(AND(0, 1, 3, 1.2))
#print(XOR(input_data, width, Vdd))

TOTAL_LEAKAGE_CURRENT , I_sub , I_body , I_gate = MULTIPLIER(0, 1, 0, 1, 6, 1.2)

print("Total Leakage current in the circuit =", round(TOTAL_LEAKAGE_CURRENT*1000000, 4), "µA") #A1, A0, B1, B0, width, Vdd
print("Total subthreshold Leakage current in the circuit =", round(I_sub*1000000, 4), "µA") #A1, A0, B1, B0, width, Vdd
print("Total body Leakage current in the circuit =", round(I_body*1000000, 4), "µA") #A1, A0, B1, B0, width, Vdd
print("Total gate Leakage current in the circuit =", round(I_gate*1000000, 4), "µA") #A1, A0, B1, B0, width, Vdd
