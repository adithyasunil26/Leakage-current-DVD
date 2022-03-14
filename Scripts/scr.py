
def packtomat(path):
  package = open(path, "r")
  package = package.read()
  package = package.split("\n")
  package = package[1:-1]
  for i in range(len(package)):
    k = package[i].split(" ")
    l=[]
    for j in k:
      if j.strip():
        l.append(j)
    package[i] = l
  return package

nmos_offW1 = packtomat("../Packages/nmos_off/nmos_offW1.txt")
pmos_offW1 = packtomat("../Packages/pmos_off/pmos_offW1.txt")
nmos_offW1 = nmos_offW1[0:-1]

AandBn = packtomat("../Stacks/n-type_stacks/AandBn.txt")


###########################################################################
# For A=0 and B=0

A = AandBn[0][1]
B = AandBn[0][2]
Vsd = AandBn[0][3]
Vsd = round(float(Vsd)/0.05)*0.05
Vsd = round(Vsd,2)
for j in range(len(nmos_offW1)):
  vd = float(nmos_offW1[j][1])
  if vd == Vsd:
    k = j
    break
Ivdn = abs(float(nmos_offW1[k][5]))
Isource = abs(float(pmos_offW1[20][7]))
Isub = Ivdn + Isp
Igate = 4*abs(float(pmos_offW1[20][6])) + 2*abs(float(nmos_offW1[k][6])) + 2*abs(float(nmos_offW1[20][6]))

print(A, B, Vsd, k, Ivdn, Isp, Isub, Ib)
###########################################################################










# if a==0 and b==0:
#   isub=


# when "00" => PrintLeakages(Isub(Wmin,2*NWmin,a00Vdd, temperature)+Isub(Wmin,2*NWmin,-Vdd, temperature), 
#                                    2.0*Ibody(Wmin,2*NWmin,+a00Vdd,0.0,temperature)+Ibody(Wmin,2*NWmin,Vdd,0.0,temperature)+2.0*Ibody(Wmin,2*NWmin,0.0,-Vdd,temperature)+Ibody(Wmin,NWmin,0.0,Vdd,temperature)+Ibody(Wmin,2*NWmin,-Vdd,0.0,temperature),
#                              4.0*Igate(1,Wmin,2*NWmin,Vdd,temperature)+2.0*Igate(0,Wmin,2*NWmin,a00Vdd,temperature)+Igate(0,Wmin,2*NWmin,Vdd,temperature)+2.0*Igate(0,Wmin,NWmin,-Vdd,temperature)+Igate(1,Wmin,2*NWmin,-Vdd,temperature));
#         when "01" => PrintLeakages(Isub(Wmin,2*NWmin,a01Vdd, temperature)+Isub(Wmin,2*NWmin,-Vdd, temperature), 
#                                    2.0*Ibody(Wmin,2*NWmin,+a01Vdd,0.0,temperature)+Ibody(Wmin,2*NWmin,Vdd,0.0,temperature)+Ibody(Wmin,2*NWmin,0.0,Vdd,temperature)+Ibody(Wmin,2*NWmin,0.0,-Vdd,temperature)+Ibody(Wmin,NWmin,0.0,Vdd,temperature)+Ibody(Wmin,2*NWmin,-Vdd,0.0,temperature),
#                              2.0*Igate(1,Wmin,2*NWmin,Vdd,temperature)+Igate(0,Wmin,2*NWmin,a01Vdd,temperature)+2.0*Igate(0,Wmin,NWmin,-Vdd,temperature)+Igate(1,Wmin,2*NWmin,-Vdd,temperature));
#         when "10" => PrintLeakages(Isub(Wmin,2*NWmin,Vdd-a10Vdd, temperature)+Isub(Wmin,2*NWmin,-Vdd, temperature),
#                                    2.0*Ibody(Wmin,2*NWmin,a10Vdd,0.0,temperature)+Ibody(Wmin,2*NWmin,Vdd,0.0,temperature)+Ibody(Wmin,2*NWmin,0.0,-Vdd,temperature)+Ibody(Wmin,2*NWmin,0.0,Vdd,temperature)+Ibody(Wmin,NWmin,0.0,Vdd,temperature)+Ibody(Wmin,2*NWmin,-Vdd,0.0,temperature),
#                              2.0*Igate(1,Wmin,2*NWmin,Vdd,temperature)+Igate(0,Wmin,2*NWmin,+Vdd,temperature)+Igate(0,Wmin,2*NWmin,a10Vdd,temperature)+2.0*Igate(0,Wmin,2*NWmin,-Vdd,temperature)+2.0*Igate(0,Wmin,NWmin,-Vdd,temperature)+Igate(1,Wmin,2*NWmin,-Vdd,temperature)); 
#         when "11" => PrintLeakages(2.0*Isub(Wmin,2*NWmin,-Vdd, temperature)+Isub(Wmin,NWmin,Vdd, temperature),
#                                    2.0*Ibody(Wmin,2*NWmin,-Vdd,0.0,temperature)+2.0*Ibody(Wmin,2*NWmin,0.0,Vdd,temperature)+Ibody(Wmin,NWmin,Vdd,0.0,temperature)+Ibody(Wmin,2*NWmin,0.0,-Vdd,temperature), 
#                                    2.0*Igate(1,Wmin,2*NWmin,-Vdd,temperature)+4.0*Igate(0,Wmin,2*NWmin,-Vdd,temperature)+2.0*Igate(1,Wmin,2*NWmin,+Vdd,temperature)+Igate(0,Wmin,NWmin,+Vdd,temperature));