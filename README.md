# AntiScreenLockVeyon
Studying interception driver...  
https://github.com/veyon/veyon/pull/622/files/81a3ec6456118d5c819ac68507fbf63555442c92 xd  
a non admin user can talk with the driver, that's good news!
Compile veyon for windows is a lot of pain... And it may not be a good idea...  I love windows, veyon why do you do this?
Since the driver is accesible for non admin users, we can use the IOCTL_WRITE to do some kind of unlock or maybe detect the lock.  
after all, the lock application is just a gui application... restart explorer.exe sendmessage wm_close... enjoy!
