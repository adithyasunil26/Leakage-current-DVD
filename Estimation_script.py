#Model to calculate leakage current

from tabulate import tabulate

rounddig = 2

######################Defining matrix indices##############################
valim = 1
vd = 2
vg = 3
vs = 4
vb = 5
Id = 6
Ig = 7
Is = 8
Ib = 9

############################################################################



######################Defining functions required #############################

def readtxt(path):
    arr = [[item for item in line.split()] for line in open(path)]
    return [list(map(float, i)) for i in arr]

def wi(w):
    i = {
        1: 0,
        2: 1,
        3: 2,
        4: 3,
        6: 4,
        8: 5
    }
    return i.get(w)


def Isn(v, w):

    rno = int(round(abs(round(v,  rounddig))/0.01 - 1))

    l = {
        0: 0,
        1: NMOS_OFF_1u[rno][Id],
        2: NMOS_OFF_2u[rno][Id],
        3: NMOS_OFF_3u[rno][Id],
        4: NMOS_OFF_4u[rno][Id],
        6: NMOS_OFF_6u[rno][Id],
        8: NMOS_OFF_8u[rno][Id]
    }
    return l.get(w)

def Isp(v, w):

    rno = int(round(abs(round(v,  rounddig))/0.01 - 1))

    l = {
        0: 0,
        1: PMOS_OFF_1u[rno][Id],
        2: PMOS_OFF_2u[rno][Id],
        3: PMOS_OFF_3u[rno][Id],
        4: PMOS_OFF_4u[rno][Id],
        6: PMOS_OFF_6u[rno][Id],
        8: PMOS_OFF_8u[rno][Id]
    }
    return l.get(w)


def Ign(v, w):

    rno = int(round(abs(round(v,  rounddig))/0.01 - 1))

    if(v > 0):
        l = {
            1: NMOS_OFF_1u[rno][Ig],
            2: NMOS_OFF_2u[rno][Ig],
            3: NMOS_OFF_3u[rno][Ig],
            4: NMOS_OFF_4u[rno][Ig],
            6: NMOS_OFF_6u[rno][Ig],
            8: NMOS_OFF_8u[rno][Ig]
        }
        return l.get(w)
    elif(v < 0):
        l = {
            1: NMOS_ON_1u[rno][Id],
            2: NMOS_ON_2u[rno][Id],
            3: NMOS_ON_3u[rno][Id],
            4: NMOS_ON_4u[rno][Id],
            6: NMOS_ON_6u[rno][Id],
            8: NMOS_ON_8u[rno][Id]
        }
        return l.get(w)
    else:
        return 0


def Igp(v, w):

    rno = int(round(abs(round(v,  rounddig))/0.01 - 1))

    if(v>0):
        l = {
            1: PMOS_ON_1u[rno][Id],
            2: PMOS_ON_2u[rno][Id],
            3: PMOS_ON_3u[rno][Id],
            4: PMOS_ON_4u[rno][Id],
            6: PMOS_ON_6u[rno][Id],
            8: PMOS_ON_8u[rno][Id]
        }
        return l.get(w)
    elif(v<0):
        l = {
            1: PMOS_OFF_1u[rno][Ig],
            2: PMOS_OFF_2u[rno][Ig],
            3: PMOS_OFF_3u[rno][Ig],
            4: PMOS_OFF_4u[rno][Ig],
            6: PMOS_OFF_6u[rno][Ig],
            8: PMOS_OFF_8u[rno][Ig]
        }
        return l.get(w)
    else:
        return 0


def Ibvdsb(v, w):

    rno = int(round(abs(round(v,  rounddig))/0.01 - 1))

    if(v > 0):
        l = {
            1: NMOS_OFF_1u[rno][Ib],
            2: NMOS_OFF_2u[rno][Ib],
            3: NMOS_OFF_3u[rno][Ib],
            4: NMOS_OFF_4u[rno][Ib],
            6: NMOS_OFF_6u[rno][Ib],
            8: NMOS_OFF_8u[rno][Ib]
        }
        return l.get(w)
    elif(v<0):
        l = {
            1: PMOS_OFF_1u[rno][Ib],
            2: PMOS_OFF_2u[rno][Ib],
            3: PMOS_OFF_3u[rno][Ib],
            4: PMOS_OFF_4u[rno][Ib],
            6: PMOS_OFF_6u[rno][Ib],
            8: PMOS_OFF_8u[rno][Ib]
        }
        return l.get(w)
    else:
        return 0

