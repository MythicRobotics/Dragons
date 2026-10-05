from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait

from library import set_drivebase
from run1 import launch_1
from run2 import test2
from run3 import test3
from run4 import test4
from library import print_drivebase_settings
from turn_tuning import tuning
from ui import add_program, user_interface
'''from xbox_teleop import teleop'''

async def main():
    # Import from xbox_teleop the teleop function if you want to use
    # the telop mode and add the telop program
    # Must be paired at starup or will crash. Disconnect block if not wanted
    # Note the code is provided disconnected.

    # Blank,  done to make code multitask
    # Needed due to how the blocks work
    await multitask(
        wait(0),
    )
    # Print to consule the default drivebase settings
    await print_drivebase_settings()
    # Override these settings. Note pybricks is conservative with speeds.
    # The default speeds are about 40% of what the motors can handle
    # You probably can double the default speeds in the robot_config file.
    # Conversely the accelration values pybricks creates tend to be too high
    # If your wheels slip your distances will be off. Lower accelration as needed
    # in the robot_config file to eliminate wheel slippage. These values will depend on wheel choice, center of gravity of your robot and robot weight.
    await set_drivebase()
    # Add the programs (Missons) below they will appear in the order placed
    # Missions will need to be imported, see example missions/utility programs
    # below
    await add_program(launch_1, '1', Color.BLUE)
    await add_program(test2, '2', Color.CYAN)
    await add_program(test3, '3', Color.MAGENTA)
    await add_program(test4, '4', Color.ORANGE)
    await add_program(tuning, 't', Color.RED)
    '''await add_program(teleop, 'X', Color.ORANGE)'''
    # Launch the user interface
    await user_interface()


run_task(main())