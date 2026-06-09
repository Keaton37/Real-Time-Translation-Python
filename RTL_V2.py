# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 17:25:00 2026

@author: keato
"""
from pytesseract import Output
import dxcam
import numpy as np
import cv2
import pyautogui
import pytesseract
from deep_translator import GoogleTranslator
from TimeClass import Timer
import asyncio
import math



target_fps = 30
camera = dxcam.create(output_color="BGR")
camera.start(target_fps=target_fps, video_mode=True)



cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Live", 1070, 680)


horizontal_offset = 0 #When using it to translate Minecraft I noticed the game had a bias to have text on the right hand side, this meant words often leaving my crop area by being too far to the right. Can adjust this to ofset bias.



crop_width = 600
crop_height = 400



resolution1 = (2560,1440)
resolution2 = (1920,1080) #I have no idea why but resolution 2 crashes the window :(


writer = cv2.VideoWriter(
    "video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), target_fps, resolution1)

 
t= Timer()
t.start()

time_between_updates = 3 #the amount of time before the program takes anotther image (5 is a good default setting) 
  

while True:  

    
    if asyncio.run(t.intervalTime(time_between_updates)):
       
        frame, ts = camera.get_latest_frame(with_timestamp=True)


        vertical_padding = int(crop_height) 
        
        horizontal_padding = int(crop_width) 
    
        cursorTuple = pyautogui.position() #Point(x=3728, y=635) example
    
        cursorTuple = (cursorTuple[0]+ horizontal_padding + horizontal_offset, cursorTuple[1] + vertical_padding)
        
        if cursorTuple[0] < (2560+horizontal_padding + horizontal_offset):
            
        
        
            y1 = cursorTuple[1] - crop_height // 2
            y2 = cursorTuple[1] + crop_height // 2
            
            x1 = cursorTuple[0] - crop_width // 2
            x2 = cursorTuple[0]+ crop_width // 2
            
            
            by1 = cursorTuple[1] - 100
            by2 = cursorTuple[1] + 100
            
            bx1 = cursorTuple[0] - crop_width // 2
            bx2 = cursorTuple[0]+ crop_width // 2
    
        
    
            frame = np.pad(frame, ((vertical_padding,vertical_padding), (horizontal_padding, horizontal_padding), (0, 0)))    
                
                
            #crop = frame[y1 : y2 , x1 : x2 ]
            
            
                
            sliced = frame[by1 : by2 , bx1 : bx2 ] 

            gray =  cv2.cvtColor(sliced, cv2.COLOR_BGR2GRAY)

            
                
                
            results = pytesseract.image_to_data(
                                gray,
                                output_type=Output.DICT,
                                config='--psm 6'
                            )
                
                
            for i in range(0, len(results["text"])):
           
         
                    #if results["text"][i].isalpha():
                         
        
                  
                        x = results["left"][i]
                        y = results["top"][i]
                        w = results["width"][i]
                        h = results["height"][i]
                        
                
                        text = results["text"][i]
                        conf = int(results["conf"][i])
                        
            
                        
                        threshold = 50
                        
                        if conf > threshold:
                            
                            
                        
                            text = "".join(text).strip()
                            
                            print(text)
                            result = GoogleTranslator(source='de', target='en').translate(text)
                            
                        
                            cv2.rectangle(sliced,
                                        (x, y),
                                        (x + w, y + h),
                                        (0, 0, 255), 2)
                            cv2.putText(sliced,
                                        result,
                                        (x, y - 10), 
                                        cv2.FONT_HERSHEY_SIMPLEX,
                                        1.2, (0, 255, 255), 3)
                            
                        
 

        writer.write(sliced)
        cv2.imshow('Live', sliced)
 

 
  

    if cv2.waitKey(1) == ord('q'):
        break
 

t.stop()
 
camera.stop()
writer.release()
cv2.destroyAllWindows()