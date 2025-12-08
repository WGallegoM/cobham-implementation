import customtkinter 

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title("implmentación Cobham")
app.geometry("900x650")

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()