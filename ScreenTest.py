
import pyautogui
import cv2
 
import numpy as np

resolution = (1920, 1080)

codec = cv2.VideoWriter_fourcc(*"XVID")

filename = "Recording2.avi"

fps = 30.0

out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Live", 1340, 880)

#print(pyautogui.size()) Size(width=2560, height=1440)


crop_width = 600
crop_height = 500

while True:
    img = pyautogui.screenshot()
 
    frame = np.array(img) 
    #print(frame.shape) #(1440, 2560, 3)
    transposedFrame = np.transpose(frame, (1,0,2)) #2560,1440,3
    print(transposedFrame.shape)
    
    cursorTuple = pyautogui.position() #Point(x=3728, y=635) example
    
    if cursorTuple[0] < 2560:
        print(transposedFrame[cursorTuple])
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow('Live', frame)

        if cv2.waitKey(1) == ord('q'): 
            break
        
    
    else:
        print("out of bounds")
     
    
  
 
 
 
out.release()

cv2.destroyAllWindows()