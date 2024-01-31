# TwitchChatPlays
Pulls chat messages from Twitch and simulates keyboard presses for games.


#### Uses Python ver 3.10.1

The only non built in python imports are ```requests``` and ```mouse```.

## How to use

Clone repository to local drive or download the exe [here](https://github.com/Gerald-Ju/TwitchChatPlays/releases).

To run the program, open a terminal in Administrator mode (because some games will override ignore inputs if not in Administrator mode)

Navigate to the path where you downloaded the files and run TwitchChatPlays.py

e.g.
```
C:\Users\Gerald\GenericFolder> python TwitchChatPlays.py
```

## Other steps needed

    1. OAUTH Token from Twitch is needed. 
    2. Log into your twitch account
    3. Go to https://twitchapps.com/tmi/ and copy your OAUTH Token.
    4. DO NOT SHARE THIS TOKEN WITH ANYONE, it is connected to your account
        Example Token: oauth:43rip6j6fgio8n5xly1oum1lph8ikw5
    5. Follow the prompts in the terminal
    6. Ctrl+C to exit

## Commands it recognises

Converts all chat input to lowercase for recognition

    - All Keys from A-Z: "w" for (w key), "a" for (a key) etc. 
    However only the standard "gaming" keys are currently coded in. 
    Other keys will need to be added in yourself.
    
        - Gaming keys that are coded in:
            - "w" for W key
            - "a" for A key
            - "s" for S key
            - "d" for D key
            - "e" for E key
            - "q" for Q key
            - "r" for R key
    
    - All Numbers from 0-9: "0" for (0 key) etc. 
    Numbers such as 10, 100, 1000 etc will be considered as "1".
    
    - Other keys that are coded in (these are not held down, only clicked): 
        - "space" for spacebar
        - "shift" for left-shift-key
        - "ctrl" for left-ctrl-key
        - "alt" for left-alt-key
        - "f1" for F1-Function-Key
    
    - Mouse Input (not held down, only clicked)
        - "m1" for Left Mouse Button
        - "m2" for Right Mouse Button
















