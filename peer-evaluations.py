"""
@author: Shawn
"""

import random

# Input min and max points to be given
print("---!! Presentation Peer Evaluation !!---")
while True:
    minPres = int(input("Minimum points (50 - 70): "))
    
    if minPres in range(50, 71):
        while True:
            maxPres = int(input("Maximum points (50 - 70): "))
            
            if maxPres in range(50, 71):
                break
            else:
                print("Don't give your classmates that grade dog!")
        break
    else:
        print("Don't give your classmates that grade dog!")

print("\n---!! Video Peer Evaluation !!---")
while True:
    minVid = int(input("Minimum points (20 - 30): "))
    
    if minVid in range(20, 31):
        while True:
            maxVid = int(input("Maximum points (20 - 30): "))
            
            if maxVid in range(20, 31):
                break
            else:
                print("Don't give your classmates that grade dog!")
        break
    else:
        print("Don't give your classmates that grade dog!")

groups = int(input("How many groups presented? (I think 24?): "))
presentList = []
videoList = []

while True:
    presentList.append(random.randrange(minPres, maxPres + 1))
    videoList.append(random.randrange(minVid, maxVid + 1))
    if len(presentList) == groups:
        if len(videoList) == groups:
            break

print("\n---!! Point distribution !!---\n")
print("Presentations: \n" + str(presentList))
print("Videos: \n" + str(videoList))