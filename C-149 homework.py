from tkinter import*
import random
root=Tk()

root.title("Lucky Winner")
root.geometry("500x500")


list1=["EGKGUG","KGEFKH","GEKHFB","GULEQV","EGQKJ"]
print(list1)

def random_numbers():
    random_no=random.randint(0,4)
    print(random_no)
    random_lucky_friend=list1[random_no]
    print("Generated Random Words"+ random_lucky_friend)
    
btn1=Button(root,text="Who is your lucky friend ", command=random_numbers)
btn1.place(relx=0.5,rely=0.5,anchor=CENTER)
    
root.mainloop()