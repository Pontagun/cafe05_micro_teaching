import tkinter as tk

# Initialize the main GUI window
root = tk.Tk()
root.title("Cafe 5 Graphic")
root.geometry("500x300")
root.configure(bg="#111111")  # Dark coffee brown background

# Create a container frame to center the text
frame = tk.Frame(root, bg="#2C1B18")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Main graphical text label
cafe_label = tk.Label(
    frame, 
    text="Cafe 5", 
    font=("Georgia", 56, "bold italic"), 
    fg="#F5E6CA",  # Warm cream/latte color
    bg="#2C1B18"
)
cafe_label.pack()

# A decorative sub-label for a nicer graphical look
subtitle_label = tk.Label(
    frame, 
    text="☕ Freshly Brewed Code ☕", 
    font=("Arial", 12), 
    fg="#A98467",  # Soft roasted bean color
    bg="#2C1B18"
)
subtitle_label.pack(pady=15)

# Run the graphical loop
root.mainloop()
