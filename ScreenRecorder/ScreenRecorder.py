import pyautogui
import cv2
import numpy as np

#confirgure settings of recording
resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Recording.avi"
fps = 20.0 #set to 20 fps because 60 fps seemed too fast in the end
out = cv2.VideoWriter(filename, codec, fps, resolution)


#create recording window
cv2.namedWindow("Recording", cv2.WINDOW_NORMAL) 
cv2.resizeWindow("Recording", 480, 270) 

#start recording
while True:
    img = pyautogui.screenshot()
    frame = np.array(img) #convert image to numpy array
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #convert to RGB
    out.write(frame) 
    cv2.imshow('Recording', frame) 

    if cv2.waitKey(1) == ord('0'): #press '0' to stop recording
        break

#release resources
out.release()
cv2.destroyAllWindows() 
