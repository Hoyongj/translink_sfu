import tkinter as tk
import translink_sfu

# START tkinter
root= tk.Tk()
root.title("SFU VAN-BUR TRAVEL")
root.geometry("720x480")
root.resizable(False,False)



# BUTTON with TXT
van_to_bur = True
def change_direction():
    global van_to_bur
    if van_to_bur: 
        btn['text'] = 'SFU: Bur -> Van'
        van_to_bur = False
    else:
        btn['text'] = 'SFU: Van -> Bur'
        van_to_bur = True

btn = tk.Button(root, text="SFU: Van -> Bur", bg="#CC0633", fg="white", font=('helvetica', 9, 'bold'), command=change_direction)  
btn.place(x=0, y=0)


# REQUIRED
root.mainloop()