def Ibvgb(v, w):

    rno = int(round(abs(round(v,  rounddig))/0.01 - 1))

    if(v > 0):
        l = {
            1: NMOS_ON_1u[rno][Ib],
            2: NMOS_ON_2u[rno][Ib],
            3: NMOS_ON_3u[rno][Ib],
            4: NMOS_ON_4u[rno][Ib],
            6: NMOS_ON_6u[rno][Ib],
            8: NMOS_ON_8u[rno][Ib]
        }
        return l.get(w)
    elif(v<0):
        l = {
            1: PMOS_ON_1u[rno][Ib],
            2: PMOS_ON_2u[rno][Ib],
            3: PMOS_ON_3u[rno][Ib],
            4: PMOS_ON_4u[rno][Ib],
            6: PMOS_ON_6u[rno][Ib],
            8: PMOS_ON_8u[rno][Ib]
        }
        return l.get(w)
    else:
        return 0


def AND(inputA, inputB, width, Vdd):
    total_leakage_power = 0

    if((inputA==0) and (inputB==0)):

        I_sub = abs(Isn(Va00[wi(width)], width)) + abs(Isp(-Vdd, width))
        
        I_body = 2*abs(Ibvdsb(Va00[wi(width)], width)) + abs(Ibvdsb(Vdd, width)) + 2*abs(Ibvgb(-Vdd, width)) + abs(Ibvgb(Vdd, width)) + abs(Ibvdsb(-Vdd, width))
        
        I_gate = 4*abs(Igp(Vdd, width)) + 2*abs(Ign(Va00[wi(width)], width)) + abs(Ign(Vdd, width)) + 2*abs(Ign(-Vdd, width)) + abs(Igp(-Vdd, width))
        
        total_leakage_power = I_sub + I_body + I_gate 
    
    elif((inputA==0) and (inputB==1)):
        
        I_sub = Isn(Va01[wi(width)], width) + Isp(-Vdd, width)
        
        I_body = 2*abs(Ibvdsb(Va01[wi(width)], width)) + abs(Ibvdsb(Vdd, width)) + abs(Ibvgb(-Vdd, width)) + abs(Ibvgb(Vdd, width)) + abs(Ibvdsb(Vdd, width))
        
        I_gate = 2*abs(Igp(Vdd, width)) + abs(Ign(Va01[wi(width)], width)) + 2*abs(Ign(-Vdd, width)) + abs(Igp(-Vdd, width))
        
        total_leakage_power = I_sub + I_body + I_gate

    elif((inputA==1) and (inputB==0)):
        
        I_sub = Isn(Vdd - Va10[wi(width)], width) + Isp(-Vdd, width)
        
        I_body = 2*abs(Ibvdsb(Va10[wi(width)], width)) + abs(Ibvdsb(Vdd, width)) + abs(Ibvgb(Vdd, width)) + abs(Ibvgb(-Vdd, width)) + abs(Ibvgb(Vdd, width)) + abs(Ibvdsb(-Vdd, width))
        
        I_gate = 2*abs(Igp(Vdd, width)) + abs(Ign(Vdd, width)) + abs(Ign(Va10[wi(width)], width)) + 2*abs(Ign(-Vdd, width)) + 2*abs(Ign(-Vdd, width)) + abs(Igp(-Vdd, width))
        
        total_leakage_power = I_sub + I_body + I_gate
    
    else:
        
        I_sub = 2*Isp(-Vdd, width) + Isn(Vdd, width)
        
        I_body = 2*abs(Ibvgb(Vdd, width)) + 2*abs(Ibvdsb(-Vdd, width)) + abs(Ibvdsb(Vdd, width)) + abs(Ibvgb(Vdd, width))
        
        I_gate = 2*abs(Igp(-Vdd, width)) + 4*abs(Ign(-Vdd, width)) + 2*abs(Igp(Vdd, width)) + abs(Ign(Vdd, width))
        
        total_leakage_power = I_sub + I_body + I_gate
    
    return total_leakage_power , I_sub  ,I_body , I_gate


