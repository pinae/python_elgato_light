import leglight
ring = leglight.LegLight('192.168.178.31', 9123)
print(ring)
print(vars(ring))
ring.on()
ring.color(3900)
ring.brightness(75)
