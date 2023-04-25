# Version: 1.0.3
# This code version includes a new function called update_timer that updates the `timer_label
import cv2
import numpy as np
import pyautogui
from win32api import GetSystemMetrics
import time
import tkinter as tk
from tkinter import messagebox

# Define function to start recording
def start_recording():
    # Access screen width:
    w = GetSystemMetrics(0)
    # Access screen height:
    h = GetSystemMetrics(1)
    # Store screen dimensions within a tuple:
    dimension = (w, h)
    # Define codec -> FourCC is a 4-byte code used to specify the video codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # VideoWriter -> This class provides C++ API for writing video files or image sequences
    # Constructor parameters-> video filename, video codec, video frame-rate(fps), screen dimensions

    # Change these settings to suit your output preferences ie: File Name and Output Directory
    output = cv2.VideoWriter("recordings/recording.mp4", fourcc, 20.0, dimension)

    # Access current system time:
    now = time.time()
    # Read screen recording duration via user input:
    # time() -> Returns the time as a floating point number expressed in seconds
    duration = int(duration_entry.get())
    # Buffer time to ensure that the recorded video duration is as specified by user:
    # This is done because, code must be executed up till line #33, prior to recording initiation.
    duration += duration
    # Identify the time at which recording must stop:
    end_time = now + duration

    # Update timer label every second
    def update_timer():
        current_time = time.time()
        remaining_time = int(end_time - current_time)
        timer_label.config(text=f"Recording duration: {remaining_time} seconds")
        if current_time >= end_time:
            # Stop recording
            output.release()
            timer_label.config(text="Screen recording completed")
            messagebox.showinfo("Success", "Screen recording completed successfully.")
            return
        else:
            root.after(1000, update_timer)

    # Update timer label
    update_timer()

    while True:
        # Take a screenshot:
        # screenshot() -> Returns an Image object
        img = pyautogui.screenshot()
        # Import image data into NumPy array:
        frame = np.array(img)
        # Use cvtColor() method to convert image from BGR to RGB color format:
        # This conversion ensures that the recording exactly resembles the content that had been recorded
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Write the frame into the file 'recording.mp4':
        output.write(frame)
        # Access current system time:
        current_time = time.time()
        # Check if it is time to stop recording. If so, break out of while loop.
        if current_time>end_time:
            break

    # Release the capture
    output.release()

# Create tkinter GUI
root = tk.Tk()
root.geometry("400x200") # Set dimensions of GUI window
root.title("Screen Recorder")

# Create label and entry for duration input
duration_label = tk.Label(root, text="Specify recording duration in seconds:")
duration_label.pack()
duration_entry = tk.Entry(root)
duration_entry.pack()

# Create label for timer
timer_label = tk.Label(root, text="")
timer_label.pack()

# Create button to start recording
start_button = tk.Button(root, text="Start Recording", command=start_recording)
start_button.pack()

root.mainloop()



# Version: 1.0.2
# import cv2
# import numpy as np
# import pyautogui
# from win32api import GetSystemMetrics
# import time
# import tkinter as tk
# from tkinter import messagebox

# # Define function to start recording
# def start_recording():
#     # Access screen width:
#     w = GetSystemMetrics(0)
#     # Access screen height:
#     h = GetSystemMetrics(1)
#     # Store screen dimensions within a tuple:
#     dimension = (w, h)
#     # Define codec -> FourCC is a 4-byte code used to specify the video codec
#     fourcc = cv2.VideoWriter_fourcc(*"XVID")
#     # VideoWriter -> This class provides C++ API for writing video files or image sequences
#     # Constructor parameters-> video filename, video codec, video frame-rate(fps), screen dimensions

#     # Change these settings to suit your output preferences ie: File Name and Output Directory
#     output = cv2.VideoWriter("recordings/recording.mp4", fourcc, 20.0, dimension)

#     # Access current system time:
#     now = time.time()
#     # Read screen recording duration via user input:
#     # time() -> Returns the time as a floating point number expressed in seconds
#     duration = int(duration_entry.get())
#     # Buffer time to ensure that the recorded video duration is as specified by user:
#     # This is done because, code must be executed up till line #33, prior to recording initiation.
#     duration += duration
#     # Identify the time at which recording must stop:
#     end_time = now + duration

