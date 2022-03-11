# -*- coding: utf-8 -*-


def header():

	print(f'''
	KG Lab
	
	███████╗██╗     ██╗   ██╗ ██████╗ ██████╗ ██╗███╗   ███╗███████╗████████╗███████╗██████╗     
	██╔════╝██║     ██║   ██║██╔═══██╗██╔══██╗██║████╗ ████║██╔════╝╚══██╔══╝██╔════╝██╔══██╗    
	█████╗  ██║     ██║   ██║██║   ██║██████╔╝██║██╔████╔██║█████╗     ██║   █████╗  ██████╔╝    
	██╔══╝  ██║     ██║   ██║██║   ██║██╔══██╗██║██║╚██╔╝██║██╔══╝     ██║   ██╔══╝  ██╔══██╗    
	██║     ███████╗╚██████╔╝╚██████╔╝██║  ██║██║██║ ╚═╝ ██║███████╗   ██║   ███████╗██║  ██║    
	╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    
	(2022)                                                                                             
	''')


def is_number(string):
	"""
	Checks if the given string is a `float` or an `int`. 
	`string.isnumeric()` only works for integers.
	"""
	try:
		float(string)
		return True
	except ValueError:
		return False

def extract_conc(string, no_samples):
	"""
	Extract concentrations from a string entered by the user.
	"""
	string = string.replace(" ", "") #Clean Spaces
	string = string.replace('\n', "") #Clean any endline
	splitted = string.split(',')
	length = len(splitted)
	if(length < no_samples):
		splitted.extend(["#"]*(no_samples-length))
	return splitted[:no_samples]
			

def create_shortcut():
	import os, winshell
	from win32com.client import Dispatch

	desktop = winshell.desktop()
	path = os.path.join(desktop, "Media Player Classic.lnk")
	target = r"P:\Media\Media Player Classic\mplayerc.exe"
	wDir = r"P:\Media\Media Player Classic"
	icon = r"P:\Media\Media Player Classic\mplayerc.exe"
	shell = Dispatch('WScript.Shell')
	shortcut = shell.CreateShortCut(path)
	shortcut.Targetpath = target
	shortcut.WorkingDirectory = wDir
	shortcut.IconLocation = icon
	shortcut.save()

	
	return

	desktop = winshell.desktop()
	path = os.path.join(desktop, "Fluorometer.lnk")

	if not os.path.exists(path):
		print("[WARNING] Creating missing desktop shortcut named `Fluorometer.lnk`.")
		cd = os.getcwd()
		print(cd)
		target = r'wt --title "KG Lab Fluorometer" powershell -c python -i  run.py'
		wDir = f"{cd}"
		icon = os.path.join(cd, "control_layer", "icon.png")
		
		shell = Dispatch('WScript.Shell')
		shortcut = shell.CreateShortCut(path)
		shortcut.Targetpath = target
		shortcut.WorkingDirectory = wDir
		shortcut.IconLocation = icon
		shortcut.save()


class WakeLock:
	from wakepy import set_keepawake, unset_keepawake
	"""
	RAII wrapper around `wakepy` API. Creation of this objects instructs 
	the Operating system not to put itaself to sleep while the process runs.
	"""

	def __init__(keep_screen_awake=False):
		"""
		Constructor - create and aquire lock.
		"""
		set_keepawake(keep_screen_awake=keep_screen_awake)
		print("[WakeLock] Sleep prevent lock has been set.")

	def __del__():
		"""
		Destructor - Release lock.
		"""
		print("[WakeLock] Sleep prevent lock has been unset.")
		unset_keepawake()
