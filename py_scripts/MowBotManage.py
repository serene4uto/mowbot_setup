import tkinter as tk
import subprocess
import os
import signal

from time import sleep

class ScriptButton:
    def __init__(self, master, start_script_path, end_script_path, name):
        self.start_script_path = start_script_path
        self.end_script_path = end_script_path
        self.name = name                # Custom name for the script
        self.state = 'Start'            # Initial state of the button

        # Create a frame to hold the label and button side by side
        self.frame = tk.Frame(master)
        self.frame.pack(pady=5)

        # Create and pack the label and button
        self.label = tk.Label(self.frame, text=self.name, width=50, anchor='w')
        self.label.pack(side='left')

        self.button = tk.Button(self.frame, text='Start', width=10, command=self.on_button_click)
        self.button.pack(side='left')

    def on_button_click(self):
        if self.state == 'Start':
            self.start_process()
        else:
            self.terminate_process()

    def start_process(self):
        """Execute the bash script file in a new terminal window."""
        if not os.path.isfile(self.start_script_path):
            print(f"Script file not found: {self.start_script_path}")
            return
    
        # Open a new terminal window and run the script
        subprocess.Popen(
            ['gnome-terminal', '--', '/bin/bash', self.start_script_path],
            preexec_fn=os.setsid
        )
        self.state = 'End'
        self.button.config(text='End')
        print(f"Started script: {self.name}")

    def terminate_process(self):
        """Execute the end script to terminate the process."""
        if not os.path.isfile(self.end_script_path):
            print(f"End script file not found: {self.end_script_path}")
            return

        # Execute the end script
        subprocess.Popen(
            ['/bin/bash', self.end_script_path],
            preexec_fn=os.setsid
        )

        self.button['state'] = 'disabled'
        print("Terminating...")
        sleep(2)
        self.button['state'] = 'normal'
        self.state = 'Start'
        self.button.config(text='Start')
        print(f"Executed end script: {self.name}")

def main():
    root = tk.Tk()
    root.title("AMR MowBot Demo")

    # List of bash scripts with custom names and their file paths
    scripts = [
        {
            'name': 'uRos Agent',
            'start_script_path': '/home/farmbot/mowbot_project/mowbot_setup/scripts/uros-agent.sh',
            'end_script_path': '/home/farmbot/mowbot_project/mowbot_setup/scripts/terminate/end-uros-agent.sh'
        },

        {
            'name': 'AMR Bring Up',
            'start_script_path': '/home/farmbot/mowbot_project/mowbot_setup/scripts/bring-up.sh',
            'end_script_path': '/home/farmbot/mowbot_project/mowbot_setup/scripts/terminate/end-bring-up.sh'
        },

        {
            'name': 'AMR Health Monitor',
            'start_script_path': '/home/farmbot/mowbot_project/mowbot_setup/scripts/amr-health-monitor.sh',
            'end_script_path': '/home/farmbot/mowbot_project/mowbot_setup/scripts/terminate/end-amr-health-monitor.sh'
        },

        {
            'name': 'GPS Waypoint Planner',
            'start_script_path': '/home/farmbot/mowbot_project/mowbot_setup/scripts/gps-wp-planner.sh',
            'end_script_path': '/home/farmbot/mowbot_project/mowbot_setup/scripts/terminate/end-gps-wp-planner.sh'
        },

        {
            'name': 'GPS Waypoint Logger',
            'start_script_path': '/home/farmbot/mowbot_project/mowbot_setup/scripts/gps-wp-logger.sh',
            'end_script_path': '/home/farmbot/mowbot_project/mowbot_setup/scripts/terminate/end-gps-wp-logger.sh'
        },

        {
            'name': 'GPS Waypoint Follower',
            'start_script_path': '/home/farmbot/mowbot_project/mowbot_setup/scripts/gps-wp-follower.sh',
            'end_script_path': '/home/farmbot/mowbot_project/mowbot_setup/scripts/terminate/end-gps-wp-follower.sh'
        }


    ]

    # Create a ScriptButton for each script
    for script_info in scripts:
        ScriptButton(root, script_info['start_script_path'], script_info['end_script_path'], script_info['name'])

    root.mainloop()

if __name__ == "__main__":
    main()
