### *Wave a flag*
1. Download the file
> wget https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm
2. Find out that it is a linux ELF binary
> file warm
3. Safe way is not to run unknown code, lets have a look for text inside the binary
4. So just use strings
> strings warm | grep picoCTF

If you set the execution bit and run the binary with the -h operator it display the same text but why run unknown code when you dont have to?
