# AutoVideoDeleter

Auto delete running VLC videos after specified time


## Installation

1. [Install Python](https://www.python.org/downloads/)
2. In the terminal type the following commands:
```
pip install send2trash
pip install tqdm
pip install psutil
```
3. Open the main.py with a text editor _(It can even be notepad)_
4. Add the full path to the video folder editing this line of code `videosMainPath = Path('YOUR PATH GOES HERE')` <br/>It's important that you make it __as specific as possible__ _(You probably don't want to accidentaly delete some videos from the "homework" folder)_


### Optional
- Change the times ***(all the times are in seconds)***
  - `refreshTime`: After the video started, it's the time interval it must wait, to check if the video is still playing 
  - `minTime`: Minimum running time to add a video to the delete list
  - `waitTime`: More like video length, the timelength of the videos you are watching 
- Add a .bat file on Windows ***(To open both the videomanager and this code)***
  1. Open a text editor
  2. Write the following code:
    ```
    @echo off
    start "" "VIDEO MANAGER .EXE FULL PATH HERE"
    python "THE PATH WERE YOU HAVE THIS CODE main.py" 
    ```
  3. Save it as launch.bat
  4. Create a Desktop Shortcut to this file
  5. If you want, change the [icon](https://youtu.be/CrCIS4RktUs)</br>
  Now both will open at the same time
 
 
 ## FAQ
 ### Why would I want to delete the videos after watching them?
 I mainly wrote this code to delete anime episodes after I watched them _(That explains the default times I choose)_
 Maybe you would like to delete a series episode, or a movie after you are done. I find it specially usefull for a binge session.
 ### Could I not choose which videos to delete instead of deleting them all?
 I plan to do this, probably soon
 ### The terminal sucks, do a GUI
 No
 ### Isn't your code pretty simple
 Yep
 ### Isn't there a way to add more videoplayers?
 I would like to, but I only use VLC. If you want me to add more, send me the name of the process of the videoplayer (The task manager thing).
 ### Can I take this code and completely change it?
 Yep
 ### Your code is shit. You could have done this and this instead
 Yeah, but I'm pretty new to programming, so I did what I could with what I know. But I would love to recieve your critics and ways to improve it. Helps me learn 
 ### What do you mean by videomanager?
 Dunno, I meant something like [Taiga](https://taiga.moe/). 
 ### Does this works on all OS?
 I think everything works except the .bat file. But I can't try it so I promise nothing
 ### But seriously, why no GUI?
 There are three reasons: 
 1. The code in itself is pretty simple, after the configuration, you just _got to click twice_. That's why I don't think it's worthy a GUI just for that.
 2. The python GUIs that I search looked ~~pretty ugly~~ not so pretty.
 3. I don't know how too.
 ### If nobody has downloaded this code, how are these FAQ?
 Shut up, I just wanted to  answer some question people might have. Feel free to ask more
 ### Do you love me?
 Maybe...
  
  
