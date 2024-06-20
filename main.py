"""
Miles to Km converter using TK inter.
1) allows user to input miles in number
2) click button to submit the number
3) labels used to output the number and provide description
day 27 of 100 days of code
"""
import tkinter as tk


def convert():
    try:
        kilometers = float(miles_in.get()) * 1.609344
        # print(kilometers)
        is_equal_label['text'] = f"is equal to: {round(kilometers, 2)} Km"
    except ValueError:
        is_equal_label['text'] = "ERROR! Use numbers please."


# setting up the window
window = tk.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=120)
window.maxsize(width=300, height=120)
window.config(padx=20 , pady=20)

# first row layout
miles_in = tk.Entry()
miles_in.config(width=20)
miles_in.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0, sticky="NE")

car_emoji = tk.Label(text="🚗")
car_emoji.grid(column=0, row=0, sticky="NW")

# second row layout
is_equal_label = tk.Label(text=f"is equal to: 0 Km")
is_equal_label.grid(column=1, row=1, sticky="EW")

# third row layout
button = tk.Button(text="calculate", command=convert)
button.grid(column=1, row=2, sticky="EW")


# the main loop thing that goes at the bottom of code
# with the 'if name', incase I need to use this as a module later
if __name__ == '__main__':
    window.mainloop()
