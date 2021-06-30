#!/usr/bin/python3
import random


file_path = r"/path/to/sshd_config"

def port_changer():
	new_port = random.randrange(1024, 32767)
	sshd_file = open(file_path, "r")
	list_of_lines = sshd_file.readlines()
	list_of_lines[14] = f"Port {new_port}\n"
	
	sshd_file = open(file_path, "w")
	sshd_file.writelines(list_of_lines)
	sshd_file.close()
	return print(f"New SSH port set to {new_port}")

port_changer()
