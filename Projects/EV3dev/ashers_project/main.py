#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
robot.settings(150,1000, 150)
# Go forward and backwards for one meter.
robot.straight(400)
robot.turn(90)
robot.turn(-180)
robot.turn(90)
ev3.speaker.beep(1000)
robot.stop()
robot.settings(500,1000,500)
robot.straight(500)
robot.turn(360)
ev3.speaker.play_file("laser.wav")
robot.straight(100)
robot.turn(140)
robot.straight(400)
robot.straight(-900)
robot.turn(140*3)
robot.stop()
robot.settings(500,1000,300)
robot.turn(25)
robot.turn(-25)
robot.turn(25)
robot.turn(-25)
robot.straight(-50)
robot.straight(-50)
robot.straight(-50)
robot.straight(-50)
robot.turn(130)
robot.straight(500)
robot.stop()
robot.settings(100,1000,50)
robot.straight(-100)
robot.turn(50)
robot.turn(-50)