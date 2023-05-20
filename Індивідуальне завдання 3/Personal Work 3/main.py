import customtkinter
from program import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.title("ТІМС ІНДИВІДУАЛЬНЕ 3")
        self.geometry(f"{1100}x{610}")

        # configure weights
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=0)


        # left sidebar
        self.left_sidebar_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.left_sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.left_sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="ТІМС \nІндивідуальне 3",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # appearance mode
        self.appearance_mode_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="Appearance Mode:",
                                                            anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=10, pady=(10, 10))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.left_sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=10, pady=10)

        # scaling
        self.scaling_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=10, pady=(10, 10))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.left_sidebar_frame,
                                                               values=["60%", "70%", "80%", "90%", "100%",
                                                                       "110%", "120%", "130%", "140%", "150%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=10, pady=(10, 10))

        # right sidebar
        self.right_sidebar_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.right_sidebar_frame.grid(row=0, column=4, rowspan=4, sticky="nsew")
        self.right_sidebar_frame.grid_rowconfigure(5, weight=1)


        # correlation frame
        self.law_frame = customtkinter.CTkFrame(self.right_sidebar_frame)
        self.law_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="new")

        self.stats_label = customtkinter.CTkLabel(self.law_frame, text="Кореляція:", font=("Times", 24), justify='center')
        self.stats_label.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="new")

        self.law = customtkinter.IntVar()
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.law_frame, font=("Times", 24), variable=self.law, value=0, text="Гіперболічна")
        self.radio_button_1.grid(row=1, column=1, pady=10, padx=20, sticky="w")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.law_frame, font=("Times", 24), variable=self.law, value=1, text="Коренева")
        self.radio_button_2.grid(row=2, column=1, pady=10, padx=20, sticky="w")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.law_frame, font=("Times", 24), variable=self.law, value=2, text="Показникова")
        self.radio_button_3.grid(row=3, column=1, pady=10, padx=20, sticky="w")
        self.radio_button_4 = customtkinter.CTkRadioButton(master=self.law_frame, font=("Times", 24), variable=self.law, value=3, text="Параболічна")
        self.radio_button_4.grid(row=4, column=1, pady=10, padx=20, sticky="w")




        self.mark_frame = customtkinter.CTkFrame(self.right_sidebar_frame)
        self.mark_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="new")

        self.mark_label = customtkinter.CTkLabel(self.mark_frame, text="Оцінка", font=("Times", 24), justify='center')
        self.mark_label.grid(row=0, column=0, columnspan=3, padx=(10, 0), pady=(10, 0))

        self.mark_label1 = customtkinter.CTkButton(self.mark_frame, text="1", font=("Times", 24), width=50, command=self.is_clicked)
        self.mark_label1.grid(row=1, column=0, padx=(10, 0), pady=(10, 0))
        self.mark_label2 = customtkinter.CTkButton(self.mark_frame, text="2", font=("Times", 24), width=50, command=self.is_clicked)
        self.mark_label2.grid(row=1, column=1, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.mark_label3 = customtkinter.CTkButton(self.mark_frame, text="3", font=("Times", 24), width=50, command=self.is_clicked)
        self.mark_label3.grid(row=1, column=2, padx=(10), pady=(10, 0), sticky="nsew")
        self.mark_label4 = customtkinter.CTkButton(self.mark_frame, text="4", font=("Times", 24), width=50, command=self.is_clicked)
        self.mark_label4.grid(row=2, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.mark_label5 = customtkinter.CTkButton(self.mark_frame, text="5", font=("Times", 24), width=50, command=self.is_clicked)
        self.mark_label5.grid(row=2, column=1, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.mark_label6 = customtkinter.CTkButton(self.mark_frame, text="6", font=("Times", 24), width=50, command=self.is_clicked)
        self.mark_label6.grid(row=2, column=2, padx=10, pady=(10, 0), sticky="nsew")
        self.mark_label7 = customtkinter.CTkButton(self.mark_frame, text="7", font=("Times", 24), width=50, command=self.is_clicked)
        self.mark_label7.grid(row=3, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.mark_label8 = customtkinter.CTkButton(self.mark_frame, text="8", font=("Times", 24), width=50, command=self.is_clicked)
        self.mark_label8.grid(row=3, column=1, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.mark_label9 = customtkinter.CTkButton(self.mark_frame, text="9", font=("Times", 24), width=50, command=self.is_clicked)
        self.mark_label9.grid(row=3, column=2, padx=10, pady=(10, 0), sticky="nsew")
        self.mark_label10 = customtkinter.CTkButton(self.mark_frame, text="10", font=("Times", 24), width=50, command=self.is_clicked)
        self.mark_label10.grid(row=4, column=1, padx=(10, 0), pady=(10, 10), sticky="nsew")


        self.mark_label1.bind("<Enter>", self.on_enter1)
        self.mark_label1.bind("<Leave>", self.on_leave1)
        self.mark_label2.bind("<Enter>", self.on_enter2)
        self.mark_label2.bind("<Leave>", self.on_leave2)
        self.mark_label3.bind("<Enter>", self.on_enter3)
        self.mark_label3.bind("<Leave>", self.on_leave3)
        self.mark_label4.bind("<Enter>", self.on_enter4)
        self.mark_label4.bind("<Leave>", self.on_leave4)
        self.mark_label5.bind("<Enter>", self.on_enter5)
        self.mark_label5.bind("<Leave>", self.on_leave5)
        self.mark_label6.bind("<Enter>", self.on_enter6)
        self.mark_label6.bind("<Leave>", self.on_leave6)
        self.mark_label7.bind("<Enter>", self.on_enter7)
        self.mark_label7.bind("<Leave>", self.on_leave7)
        self.mark_label8.bind("<Enter>", self.on_enter8)
        self.mark_label8.bind("<Leave>", self.on_leave8)
        self.mark_label9.bind("<Enter>", self.on_enter9)
        self.mark_label9.bind("<Leave>", self.on_leave9)

        self.thank_you = False
        self.thanks_frame = customtkinter.CTkFrame(self.right_sidebar_frame)
        self.thanks_frame.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="new")

        self.thanks_label = customtkinter.CTkLabel(self.thanks_frame, text="", font=("Times", 24), justify='center')
        self.thanks_label.grid(row=0, column=0, padx=(10, 0), pady=(10, 10))

        # upper frame

        self.matrix_frame = customtkinter.CTkFrame(self)
        self.matrix_frame.grid(row=0, column=1, columnspan=1, padx=10, pady=10, sticky="nsew")

        self.matrix_frame.columnconfigure(0, weight=2)
        self.matrix_frame.rowconfigure(0, weight=0)
        self.matrix_frame.rowconfigure(1, weight=2)

        self.matrix_label = customtkinter.CTkLabel(self.matrix_frame, text="Введіть матрицю", font=("Times", 24), justify='center')
        self.matrix_label.grid(row=0, column=0, padx=10, pady=10)

        self.matrix_entry = customtkinter.CTkTextbox(self.matrix_frame)
        self.matrix_entry.grid(row=1, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")


        # y_i frame
        self.y_i_frame = customtkinter.CTkScrollableFrame(self)
        self.y_i_frame.grid(row=0, column=2, padx=(0, 10), pady=10, sticky="nsew")

        self.y_i_frame.columnconfigure(0, weight=2)
        self.y_i_frame.rowconfigure(0, weight=0)
        self.y_i_frame.rowconfigure(1, weight=2)

        self.y_i_name_label = customtkinter.CTkLabel(self.y_i_frame, text="Yi", font=("Times", 24), justify='center')
        self.y_i_name_label.grid(row=0, column=0)

        self.y_i_label = customtkinter.CTkLabel(self.y_i_frame, text="", font=("Times", 24), justify='center')
        self.y_i_label.grid(row=1, column=0)


        # output frame


        self.function_frame = customtkinter.CTkFrame(self)
        self.function_frame.grid(row=2, column=1, rowspan=1, padx=10, pady=(10, 0), sticky="nsew")


        self.function_frame.columnconfigure(0, weight=2)
        self.function_frame.rowconfigure(0, weight=0)
        self.function_frame.rowconfigure(1, weight=2)

        self.function_name_label = customtkinter.CTkLabel(self.function_frame, text="Функція", font=("Times", 24), justify='center')
        self.function_name_label.grid(row=0, column=0, padx=10, sticky="nsew")

        self.function_label = customtkinter.CTkLabel(self.function_frame, text="", font=("Times", 24))
        self.function_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


        # system frame
        self.system_frame = customtkinter.CTkFrame(self)
        self.system_frame.grid(row=1, column=1, columnspan=2, padx=(10, 10), pady=0, sticky="nsew")

        self.system_frame.columnconfigure(0, weight=2)
        self.system_frame.rowconfigure(0, weight=0)
        self.system_frame.rowconfigure(1, weight=2)

        self.system_name_label = customtkinter.CTkLabel(self.system_frame, text="Система рівнянь", font=("Times", 24), justify='center')
        self.system_name_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.system_label = customtkinter.CTkLabel(self.system_frame, text="", font=("Times", 18))
        self.system_label.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10))


        # sigma delta frame
        self.sigma_delta_frame = customtkinter.CTkFrame(self)
        self.sigma_delta_frame.grid(row=2, column=2, padx=(0, 10), pady=(10, 0), sticky="nsew")


        self.sigma_name_label = customtkinter.CTkLabel(self.sigma_delta_frame, text="sigma: ", font=("Times", 24))
        self.sigma_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.sigma_label = customtkinter.CTkLabel(self.sigma_delta_frame, text="", font=("Times", 24))
        self.sigma_label.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


        self.delta_name_label = customtkinter.CTkLabel(self.sigma_delta_frame, text="delta: ", font=("Times", 24))
        self.delta_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.delta_label = customtkinter.CTkLabel(self.sigma_delta_frame, text="", font=("Times", 24))
        self.delta_label.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.sigma_delta_frame.columnconfigure(0, weight=2)
        self.sigma_delta_frame.columnconfigure(1, weight=2)
        self.sigma_delta_frame.rowconfigure(1, weight=2)

        # show plot button
        self.show_plot_button = customtkinter.CTkButton(self.sigma_delta_frame, text="Показати графік", command=self.show_plot, font=("Times", 24))
        self.show_plot_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


        # calculate_button
        self.calculate_button = customtkinter.CTkButton(self, text="Calculate", command=self.calculate, font=("Times", 24))
        self.calculate_button.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        self.path = "var17.txt"

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def calculate(self):
        dict = solve_some_law(functions[self.law.get()], self.path)

        check_if_txt = self.matrix_entry.get("end-5c", "end-1c")

        if len(self.matrix_entry.get("1.0", "end-1c")) == 0:
            dict = solve_some_law(functions[self.law.get()], "var17.txt")
        elif check_if_txt == ".txt":
            self.path = self.matrix_entry.get("1.0", "end-1c")
            dict = solve_some_law(functions[self.law.get()], self.path)
        else:
            lines = parse_from_text_box(self.matrix_entry.get("1.0", "end-1c"))
            lines = [i + "\n" for i in lines]
            with open("custom_matrix.txt", "w") as f:
                for i in lines:
                    f.write(i)
                f.close()

            self.path = "custom_matrix.txt"
            dict = solve_some_law(functions[self.law.get()], "custom_matrix.txt")


        self.sigma_label.configure(text=dict["sigma"])
        self.delta_label.configure(text=dict["delta"])
        self.system_label.configure(text=dict["system"])
        self.y_i_label.configure(text=dict["y_i_str"])
        self.function_label.configure(text=dict["function"])

    def show_plot(self):
        dict = solve_some_law(functions[self.law.get()], self.path)
        draw_plot(dict["x_i"], dict["y_i"], dict["arr_x"], dict["arr_y"])

    def on_enter1(self, event):
        self.mark_label1.configure(text="10")
    def on_enter2(self, event):
        self.mark_label2.configure(text="10")
    def on_enter3(self, event):
        self.mark_label3.configure(text="10")
    def on_enter4(self, event):
        self.mark_label4.configure(text="10")
    def on_enter5(self, event):
        self.mark_label5.configure(text="10")
    def on_enter6(self, event):
        self.mark_label6.configure(text="10")
    def on_enter7(self, event):
        self.mark_label7.configure(text="10")
    def on_enter8(self, event):
        self.mark_label8.configure(text="10")
    def on_enter9(self, event):
        self.mark_label9.configure(text="10")

    def on_leave1(self, event):
        self.mark_label1.configure(text="1")
    def on_leave2(self, event):
        self.mark_label2.configure(text="2")
    def on_leave3(self, event):
        self.mark_label3.configure(text="3")
    def on_leave4(self, event):
        self.mark_label4.configure(text="4")
    def on_leave5(self, event):
        self.mark_label5.configure(text="5")
    def on_leave6(self, event):
        self.mark_label6.configure(text="6")
    def on_leave7(self, event):
        self.mark_label7.configure(text="7")
    def on_leave8(self, event):
        self.mark_label8.configure(text="8")
    def on_leave9(self, event):
        self.mark_label9.configure(text="9")


    def is_clicked(self):
        self.thank_you = True
        self.thanks_label.configure(text="Дякую!")







if __name__ == "__main__":
    app = App()
    app.mainloop()