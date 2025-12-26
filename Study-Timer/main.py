import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from pydub import AudioSegment
from pydub.playback import play

# Create Main Window
root = tk.Tk()
root.attributes('-topmost', True)
root.title("Simple Timer")

# Load Sound File
sound = AudioSegment.from_file('/Users/work/Desktop/Python Projects/Projects-Easy.Mode/Study-Timer/finished-sound.mp3')

# Load GIF Frames
gif_file = '/Users/work/Desktop/Python Projects/Projects-Easy.Mode/Study-Timer/raccoon.gif'
gif_frames = [tk.PhotoImage(file=gif_file, format='gif - {}'.format(i)) for i in range(10)]  # Adjust as needed
gif_index = 0

# Set up GIF label
gif_label = tk.Label(root)
gif_label.pack()

def update_gif():
    global gif_index
    # Update frame index
    gif_index = (gif_index + 1) % len(gif_frames)
    gif_label.config(image=gif_frames[gif_index])
    root.after(100, update_gif)  # Update every 100 ms


# Define Timer Function
def start_timer(duration):
    global timer_running
    timer_running = True
    update_gif()
     
    def countdown(remaining):

        if not timer_running:  # If timer is stopped
            return
        
        mins, secs = divmod(remaining, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timer)

         # Update progress bar
        progress_bar['value'] = duration - remaining
        
        # Modify the color and size of the label based on remaining time
        if remaining > duration / 2:
            label.config(fg='purple', font=('Helvetica', 48))
        elif remaining > 10:  # When less than half time, switch to yellow
            label.config(fg='pink', font=('Helvetica', 48))
        else:  # When less than 10 seconds, switch to red
            label.config(fg='turquoise', font=('Helvetica', 48, 'bold'))

        
        if remaining > 0:
            # Update the timer every second
            root.after(1000, countdown, remaining - 1)
        else:
            label.config(text="You did it :D")
            play(sound)

    countdown(duration)


def end_timer():
    global timer_running
    timer_running = False
    label.config(text="All Done??")


# Label Timer Display
label = tk.Label(root, text="Enter study time in minutes:")
label.pack()

# User Input Duration
entry = tk.Entry(root)
entry.pack()


# Start Button
button = tk.Button(root, text="Start Studying", command=lambda: start_timer(int(entry.get()) * 60))
button.pack()

# End Button
end_button = tk.Button(root, text="Stop Studying", command=end_timer)
end_button.pack()

# Progress Bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)


# Configure Style for Progress Bar
style = ttk.Style()
style.theme_use('default')  # Use the default theme
style.configure("TProgressbar",
                troughcolor='white',  # Background color of the bar
                background='purple')        # Color of the filled portion


# Run App
root.mainloop()
