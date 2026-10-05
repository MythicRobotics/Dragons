from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

from pid_python import distance_pid, heading_pid

# Set up all devices.
HUB = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
DRIVE_LEFT = Motor(Port.B, Direction.COUNTERCLOCKWISE)
DRIVE_RIGHT = Motor(Port.A, Direction.CLOCKWISE)
DRIVE_BASE = DriveBase(DRIVE_LEFT, DRIVE_RIGHT, 62.4, 104)
LEFT_ATTACHMENT = Motor(Port.F, Direction.CLOCKWISE)
RIGHT_ATTACHMENT = Motor(Port.E, Direction.COUNTERCLOCKWISE)

# Initialize variables.
SPEED = 400
ACCELERATION = 500
TURN_SPEED = 85
TURN_ACCELERATION = 600
MANUAL_MOTOR_SPEED = 250
#These are for FLL table testing.  The other set of values are for outreach events.
'''
TELEOP_SPEED = 150
TELEOP_ACCEL = 500
TELEOP_TURN = 100
TELEOP_TURN_ACCEL = 500
TELEOP_ATTACH_SPEED = 1000
'''
# These are for outreach events.  The other set of values are for FLL table testing.
TELEOP_SPEED = 400
TELEOP_ACCEL = 500
TELEOP_TURN = 85
TELEOP_TURN_ACCEL = 600
TELEOP_ATTACH_SPEED = 1000

KP = 17500
KI = 3000
KD = 500
TURN_KP =17600
TURN_KI = 0
TURN_KD = 1


# The main program starts here.
# never goin give you up never goin say good by never goin do nothing to
#  hurt you.
# This is where you configure all the variables as well as
# the parts of the robot. These values are then imported/used as necessary.

# Change to match the setup of your robot. Adjust speeds as necessary
distance_pid(DRIVE_BASE, 9000)
heading_pid(DRIVE_BASE, KP, KI, KD, 0)
