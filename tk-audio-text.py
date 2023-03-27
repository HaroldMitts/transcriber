import os
import openai
import tkinter as tk
from tkinter import filedialog
import json

# Load API key from keys.json
with open("C:/keys/keys.json", "r") as f:
    keys = json.load(f)
    openai.api_key = keys["openai_api_key"]

def get_masked_api_key(api_key):
    return api_key[:6] + "*" * (len(api_key) - 6)

def show_instructions():
    # First set of instructions
    instructions_1 = """Usage:
    1. Select a folder containing 1 or more .mp3 files, using the "Start" button
    2. From the browse window, select a location and file name for the transcript, then click "Save"
    """

    # Mask the API key
    masked_api_key = get_masked_api_key(openai.api_key)

    # Display the masked API key
    api_key_info = f"\nMy OpenAI API key (partially masked): {masked_api_key}\n"
    
    # Second set of instructions
    instructions_2 = """Additional Information:
    - All .mp3 files in the selected folder will be transcribed using OpenAI Whisper API (Whisper-1).
    - Depending on the size and number of .mp3 files to transcribe, this could take some time.
    
    - If you want to transcribe only a subset of the files, move the files you want to transcribe to a separate folder.
    - The transcript will be saved in a text file with the extension .txt.

    The text file will open automatically when the transcription is complete.

    Important: Make sure you audio file is not larger than 25Mb
    """
    
    # Combine the instructions with a separator in between
    #instructions = instructions_1 + "\n\n" + instructions_2
    
    instructions = instructions_1 + api_key_info + "\n" + instructions_2
    
    # Update the instruction_label widget with the instructions
    instruction_label.config(text=instructions)

def transcribe_files():
    # Ask the user to select a folder containing mp3 files
    mp3_folder_path = filedialog.askdirectory(title="Browse for folder containing .mp3 files")
    if not mp3_folder_path:
        # User cancelled, so exit the function
        return

    # Ask the user to select a save location and file name for the text file
    filetypes = [("Text Files", "*.txt")]
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=filetypes, title="Enter the name of the text file to save the transcript as (without file extension)")
    if not save_path:
        # User cancelled, so exit the function
        return

    mp3_files = [os.path.join(mp3_folder_path, file) for file in os.listdir(mp3_folder_path) if file.endswith(".mp3")]

    with open(save_path, "a") as f:
        for file in mp3_files:
            audio_file = open(file, "rb")
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            f.write(transcript.text + "\n")

    # Open the text file
    os.startfile(save_path)

# Create a tkinter root window
root = tk.Tk()
root.title("Transcribe Audio Files to Text")

# Create a label to display the instructions
instruction_label = tk.Label(root, justify=tk.LEFT, padx=10, pady=10)
instruction_label.pack()

# Load an image
image = tk.PhotoImage(file="tape.sm.png")

# Create a label to display the image
image_label = tk.Label(root, image=image)
image_label.pack()

# Create a button to show the instructions
#show_instructions_button = tk.Button(root, text="Show Instructions", command=show_instructions)
#show_instructions_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.SE)

# Create a button to exit the application
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.SE)

# Create a button to transcribe the audio files
transcribe_button = tk.Button(root, text="Start", command=transcribe_files)
transcribe_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.SE)

# Display the initial instructions
show_instructions()

# Run the tkinter event loop
root.mainloop()
