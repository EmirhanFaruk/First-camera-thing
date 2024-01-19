
# Modification date: Tue May 17 23:16:58 2022

# Production date: Sun Sep  3 15:43:43 2023

"""
import pygame
import pygame.camera
import pygame.image
import time

pygame.init()
pygame.camera.init()
print(pygame.camera.cameras())
"""

# import the opencv library
import cv2
import time
#import numpy
#print("bir")
  
# define a video capture object
vid = cv2.VideoCapture(0)
#print("iki")
n = 0
st = time.time()
while(True):
    #print("üç")
    f = time.time()
    
    if f - st >= 1:
        print(n)
        st = time.time()
        n = 0

        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        #print("dört")
        #print(frame)
        
        for x in range(len(frame)):
            for y in range(len(frame[x])):
                gray = frame[x][y].sum()//3
                frame[x][y] = [0, gray, 0]
                """
                if frame[x][y].sum() < 255*1.5:
                    frame[x][y] = [0, 0, 0]
                else:
                    frame[x][y] = [255, 255, 255]
                """
        #print(frame)
        #print(len(frame), len(frame[0]))
        # Display the resulting frame
        cv2.imshow('frame', frame)
        #print("beş")
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    n += 1
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
