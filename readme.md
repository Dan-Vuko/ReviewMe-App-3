# Programming Task 3
## _ReviewMe_

The CEO of ReviewMe has requested that the company's business models be expanded by enabling customers to assess restaurants on touchscreen devices after dining there. This is a development of the CEO's suggestion, allowing visitors to rate the following three categories on their own: food, wine, and atmosphere.
\
The application includes a GUI (Graphical User Interface) that asks restaurant patrons to rate the establishment using the aforementioned ratings. There is a range of options, from N/A to 5. Since N/A stands for "Not Assessed," it should not be included to the final result grade. A guest's rating is saved by the application when they submit it in a file called "ratings.txt," which lists all the ratings.


## Features
1) A Easy to use GUI that is a fixed resolution to the tablet aspect ratio.
2) A soft colour pallete that is friendly on the eyes.
3) A 5 place rating system from N/A to "Excellent".
4) Easy portability for touch screen, big buttons which are easy to press.
5) The buttons change colour so the user can see what they've pressed.
6) The user can change their choice.
7) After user submits, the application resets.
8) After submit, the results are printed to "results.txt"




## Tech

ReviewMe relies on a number of open source prerequisites to function:

- [Python](https://www.python.org/) - Python is a high-level, interpreted, general-purpose programming language. 
- [Linux Bash](https://www.linux.org/) - Bash is a Unix shell and command language written by Brian Fox for the GNU Project as a free software replacement for the Bourne shell.

## Installation

ReviewMe requires [Python](https://www.python.org/) v3.10.5 to run.

```sh
tar -zxf pt3.tgz
```

Check Python version & Installation

```sh
Check version
python --version

For windows - Download latest version from the official website: 
https://www.python.org/downloads/

For Centos - use yum:
sudo yum install python3

For Ubuntu - use apt-get:
sudo apt install python3
```

## Running the Program

1) After unpacking and installing the program, once it is running it will take up the full aspect ratio of the tablet. In this window the user will see the name of the restaurant at the top, followed by "Please enter your scores below".
2) Below "Please enter your scores below" the user will see inputs for each of the aspects stipulated: Food, Wine & Atmosphere.
3) The user enters a rating for each of these aspects.
4) The user will then press submit.
5) The program will save the results to "results.txt"
6) The program will reset after displaying a "Thank You" message.


## Improvements to be made
In my opinion, the GUI has to be improved the most. I thought my creativity was missing because I don't have much expertise with the tkinter GUI; I would have preferred to do this project using HTML and CSS with some frameworks like Tailwind or Bootstrap. Even if some of the spacing is somewhat incorrect, I did my best to make it work without utilizing the column structure.
## License

UNE
