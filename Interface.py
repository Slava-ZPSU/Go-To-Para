import tkinter as tk

def submit_form(inputs):
    email = inputs['Email'].get()
    password = inputs['Password'].get()
    link = inputs['Link'].get()

    if email != '' and password != '' and link != '':
        print("Електронна пошта:", email)
        print("Пароль:", password)
        print("Посилання:", link)
    else:
        print('Error input')


class Interface:
    def __init__(self):
        self.__window = tk.Tk()
        self.__window.title("Go To Para")

        self.__window.geometry('460x260')
        self.__window.configure(bg="#828282")

        self.__inputs = {}
        self.__buttons = {}


    def run(self):
        self.__window.mainloop()

    def close_app(self):
        self.__window.quit()

    def add_input(self, label, text=''):
        tk.Label(self.__window, text=label, bg='#828282', fg='#cecece').pack()
        new_input = tk.Entry(self.__window, width=60, justify='center', bg='#5c5c5c', fg='#cecece')
        new_input.insert(0, text)
        new_input.pack()

        self.__inputs[label] = new_input

    def add_button(self, text, on_click):
        new_button = tk.Button(self.__window, text=text, command=lambda: on_click(self.__inputs),  bg='#5c5c5c', fg='#cecece')
        new_button.pack()
        self.__buttons[text] = new_button

if __name__ == "__main__":
    app = Interface()

    app.add_input('Email')
    app.add_input('Password')
    app.add_input('Link')
    app.add_button('submit', submit_form)

    app.run()
