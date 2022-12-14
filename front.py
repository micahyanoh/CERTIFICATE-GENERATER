""" IMPORTING APPLICATION DEPENDANCIES"""
import tkinter as tk
from tkinter import END, ttk,messagebox
from pdf_mail import sendpdf
from PIL import Image
import threading
import connection
import cv2


#GENERATING CERTICATE FROM TEMPLATE
def generate_cert():
    if messagebox.askyesno('Confirm Prompt?','Do you want to BATCH process many certificates'):
        connection.Database()
        connection.cursor.execute("SELECT * FROM students ORDER BY adm_no")
        fetch=connection.cursor.fetchall()
      
        for data in fetch:
            space=' ' 
            cert_num=(data[0])
            file_n=(data[3])
            names=(data[1]+space+data[2])
            cert_no=f'A1l200{cert_num}'
            template=cv2.imread('assets/certificate-template.jpg')
            cv2.putText(template,names,(1201,953),cv2.FONT_HERSHEY_SIMPLEX,4,(233, 34, 103),4,cv2.LINE_AA)
            cv2.putText(template,cert_no,(2697  ,2409),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,255),4,cv2.LINE_AA)      
            cv2.imwrite(f'generated-certificate-data/images/{file_n}.jpg',template)
            image=Image.open(f'generated-certificate-data/images/{file_n}.jpg')
            cert_p=image.convert('RGB')
            cert_p.save(f'generated-certificate-data/pdf/{file_n}.pdf')  
        connection.cursor.close()
        connection.conn.close()
    else:
        search_it=search_entry.get()
        connection.Database()
        connection.cursor.execute("SELECT * FROM students WHERE adm_no LIKE '%"+search_it+"%'")
        fetch=connection.cursor.fetchall()
        
        for data in fetch:
            space=' ' 
            cert_num=(data[0])
            file_n=(data[3])
            names=(data[1]+space+data[2])
            cert_no=f'A1l200{cert_num}'
            template=cv2.imread('assets/certificate-template.jpg')
            cv2.putText(template,names,(1201,953),cv2.FONT_HERSHEY_SIMPLEX,4,(233, 34, 103),4,cv2.LINE_AA)
            cv2.putText(template,cert_no,(2697  ,2409),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,255),4,cv2.LINE_AA)      
            cv2.imwrite(f'generated-certificate-data/images/{file_n}.jpg',template)
            image=Image.open(f'generated-certificate-data/images/{file_n}.jpg')
            cert_p=image.convert('RGB')
            cert_p.save(f'generated-certificate-data/pdf/{file_n}.pdf')
        connection.cursor.close()
        connection.conn.close()
    
    messagebox.showinfo("","    Certificates Successfully Generated    ")
    

def gen_thread():
    threading.Thread(target=generate_cert).start()
#button testing
def printer():
    print(e1.get())

#testing function
def enter_data():
    adm=e1.get().upper()
    first=e2.get().upper()
    last=e3.get().upper()
    email=e4.get().lower()
    phone=e5.get()
    
#CLEAR ENTRIES
def clear_entries():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    search_entry.delete(0,END)
    search_entry.insert(0,'C1')

def clear_btn():
    clear_entries()
    populate_view()

 #UPDATE RECORDS   
def update_data():
    adm=e1.get().upper()
    first=e2.get().upper()
    last=e3.get().upper()
    email=e4.get().lower()
    phone=e5.get()
    connection.Database()
    if messagebox.askyesno('Confirm Delete?','Are you sure you want to update this student?'):
        query="""
        UPDATE students SET adm_no = ?,
        first_name = ?,
        last_name = ?,email = ?,phone = ? WHERE adm_no = ?"""
        connection.cursor.execute(query,(adm,first,last,email,phone,adm))
        connection.conn.commit()
        populate_view()
        clear_entries()
    else:
        clear_entries()
        return True
    
#INSERTING RECORDS
def insert_data():
    adm=e1.get().upper()
    first=e2.get().upper()
    last=e3.get().upper()
    email=e4.get().lower()
    phone=e5.get()
    connection.Database()
    data_insert_query="""
    INSERT OR REPLACE INTO students(
        adm_no,
        first_name,
        last_name,
        email,
        phone
        )VALUES(?,?,?,?,?)"""
    data_insert_tuple=(adm,first,last,email,phone)
    connection.cursor.execute(data_insert_query,data_insert_tuple)
    connection.conn.commit()
    connection.cursor.close()
    connection.conn.close()
    messagebox.showinfo("","     Student Successfully Registered   ")
    populate_view()
    clear_entries()

    
#SEARCHING RECORDS BY ADM NO.
def search():
    connection.Database()
    search_it=search_entry.get()
    query="SELECT * FROM students WHERE adm_no LIKE '%"+search_it+"%'" 
    connection.cursor.execute(query)
    rows=connection.cursor.fetchall()
    trv.delete(*trv.get_children())
    if rows ==[]:
        populate_view()
        clear_entries()
    else:
        for data in rows:
            trv.insert('','end',values=(data[0],data[1],data[2],data[3],data[4]))
            clear_entries()



