import xbmc, xbmcgui
import time
import threading
import os


start = time.clock()

WINDOW_FULLSCREEN_VIDEO = 12005
IMAGE_PATH=xbmc.translatePath('special://home/addons/script.helloworld/bike_banner.png')
HEART_PATH=xbmc.translatePath('special://home/addons/script.helloworld/heart.png')
WORKOUT=xbmc.translatePath('special://home/addons/script.helloworld/angels')

window = xbmcgui.Window(WINDOW_FULLSCREEN_VIDEO)

window.show()

# Set up the labels
#alert_label = xbmcgui.ControlLabel( window.getWidth()/2, window.getHeight()/2, 0, 0, 'Hello, world!', 'WeatherTemp', alignment=0x6 )
timer_label = xbmcgui.ControlLabel( window.getWidth() - 50, 0, 300, 100, 'Timer', 'font30_title', alignment=0x5)
details_label = xbmcgui.ControlLabel( 100, 0, window.getWidth() - 300, 100, '', 'font30_title', alignment=0x4)
image = xbmcgui.ControlImage(0, 0, 1500, 100, IMAGE_PATH)
#heart = xbmcgui.ControlImage(0, 0, 50, 50, HEART_PATH)
#heart_rate = xbmcgui.ControlLabel(0,0,100,50,'', 'font30_title', alignment=0x6)

# Add the control to the FullScreenVideo window
#alert_control = window.addControl(alert_label)
#image.setAnimations([('visible', 'effect=fade time="500"',), ('hidden', 'effect=fade time="500"',)])
image_control = window.addControl(image)
#heart_control = window.addControl(heart)
#heart_rate_control =window.addControl(heart_rate)
timer_control = window.addControl(timer_label)
details_control = window.addControl(details_label)


for line in open(WORKOUT):
  line_split = line.split()
  interval_time = float(line_split[0])
  rpe = line_split[1]
  hr_zone = "(RPE %s)" % (rpe)
  details = ' '.join(line_split[2:])
  details_label.setLabel(details + ' ' + hr_zone)
  #heart_rate.setLabel(hr_zone)
  start = time.time()
  now = start
  while now - start <= interval_time:
    time_remaining = interval_time - now + start
    timer = time.strftime("%H:%M:%S", time.gmtime(time_remaining))
    timer_label.setLabel(timer)
    now = time.time()
    time.sleep(1)

    


#alert_label.setLabel('')

window.removeControl(timer_label)
window.removeControl(image)
window.removeControl(details_label)
#window.removeControl(heart)
#window.removeControl(heart_rate)

