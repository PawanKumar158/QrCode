import tkinter as tk
from tkinter import StringVar

def update_hint():
    selected_option = option.get()
    if selected_option == "text":
        hint_label.config(text="Enter your text here:")
    elif selected_option == "url":
        hint_label.config(text="Enter the URL here:")
    elif selected_option == "social":
        hint_label.config(text="Enter social media handle here:")

# Create the main window
root = tk.Tk()
root.title("Radio Button GUI")

# Define a StringVar to keep track of the selected option
option = StringVar(value="text")

# Create the radio buttons
radio_text = tk.Radiobutton(root, text="Text", variable=option, value="text", command=update_hint)
radio_text.pack(anchor='w')

radio_url = tk.Radiobutton(root, text="URL", variable=option, value="url", command=update_hint)
radio_url.pack(anchor='w')

radio_social = tk.Radiobutton(root, text="Social Media", variable=option, value="social", command=update_hint)
radio_social.pack(anchor='w')

# Create a label to display the hint
hint_label = tk.Label(root, text="Enter your text here:")
hint_label.pack(anchor='w', padx=10, pady=(10, 0))

# Create an input field
input_field = tk.Entry(root)
input_field.pack(fill='x', padx=10, pady=10)

# Start the main loop
root.mainloop()
