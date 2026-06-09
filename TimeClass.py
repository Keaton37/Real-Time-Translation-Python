# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 00:05:33 2026

@author: keato
"""
import asyncio
import time



class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
     



    def __init__(self):
        self._start_time = None
        self.last_interval_value = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()
        
        
    def checkTime(self):
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")
            
        current_time = time.perf_counter() - self._start_time
       
        return(current_time)
    

    async def intervalTime(self, interval):
 
        if self.checkTime() is not None:
  
            if int(self.checkTime()) != self.last_interval_value:
        
                if int(self.checkTime())  % interval == 0:
          
                    self.last_interval_value = int(self.checkTime())
    
                    return True
 
 
 
     

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")