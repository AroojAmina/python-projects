from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def Change(text="type", src="English", dest="Urdu"):
    text1 = text
    src1 = src
    dest1 = dest

    trans = Translator()
    trans1= trans.translate(text, src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = sor_txt.get(1.0,END)
    textget = Change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg="pink")

# Main title
lab_txt = Label(root, text="Translator", font=("time new roman", "30", "bold"), bg="yellow")
lab_txt.place(x= 100, y= 40, height= 50, width= 300)

# Frame for holding widgets
frame = Frame(root, bg="pink")
frame.pack(side=BOTTOM)

# Source text label
lab_source = Label(root, text="Source Text", font=("time new roman", "20", "bold"), bg="green")
lab_source.place(x=10, y=100, height=20, width=200)

# Source text box
sor_txt = Text(root, font=("time new roman", "10", "italic"), wrap=WORD)
sor_txt.place(x=25, y=140, height=150, width=450)

# Source language combo box
list_text = list(LANGUAGES.values())
comb_sor = ttk.Combobox(root, values=list_text)
comb_sor.place(x=10, y=300, height=30, width=150)
comb_sor.set("English")

# Translate button
button_change = Button(root, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=300, height=30, width=150)

# Destination language combo box
comb_dest = ttk.Combobox(root, values=list_text)
comb_dest.place(x=340, y=300, height=30, width=150)
comb_dest.set("English")

lab_txt = Label(root, text="dest text", font=("time new roman", "30", "bold"), bg="pink")
lab_txt.place(x= 100, y= 350, height= 40, width= 300)

dest_txt = Text(root, font=("time new roman", "10", "italic"), wrap=WORD)
dest_txt.place(x=25, y=400, height=150, width=450)


root.mainloop()