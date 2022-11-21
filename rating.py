## REVIEWME! ##

# BUG:
# Buttons could be improved.


from tkinter import * # Importing the required modules
import tkinter as tk # Importing tkinter as tk is the same as importing tkinter and then using tk = tkinter, so you can use tk instead of tkinter

window = tk.Tk() # Initializes the window

window.geometry("800x600") # Set the window geometry to 800x600, this is the size of the window, the window is 800 pixels wide and 600 pixels high, optimised for Tablets.
window.configure(bg = "#FFFFFF") # background = White Hex Code
window.resizable(0,0) # Makes the window NOT resizable

restaurant_name = "Baba's Kitchen" # Set Restaurant Name to Variable so it can be changed according to the Restaurant.

canvas = Canvas( # Creates a canvas
    window, # The canvas is inside of the window
    bg = "#C5F9D7", # background = Green Hex Code
    height = 600, # 
    width = 800,
    bd = 0, # border = 0
    highlightthickness = 0, # This is the thickness of the border around the canvas, 0 means no border.
    relief = "ridge" # Ridge is the border style, it means the border is raised.
)

canvas.place(x = 0, y = 0) # 0 x and 0 y means that the canvas is placed at the top left corner of the window.

hero = canvas.create_rectangle( # This is colour of the background of the of the header
    800, # This is the width
    117, # This is the height
    0, # This is the x position
    0, # This is the y position
    fill = "#F27A7D", # This is the colour of the background of the header
    outline = "") # IF outline = "" then there is no border.


heading = canvas.create_text( # This is the heading text
    400.0, # X position
    50.0, #  Y position
    # Insert restaurant name variable in text.
    text = restaurant_name, # Variable for Restaurant Name
    fill = "#FFFFFF", # Colour: White
    font = ("Roboto", int(36.0)), 
)

# The syntax order is the same as the above. 
subheading = canvas.create_text( # This is the subheading text
    400.0,
    100.0,
    text = "Please enter your scores below!",
    fill = "#FFFFFF",
    font = ("Roboto", int(18.0))
)

# ""
food_score_heading = canvas.create_text( # Food Score Heading
    400.0,
    135.0,
    text = "Please enter rating for Food!",
    fill = "#000000",
    font = ("Roboto", int(16.0))
)

# ""
wine_score_heading = canvas.create_text( # Wine Score Heading
    400.0,
    290.0,
    text = "Please enter rating for Wine!",
    fill = "#000000",
    font = ("Roboto", int(16.0))
)
# ""
atmosphere_score_heading = canvas.create_text( # Atmosphere Score Heading
    400.0,
    445.0,
    text = "Please enter rating for Atmosphere!",
    fill = "#000000",
    font = ("Roboto", int(16.0))
)



food_intvar = tk.StringVar() # This tk.StringVar is used to store the value of the radio button clicked.
wine_intvar = tk.StringVar() 
atmosphere_intvar = tk.StringVar()


def Food_Radio_Buttons(): # This is the function for the Food Radio Buttons
    Food_Rating = (('N/A', "N/A"), ('Bad', 2), ('Good', 3), ('Great', 4), ('Excellent', 5)) # This is the list of the Food Ratings
    for i, (text, value) in enumerate(Food_Rating): # This is a for loop, it loops through the list of Food Ratings.

        # Thoughts:

        # Enumerate in this instance is used to get the index of the list, so it can be used to place the buttons.
        # I only recently started learning about enumerate when it comes to understanding lists, dictionaries and tuples.
        # After watching a video on YouTube, I decided to use enumerate in this instance.
        # I have also compiled an Anki deck of all the things to do with sets, lists, tuples and dictionaries.
        # There is a good medium article called 60 Questions to test your knowledge of Python Lists, Tuples, Sets and Dictionaries.
        # I have learnt a lot from this article, and I have compiled an Anki deck of all the questions and answers this last week.
        # So I was really happy that I remembered to use enumerate in this instance.

        tk.Radiobutton( # This is the Radio Button that is created for each item in the list.
            window, text = text, variable = food_intvar, value = value, # This is the text, variable and value of the Radio Button.
            bg = "#C5F9D7", indicator = 0, activebackground = "#f7d486", # This is the background colour, indicator and active background colour.
            # indicator = 0 means that there is no indicator.
            activeforeground = "#000000", selectcolor="#f7d486", border = 0, # The activeforeground is the colour of the text when the button is clicked.
            # selectcolor is the colour of the button when it is highlighted.
            command = lambda: print(food_intvar.get()) # This lambda function prints the value of the variable when the button is clicked.
            # I used this to check if the button was working.
        ).place(x = i*160, y = 150, width = 160, height = 80) # Positional Arguments

# I wont explain the code for the Atmosphere or Wine Radio Buttons as it is the same as the Food Radio Buttons just changing the subject specific terminology.

