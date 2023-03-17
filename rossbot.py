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
ev3.screen.set_font(Font(size=24))
code = []
p1 = p2 = p3 = p4 = 0
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
    p1 = 1
elif cs.color() == Color.WHITE:
    p1 = 0
db.straight(dist2)
if cs.color() == Color.BLACK:
    p2 = 1
elif cs.color() == Color.WHITE:
    p2 = 0
db.straight(dist2)
if cs.color() == Color.BLACK:
    p3 = 1
elif cs.color() == Color.WHITE:
    p3 = 0
db.straight(dist2)
if cs.color() == Color.BLACK:
    p4 = 1
elif cs.color() == Color.WHITE:
    p4 = 0
#--------------------------------------------------------------------------
code = [p4, p3, p2, p1]
#code = [p1, p2, p3, p4]
if code == [0, 0, 0, 1]:
    ev3.screen.print('1', sep=' ', end='\n')
elif code == [0, 0, 1, 0]:
    ev3.screen.print('2', sep=' ', end='\n')
elif code == [0, 0, 1, 1]:
    ev3.screen.print('3', sep=' ', end='\n')
elif code == [0, 1, 0, 0]:
    ev3.screen.print('4', sep=' ', end='\n')
elif code == [0, 1, 0, 1]:
    ev3.screen.print('5', sep=' ', end='\n')
elif code == [0, 1, 1, 0]:
    ev3.screen.print('6', sep=' ', end='\n')
elif code == [0, 1, 1, 1]:
    ev3.screen.print('7', sep=' ', end='\n')
elif code == [1, 0, 0, 0]:
    ev3.screen.print('8', sep=' ', end='\n')
elif code == [1, 0, 0, 1]:
    ev3.screen.print('9', sep=' ', end='\n')
elif code == [1, 0, 1, 0]:
    ev3.screen.print('10', sep=' ', end='\n')
elif code == [1, 0, 1, 1]:
    ev3.screen.print('11', sep=' ', end='\n')
elif code == [1, 1, 0, 0]:
    ev3.screen.print('12', sep=' ', end='\n')
elif code == [1, 1, 0, 1]:
    ev3.screen.print('13', sep=' ', end='\n')
elif code == [1, 1, 1, 0]:
    ev3.screen.print('14', sep=' ', end='\n')
elif code == [1, 1, 1, 1]:
    ev3.screen.print('15', sep=' ', end='\n')
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
db.straight(10)
pen.run_angle(300,180,then=Stop.BRAKE)
if code == [0, 0, 0, 1]:
    quit()
db.straight(10)
pen.run_angle(300,-180,then=Stop.BRAKE)
if code == [0, 0, 1, 0]:
    quit()
db.straight(10)
pen.run_angle(300,180,then=Stop.BRAKE)
if code == [0, 0, 1, 1]:
    quit()
db.straight(10)
pen.run_angle(300,-180,then=Stop.BRAKE)
if code == [0, 1, 0, 0]:
    quit()
db.straight(10)
pen.run_angle(300,180,then=Stop.BRAKE)
if code == [0, 1, 0, 1]:
    quit()
db.straight(10)
pen.run_angle(300,-180,then=Stop.BRAKE)
if code == [0, 1, 1, 0]:
    quit()
db.straight(10)
pen.run_angle(300,180,then=Stop.BRAKE)
if code == [0, 1, 1, 1]:
    quit()
db.straight(10)
pen.run_angle(300,-180,then=Stop.BRAKE)
if code == [1, 0, 0, 0]:
    quit()
db.straight(10)
pen.run_angle(300,180,then=Stop.BRAKE)
if code == [1, 0, 0, 1]:
    quit()
db.straight(10)
pen.run_angle(300,-180,then=Stop.BRAKE)
if code == [1, 0, 1, 0]:
    quit()
db.straight(10)
pen.run_angle(300,180,then=Stop.BRAKE)
if code == [1, 0, 1, 1]:
    quit()
db.straight(10)
pen.run_angle(300,-180,then=Stop.BRAKE)
if code == [1, 1, 0, 0]:
    quit()
db.straight(10)
pen.run_angle(300,180,then=Stop.BRAKE)
if code == [1, 1, 0, 1]:
    quit()
db.straight(10)
pen.run_angle(300,-180,then=Stop.BRAKE)
if code == [1, 1, 1, 0]:
    quit()
db.straight(10)
pen.run_angle(300,180,then=Stop.BRAKE)
if code == [1, 1, 1, 1]:
    quit()