from picamera2 import Picamera2
from libcamera import controls
import time

picam2 = Picamera2()
# picam2.preview_configuration.main.size = (1280,720)
# picam2.start(show_preview=False)
# picam2.start_and_capture_files("./Collect_Data/test{:d}.jpg", num_files=3, delay=0.5)
# picam2.stop_preview()
# picam2.stop()
iter = 0
start_time = time.time()
picam2.preview_configuration.main.size = (1280,720)
picam2.preview_configuration.main.format ="RGB888"
picam2.preview_configuration.main.align()
picam2.configure("preview")
while True:
    # picam2.start()
    # print(start_time)
    # print(time.time())
    if(time.time()-start_time>10):
        print("More than 10 sec",flush=True)
        picam2.start_and_capture_files("./Collect_Data/tes"+str(iter)+".jpg",show_preview=False)
        iter+=1
        start_time = time.time()
        print(iter)
