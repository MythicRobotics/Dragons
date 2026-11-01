from pybricks.tools import StopWatch, multitask, run_task, wait

from robot_config import DRIVE_BASE, HUB
from library import elevator_up, elevator_down, elevator_left, elevator_right, drive_turn_right, drive_turn_left, drive_straight_forward, drive_straight_backward, telemetry, E_stop, heading_check, drive_straight_speed
# Set up all devices.
watch = StopWatch()
# ᓚᘏᗢ



async def turn_by_turn_3():
    watch.reset()
    print(HUB.battery.voltage())
    DRIVE_BASE.use_gyro(True)
    await drive_straight_backward(10)
    await drive_straight_forward(90)
    await drive_turn_left(20)
    await drive_straight_forward(245)
    await drive_turn_right(20)
    await drive_straight_forward(65)
    await multitask(
        drive_straight_forward(15),
        elevator_up(10)
    )                                     #rock finished
    await multitask(
        elevator_left(225),
        drive_straight_backward(300)
    )
    await drive_turn_right(45)
    await multitask(
        elevator_left(225),
        drive_straight_forward(520)
    )
    await elevator_up(300)
    await drive_straight_speed(40)
    await multitask(
        elevator_up(110),
        drive_straight_backward(145)
    )
    await drive_straight_speed(60)

'''await DRIVE_BASE.straight(250)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(-45)
    async def subtask2():
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(45)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(270)

async def subtask3():
    await wait(1000)
    await LEFT_ATTACHMENT.run_angle(250, -260)

async def subtask4():
    await wait(1000)
    await LEFT_ATTACHMENT.run_angle(250, -260)

async def subtask5():
    await multitask(
        RIGHT_ATTACHMENT.run_angle(1000, -265),
        subtask3(),
    )

async def subtask6():
    await wait(50)
    print('who lived here? complete ^', HUB.imu.heading())
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(-30)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(10)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(420)

async def subtask7():
    watch.reset()
    print(HUB.battery.voltage())
    DRIVE_BASE.use_gyro(True)
    await multitask(
        subtask(),
        RIGHT_ATTACHMENT.run_angle(1000, 400),
    )
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(250)
    await multitask(
        subtask2(),
        subtask5(),
    )
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(-50)
    # forge complete ^
    await RIGHT_ATTACHMENT.run_angle(1000, 30)
    await LEFT_ATTACHMENT.run_angle(1000, -260)
    await DRIVE_BASE.turn(-30)
    # who lived here? complete ^
    await multitask(
        subtask6(),
        RIGHT_ATTACHMENT.run_angle(1000, 800),
    )
    await wait(50)
    print('after  veer ', HUB.imu.heading())
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(20)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(-230)
    await DRIVE_BASE.straight(100)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(-30)
    await DRIVE_BASE.arc(-400, distance=-350, then=Stop.NONE)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(-500)
    # last code above this line
    DRIVE_BASE.stop()
    print(watch.time())'''

async def launch_3():
    await wait(0)
    await multitask(
        turn_by_turn_3(),
        telemetry(),
        E_stop(),
        race=True,
    )

async def main():
    await multitask(
        wait(0),
    )


run_task(main())