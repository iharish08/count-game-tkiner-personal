import tkinter as count
a=count.Tk()
s=0

def main():
    global s
    s +=1
    print(s)
    
a.geometry("350x350")
b=count.Button (
    a,
    text="click!",
    command=main
)
b.pack()


a.mainloop()

    
