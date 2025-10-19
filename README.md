# This repo is for making Time Zone Converter.

My plan was like this: \
<img width="800" height="600" alt="Image" src="https://github.com/user-attachments/assets/d3f6f2bd-9cac-4f52-ab08-f415cd7bcb5d" />

And followings are what I got:\
<img width="180" height="150" alt="Image" src="https://github.com/user-attachments/assets/f9b891c3-87d9-4419-9550-4507c049c1c8" />
<img width="180" height="150" alt="Image" src="https://github.com/user-attachments/assets/2ca2e41f-73d1-4a4b-98b0-642dd0af6f9d" />


As you can see on the 'main.py' code, I used tkinter on Python.\
... is a very raw and simple tool for making GUI applications.\
\
Reason I chose this tool is this app would be that simple.


## Way to use
Just download py file and compile with any tools. Then you could see this tiny window.\
You would just put time you want to convert; ex: 17:30 \
and put GMT+? what time zone you are at, and what time zone he/she are in you're contacting with.\
Push CONVERT button and you get time.\

## Methodology
The title and putting convertin' time area are grouped with f1 Frame.\
And remainings except Converted Time area are grouped with f2 Frame.\
This is because I had problem with just using pack() method to make the coding simple,\
just wanting putting hour and minute Entry in a row had problem.\
So I used side='left' method to let them be in a row, and for not messing the whole grid by mixing pack(side=...)\
and pack(anchor=...), I used frame to separate them spatially.
