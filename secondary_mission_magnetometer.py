from sense_hat import SenseHat
import time
import datetime

sense = SenseHat()
sense.clear()

back_gd = [0,100,0]
back_gd_red = [100,0,0]
p = [0, 0, 0] # blank
w = [255, 255, 255] # white
b = [0, 0, 200] # blue
image_esa = [
  		p,p,b,b,b,b,p,p,
  		p,b,b,b,b,b,b,p,
  		b,b,b,b,w,w,w,b,
  		b,w,b,b,w,b,w,b,
  		b,b,b,b,w,w,w,b,
  		b,b,b,b,w,b,b,b,
  		p,b,b,b,b,w,w,p,
  		p,p,b,b,b,b,p,p,
  		]
str_time = time.strftime("%I:%M:%S")
sense.show_message(str_time)
sense.set_pixels(image_esa)
log = open('log_magnetic_field.csv','w')
log.write('Time\tAxis z microTeslas\tAxis y microTeslas\tAxis z microTeslas\n')
initial_date = datetime.datetime.now()
final_date = initial_date + datetime.timedelta(seconds=6600)


while datetime.datetime.now() < final_date: 
    sense.set_imu_config(True, False, False)
    raw = sense.get_compass_raw()
    msg2 = "starting the capture state" 
    t = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    sense.show_message(msg2, scroll_speed=0.05, back_colour=back_gd_red)
    axis_x = ('{x}'.format(**raw))
    axis_y = ('{y}'.format(**raw))
    axis_z = ('{z}'.format(**raw))
    data = '{0}\t{1}\t{2}\t{3}\n'.format(t,round(float(axis_x),1),round(float(axis_y),1),round(float(axis_z),1))	
    print data
    log.write(data) 
    msg1 = "next measure in one minute"
    sense.show_message(msg1, scroll_speed=0.05, back_colour=back_gd)
    sense.set_pixels(image_esa)
    time.sleep(60) #next measure in 60 seconds

log.close()    
    
    
 
    
    
	

  
