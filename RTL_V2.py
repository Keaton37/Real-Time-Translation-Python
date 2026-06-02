# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 17:25:00 2026

@author: keato
"""
 
import dxcam

import cv2

target_fps = 30
camera = dxcam.create(output_color="BGR")
camera.start(target_fps=target_fps, video_mode=True)



cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Live", 480, 270)




writer = cv2.VideoWriter(
    "video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), target_fps, (1920, 1080))

 

while True:
     
    
    
    frame, ts = camera.get_latest_frame(with_timestamp=True)
    
     


    writer.write(frame)
    cv2.imshow('Live', frame)


    if cv2.waitKey(1) == ord('q'):
        break
 


 
camera.stop()
writer.release()
cv2.destroyAllWindows()