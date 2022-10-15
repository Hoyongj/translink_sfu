import tkinter as tk
import translink_sfu
from PIL import Image, ImageTk

# START tkinter
root= tk.Tk()
root.title("SFU VAN-BUR TRAVEL")
root.geometry("720x480")
root.resizable(False,False)

# ADD bg image
bg_bur = ImageTk.PhotoImage(Image.open("map_bur.png")) # IMAGE FROM GOOGLE MAP
bg_van = ImageTk.PhotoImage(Image.open("map_van.png")) # IMAGE FROM GOOGLE MAP
bg_image = tk.Label(root, image = bg_bur)
bg_image.place(x=0, y=0)

# BUTTON with TXT
van_to_bur = True
def change_direction():
    global van_to_bur
    if van_to_bur: 
        van_to_bur = False
        btn['text'] = 'SFU: Bur -> Van'
        bg_image.configure(image=bg_van)
        bg_image.image=bg_van
    else:
        van_to_bur = True
        btn['text'] = 'SFU: Van -> Bur'
        bg_image.configure(image=bg_bur)
        bg_image.image=bg_bur

btn = tk.Button(root, text="SFU: Van -> Bur", bg="#CC0633", fg="white", font=('helvetica', 9, 'bold'), command=change_direction)  
btn.place(x=0, y=0)


# REQUIRED
root.mainloop()