# Untitled - By: robot - Wed May 14 2025

import sensor, image, time
from motors import move

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_gainceiling(16)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)


blackc = [(0, 31, -12, 7, -14, 18)]
vel=80
Kp= vel / 57

while True:
    img = sensor.snapshot()
    black = img.find_blobs(blackc, area_threshold=300,roi=(0,120,320,120))
    #SEGUIMIENTO DE LINEA
    if black:
        black = max(black, key=lambda b: b.pixels())
        error = abs(160 - black.cx())
        fix = error * Kp
        m1 = vel - fix if black.cx() < 160 else vel
        m2 = vel - fix if black.cx() > 160 else vel

        move(m1,m2)

        print(m2)
