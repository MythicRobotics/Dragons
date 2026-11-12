from pybricks.tools import StopWatch, multitask, run_task, wait
from robot_config import DRIVE_BASE, HUB
from library import elevator_up, elevator_down, elevator_left, elevator_right, drive_turn_right, drive_turn_left, drive_straight_forward, drive_straight_backward, telemetry, E_stop, heading_check, drive_straight_speed
# Set up all devices.
watch = StopWatch()
# ᓚ

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
    await drive_straight_forward(100)
    await elevator_up(90)
    await drive_straight_backward(100)
    
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
    print(f"Time: {watch.time()/1000} seconds")

async def main():
    await multitask(
        wait(0),
    )


run_task(main())