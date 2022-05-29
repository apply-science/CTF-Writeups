Matryoshka Doll

1. Download the challenge file
2. The trick here is realizing it is things within things.
3. Use binwalk to verify that the image does contain more data than just an image
> binwalk dolls.jpg
4. Use binwalk to extract and do so recursively (automatically run binwalk on extracted data). The tool calls this matryoshka.
> binwalk -e -M dolls.jpg
5. Follow the directory strycture down untl you reach the flag.txt file.
