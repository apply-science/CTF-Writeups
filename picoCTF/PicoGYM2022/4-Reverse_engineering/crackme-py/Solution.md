# *Crackme-py*

1. Download the file
> wget https://mercury.picoctf.net/static/f440bf2510a28914afae2947749f2db0/crackme.py
2. Open the file and have a look inside. There you see two functions, one decoding and one irrelevant. However the decoding function is never used. Modify the last row of the code as below.
```
# choose_greatest()
decode_secret(bezos_cc_secret)
```
4. Run the code and get the flag
