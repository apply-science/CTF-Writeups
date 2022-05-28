c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
PQ = [1617549722683965197900599011412144490161, 475693130177488446807040098678772442581573]
e = 65537
phi = 1

for z in PQ:
    phi = phi * (z - 1)
  
d = pow(e, -1, phi)
answer = pow(c, d, n)
print(bytes.fromhex(hex(answer)[2:]).decode('ascii'))
