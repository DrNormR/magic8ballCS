import tkinter as tk
from PIL import Image, ImageTk
import random
import os

# List of Magic 8-Ball responses
responses = [
    "It is certain", "It is decidedly so", "Without a doubt", "Yes – definitely",
    "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes",
    "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now",
    "Cannot predict now", "Concentrate and ask again", "Don't count on it",
    "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"
]

# Function to display a random response
def get_response(event=None):
    question = question_entry.get().lower()  # Convert to lowercase
    cs_keywords = ["computer science", "cs", "computer sceince","computer scientist","computer","computers"]
    
    if any(keyword in question for keyword in cs_keywords):
        answer = "Yes, definitely, no doubt, 100%. I've never been more sure of anything."
    else:
        answer = random.choice(responses)
    
    if question:
        response_label.config(text=answer)
        root.after(5000, clear_response)  # Schedule the response to disappear after 5 seconds
        question_entry.delete(0, tk.END)  # Clear the question entry box after submission
    else:
        response_label.config(text="Please ask a question.")

# Function to clear the response text
def clear_response():
    response_label.config(text="")


# Set up the main application window
root = tk.Tk()
root.title("Magic 8-Ball")
root.geometry("400x500")
root.config(bg="black")

# Title Label
title_label = tk.Label(root, text="Magic 8-Ball", font=("Helvetica", 24), fg="white", bg="black")
title_label.pack(pady=10)

# Load and Display the Image
try:
    image_path = "magic8ball.png"  # Path to your image
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img = img.resize((150, 150)) #removed , Image.ANTIALIAS
        img = ImageTk.PhotoImage(img)

        img_label = tk.Label(root, image=img, bg="black")
        img_label.image = img
        img_label.pack(pady=10)
    else:
        print(f"Image file not found at {image_path}")
except Exception as e:
    print("Error loading image:", e)

# Question Entry
question_label = tk.Label(root, text="Ask a yes or no question:", font=("Helvetica", 14), fg="white", bg="black")
question_label.pack(pady=5)
question_entry = tk.Entry(root, font=("Helvetica", 14), width=30)
question_entry.pack(pady=10)
question_entry.bind("<Return>", get_response)  # Bind the Enter key to the get_response function

# Response Button
ask_button = tk.Button(root, text="Ask the 8-Ball", font=("Helvetica", 14), command=get_response)
ask_button.pack(pady=10)

# Response Label
response_label = tk.Label(root, text="", font=("Helvetica", 16), fg="cyan", bg="black", wraplength=300)
response_label.pack(pady=20)

# Run the application
root.mainloop()
