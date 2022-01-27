import time
import shutil
import picamera
print("running")
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('../pics/pycam.jpg')
time.sleep(2)
#shutil.move("home/pi/Documents/Engineering_4_Notebook/python/pycam.jpg", "home/pi/Documents/Engineering_4_Notebook/pics")
print("done")
