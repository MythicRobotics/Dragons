from pybricks.parameters import Button, Stop
from pybricks.tools import StopWatch, multitask, run_task, wait

from pid_python import heading_pid
from robot_config import DRIVE_BASE, HUB, KD, KI, KP, LEFT_ATTACHMENT, RIGHT_ATTACHMENT, TURN_KD, TURN_KI, TURN_KP

# Set up all devices.
watch = StopWatch()

async def subtask():
    watch.reset()
    await LEFT_ATTACHMENT.run_angle(-1000, 90)
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.straight(-10, then=Stop.BRAKE)
    await DRIVE_BASE.straight(100)
    await wait(50)
    DRIVE_BASE.settings(turn_rate=500)
    DRIVE_BASE.settings(turn_acceleration=250)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, 11250, 5625, 0)
    await DRIVE_BASE.turn(45)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    # -750  mm
    await DRIVE_BASE.arc(-730, angle=45, then=Stop.NONE)
    await DRIVE_BASE.straight(120, then=Stop.NONE)
    await DRIVE_BASE.arc(-700, angle=15)
    await LEFT_ATTACHMENT.run_angle(200, 225)
    DRIVE_BASE.stop()
    print(watch.time())

async def subtask2():
    while True:
        await wait(0)
        await wait(100)
        print(DRIVE_BASE.angle())
        print(HUB.battery.voltage())

async def subtask3():
    await wait(1000)
    while True:
        await wait(0)
        if Button.CENTER in HUB.buttons.pressed():
            raise SystemExit

async def test4():
    await wait(0)
    await multitask(
        subtask(),
        subtask2(),
        subtask3(),
        race=True,
    )

async def main():
    await multitask(
        wait(0),
    )


run_task(main())