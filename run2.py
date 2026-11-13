from pybricks.parameters import Stop
from pybricks.tools import StopWatch, multitask, run_task, wait

from robot_config import DRIVE_BASE, HUB
from library import elevator_up, elevator_down, elevator_left, elevator_right, drive_turn_right, drive_turn_left, drive_straight_forward, drive_straight_backward, telemetry, E_stop, heading_check, all_stop
# Set up all devices.
watch = StopWatch()




async def turn_by_turn_2():
    await drive_straight_backward(10)
    await drive_straight_forward(100)
    await drive_turn_right(20) 
    await heading_check()
    await multitask(
        drive_straight_forward(710),
        elevator_left(20)
    )
    await drive_turn_right(70)
    await heading_check()
    await drive_straight_forward(50)                               
    await drive_turn_right(90)
    await heading_check()
    #simplify lines 23-28?                
    await multitask(
        drive_straight_forward(92),      #pass the seeds
        elevator_left(120)
    )
    await multitask(
        elevator_up(200),#150au
        elevator_left(45)
    )
    await multitask(
        elevator_up(500),#450au
        elevator_left(300)
    )
    await elevator_right(200)
    await multitask(
        elevator_down(670),#570au
        elevator_right(120)
    )
    await elevator_right(100)
    await heading_check()
    await drive_straight_backward(90)
    #await drive_turn_right(20)
    await drive_turn_right(110)
    await heading_check()
    await drive_straight_backward(260)
    await drive_turn_left(90)
    await heading_check()
    await elevator_left(80)
    await drive_straight_forward(37)
    await elevator_up(910)#670au
    await elevator_left(130)             #reaching roots A
    await multitask(
        elevator_left(280),
        elevator_down(100)#75au
    )
    await elevator_right(510)                   #610) 10th
    await elevator_down(375)#275          
    await multitask(
        elevator_up(500),#400
        elevator_left(310, 500)                  #340 10th
    )
    await multitask(
        elevator_up(330),
        elevator_left(70)
    )
    await multitask(
        elevator_left(130),                      #200 10th
        elevator_down(200) 
    )                                 #reaching roots B           
   
    await elevator_right(200)
    await multitask(                         #reaching roots finished
        drive_straight_forward(100),
        elevator_down(1000),
        elevator_right(200)
    )
    await drive_straight_forward(50)
    await multitask(
        wait(4500),
        
        multitask(                              #tree gose up:3
            elevator_up(1000),
            elevator_left(130)
        ),   
        race=True,      
    )
    await elevator_down(200)
    await drive_straight_backward(60)
    await drive_turn_right(180)

    await multitask(
        multitask(
            drive_straight_forward(400),
            elevator_right(400),
            elevator_down(945),
        ),  
        wait(2000),#2000
        race=True,      
    )

    await drive_turn_right(210)
    await drive_straight_forward(300)
    
async def launch_2():
    await wait(0)
    watch.reset()
    print(HUB.battery.voltage())
    DRIVE_BASE.use_gyro(True)
    DRIVE_BASE.reset()
    await multitask(    
        turn_by_turn_2(),
        #telemetry(),
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