import tkinter as tk
from tkinter import messagebox

# Function to perform classification based on user input
def perform_classification():
    try:
        # Get user input values
        cylinders = int(cylinders_entry.get())
        displacement = float(displacement_entry.get())
        horsepower = float(horsepower_entry.get())
        weight = float(weight_entry.get())
        acceleration = float(acceleration_entry.get())
        model_year = int(model_year_entry.get())
        
        # Perform classification based on the user input (add your classification logic here)
        # You can use the input values to make predictions using your trained classification model
        
        # Example classification logic (replace with your own)
        if horsepower < 100:
            predicted_category = "Low"
        elif horsepower < 200:
            predicted_category = "Medium"
        else:
            predicted_category = "High"

        # Display the predicted mileage category
        messagebox.showinfo("Prediction Result", f"Predicted Mileage Category: {predicted_category}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for all attributes.")

# Create the main GUI window
window = tk.Tk()
window.title("Mileage Category Predictor")

# Create labels and entry fields for attributes
cylinders_label = tk.Label(window, text="Cylinders:")
cylinders_label.grid(row=0, column=0, padx=10, pady=5)
cylinders_entry = tk.Entry(window)
cylinders_entry.grid(row=0, column=1, padx=10, pady=5)

displacement_label = tk.Label(window, text="Displacement:")
displacement_label.grid(row=1, column=0, padx=10, pady=5)
displacement_entry = tk.Entry(window)
displacement_entry.grid(row=1, column=1, padx=10, pady=5)

horsepower_label = tk.Label(window, text="Horsepower:")
horsepower_label.grid(row=2, column=0, padx=10, pady=5)
horsepower_entry = tk.Entry(window)
horsepower_entry.grid(row=2, column=1, padx=10, pady=5)

weight_label = tk.Label(window, text="Weight:")
weight_label.grid(row=3, column=0, padx=10, pady=5)
weight_entry = tk.Entry(window)
weight_entry.grid(row=3, column=1, padx=10, pady=5)

acceleration_label = tk.Label(window, text="Acceleration:")
acceleration_label.grid(row=4, column=0, padx=10, pady=5)
acceleration_entry = tk.Entry(window)
acceleration_entry.grid(row=4, column=1, padx=10, pady=5)

model_year_label = tk.Label(window, text="Model Year:")
model_year_label.grid(row=5, column=0, padx=10, pady=5)
model_year_entry = tk.Entry(window)
model_year_entry.grid(row=5, column=1, padx=10, pady=5)

# Create a button to perform classification
classify_button = tk.Button(window, text="Classify", command=perform_classification)
classify_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Start the main GUI loop
window.mainloop()
