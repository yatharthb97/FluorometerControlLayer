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
			

