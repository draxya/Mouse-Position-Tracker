import tkinter as tk
import pyautogui

def update_mouse_position():
    # Get the current mouse position
    x, y = pyautogui.position()
    
    # Update the label text with the mouse coordinates
    label.config(text=f"Mouse Position: {x}, {y}")
    
    # Schedule the next update after 100 milliseconds
    label.after(100, update_mouse_position)

# Create the GUI window
window = tk.Tk()
window.title("Mouse Tracker")

# Create a label to display the mouse coordinates
label = tk.Label(window, text="Mouse Position: ")
label.pack(padx=10, pady=10)

# Start updating the mouse position
update_mouse_position()

# Run the GUI event loop
window.mainloop()
