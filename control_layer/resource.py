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
    try:
        float(string)
        return True
    except ValueError:
        return False

def extract_conc(string, no_samples):

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
	path = os.path.join(desktop, "Fluorometer.lnk")

	if not os.path.exists(path):
		print("[WARNING] Creating missing desktop shortcut named `Fluorometer`.")
		cd = os.getcwd()
		print(cd)
		target = r"python.exe ./run.py"
		wDir = f"{cd}"
		icon = os.path.join(cd, "control_layer", "icon.png")
		
		shell = Dispatch('WScript.Shell')
		shortcut = shell.CreateShortCut(path)
		shortcut.Targetpath = target
		shortcut.WorkingDirectory = wDir
		shortcut.IconLocation = icon
		shortcut.save()