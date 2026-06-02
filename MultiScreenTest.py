# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:38:49 2026

@author: keato
"""
 
import pyautogui
import cv2

from pytesseract import Output

import numpy as np
import pytesseract
from deep_translator import GoogleTranslator

resolution = (1920, 1080)

codec = cv2.VideoWriter_fourcc(*"XVID")

filename = "Recording2.avi"

fps = 30.0

out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Live", 1340, 880)

 
horizontal_offset = 0



crop_width = 600
crop_height = 400

 
 
frame_count =  0


while True:
    img = pyautogui.screenshot()
 
    frame = np.array(img) 
    #print(frame.shape) #(1440, 2560, 3)
  
    
    vertical_padding = int(crop_height) 
        
    horizontal_padding = int(crop_width) 
 
    cursorTuple = pyautogui.position() #Point(x=3728, y=635) example
   
    cursorTuple = (cursorTuple[0]+ horizontal_padding + horizontal_offset, cursorTuple[1] + vertical_padding)
    
    if cursorTuple[0] < (2560+horizontal_padding + horizontal_offset):
        
    
     
        y1 = cursorTuple[1] - crop_height // 2
        y2 = cursorTuple[1] + crop_height // 2
        
        x1 = cursorTuple[0] - crop_width // 2
        x2 = cursorTuple[0]+ crop_width // 2
        
        
        by1 = cursorTuple[1] - 30
        by2 = cursorTuple[1] + 100
        
        bx1 = cursorTuple[0] - crop_width // 2
        bx2 = cursorTuple[0]+ crop_width // 2
  
     
 
        frame = np.pad(frame, ((vertical_padding,vertical_padding), (horizontal_padding, horizontal_padding), (0, 0)))    
            
            
        crop = frame[y1 : y2 , x1 : x2 ]
        
 
        this = True
      
        if this:
  
            
            sliced = frame[by1 : by2 , bx1 : bx2 ] 
            
            
            results = pytesseract.image_to_data(sliced, output_type=Output.DICT)
            
            
            for i in range(0, len(results["text"])):
    
                # We can then extract the bounding box coordinates
                # of the text region from  the current result
                x = results["left"][i]
                y = results["top"][i]
                w = results["width"][i]
                h = results["height"][i]
                
                
                # We will also extract the OCR text itself along
                # with the confidence of the text localization
                text = results["text"][i]
                conf = int(results["conf"][i])
                
     
                
                threshold = 50
                
                if conf > threshold:
                    
                    
                
                    text = "".join(text).strip()
                    
                    
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
                    
                     
         
        
       
        sliced= cv2.cvtColor(sliced, cv2.COLOR_BGR2RGB)
        out.write(crop)
        cv2.imshow('Live', sliced)
        
        
        frame_count +=1

        if cv2.waitKey(1) == ord('q'): 
            break
        
    
    else:#Doesnt do anything if you leave the first monitor. Prevents crashing by going out of array index
        print("out of bounds")
        
     
 
 
 
 
out.release()

cv2.destroyAllWindows()