#DISPLAYING DATA
def populate_view():
    trv.tag_configure('gray',background='lightgray')
    trv.tag_configure('normal',background='white')
    my_tag='normal'#default tag

    trv.delete(*trv.get_children())
    connection.Database()
    connection.cursor.execute("SELECT * FROM students ORDER BY adm_no")
    fetch=connection.cursor.fetchall()
    for data in fetch:
        my_tag='gray' if my_tag =='normal' else 'normal'
        trv.insert('','end',values=(data[0],data[1],data[2],data[3],data[4]),tags=my_tag)
    connection.cursor.close()
    connection.conn.close()

#DELETING ENTRIES
def delete_ent():
    connection.Database()
    delete_id=e1.get()
    if messagebox.askyesno('Confirm Delete?','Are you sure you want to delete this student?'):
        connection.cursor.execute("""DELETE from students WHERE adm_no=?""",(delete_id,))
        connection.conn.commit()
        populate_view()
        clear_entries()
    else:
        clear_entries()
        return True

#EXIT FUNCTION   
def homer(): 
    if messagebox.askyesno('Confirm Exit?','Are you sure you want to Close this App?'):
        app.destroy()
    else:
        return True      

 
#INSERTING DATA INTO TREE-VIEW   
def get_row(event):
    clear_entries()
    search_entry.delete(0,END)
    rowid=trv.identify_row(event.y)
    item=trv.item(trv.focus())
    e1.insert(0,item['values'][0])
    e2.insert(0,item['values'][1])
    e3.insert(0,item['values'][2])
    e4.insert(0,item['values'][3])
    e5.insert(0,item['values'][4])
    search_entry.insert(0,item['values'][0])


def post_popup(event):
    rowid=trv.identify_row(event.y) 
    #trv.selection_set(rowid)  
    #row_values=trv.item(rowid)['values']
    row_values=trv.item(trv.focus())
    print(row_values)
    popup=tk.Menu(trv,tearoff=0,font=('Verdana',11))
    popup.add_command(label='Edit/Update',accelerator='Ctrl+E')
    popup.add_command(label='Delete',accelerator='Delete',command=delete_ent)
    popup.add_separator()
    popup.add_command(label='Edit/Update',accelerator='Ctrl+E')
    popup.add_command(label='Delete',accelerator='Delete',command=delete_ent)
    popup.post(event.x_app,event.y_app)
    
    
#EMAILING CERTIFICATES TO STUDENTS
def send_cert():
    sender=input()
    receiver=input()
    email_password=input()
    subject=input()
    body=input()
    filename=input()
    file_location=input()
    message=sendpdf(
        sender,
        receiver,
        email_password,
        subject,
        body,
        filename,
        file_location
    )
 

     
"""INITIALIZING APPLICATION"""
app=tk.Tk()
app.geometry('1025x500')
app.minsize(1025,500)#minimum window size
#style=ttk.Style(app)
cl='#40E0D0'
#style.theme_use('clam')
#style.configure('Treeview',font=('Verdana',10),cellpadding=19)
#style.configure('Treeview.Heading',font=('Verdana',10,'bold'),cellpadding=19,background=cl)


app.configure(background=cl)#'#2f935a')
#app.configure(background= 'white')
app.title('STUDENT MANAGEMENT SYSTEM')
app.state('zoomed')#maximizing the window to screen size


'''frame one'''
first_frame=tk.LabelFrame(
    app,
    background=cl,
    text='STUDENT DATA ENTRY FORM',
    width='330',
    height='480'
    )
first_frame.pack(
    side=tk.LEFT,
    padx=8,pady=10,
    fill=tk.BOTH,expand=1
    )


#creating labels and entries in frame one
empty_label_a=tk.Label(
    first_frame,
    background=cl,
    text=None
    ).grid(column=1,row=0,pady=10)
empty_label_b=tk.Label(
    first_frame,
    background=cl,
    text=None
    ).grid(column=1,row=6,pady=15)

l1=tk.Label(
    first_frame,
    text='ADM NUMBER',
    background=cl#'#2f935a'
    )
l1.grid(row=1,column=0,padx=10,pady=5)

e1=tk.Entry(
    first_frame
    )
e1.grid(row=1,column=1,padx=20,pady=5)

l2=tk.Label(
    first_frame,
    text='FIRST NAME',
    background=cl#'#2f935a',
    )
l2.grid(row=2,column=0,padx=10,pady=5)

e2=tk.Entry(
    first_frame
    )
e2.grid(row=2,column=1,padx=20,pady=5)

l3=tk.Label(
    first_frame,
    text='LAST NAME',
    background=cl#'#2f935a'
    )
l3.grid(row=3,column=0,padx=10,pady=5)

e3=tk.Entry(
    first_frame
    )
e3.grid(row=3,column=1,padx=20,pady=5)

l4=tk.Label(
    first_frame,
    text='EMAIL',
    background=cl#'#2f935a'
    )
l4.grid(row=4,column=0,padx=10,pady=5)