#     while True:
#         # Take a screenshot:
#         # screenshot() -> Returns an Image object
#         img = pyautogui.screenshot()
#         # Import image data into NumPy array:
#         frame = np.array(img)
#         # Use cvtColor() method to convert image from BGR to RGB color format:
#         # This conversion ensures that the recording exactly resembles the content that had been recorded
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         # Write the frame into the file 'recording.mp4':
#         output.write(frame)
#         # Access current system time:
#         current_time = time.time()
#         # Check if it is time to stop recording. If so, break out of while loop.
#         if current_time>end_time:
#             break

#     # Release the capture
#     output.release()
#     messagebox.showinfo("Success", "Screen recording completed successfully.")


# # Create tkinter GUI
# root = tk.Tk()
# root.geometry("400x150") # Set dimensions of GUI window
# root.title("Screen Recorder")

# # Create label and entry for duration input
# duration_label = tk.Label(root, text="Specify recording duration in seconds:")
# duration_label.pack()
# duration_entry = tk.Entry(root)
# duration_entry.pack()

# # Create button to start recording
# start_button = tk.Button(root, text="Start Recording", command=start_recording)
# start_button.pack()

# root.mainloop()






# Version: 1.0.1
# import tkinter as tk
# from tkinter import messagebox
# import cv2
# import numpy as np
# import pyautogui
# from win32api import GetSystemMetrics
# import time

# # Create the GUI
# root = tk.Tk()
# root.title("Screen Recorder")

# # Access screen width and height
# w = GetSystemMetrics(0)
# h = GetSystemMetrics(1)
# dimension = (w, h)

# # Define codec
# fourcc = cv2.VideoWriter_fourcc(*"XVID")

# # Define video output settings
# output = cv2.VideoWriter("recording.mp4", fourcc, 20.0, dimension)

# # Define recording duration
# duration = 10

# # Define recording end time
# end_time = time.time() + duration

# # Define function to start recording
# def start_recording():
#     global end_time
#     end_time = time.time() + duration
#     while True:
#         # Take a screenshot
#         img = pyautogui.screenshot()
#         # Convert image to NumPy array
#         frame = np.array(img)
#         # Convert color format from BGR to RGB
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         # Write the frame to the output file
#         output.write(frame)
#         # Check if it is time to stop recording
#         if time.time() >= end_time:
#             stop_recording()
#             break

# # Define function to stop recording
# def stop_recording():
#     # Release the video writer
#     output.release()
#     # Display a message box
#     messagebox.showinfo("Screen Recorder", "Recording complete!")

# # Create the GUI elements
# label = tk.Label(root, text="Click the button to start recording.")
# label.pack()

# button = tk.Button(root, text="Record", command=start_recording)
# button.pack()

# # Run the GUI
# root.mainloop()





# Version: 1.0
# import cv2
# import numpy as np
# import pyautogui
# from win32api import GetSystemMetrics
# import time

# # Access screen width:
# w = GetSystemMetrics(0)
# # Access screen height:
# h = GetSystemMetrics(1)
# # Store screen dimensions within a tuple:
# dimension = (w, h)
# # Define codec -> FourCC is a 4-byte code used to specify the video codec
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# # VideoWriter -> This class provides C++ API for writing video files or image sequences
# # Constructor parameters-> video filename, video codec, video frame-rate(fps), screen dimensions

# # Change these settings to suit your output preferences ie: File Name and Output Directory
# output = cv2.VideoWriter("recordings/recording.mp4", fourcc, 20.0, dimension)

# # Access current system time:
# now = time.time()
# # Read screen recording duration via user input:
# # time() -> Returns the time as a floating point number expressed in seconds
# duration = int(input('Specify recording duration in seconds: '))
# # Buffer time to ensure that the recorded video duration is as specified by user:
# # This is done because, code must be executed up till line #33, prior to recording initiation.
# duration += duration
# # Identify the time at which recording must stop:
# end_time = now + duration

# while True:
#     # Take a screenshot:
#     # screenshot() -> Returns an Image object
#     img = pyautogui.screenshot()
#     # Import image data into NumPy array:
#     frame = np.array(img)
#     # Use cvtColor() method to convert image from BGR to RGB color format:
#     # This conversion ensures that the recording exactly resembles the content that had been recorded
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     # Write the frame into the file 'recording.mp4':
#     output.write(frame)
#     # Access current system time:
#     current_time = time.time()
#     # Check if it is time to stop recording. If so, break out of while loop.
#     if current_time>end_time:
#         break

# # Release the capture
# output.release()