import tkinter as tk
from tkinter import Button, StringVar, Widget, ttk
from tkinter.constants import END

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Management System")
win.iconbitmap('logo.ico')

#Background Color
win.config(bg="lightgray")

#Adding some style
style = ttk.Style()

#Pick a theme
style.theme_use("default")

style.configure("Treeview",background="white",foreground="black",rowheight=25,fieldbackground = 'white')

#Change selected color
style.map("Treeview",background=[("selected","darkred")])

#Top menu
title_label = tk.Label(win,text="Student Management System",font=("Arial" , 20 , "bold"),padx=15,pady=15,border=0,relief= tk.GROOVE,bg="teal",foreground="white")
title_label.pack(side=tk.TOP,fill=tk.X)

#Left Menu
detail_frame = tk.LabelFrame(win,text="Student Records",font=("Arial",14),bg="lightgray",foreground="black",relief=tk.GROOVE)
detail_frame.place(x=40,y=90, width=420, height=570)

#Data frame

data_frame = tk.Frame(win,bg="teal",relief=tk.GROOVE)
data_frame.place(x=490, y=98 , width=830 , height=565)

#Label With Entry
id_lab = tk.Label(detail_frame,text="ID:",font=("Arial",16),bg="lightgray",foreground="black")
id_lab.place(x=20,y=15)

#entry
id_ent = tk.Entry(detail_frame,bd=1,font=("arial",16),bg="white",foreground = "black")
id_ent.place(x=110 , y=17 , width = 250,height=30)

#2
name_lab = tk.Label(detail_frame,text="Name:",font=("Arial",16),bg="lightgray",foreground="black")
name_lab.place(x=20, y=65)

#Entry
name_ent = tk.Entry(detail_frame,bd=1,font=("arial",16),bg="white",foreground="black")
name_ent.place(x=110, y=65, width=250, height=30)

#3
gen_lab = tk.Label(detail_frame,text="Gender:",font=("Arial",16),bg="lightgray",foreground="black")
gen_lab.place(x=20, y=113)

#entry
gen_ent = ttk.Combobox(detail_frame,font=("Arial",16))
gen_ent["values"] = ("Male","Female","Others")
gen_ent.place(x=110, y=113 , width=250 , height = 30)

#4
age_lab = tk.Label(detail_frame,text="Age:",font=("Arial",16),bg="lightgray",foreground="black")
age_lab.place(x=20, y=161)

#Entry
age_ent = tk.Entry(detail_frame,bd=1,font=("Arial",16),bg="white",foreground="black")
age_ent.place(x=110 , y=161 , width=250 , height = 30)

#5
ent_lab = tk.Label(detail_frame,text="En-date:",font=("Arial",16),bg="lightgray",foreground="black")
ent_lab.place(x=20, y=209)

#entry
ent_ent = tk.Entry(detail_frame,bd=1,font=("Arial",16),bg="White",foreground="Black")
ent_ent.place(x=110 , y=209 , width=250 , height= 30)

#6
mid_lab = tk.Label(detail_frame,text="Midterm:",font=("Arial",16),bg="lightgray",foreground="black")
mid_lab.place(x=20, y=257)

#entry
mid_ent = tk.Entry(detail_frame,bd=1,font=("Arial",16),bg="White",foreground="black")
mid_ent.place(x=110, y=257,width=250,height=30)

#7
fin_lab = tk.Label(detail_frame,text="Final:",font=("Arial",16),bg="lightgray",foreground="black")
fin_lab.place(x=20, y=305)

#Entry
fin_ent = tk.Entry(detail_frame,bd=1,font=("Arial",16),bg="white",foreground="black")
fin_ent.place(x=110, y=305, width=250, height=30)

#8
gpa_lab = tk.Label(detail_frame,text="GPA:",font=("Arial",16),bg="lightgray",foreground="black")
gpa_lab.place(x=20, y=353)

#Entry
gpa_ent = tk.Entry(detail_frame,bd=1,font=("Arial",16), bg="white",foreground="Black")
gpa_ent.place(x=110, y=353 , width=250 , height=30)