e4=tk.Entry(
    first_frame
    )
e4.grid(row=4,column=1,padx=20,pady=5)

l5=tk.Label(
    first_frame,
    text='PHONE NUMBER',
    background=cl#'#2f935a'
    )
l5.grid(row=5,column=0,padx=10,pady=5)

e5=tk.Entry(
    first_frame
    )
e5.grid(row=5,column=1,padx=20,pady=5)


#buttons frame one
b1=tk.Button(
    first_frame,
    text='ADD',
    width=10,
    background='#D9D9D9'
    )
b1.grid(column=0,row=9,padx=20,pady=20)

b2=tk.Button(
    first_frame,
    text='CLEAR',
    width=10,
    background='#D9D9D9'
    )
b2.grid(column=1,row=9)

b3=tk.Button(
    first_frame,
    text='UPDATE',
    width=10,
    background='#D9D9D9'
    )
b3.grid(column=0,row=10,padx=20,pady=10)

b4=tk.Button(
    first_frame,
    text='DELETE',
    width=10,
    background='#D9D9D9'
    )
b4.grid(column=1,row=10)

search_entry=tk.Entry(first_frame)
search_entry.insert(0,'C1')
search_entry.grid(column=0,row=8,padx=20)

search_b=tk.Button(
    first_frame,
    text='SEARCH',
    width=10,
    background='#D9D9D9'
    )
search_b.grid(column=1,row=8)

search_lab=tk.Label(
    first_frame,
    text=' ADM SEARCH',
    width=10,
    background=cl#'#2f935a'
    )
search_lab.grid(column=0,row=7)

cert_lab=tk.Label(
    first_frame,
    text='',
    width=10,
    background=cl#'#2f935a'
    )
cert_lab.grid(column=0,row=11,pady=15)

cert_lab=tk.Label(
    first_frame,
    text='CERTIFICATES',
    width=10,
    background=cl#cl#'#2f935a'
    )
cert_lab.grid(column=1,row=11,pady=15)

cert_b=tk.Button(
    first_frame,
    text='GENERATE',
    width=10,
    background='#D9D9D9',
    cursor='hand2',
    )
    
cert_b.grid(column=1,row=12)

home=tk.Button(
    first_frame,
    text='EXIT',
    width=10,
    background='#D9D9D9',
    cursor='hand2'
    )
home.grid(column=0,row=12,)


'''frame two'''
second_frame=tk.LabelFrame(
    app,
    text='STUDENT  RECORDS',
    width='330',
    height='480',
    background=cl#'#2f935a'
    )
second_frame.pack(side=tk.LEFT,fill=tk.BOTH,expand=1,pady=10)


scrollbar_x=ttk.Scrollbar(second_frame,orient=tk.HORIZONTAL)
scrollbar_x.pack(side=tk.BOTTOM,fill=tk.X)
scrollbar_y=ttk.Scrollbar(second_frame,orient=tk.VERTICAL)
scrollbar_y.pack(side=tk.RIGHT,fill=tk.Y)


"""TREE-VIEW TO DISPLAY DATA ON SECOND FRAME"""
trv=ttk.Treeview(
    second_frame,
    columns=(
        'ID',
        'FIRST NAME',
        'LAST NAME',
        'EMAIL',
        'PHONE'
        ),
    show='headings',
    selectmode='browse',
    yscrollcommand=scrollbar_y.set,
    xscrollcommand=scrollbar_x.set
    )
style=ttk.Style(trv)
style.theme_use('clam')
style.configure('Treeview',font=('Verdana',10),cellpadding=19)
style.configure('Treeview.Heading',font=('Verdana',10,'bold'),cellpadding=19,background=cl)
style.map('Treeview',background=[('selected',cl)])

style.configure('Treeview',rowheight=30)

trv.pack(fill=tk.BOTH,expand=1)


#TREE-VIEW CONFIGURATION
trv.heading('#1',text='ADM NO',anchor='center')
trv.heading('#2',text='FIRST NAME',anchor='center')
trv.heading('#3',text='LAST NAME',anchor='center')
trv.heading('#4',text='EMAIL',anchor='center')
trv.heading('#5',text='PHONE NO',anchor='center')

trv.column('#1',anchor='center',stretch=0)
trv.column('#2',anchor='center',stretch=0)
trv.column('#3',anchor='center',stretch=0)
trv.column('#4',anchor='center',stretch=0)
trv.column('#5',anchor='center',stretch=0)
trv.bind('<Double 1>',get_row)
trv.tag_bind('row','<Button-3>',lambda event:post_popup(event))


#SCROLL BARS ON X & Y AXIS
scrollbar_y.configure(command=trv.yview)
scrollbar_x.configure(command=trv.xview)
#trv.tag_configure('even',background=cl)


#BUTTON CONFIGURATIONS
search_b.configure(command=search)
b1.configure(command=insert_data)
b2.configure(command=clear_btn)
b3.configure(command=update_data)
b4.configure(command=delete_ent)
home.configure(command=homer)
cert_b.configure(command=gen_thread)
populate_view()
app.mainloop()