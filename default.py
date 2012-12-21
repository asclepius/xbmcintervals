import xbmc, xbmcgui
import time
import threading
import os


start = time.clock()

WINDOW_FULLSCREEN_VIDEO = 12005
WINDOW_OSD = 12901
IMAGE_PATH=xbmc.translatePath('special://home/addons/script.intervaltrainer/bike_banner.png')

dialog = xbmcgui.Dialog()
WORKOUT=xbmc.translatePath(dialog.browse(1,'Workout selection','files','',False,False,'special://home/addons/script.intervaltrainer/workouts/test'))
workout_file=open(WORKOUT)

window = xbmcgui.Window(WINDOW_FULLSCREEN_VIDEO)


# Set up the labels
timer_label = xbmcgui.ControlLabel( window.getWidth() - 50, 0, 300, 100, 'Timer', 'font30_title', alignment=0x5)
details_label = xbmcgui.ControlLabel( 100, 0, window.getWidth() - 300, 100, '', 'font30_title', alignment=0x4)
image = xbmcgui.ControlImage(0, 0, 1500, 100, IMAGE_PATH)

# Add the control to the FullScreenVideo window
#image.setAnimations([('Visible', 'effect=fade time="1000"')])

window.show()
window.addControl(image)
#image.setAnimations([('visible', 'effect=fade start=0 end=100 time=500'), ('hidden', 'effect=fade start=0 end=100 time=500',)])
#image.setAnimations([('Conditional', 'effect=fade time=500 condition=Control.IsVisible(%d)' % image.getId()),('Conditional', 'effect=fade time=500 condition="!Control.IsVisible(%d)"' % image.getId())])
window.addControl(timer_label)
window.addControl(details_label)

if xbmc.Player().isPlayingVideo():
  for line in workout_file:
    line_split = line.split()
    interval_time = float(line_split[0])
    rpe = line_split[1]
    hr_zone = "(RPE %s)" % (rpe)
    details = ' '.join(line_split[2:])
    details_label.setLabel(details + ' ' + hr_zone)
    start = time.time()
    now = start
    while now - start <= interval_time and xbmc.Player().isPlayingVideo(): 
        time_remaining = interval_time - now + start
        timer = time.strftime("%H:%M:%S", time.gmtime(time_remaining))
        timer_label.setLabel(timer)
        now = time.time()
        time.sleep(1)

try:
  window.removeControl(timer_label)
  window.removeControl(image)
  #window.removeControl(progress)
  window.removeControl(details_label)
except:
  None


