#/usr/bin/python3

import os
#import hashlib

def ssh_installer():
	os.system("sudo apt install openssh-server")
	os.system("cls")

def save_old_keys():
	os.mkdir("/etc/ssh/old_keys")
	os.system("mv ssh_h* old_keys")

def generate_new_keys():
	os.chdir("/etc/ssh/")
	os.system("dpkg-reconfigure openssh-server")

def key_printer():
	os.system("md5sum /etc/ssh/old_keys/ssh_h*")
	print("-" * 70)
	os.system("md5sum /etc/ssh/ssh_h*")

"""
def key_validator():
	old_keys = []
	new_keys = []
	os.chdir("/etc/ssh")
	for key in os.listdir("old_keys"):
		if key.startswith("ssh_h"):
			generated_hash = hashlib.md5(open(key, 'rb').read()).hexdigest()
			print(generated_hash)
			#old_keys.append(generated_hash)
	
	for new in os.listdir("/etc/ssh"):
		if new.startswith("ssh_h"):
			generated_hash = hashlib.md5(new).hexdigest()
			new_keys.append(generated_hash)
			
	for index, key in enumerate(old_keys):
		print(key, new_keys[index])
"""

if __name__ == "__main__":
	while True:
		try:
			if os.path.isdir("/etc/ssh"):
				if os.path.isdir("/etc/ssh/old_keys"):
					#key_validator()
					key_printer()
					break
				else:
					save_old_keys()
					generate_new_keys()
					continue
			else:
				ssh_installer()
				continue
		except:
			print("Something went wrong... This script is for debian based distros..\n\n")
			print("Checking placement of ssh keys...\n")
			os.system("locate ssh_host_rsa_key")
			break
