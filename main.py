from tkinter import *
window = Tk()
answer_label = Label(text="0", font=("Arial", 15))
input_box = Entry(width=10)


def configure_window():
    window.title("Mile to Km Converter")
    window.minsize(width=300, height=200)
    window.config(padx=35, pady=50)


def miles_to_km():
    number = float(input_box.get())
    number *= 1.609
    answer_label.config(text=f"{number}", fg="red")


def main():
    configure_window()
    equal_label = Label(text="is equal to", font=("Arial", 15))
    equal_label.grid(column=0, row=1)
    equal_label.config()

    input_box.grid(column=1, row=0)
    answer_label.grid(column=1, row=1)

    calc_button = Button(text="Calculate", command=miles_to_km)
    calc_button.grid(column=1, row=2)

    miles_label = Label(text="Miles", font=("Arial", 15))
    miles_label.grid(column=2, row=0)
    miles_label.config(padx=10)
    km_label = Label(text="Km", font=("Arial", 15))
    km_label.grid(column=2, row=1)

    window.mainloop()


if __name__ == "__main__":
    main()