
# The code and readme are all generated using gpt4. 
# So this may not work at all. I am just trying to get a feel for how it works.


# Building a Chatbot with OpenAI's ChatGPT API.

import os
import tkinter as tk
import openai
import PyPDF2

# Set OpenAI API key.
# openai.api_key = "<your_api_key>" 
openai.api_key = os.getenv("OPENAI_API_KEY") 

def read_file_contents(filepath: str) -> str:
    if filepath.endswith(".pdf"):
        with open(filepath, "rb") as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text = " ".join([pdf_reader.getPage(i).extractText() for i in range(pdf_reader.numPages)])
    else:
        with open(filepath, "r") as file:
            text = file.read()
    return text


# Send message to ChatGPT API and return the response
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-codex-002",
        prompt=prompt,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text.strip()
    return message


# Concatenate user message and ChatGPT response
def send_message():
    user_input = entry.get()
    chat_history.insert(tk.END, f"User: {user_input}\n")
    entry.delete(0, tk.END)

    response = generate_response(user_input)
    chat_history.insert(tk.END, f"ChatGPT: {response}\n")


# Set up tkinter GUI
root = tk.Tk()
root.title("ChatGPT App")

frame = tk.Frame(root)
scrollbar = tk.Scrollbar(frame)
chat_history = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_history.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frame.pack(fill=tk.BOTH, expand=True)

entry = tk.Entry(root)
entry.bind("<Return>", lambda event: send_message())
entry.pack(fill=tk.X)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

# Function to import files and display contents
def import_and_display_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("All Files", "*"), ("Text Files", "*.txt"), ("PDF Files", "*.pdf"), ("Markdown Files", "*.md"), ("R Files", "*.r")]
    )
    file_contents = read_file_contents(file_path)
    chat_history.insert(tk.END, f"File Contents: {file_contents}\n")


# Import file button
import_button = tk.Button(root, text="Import File", command=import_and_display_file)
import_button.pack(side=tk.LEFT)

root.mainloop()