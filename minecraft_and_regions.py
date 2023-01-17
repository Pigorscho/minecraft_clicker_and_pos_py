import pyautogui, clipboard, pyttsx3, os
from time import sleep, strftime
from pynput import keyboard
from datetime import datetime

pyautogui.FAILSAFE = False

engine = pyttsx3.init()
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)

hotkeyvar = None

def say(content):
	engine.say(content)
	engine.runAndWait()
	pass

def hotkey(shortcut):
	global hotkeyvar
	if(hotkeyvar == str(shortcut)):
		hotkeyvar = None
		return True

def on_activate_r():
	global hotkeyvar
	hotkeyvar = "ctrl + r"

def on_activate_i():
	global hotkeyvar
	hotkeyvar = "ctrl + i"

def on_activate_o():
	global hotkeyvar
	hotkeyvar = "ctrl + o"

def on_activate_p():
	global hotkeyvar
	hotkeyvar = "ctrl + p"

def on_activate_m():
	global hotkeyvar
	hotkeyvar = "ctrl + m"

def on_activate_k():
	global hotkeyvar
	hotkeyvar = "ctrl + k"






hotlistener =  keyboard.GlobalHotKeys({
		'<ctrl>+r': on_activate_r,
		'<ctrl>+i': on_activate_i,
		'<ctrl>+o': on_activate_o,
		'<ctrl>+p': on_activate_p,
		'<ctrl>+m': on_activate_m,
		'<ctrl>+k': on_activate_k},
)
hotlistener.start()






def position():
	if(hotkey('ctrl + p')):
		x,y = pyautogui.position()
		x,y = str(x), str(y)
		comma = " ,"
		pos = x + comma + y
		clipboard.copy(pos)
		print(pos)
		say("Position captured!")

def region():
	if(hotkey('ctrl + r')):
		x,y = pyautogui.position()
		x,y = str(x), str(y)
		comma = ", "
		minus = " - "
		pos = x + comma + y
		say("Move to second point now, press o for OK!")
		pausing = True
		while(pausing == True):
			sleep(.5)
			if(hotkey('ctrl + o')):
				pausing = False
		x2,y2 = pyautogui.position()
		x2,y2 = str(x2), str(y2)
		pos2 = x2 + comma + y2
		
		xz = x2 + minus + x
		yz = y2 + minus + y
		region = pos + comma + xz + comma + yz
		clipboard.copy(region)
		print(region)
		say("Region captured!")

def imageandregion():
	if(hotkey('ctrl + i')):
		x,y = pyautogui.position()
		say("Move to second point now, press o for OK!")
		pausing = True
		while(pausing == True):
			sleep(.5)
			if(hotkey('ctrl + o')):
				pausing = False
		x2,y2 = pyautogui.position()
		pic = pyautogui.screenshot(region=(x,y,x2-x,y2-y))
		path = rf"C:\Users\Lennart\PycharmProjects\pos_py_pics\{str(datetime.now()).replace(':', '')}.png"
		pic.save(path)
		pic.close()
		x -= 25
		y -= 25
		x2 += 25
		y2 += 25
		comma = ", "
		minus = " - "
		x,y = str(x), str(y)
		pos = x + comma + y
		x2,y2 = str(x2), str(y2)
		pos2 = x2 + comma + y2
		xz = x2 + minus + x
		yz = y2 + minus + y
		region = pos + comma + xz + comma + yz
		clipboard.copy(region)
		print(region)
		with open(path.replace('png', 'txt'), 'w') as file:
			file.write(region)
		say("Image and region captured!")



def minecraftclickerraid():
	if(hotkey('ctrl + m')):
		say("Minecraft Raid Farm Clicker activated")
		while True:
			pyautogui.mouseDown(button='left')
			print('pressing button down..')
			sleep(1.5)
			pyautogui.mouseUp(button='left')
			print('lifting button up..')
			sleep(.05)
			if (hotkey('ctrl + k')):
				say("using the force to quit loop")
				quit()

print("running...")


while True:
	position()
	region()
	imageandregion()
	minecraftclickerraid()
	sleep(.5)