def XOR(inputA, inputB, width, Vdd):
    total_leakage_power = 0

    if((inputA==0) and (inputB==0)):

        I_sub = 2*abs(Isp(Vb00x[wi(width)] - Vdd, width))
        
        I_body = 2*abs(Ibvgb(Vdd, width)) + 2*abs(Ibvdsb(-Vdd, width)) + 4*abs(Ibvdsb(Vb00x[wi(width)] - Vdd, width)) + 2*abs(Ibvgb(-Vdd, width))
        
        I_gate = 4*abs(Ign(-Vdd, width)) + 2*abs(Igp(Vb00x[wi(width)], width)) + 2*abs(Igp(Vb00x[wi(width)] - Vdd, width))
        
        total_leakage_power = I_sub + I_body + I_gate
    
    elif((inputA==0) and (inputB==1)):
        
        I_sub = 2*abs(Isn(Va01x[wi(width)], width))
        
        I_body = 4*abs(Ibvdsb(Va01x[wi(width)], width)) + 2*abs(Ibvdsb(Vdd, width)) + 2*abs(Ibvgb(Vdd - Va01x[wi(width)], width)) + 2*abs(Ibvgb(-Vdd, width))
        
        I_gate = 2*abs(Ign(Va01x[wi(width)], width)) + 2*abs(Ign(Va01x[wi(width)] - Vdd, width)) + 6*abs(Igp(Vdd, width))
        
        total_leakage_power = I_sub + I_body + I_gate

    elif((inputA==1) and (inputB==0)):

        I_sub = 2*abs(Isn(Vdd - Va10x[wi(width)], width))
        
        I_body = 4*abs(Ibvdsb(Va10x[wi(width)], width)) + 2*abs(Ibvdsb(Vdd, width)) + 2*abs(Ibvgb(Vdd, width)) + 2*abs(Ibvgb(-Vdd, width))
        
        I_gate = 2*abs(Ign(-Vdd, width)) + 2*abs(Ign(Va10x[wi(width)] - Vdd, width)) + 2*abs(Ign(Va10x[wi(width)], width)) + 2*abs(Ign(Vdd, width)) + 4*abs(Igp(Vdd, width))
        
        total_leakage_power = I_sub + I_body + I_gate

    else:
        
        I_sub = 2*abs(Isp(-Vb11x[wi(width)], width))
        
        I_body = 2*abs(Ibvdsb(-Vdd, width)) + 4*abs(Ibvdsb(Vb11x[wi(width)] - Vdd, width)) + 2*abs(Ibvgb(Vdd, width)) + 2*abs(Ibvgb(-Vdd, width))
        
        I_gate = 4*abs(Ign(-Vdd, width)) + 2*abs(Igp(-Vdd, width)) + 2*abs(Igp(Vb11x[wi(width)]-Vdd, width)) + 2*abs(Igp(Vdd, width))
        
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

    print("Inputs A1, A0, B1, B0:       ", inputA1, inputA0, inputB1, inputB0)
    print("Outputs S3, S2, S1, S0:      ", S3, S2, S1, S0)

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
    total_leak_k, I_sub_k, I_body_k, I_gate_k =  XOR(I1, I2, width, Vdd) #X5-XOR GATE

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
    total_leak_k, I_sub_k, I_body_k, I_gate_k =  XOR(C0, inputA1&inputB1, width, Vdd) #X8-XOR GATE
    
    I_sub += I_sub_k
    I_body += I_body_k
    I_gate += I_gate_k
    total_leak += total_leak_k

    return total_leak, I_sub, I_body, I_gate


#####################################################################################################


############################Importing data from text files##################

NMOS_OFF_1u = readtxt(r'Packages/txt/NMOS_OFF_1u.txt')
NMOS_OFF_2u = readtxt(r'Packages/txt/NMOS_OFF_2u.txt')
NMOS_OFF_3u = readtxt(r'Packages/txt/NMOS_OFF_3u.txt')
NMOS_OFF_4u = readtxt(r'Packages/txt/NMOS_OFF_4u.txt')
NMOS_OFF_6u = readtxt(r'Packages/txt/NMOS_OFF_6u.txt')
NMOS_OFF_8u = readtxt(r'Packages/txt/NMOS_OFF_8u.txt')

PMOS_OFF_1u = readtxt(r'Packages/txt/PMOS_OFF_1u.txt')
PMOS_OFF_2u = readtxt(r'Packages/txt/PMOS_OFF_2u.txt')
PMOS_OFF_3u = readtxt(r'Packages/txt/PMOS_OFF_3u.txt')
PMOS_OFF_4u = readtxt(r'Packages/txt/PMOS_OFF_4u.txt')
PMOS_OFF_6u = readtxt(r'Packages/txt/PMOS_OFF_6u.txt')
PMOS_OFF_8u = readtxt(r'Packages/txt/PMOS_OFF_8u.txt')

