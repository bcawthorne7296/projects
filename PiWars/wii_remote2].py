#Connects a wii remote
import cwiid, time, motor_control as mc, RPi.GPIO as GPIO #imports modules that allows the user to connect a wii remote via Bluetooth, time and the Pibrella module

button_delay = 0.001

try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error connecting"
  quit()

#If the wii remote connects successfully, it will vibrate for one second
wii.rumble = 1
time.sleep(1)
wii.rumble = 0
print 'Wii Remote connected.'

wii.rpt_mode = cwiid.RPT_BTN
 
while True: #loops infinitely

  buttons = wii.state['buttons']
  
  #when the plus and minus buttons are pressed together, it will make the remote vibrate and then break the connection
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    GPIO.cleanup() #turns off all GPIO pins
    exit(wii)

  #if the left button is pressed on the wii remote, the robot turns left
  elif (buttons & cwiid.BTN_LEFT): 
    mc.clockwise(100,1)
    time.sleep(button_delay)
    
  #if the right buttton on the wii remote is pressed, the robot will turn right
  elif(buttons & cwiid.BTN_RIGHT): 
    mc.anticlockwise(100,1)
    time.sleep(button_delay)

  
  #if the forward buttton on the wii remote is pressed, the robot will drive forward by turning on both wheels
  elif (buttons & cwiid.BTN_UP): 
    mc.fwd(100,1)
    time.sleep(button_delay)

  #if the backward buttton on the wii remote is pressed, the robot will drive backward by turning on both wheels  
  elif (buttons & cwiid.BTN_DOWN):
   mc.bwd(100,1)
   time.sleep(button_delay)  
    
  elif (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    time.sleep(button_delay)          

  elif (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    time.sleep(button_delay)          

  elif (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    time.sleep(button_delay)          

  elif (buttons & cwiid.BTN_B):
    time.sleep(button_delay)          

  elif (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
    time.sleep(button_delay)           

  #when the minus button is pressed on the wii remote, the motor speed will decrease by 0.1, slowing the robot down
  elif (buttons & cwiid.BTN_MINUS):
    time.sleep(button_delay)   

  #when the plus button is pressed on the wii remote, the motor speed will increase by 0.1, speeding up the robot
  elif (buttons & cwiid.BTN_PLUS):
    time.sleep(button_delay)

