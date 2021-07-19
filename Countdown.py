#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
t = input("Enter the time in seconds: ")
countdown(int(t))


# In[ ]:




