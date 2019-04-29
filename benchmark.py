from threading import Thread
import urllib.request
import math
import time
import random
from statistics import mean

# Global variables
timeArray = []
reqFreq = 2  # request frequency
trials = 100


class Job(Thread):

    global timeArray

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print("Thread '" + self.name + "' started")
        startDownload = time.time() * 1000.0
        contents = urllib.request.urlopen("http://repubblica.it").read()
        stopDownload = time.time() * 1000.0
        delay=stopDownload-startDownload
        timeArray.append(delay)
        print("Thread '" + self.name + "' terminated "+"duration :"+str(delay)+"(ms)")


# Main

if __name__ == "__main__":


    for i in range(1, trials+1):
        thread = Job("Thread "+str(i))
        thread.start()
        intertime = -(1.0/reqFreq) * math.log(1-random.uniform(0, 1))
        time.sleep(intertime)
    print(" Average delay: "+str(mean(timeArray)))
