# openspace_organizer
BeCode_Challenge_1

## Description
Your company moved to a new office at the Gent Zuiderport. Its an openspace with 6 tables of 4 seats. 
As many of you are new colleagues, you come up with the idea of changing seats every day and get to know each other better by working side by side with your new colleagues.

You will create a program that runs every day to re-assign everybody to a new seat.

## Usage


1. Open Visual Studio Code
2. Select file > open folder > "01-openspace-organizer" > click Select Folder
3. Locate the `main.py` file.
3. Run `main.py` by double-clicking it or using the command `python main.py` in your terminal or command prompt.
4. Follow the on-screen instructions to view the seating arrangement for the day.
5. Optionally, you can modify the seating arrangement logic or customize the program to suit your needs.

## Visuals

## Contributors
BeCode class 

## Timeline
This project was created in two days. 

## Personal situation
My first solo project @ BeCode 

### Mission objectives

Create an algorithm that randomly assign people to a spot in the open space.
In an open space with 6 tables of 4 seats. come up with the idea of changing seats every day and get to know each other better by working side by side with your new colleagues.
Create a program that runs every day to re-assign everybody to a new seat.
You want to build a program that allows you to get a list of colleagues from an excel file and place them randomly on the different tables of the open space.


### Learning Objectives

- Make a good usage of classes.
- Use Object-Oriented-Programming (OOP).
- Use imports in a clean way.
- Use a clean architecture.
- Read data from a csv file
- Structure a project.
- Integrate versioning and project management
  - split functionalities into tasks
  - develop functionalities on proper branch
  - use PR to merge branches

## The Mission

Your company moved to a new office at the Gent Zuiderport. It’s an open space with 6 tables of 4 seats. 
As many of you are new colleagues, you come up with the idea of changing seats every day and get to know each other better by working side by side with your new colleagues.

You will create a program that runs every day to re-assign everybody to a new seat. 

### Must-have features: MVP (Minimum Viable Product)

You want to build a program that allows you to get a list of colleagues from an excel file and place them ***randomly*** on the different tables of the open space.

#### Note: The default setup of the open space is 6 tables of 4 seats → 24 seats. ####

- The program can take a file path as an argument to load the list of colleagues. 
- The program distributes randomly the people on the existing tables and says how much seats are left.
- The program can deal with the possibility of having to much people in the room.

### Nice-to-have features: Only when MVP is achieved!

Now you have a basic working program but you want to make it more interactive and more configurable.

- Allow the possibility to define the room setup from a config.json file. Allow the possibility to change dynamically the setup and re-run the program.
- Make the program more dynamic and interactive by adding the possibility to add someone in the room (a new colleague arriving or someone being late) and the possibility to add a table if the room is full.
- Improve the algorithm to avoid having someone alone at a table
- Allow the possibility of which list (or black list) in the excel file → _X wants to be seated beside Y_ or _X doesn't want to be seated beside Y_
- Allow the possibility to ask : 
  - how much seats are in the room
  - how much people are in the room
  - how much seats are left
