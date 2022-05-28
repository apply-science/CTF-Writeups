### *Nice Netcat*
1. Description provides a netcat session to be investigated
> nc mercury.picoctf.net 35652
2. This gives a long row of integers, some sort of encoding perhaps?
3. Not really, it's just integer representation of ASCII text. The clean way would be writing a python script to decode it. However, I got lazy and just used https://www.dcode.fr/ascii-code
4. Paste all numbers and press decode to get the flag

I plan to return to this and write a python integer to char decoder but thats for a later date...
