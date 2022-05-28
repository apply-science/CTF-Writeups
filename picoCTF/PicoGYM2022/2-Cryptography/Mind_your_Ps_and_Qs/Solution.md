### *Mind your Ps and Qs*
The trick here is reading the description. Basically it states something is to small. Of all things involved in RSA that needs to be large in order to be secure I thought that the prime number N has to be to small, that results in smaller primes and theoretically a weak encryption.
1. Download the supplied file
> wget https://mercury.picoctf.net/static/3cfeb09681369c26e3f19d886bc1e5d9/values
  
> c: 8533139361076999596208540806559574687666062896040360148742851107661304651861689

> n: 769457290801263793712740792519696786147248001937382943813345728685422050738403253

> e: 65537
2. True, n is endeed small. Let's try to factorize it with a tool like https://www.alpertron.com.ar/ECM.HTM
> P: 1617549722683965197900599011412144490161     Q: 475693130177488446807040098678772442581573
3. OK. This is something to work with. Let's pull out some python code and try to solve it
4. Win!
