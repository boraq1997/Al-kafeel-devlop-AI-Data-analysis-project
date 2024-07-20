import tkinter as tk
from tkinter import PhotoImage

# Create the main tkinter window
root = tk.Tk()
root.title("Button with Image Example")

# Load the image file
image_file = "files/images/a.png"
img = PhotoImage(file=image_file)

# Define a function to be called when the button is clicked
def button_click():
    print("Button clicked!")

# Create a button with text and image
button = tk.Button(root, text="Click Me", image=img, compound=tk.LEFT, command=button_click)
button.pack(padx=10, pady=10)  # Adjust padding as needed

# Run the tkinter main loop
root.mainloop()
