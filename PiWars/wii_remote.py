#!/usr/bin/python
#Connects a wii remote
import cwiid, time, pibrella #imports modules that allows the user to connect a wii remote via Bluetooth, time and the Pibrella module

button_delay = 0.1
motor_speed = 0.7

def left_wheel(): #defines the function for turning on the left wheel
  pibrella.output.e.write(motor_speed) #turns on output e

def right_wheel(): #defines the function for turning on the right wheel
  pibrella.output.g.write(motor_speed) #turns on output g

def stop(): #defines the function to turn off all outputs to stop the robot
  pibrella.output.e.write(0)
  pibrella.output.f.write(0)
  pibrella.output.g.write(0)
  pibrella.output.h.write(0)
    
print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)

# Connects to the Wii Remote

try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error connecting"
  quit()

print 'Wii Remote connected.'

wii.rpt_mode = cwiid.RPT_BTN
 
while True: #loops infinitely

  buttons = wii.state['buttons']
  
  #when the plus and minus buttons are pressed together, it will make the remote vibrate and then break the connection
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)

  #if the left button is pressed on the wii remote, the robot turns left
  if (buttons & cwiid.BTN_LEFT): 
    right_wheel() 
    time.sleep(button_delay)
    
  #if the right buttton on the wii remote is pressed, the robot will turn right
  if(buttons & cwiid.BTN_RIGHT): 
    left_wheel() 
    time.sleep(button_delay)

  
  #if the forward buttton on the wii remote is pressed, the robot will drive forward by turning on both wheels
  if (buttons & cwiid.BTN_UP): 
    left_wheel() 
    right_wheel()
    time.sleep(button_delay)

  #if the backward buttton on the wii remote is pressed, the robot will drive forward by turning on both wheels  
  if (buttons & cwiid.BTN_DOWN):
   left_wheel()
   right_wheel()
   time.sleep(button_delay)  
    
  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_B):
    stop()
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
    time.sleep(button_delay)           

  #when the minus button is pressed on the wii remote, the motor speed will decrease by 0.1, slowing the robot down
  if (buttons & cwiid.BTN_MINUS):
    motor_speed = motor_speed - 0.1
    time.sleep(button_delay)   

  #when the plus button is pressed on the wii remote, the motor speed will increase by 0.1, speeding up the robot
  if (buttons & cwiid.BTN_PLUS):
    motor_speed = motor_speed + 0.1
    time.sleep(button_delay)
