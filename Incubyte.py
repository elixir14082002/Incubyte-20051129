#!/usr/bin/env python
# coding: utf-8

# # Incubyte Test

# ### Problem Statement

# In[ ]:


## Chandrayaan 3 Lunar Craft: Galactic Space Craft Control


# ## Description

# In[ ]:


"""As a scientist at ISRO controlling the latest lunar spacecraft Chandrayaan 3, 
your task is to develop a program that translates commands sent from Earth into instructions 
understood by the spacecraft. The spacecraft navigates through the galaxy using galactic coordinates, 
represented by x, y, z coordinates (x for east or west location, y for north or south location, 
and z for distance above or below the galactic plane)."""


# In[6]:


def move_spacecraft(command, initial_dir, initial_cord):
    # List of possible horizontal directions
    hor_dir = ['N', 'E', 'S', 'W']
    
    # Initialize the current direction and its index
    direction = initial_dir
    initih = hor_dir.index(direction)
    
    # Initialize the vertical direction
    initiv = ''

    # Loop through each command in the sequence
    for i in command:
        if i == 'r':
            # Update the horizontal direction to the right
            initih = (initih + 1 + 4) % 4
            direction = hor_dir[initih]
        elif i == 'l':
            # Update the horizontal direction to the left
            initih = (initih - 1 + 4) % 4
            direction = hor_dir[initih]
        elif i == 'u' and initiv != 'U':
            # Update the direction to face upward
            direction = initiv = 'U'
        elif i == 'd' and initiv != 'D':
            # Update the direction to face downward
            direction = initiv = 'D'
        elif i == 'f' or i == 'b':
            # Calculate the delta based on the command
            delta = -1 if i == 'b' else 1
            
            # Update the spacecraft coordinates based on the direction
            if direction == 'N':
                initial_cord[1] += delta
            elif direction == 'S':
                initial_cord[1] -= delta
            elif direction == 'E':
                initial_cord[0] += delta
            elif direction == 'W':
                initial_cord[0] -= delta
            elif direction == 'U':
                initial_cord[2] += delta
            elif direction == 'D':
                initial_cord[2] -= delta
                
        # Print the current command, direction, and coordinates
        print(i, direction, initial_cord)

# Example usage
command = 'frubl'
initial_dir = 'N'
initial_cord = [0, 0, 0]
move_spacecraft(command, initial_dir, initial_cord)


# In[7]:


def determine_final_direction(initial_dir, commands):
    # List of possible horizontal directions
    hor_dir = ['N', 'E', 'S', 'W']
    
    # Initialize the current direction and its index
    direction = initial_dir
    initih = hor_dir.index(direction)
    
    # Initialize the vertical direction
    initiv = ''

    # Loop through each command in the sequence
    for cmd in commands:
        if cmd == 'r':
            # Update the horizontal direction to the right
            initih = (initih + 1) % 4
            direction = hor_dir[initih]
        elif cmd == 'l':
            # Update the horizontal direction to the left
            initih = (initih - 1) % 4
            direction = hor_dir[initih]
        elif cmd == 'u' and initiv != 'U':
            # Update the direction to face upward
            direction = initiv = 'U'
        elif cmd == 'd' and initiv != 'D':
            # Update the direction to face downward
            direction = initiv = 'D'

    return direction

def main():
    # Get the initial direction from user input
    initial_direction = input("Enter the initial direction (N/E/S/W): ").upper()
    
    # Validate the initial direction
    if initial_direction not in ['N', 'E', 'S', 'W']:
        print("Invalid initial direction.")
        return
    
    # Get the sequence of commands from user input
    commands = input("Enter the sequence of commands: ")
    
    # Determine the final direction based on the initial direction and commands
    final_direction = determine_final_direction(initial_direction, commands)
    
    # Print the final direction
    print("Final Direction:", final_direction)

if __name__ == "__main__":
    main()


# In[ ]:




