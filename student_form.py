from tkinter import *
# from sqlite3 import *                   

root=Tk()

root.title("Login Form")
root.geometry("600x500+100+50")
# root.wm_icomBitmap("")




name_v=StringVar()
email_v=StringVar()
password_v=StringVar()
male_v=StringVar()






title_name=Label(root,text="Student Login Form",font=('alual',40,'bold'))
title_name.pack(side="top")


main_frame=Frame(root,bd=5,relief="solid",bg="white")
main_frame.place(x=20,y=70,width=550,height=400)

# Lavbels

name=Label(main_frame,text="Full Name",font=('arial',15,'bold'))
name.grid(row=0,column=1,padx=10,pady=10)

email=Label(main_frame,text="Email",font=('arial',15,'bold'))
email.grid(row=1,column=1,padx=10,pady=10)

chechk_label=Label(main_frame,text="Gender",font=('arial',15,'bold'))
chechk_label.grid(row=4,column=1,padx=10,pady=10)

skills_label=Label(main_frame,text="Skills",font=('arial',15,'bold'))
skills_label.grid(row=5,column=1,padx=10,pady=10)


password=Label(main_frame,text="Password",font=('arial',15,'bold'))
password.grid(row=3,column=1,padx=10,pady=10)


# Entries
name_entry=Entry(main_frame,textvariable=name_v,font=("aarial",15,"bold"))
name_entry.grid(row=0,column=2,padx=10,pady=10)

email_entry=Entry(main_frame,textvariable=email_v,font=("aarial",15,"bold"))
email_entry.grid(row=1,column=2,padx=10,pady=10)

password_entry=Entry(main_frame,textvariable=password_v,font=("aarial",15,"bold"),show="*")
password_entry.grid(row=3,column=2,padx=10,pady=10)

# Radio Button
radio_male=Radiobutton(main_frame,text="Male",textvariable=male_v,value="male",font=("arial",15,"bold"))
radio_male.grid(row=4,column=2)
male_v.set("male")

radio_female=Radiobutton(main_frame,text="FEMale",textvariable=male_v,value="female",font=("arial",15,"bold"))
radio_female.grid(row=4,column=3)


# Checkbboxes

check_html=Checkbutton(main_frame,text="HTML",font=("aarial",15,"bold"))
check_html.grid(row=5,column=2,padx=10,pady=10)

check_css=Checkbutton(main_frame,text="CSS",font=("aarial",15,"bold"))
check_css.grid(row=5,column=3,padx=10,pady=10)

check_Jjs=Checkbutton(main_frame,text="JS",font=("aarial",15,"bold"))
check_Jjs.grid(row=6,column=2,padx=10,pady=10)

check_php=Checkbutton(main_frame,text="PHP",font=("aarial",15,"bold"))
check_php.grid(row=6,column=3,padx=10,pady=10)



def show_result():
    Label(main_frame,text=name_v.get()) .grid(row=7,column=1)
    Label(main_frame,text=email_v.get()).grid(row=8,column=1)
    Label(main_frame,text=password_v.get()).grid(row=9,column=1)
    Label(main_frame,text=male_v.get()).grid(row=10,column=1)


# Buttons
button=Button(main_frame,text="Submit",bg="blue",fg="white",activebackground="blue",activeforeground="white",command=show_result)
button.grid(row=7,column=2)

root.mainloop()