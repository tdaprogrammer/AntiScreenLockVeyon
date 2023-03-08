# AntiScreenLockVeyon
This solution is not generic and it depends on your screen coordinates, opened programs, etc.
It's still better than nothing but I don't like it at all, it requires a lot of previous setup.   
Studying interception driver...   
https://github.com/veyon/veyon/pull/622/files/81a3ec6456118d5c819ac68507fbf63555442c92 xd  
A non admin user can talk with the driver, that's good news!
Compile veyon for windows is a lot of pain... And it may not be a good idea...  I love windows, veyon why do you do this?   
Since the driver is accesible for non admin users, we can use the IOCTL_WRITE to do some kind of unlock or maybe detect the lock using the driver itself.   
After all, the lock application is just a gui application...   We can close it manually but not using sendmessage since veyon-worker runs with privileges...   
pyautogui seems to be the answer.
It seems that there could be a more generic solution, using the driver itself to get the mouse coordinates.
