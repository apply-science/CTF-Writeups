### *Information*
1. Download the image
> wget https://mercury.picoctf.net/static/a614a27d4cb251d04c7d2f3f3f76a965/cat.jpg
2. Look at the metadata
> exiftool cat.jpg
3. That is a wierd looking license text right? Copy that string to a file
> echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" > encoded.txt
4. It's base64 encoded, decode it
> base64 -d encoded.txt

Another way is using a tool like Cyberchef in order to find the type of encoding and decode it. Browse to https://gchq.github.io/CyberChef/ and add a Magic recepie. Copy encoded text above into the tool and let it identify end run the appropriate decoder.
