from tkinter import *
import speedtest
def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10 ** 6), 3)) + " Mbps"

    download_speed_label.config(text=down)
    upload_speed_label.config(text=up)


sp = Tk()
sp.title("Internet Speed")
sp.geometry("500x500")
sp.config(bg="Blue")

title_label = Label(sp, text="Internet Speed", font=("Time New Roman", 25, "bold"), bg="Blue", fg="White")
title_label.place(x=90, y=40, height=30, width=280)

download_label = Label(sp, text="Download Speed", font=("Time New Roman", 20, "bold"))
download_label.place(x=90, y=130, height=30, width=280)

download_speed_label = Label(sp, text="00", font=("Time New Roman", 20, "bold"))
download_speed_label.place(x=90, y=200, height=30, width=280)

upload_label = Label(sp, text="Upload Speed", font=("Time New Roman", 20, "bold"))
upload_label.place(x=90, y=290, height=30, width=280)

upload_speed_label = Label(sp, text="00", font=("Time New Roman", 20, "bold"))
upload_speed_label.place(x=90, y=360, height=30, width=280)

button = Button(sp, text="Check Speed", font=("Time New Roman", 20, "bold"), relief=RAISED, bg="Yellow",
                command=speedcheck)
button.place(x=90, y=430, height=30, width=280)

sp.mainloop()
