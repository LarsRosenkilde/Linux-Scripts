import os
import random

class SSH_Setup(object):
    	
ssh_location = "/etc/ssh"


def ssh_installer():
	os.system("sudo apt install openssh-server")
	os.system("cls")


def key_manager():
	os.mkdir(f"{ssh_location}/old_keys")
	os.system("mv ssh_h* old_keys")
	os.chdir("/etc/ssh/")
	os.system("dpkg-reconfigure openssh-server")


def key_printer():
	os.system("md5sum /etc/ssh/old_keys/ssh_h*")
	print("-" * 70)
	os.system("md5sum /etc/ssh/ssh_h*")


def port_changer():
    new_port = random.randrange(1024, 32767)
	sshd_file = open(file_path, "r")
	list_of_lines = sshd_file.readlines()
	list_of_lines[14] = f"Port {new_port}\n"
	
	sshd_file = open(file_path, "w")
	sshd_file.writelines(list_of_lines)
	sshd_file.close()
	return print(f"New SSH port set to {new_port}")


if __name__ == "__main__":
	while True:
		try:
			if os.path.isdir(ssh_location):
    			os.chdir(ssh_location)
				if os.path.isdir("/etc/ssh/old_keys"):
					#key_validator()
					key_printer()
					break
				else:
					key_manager()
					continue
			else:
				ssh_installer()
				continue
		except:
			print("Something went wrong... This script is for debian based distros..\n\n")
			print("Checking placement of ssh keys...\n")
			os.system("locate ssh_host_rsa_key")
			break




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