import leglight
import time
ring = leglight.LegLight('192.168.178.31', 9123)
ring.brightness(0)
ring.color(3900)
ring.on()
for i in range(100):
    time.sleep(0.1)
    ring.brightness(i)
