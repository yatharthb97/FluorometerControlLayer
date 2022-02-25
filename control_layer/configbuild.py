# -*- coding: utf-8 -*-


"""
Builds and checks the configuration file required for the fluorimeter operation.
"""

import os
import json

def check_config():
	"""
	Checks for configuration files within the current working directory.
	"""

	# Extract all files within the folder
	file_list = [file for file in os.listdir(".") if file.endswith(".json")]
	file_list = [file for file in file_list if "config" in file]
	file_list = sorted(file_list)

	if not file_list:
		return None

	else:
		return file_list[0]

"""
Default configuration options.
"""
default_config = {
					"Port" : "COM7",
					"Baud" : 9600,
					"Sampling Delay ms" : 100,
					"Save Directory" : ".",
					"Header Lines" : 7,
					"Data Seperator" : '\t',
					"Print Data" : bool(True),
					"Export Config to MetaData" : bool(True),
					"Plot Points" : 200
				 }

default_autoconfig_name = "autogenerated_config.json"

def generate_config():
	"""
	Generates a configuration file with default configuration options.
	"""
	with open(default_autoconfig_name, 'w') as file:
		j_config = json.dumps(default_config, indent=4)
		file.write(j_config)
	print(f"Configuration file generated → `{default_autoconfig_name}`.")


def fill_missing(filename):
	"""
	Fill missing configuration options.
	"""
	update_state = False
	with open(filename, 'r') as f:
		config = json.load(f)
	
	# Unknown keys
	for key in config:
		if not key in default_config:
			print(f"[Warning] Unrecognised configuration: {key} : {config[key]}")

	# Missing keys
	for key in default_config:
		if not key in config:
			config[key] = default_config[key] #Add
			print(f"[Warning] Configuration : Missing field added -> `{key}: {config[key]}` .")
			update_state = True



	if update_state == True:
		j_config = json.dumps(config, indent=4)
		with open(filename, 'w') as file:
			file.write(j_config)


def config_load_operations():
	"""
	All configuration operations clubbed into one function.
	"""
	conf = check_config()
	if conf == None:
		print("[ERROR] No configuration file was found in the current directory.")
		generate_config()
		conf = default_autoconfig_name

	config_file = os.path.abspath(conf)
	fill_missing(config_file)
	config = None
	with open(config_file, 'r') as configF:
		config = json.load(configF)
	return config