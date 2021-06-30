import os
import random

class SSH_Setup(object):
    def __init__(self):
        self.new_port = random.randrange(1024, 32767)
        self.config_file = "sshd_config"
        self.ssh_dir = "/etc/ssh"
        
    
    def ssh_installer(self):
        os.system("sudo apt install openssh-server")
        os.system("clear")
        print("SSH installed!")
    

    def key_manager(self):
        os.mkdir("/old_keys")
        os.system("mv ssh_h* old_keys")
        print("Old keys moved to new folder..")
        os.system("dpkg-reconfigure openssh-server")
        os.system("clear")
        print("New SSH keys generated!")


    def key_validator(self):
        os.system("clear")
        print("[ - Validate that old and new keys are different - ]\n")
        os.system("md5sum old_keys/ssh_h*")
        print("-" * 70)
        os.system("md5sum ssh_h*")


    def port_changer(self):
        sshd_file = open(self.config_file, "r")
        list_of_lines = sshd_file.readlines()
        list_of_lines[14] = f"Port {self.new_port}\n"
        
        sshd_file = open(self.config_file, "w")
        sshd_file.writelines(list_of_lines)
        sshd_file.close()
        print(f"\nNew SSH port set to {self.new_port}")


if __name__ == "__main__":
    ssh = SSH_Setup()
    while True:
        try:
            if os.path.isdir(ssh.ssh_dir):
                os.chdir(ssh.ssh_dir)
                if os.path.isdir("old_keys"):
                    ssh.key_validator()
                    ssh.port_changer()
                    break
                else:
                    ssh.key_manager()
                    continue
            else:
                ssh.ssh_installer()
                continue
        except:
            os.system("clear")
            print("Something went wrong... This script is for debian based distros..\n\n")
            print("Checking placement of ssh keys...\n")
            os.system("locate ssh_host_rsa_key")
            break
