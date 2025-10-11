from tkinter import *
import requests

#vybratie informacii z API
def get_quote():
    response = requests.get("https://api.kanye.rest") #nacitanie API
    response.raise_for_status()

    #ziskanie dat
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


#tvorba GUI okna
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

#tvorba platna
canvas = Canvas(width=350, height=470)
background_img = PhotoImage(file="background.png") #obrazok v pozadi
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

#Tvorba kanye tlacidla
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()