def Wine_Radio_Buttons():
    Wine_Rating = (('N/A', "N/A"), ('Bad', 2), ('Good', 3), ('Great', 4), ('Excellent', 5))
    for i, (text, value) in enumerate(Wine_Rating):
        tk.Radiobutton(
            window, text = text, variable = wine_intvar, value = value,
            bg = "#C5F9D7", indicator = 0, activebackground = "#f7d486",
            activeforeground = "#000000", selectcolor="#f7d486", border = 0,
            command = lambda: print(wine_intvar.get())
        ).place(x = i*160, y = 305, width = 160, height = 80)


def Atmosphere_Radio_Buttons():
    Atmosphere_Rating = (('N/A', "N/A"), ('Bad', 2), ('Good', 3), ('Great', 4), ('Excellent', 5))
    for i, (text, value) in enumerate(Atmosphere_Rating):
        tk.Radiobutton(
            window, text = text, variable = atmosphere_intvar, value = value,
            bg = "#C5F9D7", indicator = 0, activebackground = "#f7d486",
            activeforeground = "#000000", selectcolor="#f7d486", border = 0,
            command = lambda: print(atmosphere_intvar.get())
        ).place(x = i*160, y = 460, width = 160, height = 80)


def results(): # Results
    results_window = tk.Toplevel() # Assigns the results window to a variable
    results_window.geometry("400x100+{}+{}".format(int(window.winfo_x() + window.winfo_width()/2 - 200), int(window.winfo_y() + window.winfo_height()/2 - 50)))

    # Thoughts:
    # This is the geometry of the results window, it is 400x100 and it is placed in the middle of the main window.
    # I got the idea from here: https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter

    # (Not sure if posting sources for code inspiration is a bad idea, but I am not copying the code, I am just using it as a reference and showing how I came to use this 
    # complex line)

    results_window.title("Thank You") # This is the title of the results window.
    results_window.configure(bg = "#C5F9D7") # This is the background colour of the results window.
    results_window.resizable(False, False) # NOT RESIZABLE
    tk.Label(results_window, text = "Thank you for your feedback!", bg = "#C5F9D7", fg = "#000000", font = ("Roboto", int(18.0))).pack(pady = 30)
    # This is the label that is placed in the results window.
    # pady = 10 is the padding on the y axis, it is placed at the end of the pack method because it is a positional argument.
    with open ("results.txt", "a") as results_file: # This opens the results.txt file in append mode.
        results_file.write("{},{}:{}\n".format(restaurant_name, "food", food_intvar.get())) 
        # This writes the restaurant name, food and the value of the food_intvar to the results.txt file.
        results_file.write("{},{}:{}\n".format(restaurant_name, "wine", wine_intvar.get()))
        results_file.write("{},{}:{}\n".format(restaurant_name, "atmosphere", atmosphere_intvar.get()))

        # Thoughts:
        # I have been reading a book called Python One-Liners by David Beazley and Brian K. Jones.
        # The book is a bit advanced for me, but I have learnt a lot from it.
        # It talks a lot about comprehensions. I find them to be useful, albeit hard to understand at first.
        # But I think that the logic flows well and it's easy to read, it's just hard to write off the top of your head without
        # mapping it out the long way first, which is what I originally did.
        # Also that medium article I mentioned earlier, it has a lot of comprehensions in it that I am trying to commit to memory.

        results_file.write("\n") # This is used to add a new line to the results.txt file to avoid confusion.
        results_file.close() # This closes the results.txt file.

    food_intvar.set(0) # This sets the value of the food_intvar to 0 to reset the radio buttons.
    wine_intvar.set(0)
    atmosphere_intvar.set(0)

    # For some reason, this was one of the hardest parts for me to figure out, I originally had this in a separate function, but it didn't work.
    # After a lot of trial and error, I managed to get it working.
    # It's funny how sometimes the simplest things are the hardest to figure out.


submit_button = tk.Button( # Submit
    window, # The window that button is placed in.
    text = "Submit",
    bg = "#F27A7D",
    fg = "#FFFFFF",
    activebackground = "#FFFFFF",
    activeforeground = "#F27A7D",
    border = 0,
    # close window and open results window
    command = results
    # explain command = results in detail:
    # command = results means that when the button is clicked, the results function is called.  
)


submit_button.place( # Place the submit button
    x = 640.0,
    y = 550.0,
    width = 150.0,
    height = 40.0
)


def main(): # Main
    while True: # This is a while loop.
        try:
            Food_Radio_Buttons() # This calls the Food_Radio_Buttons function.
            Wine_Radio_Buttons() # This calls the Wine_Radio_Buttons function.
            Atmosphere_Radio_Buttons() # This calls the Atmosphere_Radio_Buttons function.
            submit_button.config(command = results) # This configures the submit button to call the results function when it is clicked.
            window.mainloop() # This is the mainloop of the main window.
        except: # except without a specific error means that it will catch any error.
            break # This breaks the while loop.

if __name__ == "__main__": # General Protocal for Python, this will only run if the file is run directly.
    main() # This calls the main function.