#Database Frame
main_frame = tk.Frame(data_frame,bg="teal",bd=2,relief = tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

Y_Scroll = tk.Scrollbar(main_frame,orient=tk.VERTICAL)
X_Scroll = tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

#TreeView database
student_table = ttk.Treeview(main_frame, columns=("ID","Name","Gender","Age","Enroll date","Midterm","Final","GPA") , yscrollcommand=Y_Scroll.set , xscrollcommand=X_Scroll.set)

Y_Scroll.config(command=student_table.yview)
X_Scroll.config(command=student_table.xview)

Y_Scroll.pack(side=tk.RIGHT, fill=tk.Y)
X_Scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_table.heading("ID", text="ID")
student_table.heading("Name", text="Name")
student_table.heading("Gender", text="Gender")
student_table.heading("Age", text="Age")
#student_table.heading("Enroll Date", text="Enroll Date")
student_table.heading("Enroll date", text="Enroll Date")
student_table.heading("Midterm", text="Midterm")
student_table.heading("Final", text="Final")
student_table.heading("GPA", text="GPA")

#student_table["Show"] = "headings"
student_table["show"] = "headings"


student_table.column("ID", width=100)
student_table.column("Name", width=100)
student_table.column("Gender", width=100)
student_table.column("Age", width=100)
student_table.column("Enroll date", width=100)
student_table.column("Midterm", width=100)
student_table.column("Final", width=100)
student_table.column("GPA", width=100)

student_table.pack(fill=tk.BOTH , expand= True )

#Default Data

data = []


#Create Stripped row tags
student_table.tag_configure("oddrow",background="white")
student_table.tag_configure("evenrow", background= "#00AEAE")

global count
count = 0
for record in data:
    if count % 2 == 0:
        student_table.insert(parent="",index="end", iid=count , text= "" , values = (record[0], record[1] , record[2],record[3], record[4] , record[5], record[6], record[7]))
    else:
        student_table.insert(parent="",index="end", iid=count , text= "" , values = (record[0], record[1] , record[2],record[3], record[4] , record[5], record[6], record[7]))

    count +=1


#Functions

#Add Function

def add_record():
    student_table.tag_configure("oddrow",background="white")
    student_table.tag_configure("evenrow",background="#00AEAE")

    global count
    if count % 2 == 0:
        student_table.insert(parent="" , index="end" , iid = count , text="", values=(id_ent.get(),name_ent.get(),age_ent.get(),gen_ent.get(), ent_ent.get(), mid_ent.get(), fin_ent.get() , gpa_ent.get()),tags=("evenrow"))
    else:
        student_table.insert(parent="" , index="end" , iid = count , text="", values=(id_ent.get(),name_ent.get(),age_ent.get(),gen_ent.get(), ent_ent.get(), mid_ent.get(), fin_ent.get() , gpa_ent.get()),tags=("oddrow"))
    
    count += 1

#Delete All Function
def delete_all():
    for record in student_table.get_children():
        student_table.delete(record)

#Delete One Function

'''def delete_one():
    x = student_table.selection()[0]
    student_table.delete(x)'''
def delete_one():
    selected = student_table.selection()
    if selected:  # This checks if the tuple is not empty
        student_table.delete(selected[0])
    else:
        print("No item selected")  # Optionally, alert the user that no item is selected


#Select Record

def select_record():

    id_ent.delete(0 , END)
    name_ent.delete(0, END)
    age_ent.delete(0, END)
    gen_ent.delete(0, END)
    ent_ent.delete(0, END)
    mid_ent.delete(0, END)
    fin_ent.delete(0, END)
    gpa_ent.delete(0, END)

    Selected = student_table.focus()
    values = student_table.item(Selected, "values")

    id_ent.insert(0 , values[0])
    name_ent.insert(0 , values[1])
    age_ent.insert(0 , values[2])
    gen_ent.insert(0 , values[3])
    ent_ent.insert(0 , values[4])
    mid_ent.insert(0 , values[5])
    fin_ent.insert(0 , values[6])
    gpa_ent.insert(0 , values[7])


#Update Button
def update_record():
    Selected = student_table.focus()
    student_table.item(Selected, text="", values=(id_ent.get(), name_ent.get(),age_ent.get(),gen_ent.get(),ent_ent.get(),mid_ent.get(),fin_ent.get(),gpa_ent.get()))

    id_ent.delete(0 , END)
    name_ent.delete(0, END)
    age_ent.delete(0, END)
    gen_ent.delete(0, END)
    ent_ent.delete(0, END)
    mid_ent.delete(0, END)
    fin_ent.delete(0, END)
    gpa_ent.delete(0, END)

#Clear Boxes
    id_ent.delete(0 , END)
    name_ent.delete(0, END)
    age_ent.delete(0, END)
    gen_ent.delete(0, END)
    ent_ent.delete(0, END)
    mid_ent.delete(0, END)
    fin_ent.delete(0, END)
    gpa_ent.delete(0, END)


#Buttons

#btn_frame = tk.Frame(detail_frame,bg="Lightgray",bd=0,relief=tk.GROOVE)
#btn_frame.place(x=40 , y=400, width=310, height= 130)
btn_frame = tk.Frame(detail_frame, bg="lightgray", bd=0, relief=tk.GROOVE)
btn_frame.place(x=40, y=400, width=310, height=130)

# Add Button
add_btn = tk.Button(btn_frame, bg="teal", foreground="White", text="Add", bd=2, font=("Arial", 13), width=15, command=add_record)
add_btn.grid(row=0, column=0, padx=2, pady=2)

# Update Button
update_btn = tk.Button(btn_frame, bg="teal", foreground="White", text="Update", bd=2, font=("Arial", 13), width=15, command=select_record)
update_btn.grid(row=0, column=1, padx=2, pady=2)

# Calculate Button
calculate_btn = tk.Button(btn_frame, bg="teal", foreground="White", text="Calculate", bd=2, font=("Arial", 13), width=15)  # Assuming this needs a function
calculate_btn.grid(row=1, column=0, padx=2, pady=2)

# Save Button
save_btn = tk.Button(btn_frame, bg="teal", foreground="White", text="Save", bd=2, font=("Arial", 13), width=15, command=update_record)
save_btn.grid(row=1, column=1, padx=2, pady=2)

# Clear Button
clear_btn = tk.Button(btn_frame, bg="teal", foreground="White", text="Clear", bd=2, font=("Arial", 13), width=15, command=delete_all)  # Assuming this clears all entries
clear_btn.grid(row=2, column=0, padx=2, pady=2)

# Delete Button
delete_btn = tk.Button(btn_frame, bg="teal", foreground="White", text="Delete", bd=2, font=("Arial", 13), width=15, command=delete_one)
delete_btn.grid(row=2, column=1, padx=2, pady=2)


'''
# Add Button: Adds new records
add_btn = tk.Button(btn_frame, bg="teal", foreground="White", text="Add", bd=2, font=("Arial", 13), width=15, command=add_record)
add_btn.grid(row=0, column=0, padx=2, pady=2)

# Update Button: Updates selected record
update_btn = tk.Button(btn_frame, bg="teal", foreground="White", text="Update", bd=2, font=("Arial", 13), width=15, command=select_record)
update_btn.grid(row=0, column=1, padx=2, pady=2)

# Calculate Button: Placeholder for a future implementation (currently not linked to a function)
print_btn = tk.Button(btn_frame, bg="teal", foreground="White", text="Calculate", bd=2, font=("Arial", 13), width=15)
print_btn.grid(row=0, column=2, padx=2, pady=2)

# Save Button: Saves updates to a record
cal_btn = tk.Button(btn_frame, bg="teal", foreground="White", text="Save", bd=2, font=("Arial", 13), width=15, command=update_record)
cal_btn.grid(row=0, column=3, padx=2, pady=2)

# Delete All Button: Deletes all records
save_btn = tk.Button(btn_frame, bg="teal", foreground="White", text="Delete All", bd=2, font=("Arial", 13), width=15, command=delete_all)
save_btn.grid(row=0, column=4, padx=2, pady=2)

# Delete Button: Deletes the selected record
delete_btn = tk.Button(btn_frame, bg="teal", foreground="White", text="Delete Selected", bd=2, font=("Arial", 13), width=15, command=delete_one)
delete_btn.grid(row=0, column=5, padx=2, pady=2)'''


win.mainloop()

