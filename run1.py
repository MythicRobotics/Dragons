from pybricks.tools import StopWatch, multitask, run_task, wait

from robot_config import DRIVE_BASE, HUB
from library import elevator_up, elevator_down, elevator_left, elevator_right, drive_turn_right, drive_straight_forward, drive_straight_backward, telemetry, E_stop
# Set up all devices.
watch = StopWatch()




async def turn_by_turn_1():
    watch.reset()
    print(HUB.battery.voltage())
    DRIVE_BASE.use_gyro(True)
    await drive_straight_backward(10)
    await multitask(
       elevator_up(320),
        drive_straight_forward(320),
    )
    await drive_turn_right(47)
    await multitask(
        drive_straight_forward(565),
        elevator_up(600)
    )
    await drive_turn_right(47)


    await elevator_left(400, 1100)
    await elevator_down(390, 500)

    await multitask(
        elevator_left(400, 1100),
        elevator_down(390, 780),
        elevator_left(350, 1000),
        elevator_down(390, 780),
    )
    # left before down
    await elevator_up(460, 1000)
    await elevator_right(470, 780)

    await drive_straight_backward(40)
    await elevator_down(470, 1000)
    await elevator_left(300, 780)
    await elevator_down(470, 1000)
    #this is where the robot does tangled
    '''

    watch.reset()
    print(HUB.battery.voltage())
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.straight(-10, then=Stop.BRAKE)
    await multitask(
       Raise_Elevator(320),
        DRIVE_BASE.straight(640, then=Stop.BRAKE),
    )
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(-70)
    # new blcok for lower attachment
    await RIGHT_ATTACHMENT.run_angle(1000, 100)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(-100, then=Stop.BRAKE)
    await LEFT_ATTACHMENT.run_angle(1000, -170)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(-20)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(105, then=Stop.BRAKE)
    # raise brush
    await RIGHT_ATTACHMENT.run_angle(1000, 450)
    await multitask(
        subtask2(),
        RIGHT_ATTACHMENT.run_angle(150, -600),
    )
    await DRIVE_BASE.straight(-25, then=Stop.BRAKE)
    await RIGHT_ATTACHMENT.run_angle(1000, 320)
    await wait(50)
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(-20)
    await multitask(
        RIGHT_ATTACHMENT.run_angle(1000, -384),
        subtask3(),
    )
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    # you need to turn more try -20 if it dose not work try -25
    await DRIVE_BASE.turn(-30)
    await RIGHT_ATTACHMENT.run_angle(1000, 850)
    # turn before long straight drive after minecart
    print('turn correction', 0 + ((-330 - DRIVE_BASE.angle()) + 50), DRIVE_BASE.angle())
    await DRIVE_BASE.turn(55)
    await multitask(
        subtask4(),
        RIGHT_ATTACHMENT.run_angle(1000, -416),
    )
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(130, then=Stop.BRAKE)
    # pshing the tip the schlas
    await RIGHT_ATTACHMENT.run_angle(1000, -250)
    await DRIVE_BASE.straight(-50, then=Stop.BRAKE)
    await multitask(
        DRIVE_BASE.straight(550, then=Stop.BRAKE),
        RIGHT_ATTACHMENT.run_angle(1000, 324),
    )
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(90)
    await multitask(
        subtask5(),
        RIGHT_ATTACHMENT.run_angle(1000, -148),
    )
    await LEFT_ATTACHMENT.run_angle(1000, 170)
    await RIGHT_ATTACHMENT.run_angle(1000, -192)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(0 - ((DRIVE_BASE.angle() + 90) + 20))
    await DRIVE_BASE.turn(20)
    await DRIVE_BASE.turn(0 - ((DRIVE_BASE.angle() + 90) + 20))
    await DRIVE_BASE.turn(20)
    await DRIVE_BASE.turn(0 - ((DRIVE_BASE.angle() + 90) + 20))
    await DRIVE_BASE.turn(20)
    await DRIVE_BASE.turn(0 - ((DRIVE_BASE.angle() + 90) + 20))
    await DRIVE_BASE.turn(20)
    await DRIVE_BASE.turn(0 - ((DRIVE_BASE.angle() + 90) + 20))
    await DRIVE_BASE.turn(20)
    await DRIVE_BASE.turn(0 - ((DRIVE_BASE.angle() + 90) + 20))
    await DRIVE_BASE.turn(20)
    await DRIVE_BASE.turn(0 - ((DRIVE_BASE.angle() + 90) + 20))
    await DRIVE_BASE.turn(20)
    await DRIVE_BASE.turn(0 - ((DRIVE_BASE.angle() + 90) + 20))
    await DRIVE_BASE.turn(20)
    await DRIVE_BASE.turn(0 - ((DRIVE_BASE.angle() + 90) + 20))
    await DRIVE_BASE.turn(20)
    await DRIVE_BASE.turn(0 - ((DRIVE_BASE.angle() + 90) + 20))
    await DRIVE_BASE.turn(0 + ((DRIVE_BASE.angle() + 110) + 35))
    DRIVE_BASE.stop()
    await RIGHT_ATTACHMENT.run_angle(1000, 500)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await multitask(
        subtask6(),
        subtask7(),
        LEFT_ATTACHMENT.run_angle(1000, 5),
    )
    DRIVE_BASE.stop()
    print(watch.time())
    '''



async def launch_1():
    await wait(0)
    await multitask(
        turn_by_turn_1(),
        telemetry(),
        E_stop(),
        race=True,
    )

async def main():
    await multitask(
        wait(0),
    )


run_task(main())