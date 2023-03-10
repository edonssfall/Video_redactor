from terminal import *

if __name__ == '__main__':
    # Make terminal cursor
    bash = Cursor()
    # To exit program just send empty command
    while bash.command != "":
        # Move commands
        if bash.command.startswith('cd'):
            # Move to home directory send just "cd"
            if bash.command == 'cd':
                bash.basic_location()
            # Move to folder
            else:
                bash.move()
        # Show list of connected devices
        elif bash.command.startswith('-d'):
            bash.hard_driver_list()
        # Move to connected device
        elif bash.command.startswith('/d'):
            bash.hard_driver_move()
        # Show data of first video
        elif bash.command.startswith('-v'):
            pass
        # Open function for editing, after chosen folder with videos
        elif bash.command.startswith('/v'):
            pass
        # Other bash commands supported by Python_3.10
        else:
            bash.bash_commands()
        # Input command
        bash.command = input(bash)
