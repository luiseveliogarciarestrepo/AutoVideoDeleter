import psutil
from send2trash import send2trash
from pathlib import Path
import time
from tqdm import tqdm
import threading
import sys


#Edit to change Refresh time
videosMainPath = Path('YOUR PATH GOES HERE')
refreshTime = 60#Default 1 minute = 60s
minTime = 900   #Check if the video has been running for at least 15 min = 900s
waitTime = 1200 #Count 20 minutes = 1200s until File is added to delete list
tobeDeletedList = [] #List of videos to be deleted
videosNames = []


def runningVid():
    while True:
        videoPath=""
        global stopProgram
        if stopProgram:
            break
        sys.stdout.write('\rSearching for video...')
        sys.stdout.flush()
        for proc in psutil.process_iter(['pid', 'name', 'open_files']):
                 if(proc.info['name'] == 'vlc.exe'):
                    for file in proc.info['open_files']:
                        if(file.path.endswith('.mkv') or file.path.endswith('.mp4')):
                            videoPath = Path(file.path)
                            pid = proc.info['pid']
                            process = psutil.Process(pid)

        if(videoPath != ""):
            if(videosMainPath in videoPath.parents): #Check if the video is in the specified folder
                print(f"\nVideo: {videoPath.name}")
                for i in tqdm(range(waitTime)):
                    if ((i%refreshTime)==0):
                        if(not(process.is_running())):
                            break;
                    time.sleep(1)
                if(i>=minTime):
                    tobeDeletedList.append(videoPath)
                    while(process.is_running()):
                        time.sleep(1)
                else:
                    print(f"Video {videoPath.name} is not going to be deleted")

            else: #If a Video was not found, rest for 1 minute
                sys.stdout.write('\rNo Video Found        ')
                sys.stdout.flush()
                time.sleep(10)

        else: #If a Video was not found, rest for 1 minute
            sys.stdout.write('\rNo Video Found        ')
            sys.stdout.flush()
            time.sleep(10)



def deleteVid(videoList):
    for video in videoList:
        print(f"Deleted {video.name}")
        try:
            send2trash(str(video))
        except:
            pass


stopProgram = False                             #Create variable to see if stops the program
mainLoop = threading.Thread(target = runningVid)
print("\n\t\t\tScript is Starting\n\t\t\tIf you want to stop, press any key\n\n\n")
mainLoop.start()                                #Run the main program loop
input()
print("\n\n\t\t\tPlease wait until the loop stops\n\n\n")
stopProgram = True                                 #Stop the thread
mainLoop.join()                                 #Kill the thread

for video in tobeDeletedList:
    videosNames.append(video.name)
if(len(videosNames)>=1):
    print(f"The Videos to be deleted are\n{videosNames} ")

    sure = input("Are you sure you want to delete all the videos?\nY/N=  ")
    if(sure =="Y"):
        deleteVid(tobeDeletedList)
    else:
        print("No videos where deleted")
else:
    print("No videos in the list\n")
input("\nExit")
