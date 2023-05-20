import tkinter
import tkinter.messagebox
import customtkinter

import program
from program import *
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("ТІМС Індивідуальне 2")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="ТІМС\nІндивідуальне завдання 2", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["60%", "70%", "80%", "90%", "100%", "110%", "120%", "130%", "140%", "150%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="хочу 10 балів")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.label_frame1 = customtkinter.CTkFrame(self)
        self.label_frame1.grid(row=0, column=1, padx=(10, 0), pady=(20, 20), sticky="nsew")
        self.labelNormalLaw1 = customtkinter.CTkLabel(master=self.label_frame1, text="Нормальний закон розподілу")
        self.labelNormalLaw1.grid(row=1, column=3, pady=(5, 5), padx=20, sticky="n")
        self.entry1 = customtkinter.CTkEntry(master=self.label_frame1, placeholder_text="Intervals: ")
        self.entry1.grid(row=2, column=3, pady=(5, 5), padx=10, sticky="n")
        self.entry2 = customtkinter.CTkEntry(master=self.label_frame1, placeholder_text="Counts:")
        self.entry2.grid(row=3, column=3, pady=(5, 5), padx=10, sticky="n")
        self.entry_alpha1 = customtkinter.CTkEntry(master=self.label_frame1, placeholder_text="Alpha:")
        self.entry_alpha1.grid(row=4, column=3, pady=(5, 5), padx=10, sticky="n")
        self.entry_a1 = customtkinter.CTkEntry(master=self.label_frame1, placeholder_text="a:")
        self.entry_a1.grid(row=5, column=3, pady=(5, 5), padx=10, sticky="n")
        self.entry_sigma1 = customtkinter.CTkEntry(master=self.label_frame1, placeholder_text="Sigma:")
        self.entry_sigma1.grid(row=6, column=3, pady=(5, 5), padx=10, sticky="n")

        self.label_frame2 = customtkinter.CTkFrame(self)
        self.label_frame2.grid(row=0, column=2, padx=(10, 0), pady=(20, 20), sticky="nsew")
        self.entry3 = customtkinter.CTkLabel(master=self.label_frame2, text="Рівномірний закон розподілу")
        self.entry3.grid(row=1, column=3, pady=5, padx=10, sticky="n")
        self.entry3 = customtkinter.CTkEntry(master=self.label_frame2, placeholder_text="Values:")
        self.entry3.grid(row=2, column=3, pady=5, padx=10, sticky="n")
        self.entry4 = customtkinter.CTkEntry(master=self.label_frame2, placeholder_text="Counts:")
        self.entry4.grid(row=3, column=3, pady=5, padx=10, sticky="n")
        self.entry_alpha2 = customtkinter.CTkEntry(master=self.label_frame2, placeholder_text="Alpha:")
        self.entry_alpha2.grid(row=4, column=3, pady=(5, 5), padx=10, sticky="n")
        self.entry_a2 = customtkinter.CTkEntry(master=self.label_frame2, placeholder_text="a:")
        self.entry_a2.grid(row=5, column=3, pady=(5, 5), padx=10, sticky="n")
        self.entry_b2 = customtkinter.CTkEntry(master=self.label_frame2, placeholder_text="b:")
        self.entry_b2.grid(row=6, column=3, pady=(5, 5), padx=10, sticky="n")

        self.result_frame1 = customtkinter.CTkScrollableFrame(self)
        self.result_frame1.grid(row=2, column=1, columnspan=2, padx=(20, 0), sticky="nsew")

        self.label_result = customtkinter.CTkLabel(master=self.result_frame1, text="Тут з’явиться результат, коли ви натиснете 'Обчислити'")
        self.label_result.grid(row=1, column=1, padx=20, pady=(20, 20), sticky="n")

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=2, column=3, padx=(20, 20), pady=(0, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Виберіть закон для перевірки:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="nsew")

        self.law = customtkinter.IntVar()
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.law, value=0, text="H0 - нормальний закон розподілу")
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.law, value=1, text="H0 - рівномірний закон розподілу")
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        self.main_button_1 = customtkinter.CTkButton(self.radiobutton_frame, command=lambda: self.update_label(self.law.get()), text="Обчислити")
        self.main_button_1.grid(row=3, column=2, padx=10, pady=20)

        # create scrollable frame
        self.main_button_1 = customtkinter.CTkButton(self, text="Показати гістограму", command=lambda: self.show_plt(self.law.get()))
        self.main_button_1.grid(row=0, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    def update_label(self, law_number):
        if law_number == 0:
            intervals = [(float(x.split('-')[0]), float(x.split('-')[1])) for x in self.entry1.get().split(', ')] if len(self.entry1.get()) != 0 else []
            counts = [int(x) for x in self.entry2.get().split(', ')] if len(self.entry2.get()) != 0 else []

            alpha = float(self.entry_alpha1.get()) if len(self.entry_alpha1.get()) != 0 else -1
            a = float(self.entry_a1.get()) if len(self.entry_a1.get()) != 0 else -1
            sigma = float(self.entry_sigma1.get()) if len(self.entry_sigma1.get()) != 0 else -1

            self.label_result.configure(text=normalLaw(intervals, counts, a, sigma, alpha))

        elif law_number == 1:
            numbers = [int(x) for x in self.entry3.get().split(', ')] if len(self.entry3.get()) != 0 else []
            counts = [int(x) for x in self.entry4.get().split(', ')] if len(self.entry4.get()) != 0 else []

            alpha = float(self.entry_alpha2.get()) if len(self.entry_alpha2.get()) != 0 else 0.05
            a = float(self.entry_a2.get()) if len(self.entry_a2.get()) != 0 else -1
            b = float(self.entry_b2.get()) if len(self.entry_b2.get()) != 0 else -1

            self.label_result.configure(text=evenLaw(numbers, counts, a, b, alpha))
    def show_plt(self, law_number):
        if law_number == 0:
            intervals = [(float(x.split('-')[0]), float(x.split('-')[1])) for x in self.entry1.get().split(', ')]
            counts = [int(x) for x in self.entry2.get().split(', ')]
            show_plot_normal(intervals, counts)
        elif law_number == 1:
            numbers = [int(x) for x in self.entry3.get().split(', ')]
            counts = [int(x) for x in self.entry4.get().split(', ')]
            show_plot_even(numbers, counts)


if __name__ == "__main__":
    app = App()
    app.mainloop()