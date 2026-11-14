from pybricks.tools import StopWatch, multitask, run_task, wait
from robot_config import DRIVE_BASE, HUB
from library import elevator_up, elevator_down, elevator_left, elevator_right, drive_turn_right, drive_turn_left, drive_straight_forward, drive_straight_backward, telemetry, E_stop, heading_check, drive_straight_speed, all_stop
# Set up all devices.
watch = StopWatch()
# ᓚᘏᗢ

async def turn_by_turn_4():
    await drive_straight_backward(10)
    await drive_straight_forward(400)
   
    await drive_turn_left(-30)
    await multitask(
        elevator_up(200),
        drive_straight_forward(200)
    )
    await drive_turn_right(0)
    await drive_straight_forward(170)
    await elevator_down(200)
    await drive_straight_backward(95)
    await drive_straight_forward(100)            #fungus good :)
    await elevator_up(105)
    await drive_straight_backward(85)
    await elevator_up(300)
    await drive_turn_right(45)
    await drive_straight_backward(80)
    await drive_turn_left(-50)                   #window to past good :)
    await multitask(
        drive_straight_forward(230),      #more ?
        elevator_up(400)
    )
    await drive_turn_right(45)
    await multitask(
        drive_straight_backward(50),
        elevator_down(715)
    )
    await drive_straight_speed(50)
    await drive_straight_forward(150)
    await drive_straight_speed(400)

async def launch_4():
    await wait(0)
    watch.reset()
    print(HUB.battery.voltage())
    DRIVE_BASE.use_gyro(True)
    DRIVE_BASE.reset()
    await multitask(
        turn_by_turn_4(),
        telemetry(),
        E_stop(),
        race=True,
    )
    await all_stop()
    print(f"Time: {watch.time()/1000} seconds")

async def main():
    await multitask(
        wait(0),
    )


run_task(main())