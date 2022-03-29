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
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait
import logging
log = logging.getLogger('FLL')
log.setLevel(logging.DEBUG)
# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.A)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
robot.settings(150,1000, 150)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S1)

# Calculate the light threshold. Choose values based on your measurements.
BLACK = 9
WHITE = 100
threshold = (BLACK + WHITE) / 2

# Set the drive speed at 100 millimeters per second.
DRIVE_SPEED = 200

# Set the gain of the proportional line controller. This means that for every
# percentage point of light deviating from the threshold, we set the turn
# rate of the drivebase to 1.2 degrees per second.

# For example, if the light value deviates from the threshold by 10, the robot
# steers at 10*1.2 = 12 degrees per second.
PROPORTIONAL_GAIN_SPEED = 1.8
PROPORTIONAL_GAIN_TURN = 1.1
side = "right"
# Start following the line endlessly.
while True:
    reflection=line_sensor.reflection()
    deviation = reflection - threshold
    

    #log.info("LightSensor, %s"%reflection)
    
    # Calculate the turn rate.
    if side == "left": 
        turn_rate = PROPORTIONAL_GAIN_TURN * deviation
    else:
        turn_rate = PROPORTIONAL_GAIN_TURN * deviation * -1
    Speed=DRIVE_SPEED-PROPORTIONAL_GAIN_SPEED*abs(deviation)
    # Set the drive base speed and turn rate.
    robot.drive(Speed, turn_rate)
    
    # You can wait for a short time or do other things in this loop.
    wait(1)