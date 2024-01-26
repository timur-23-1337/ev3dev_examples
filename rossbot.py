#!/usr/bin/env pybricks-micropython
#--------------------------------------------------------------------------
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Color, Stop, Direction, Button
from pybricks.media.ev3dev import Font, ImageFile
from pybricks.tools import wait
#--------------------------------------------------------------------------
ev3 = EV3Brick()
lm = Motor(Port.C)
rm = Motor(Port.B)
db = DriveBase(lm, rm, wheel_diameter=30, axle_track=120)
us = UltrasonicSensor(Port.S4)
cs = ColorSensor(Port.S3)
pen = Motor(Port.D)
ev3.screen.set_font(Font(size=32))
code = 0
dist2 = 28
dist1 = 40
#--------------------------------------------------------------------------
ev3.light.on(Color.RED)
ev3.screen.load_image(ImageFile.EV3_ICON)
while True:
    if Button.CENTER in ev3.buttons.pressed():
        break
ev3.light.on(Color.GREEN)
ev3.screen.clear()
#--------------------------------------------------------------------------
db.drive(150, 0)
while True:
    if cs.color() == Color.BLACK:
        db.stop()
        break
while True:
    db.drive(30, 0)
    if cs.color() == Color.WHITE:
        db.stop()
        break
while True:
    db.drive(30, 0)
    if cs.color() == Color.BLACK:
        db.stop()
        db.straight(dist1)
        break
if cs.color() == Color.BLACK:
    code += 8
db.straight(dist2)
if cs.color() == Color.BLACK:
    code += 4
db.straight(dist2)
if cs.color() == Color.BLACK:
    code += 2
db.straight(dist2)
if cs.color() == Color.BLACK:
    code += 1
#--------------------------------------------------------------------------
ev3.screen.print(code, sep=' ', end='\n')
wait(3000)
pen.run_angle(300, -360, then=Stop.COAST, wait=True)
#--------------------------------------------------------------------------
while us.distance() > 30:
    if us.distance() >= 150:
        db.drive(300,0)
    elif us.distance() < 150:
        db.drive(100,0)
db.turn(90)
pen.reset_angle(0)
#--------------------------------------------------------------------------
for i in range(code):
    if i%2 == 0:
        pen.run_angle(300,180,then=Stop.BRAKE)
    else:
        pen.run_angle(300,-180,then=Stop.BRAKE)
    db.straight(10)
#--------------------------------------------------------------------------
