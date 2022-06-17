
  
import threading as thr
import time  
event = thr.Event() 
 
def list():
    print("Dasturchi bolish uchun shu dasturlarni o'rganish kerak ")
    time.sleep(2)
    event.wait()
    print(" CSS JAVA HTML PHYTON BOTSTRAP... ")
    time.sleep(2)
  
javob = input("Dasturchi bo'lishni istaysizmi ")
time.sleep(2)  
t1 = thr.Thread(target=list)
t1.start()  

if javob == 'ha':
    event.set() 
else:
    print("Sizga omad tilymiz")   
    