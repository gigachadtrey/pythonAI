import tkinter as tk
from tkinter import ttk
import google.generativeai as genai

# Replace with your actual API key
API_KEY = "AIzaSyBtaKEQYOgKNLHoKbnh_TUTA6oyQSJvlpg"

# Initialize the model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def send_message():
  user_input = entry.get()
  entry.delete(0, tk.END)  # Clear the entry field after sending

  # Generate response from Gemini
  response = model.generate_content(user_input)
  chat_history.insert(tk.END, f"You: {user_input}\n")  # Add newline after "You" message
  chat_history.insert(tk.END, f"Gemini: {response.text}")
  chat_history.see(tk.END)  # Scroll to the latest message


# Create the main window
root = tk.Tk()
root.title("Chat with Gemini")

# Create the chat history display
chat_history = tk.Text(root, width=50, height=15)
chat_history.pack()

# Create the user input entry field
entry = tk.Entry(root, width=50)
entry.pack()

# Create the send button
send_button = ttk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()