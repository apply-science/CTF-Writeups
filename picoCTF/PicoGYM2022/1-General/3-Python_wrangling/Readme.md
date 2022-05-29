### *Python wrangling*
1. Download all three files in the description 
```
wget https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/ende.py
wget https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/pw.txt
wget https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/flag.txt.en
```
2. Open and investigate ende.py or the lazy (insecure) way run it
3. This tells you that ende.py wants a operator and a file
4. Print the password
> cat pw.txt
5. Run ende.py on the encoded file
> python ende.py -d flag.en.txt
6. Copy and paste password from pw.txt and see the decoded flag