NMOS_ON_1u = readtxt(r'Packages/txt/NMOS_ON_1u.txt')
NMOS_ON_2u = readtxt(r'Packages/txt/NMOS_ON_2u.txt')
NMOS_ON_3u = readtxt(r'Packages/txt/NMOS_ON_3u.txt')
NMOS_ON_4u = readtxt(r'Packages/txt/NMOS_ON_4u.txt')
NMOS_ON_6u = readtxt(r'Packages/txt/NMOS_ON_6u.txt')
NMOS_ON_8u = readtxt(r'Packages/txt/NMOS_ON_8u.txt')

PMOS_ON_1u = readtxt(r'Packages/txt/PMOS_ON_1u.txt')
PMOS_ON_2u = readtxt(r'Packages/txt/PMOS_ON_2u.txt')
PMOS_ON_3u = readtxt(r'Packages/txt/PMOS_ON_3u.txt')
PMOS_ON_4u = readtxt(r'Packages/txt/PMOS_ON_4u.txt')
PMOS_ON_6u = readtxt(r'Packages/txt/PMOS_ON_6u.txt')
PMOS_ON_8u = readtxt(r'Packages/txt/PMOS_ON_8u.txt')


###############################################################################


########################### AND GATE VOLTAGE #################################
# [1µm, 2µm, 3µm, 4µm, 6µm, 8µm]

Va00 = [0.0863   , 0.0864   , 0.0864   , 0.08641  , 0.086426 , 0.086449 ]
Va01 = [0.0001216, 0.0001219, 0.0001220, 0.0001221, 0.0001221, 0.0001222]
Va10 = [1.002459 , 1.002459 , 1.002458 , 1.002456 , 1.002452 , 1.002445 ]
Va11 = [0.0005923, 0.0005940, 0.0005945, 0.0005947, 0.0005950, 0.0005950]

##############################################################################


########################## XOR GATE VOLTAGE ################################
# [1µm, 2µm, 3µm, 4µm, 6µm, 8µm]

Va00x = [0.1403495, 0.1407   , 0.1408   , 0.1408   , 0.1408   , 0.1408   ]
Va01x = [1.00217  , 1.00217  , 1.00217  , 1.00217  , 1.00217  , 1.00217  ]
Va10x = [0.0001215, 0.0001218, 0.0001219, 0.0001219, 0.0001219, 0.0001219]
Va11x = [0.0004064, 0.0004075, 0.0004079, 0.0004079, 0.0004079, 0.0004079]
Vb00x = [0.6927653, 0.6929   , 0.6929   , 0.6929   , 0.6929   , 0.6929   ]
Vb01x = [1.198743 , 1.198743 , 1.199214 , 1.199214 , 1.199214 , 1.199214 ]
Vb10x = [1.198215 , 1.1989   , 1.1989   , 1.1989   , 1.1989   , 1.1989   ]
Vb11x = [1.199374 , 1.199374 , 1.199374 , 1.199374 , 1.199374 , 1.199374 ]

#################################################################################

table = [['W','A0','A1','B0','B1','Leakage current','Subthreshold current','Body current','Gate current']]

for i in (1,2,3,4,6,8):
    for j in (0,1):
        for k in (0,1):
            for l in (0,1):
                for m in (0,1):
                    TOTAL_LEAKAGE_CURRENT , I_sub , I_body , I_gate = MULTIPLIER(j, k, l, m, i, 1.2)
                    print("Width = ", i, "µm")
                    print("Total leakage current = ", round(TOTAL_LEAKAGE_CURRENT*1000000, 4), "µA") #A1, A0, B1, B0, width, Vdd
                    print("Total subthreshold Leakage current = ", round(I_sub*1000000, 4), "µA") #A1, A0, B1, B0, width, Vdd
                    print("Total body Leakage current = ", round(I_body*1000000, 4), "µA") #A1, A0, B1, B0, width, Vdd
                    print("Total gate Leakage current = ", round(I_gate*1000000, 4), "µA") #A1, A0, B1, B0, width, Vdd
                    table.append([i, j, k, l, m, round(TOTAL_LEAKAGE_CURRENT*1000000, 4), round(I_sub*1000000, 4), round(I_body*1000000, 4), round(I_gate*1000000, 4)])


print(tabulate(table, headers='firstrow', tablefmt='grid'))                

