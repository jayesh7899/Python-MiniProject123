from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

from tkinter import messagebox
import mysql.connector as my
from ttkbootstrap import*

#from EmpModule import*
#from EmpData import*

global lblframe4,lblframe3


style=Style(theme="cosmo")

root=style.master

#frame5 for tv

lblframe77=LabelFrame(root,width=1518,height=260,font=
                     ('constantia',14,'bold'),bd=3)
lblframe77.place(x=5,y=567)


tv=ttk.Treeview(lblframe77)
tv.place(x=20,y=2)

#===============variables

id1=StringVar()
nm1=StringVar()
mb1=StringVar()
adr1=StringVar()
dob1=StringVar()
cn1=StringVar()
em1=StringVar()
ms1=StringVar()
que1=StringVar()
pan1=StringVar()
gen22=StringVar()

dept1=StringVar()
sal78=StringVar()

search1=StringVar()

combosearch1=StringVar()


############################### function slider label#########################################
def introlabel():
    global count,text
    if(count>=len(ss)):
        count=0
        text=""
        sliderlabel.config(text=text)

    else:
        text=text+ss[count]

        sliderlabel.config(text=text)
        count=count+1

    sliderlabel.after(300,introlabel)
    
    





def Tabelshow():
    try:

        ch=tv.get_children()
        for y in ch:
            tv.delete(y)

        mydb=my.connect(
            host='localhost',
            user='root',
            password='',
            database='live'
            )
        
        mycursor=mydb.cursor()
        sql="select * from emp";
        mycursor.execute(sql)
        result=mycursor.fetchall()

        i=1

        for data in result:

            tv.insert(parent="",index=i,values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11]))

            i=i+1


    except Exception as e9:
        print('tableerror',e9)

def selectview(event):
    view=tv.selection()
    item=tv.item(view)
    data=item['values']

    id1.set(data[0])
    nm1.set(data[1])
    mb1.set(data[2])
    adr1.set(data[3])
    dob1.set(data[4])
    cn1.set(data[5])
    em1.set(data[6])
    ms1.set(data[7])
    que1.set(data[8])
    gen22.set(data[9])
    #pan1.set("Select")

    dept1.set(data[10])
    sal78.set(data[11])



def update():
    try:
        
    

        mydb=my.connect(
            host='localhost',
            user='root',
            password='',
            database='live'
            )
        sql="update emp set Name='"+nm1.get()+"',Mobile='"+mb1.get()+"',Address='"+adr1.get()+"',Dob='"+dob1.get()+"',Country='"+cn1.get()+"',Email='"+em1.get()+"',Marriedstatus='"+ms1.get()+"',Qualification='"+que1.get()+"',Gender='"+gen22.get()+"',Dept='"+dept1.get()+"',Salary='"+sal78.get()+"' where Id="+id1.get()

      
                                                                
        mycursor=mydb.cursor()
        mycursor.execute(sql)

        mydb.commit()
        messagebox.showinfo('update','recoard is updated')

        Tabelshow()
        new()
        show()
        
    except Exception as e3:

        messagebox.showerror('error','record is not Updated')

        print('record is not updated',e3)





def find():
    
    try:
        mydb=my.connect(
            host='localhost',
            user='root',
            password='',
            database='live'
            )
        mycursor=mydb.cursor()

        search2=search1.get()

        

        sql="select * from emp where Id="+search1.get()
        mycursor.execute(sql)

        res=mycursor.fetchone()

        id1.set(res[0])
        nm1.set(res[1])
        mb1.set(res[2])
        adr1.set(res[3])
        dob1.set(res[4])
        cn1.set(res[5])
        em1.set(res[6])
        ms1.set(res[7])
        que1.set(res[8])
        gen22.set(res[9])
        #pan1.set("Select")

        dept1.set(res[10])
        sal78.set(res[11])



        
        
            
        messagebox.showinfo('find','record is found')
        
        mydb.commit()
        mydb.close()

        Tabelshow()

    except Exception as e3:

        print('finderror',e3)

        
        messagebox.showerror('find','record is not found')

def show():
    try:
        mydb=my.connect(
            host='localhost',
            user='root',
            password='',
            database='live'
            )
        mycursor=mydb.cursor()
        sql='select count(Id) from emp';

        mycursor.execute(sql)
        result=mycursor.fetchone()

        pk=result[0]
        

        pk=pk+1
        id1.set(str(pk))
        
        mydb.commit()

        
        

    except Exception as e1:
        print('ShowError',e1)








def delete():
    
    
    try:

        mydb=my.connect(
            host='localhost',
            user='root',
            password='',
            database='live'
            )

        mycursor=mydb.cursor()
        sql="delete from emp where Id="+id1.get()
        mycursor.execute(sql)
        mydb.commit()

        messagebox.showinfo('delete','record is delete')
        
        
        Tabelshow()

        new()
        
        show()

    except Exception as e3:

        messagebox.showerror('error','record is not delete')

        print('delete record',e3)
def new():

    id1.set('')
    nm1.set('')
    mb1.set('')
    adr1.set('')
    dob1.set('')
    cn1.set('')
    em1.set('')
    ms1.set('')
    que1.set('')
    

    gen22.set('')

    dept1.set('')
    sal78.set('')

    search1.set('')

    show()

    Tabelshow()

    


def insert():
    
    try:
        mydb=my.connect(
            host='localhost',
            user='root',
            password='',
            database='live'
            )
        mycursor=mydb.cursor()

        id2=id1.get()
        nm2=nm1.get()
        mb2=mb1.get()
        adr2=adr1.get()
        dob2=dob1.get()
        cn2=cn1.get()
        em2=em1.get()
        ms2=ms1.get()
        que2=que1.get()
        gen12=gen22.get()
        dept2=dept1.get()
        sal2=sal78.get()
        


        #gender sathi insert madhe latest value means p ghavi

        
        sql="insert into emp values('"+id2+"','"+nm2+"','"+mb2+"','"+adr2+"','"+dob2+"','"+cn2+"','"+em2+"','"+ms2+"','"+que2+"','"+gen12+"','"+dept2+"','"+sal2+"')";

        mycursor.execute(sql)

        mydb.commit()

        
        messagebox.showinfo('insert','record is inserted')
        Tabelshow()
        
        new()

        

        show()

       
        
        '''i.set('')
        
        n.set('')
        
        a.set('')

        c.set('')

        m.set('')
        
        l.set('')
        
        g.set('')'''

        

        
        
        
    except Exception as e:

        messagebox.showerror('insert','record is not inserted')


        print('error',e)



#====================================Search data==================================================
def Search():

    global search
    if combosearch1.get()=="" or search1.get()=="":
        messagebox.showerror("Error","Please select option")
    else:
        try:
            mydb=my.connect(
            host='localhost',
            user='root',
            password='',
            database='live'
            )
            mycursor=mydb.cursor()

            sql=("select * from emp where " +str(combosearch1.get())+" LIKE  '%" +str(search1.get())+"%' ")
            mycursor.execute(sql)
            row=mycursor.fetchall()

            
            if len(row)!=0:
                tv.delete(*tv.get_children())
                for i in row:
                    tv.insert("",END,values=i)  
                        
                mydb.commit()

                messagebox.showinfo('find','record is found')

            else:
                messagebox.showerror('find','record is not found')
                   
            mydb.close()

            
        except Exception as ep3:
                
            messagebox.showerror("Record is Not Found",ep3)



def ShowAllRecord():
        
    mydb=my.connect(
            host='localhost',
            user='root',
            password='',
            database='live'
            )
    mycursor=mydb.cursor()
    sql="select * from emp"
    mycursor.execute(sql)
    data=mycursor.fetchall()
        
    if len(data)!=0:
        tv.delete(*tv.get_children())
        for A in data:
            tv.insert("",END,values=A)
        mydb.commit()
            
    mydb.close()





        

new()

show()

Tabelshow()






root.title("Student Management system")
#root.config(bg="yellow")



width=root.winfo_screenwidth()
height=root.winfo_screenwidth()

root.geometry("%dx%d+0+0"%(width,height))
root.iconbitmap("D:/pictures/icons/images (3).jfif")

root.resizable(False,False)

root.configure(bg='white')

#l1=Label(root,text="Employee Management System",bg="white",fg="blue",font=("constantia",29,"bold"))
#l1.place(x=420,y=0)



#img1

img1=Image.open("D:/pictures/emp/images (7).jpg")
img1=img1.resize((510,140),Image.ANTIALIAS)
photoimg1=ImageTk.PhotoImage(img1)

label=ttk.Label(root,image=photoimg1)
label.place(x=0,y=60)

#img2

img2=Image.open("D:/pictures/emp/images (1).jpg")
img2=img2.resize((510,140),Image.ANTIALIAS)
photoimg2=ImageTk.PhotoImage(img2)

label=ttk.Label(root,image=photoimg2)
label.place(x=510,y=60)

#img3


img3=Image.open("D:/pictures/emp/images (12).jpg")
img3=img3.resize((510,140),Image.ANTIALIAS)
photoimg3=ImageTk.PhotoImage(img3)

label=ttk.Label(root,image=photoimg3)
label.place(x=1020,y=60)

#back img 4

img4=Image.open("D:/pictures/emp/download (10).jpg")
img4=img4.resize((1530,371),Image.ANTIALIAS)
photoimg4=ImageTk.PhotoImage(img4)

label=ttk.Label(root,image=photoimg4)
label.place(x=0,y=192)
#======================Label frame=================

#frame1

lblframe=LabelFrame(root,text='Employee Information',font=('time new roman',16,'bold'),
                    width=1520, height=365,bg="white",fg="green",bd=4)
lblframe.place(x=5, y=198)

#frame2

lblframe1=LabelFrame(lblframe,font=('time new roman',20,'bold'),
                    width=1490, height=250,bg="white",bd=6)
lblframe1.place(x=13, y=5)

#emp id

empid=Label(lblframe,text="Id :",bg="white",font=('constantia',13,'bold'))
empid.place(x=30,y=20)

txtempid=Entry(lblframe,bg="white",width=17,font=
               ('time new roman',13,'bold'),bd=2,textvariable=id1)
txtempid.place(x=160,y=20)

#emp name

empname=Label(lblframe,text="Name :",bg="white",font=('constantia',13,'bold'))
empname.place(x=350,y=20)

txtempname=Entry(lblframe,bg="white",width=17,font=
                 ('time new roman',13,'bold'),bd=2,textvariable=nm1)
txtempname.place(x=490,y=20)

#emp mobile

empmob=Label(lblframe,text="Mobile :",bg="white",font=('constantia',13,'bold'))
empmob.place(x=680,y=20)

txtempmob=Entry(lblframe,bg="white",width=17,font=
                ('time new roman',13,'bold'),bd=2,textvariable=mb1)
txtempmob.place(x=810,y=20)

#emp address

empaddress=Label(lblframe,text="Address :",bg="white",font=('constantia',13,'bold'))
empaddress.place(x=30,y=80)

txtempaddress=Entry(lblframe,bg="white",width=17,font=
                    ('time new roman',13,'bold'),bd=2,textvariable=adr1)
txtempaddress.place(x=160,y=80)

#emp dob

empdob=Label(lblframe,text="DOB :",bg="white",font=('constantia',13,'bold'))
empdob.place(x=350,y=80)

txtempdob=Entry(lblframe,bg="white",width=17,font=
                ('time new roman',13,'bold'),bd=2,textvariable=dob1)
txtempdob.place(x=490,y=80)

#emp Country

empcntry=Label(lblframe,text="Country :",bg="white",font=('constantia',13,'bold'))
empcntry.place(x=680,y=80)

txtempcntry=Entry(lblframe,bg="white",width=17,font=
                  ('time new roman',13,'bold'),bd=2,textvariable=cn1)
txtempcntry.place(x=810,y=80)


#emp Email

empemail=Label(lblframe,text="E-mail :",bg="white",font=('constantia',13,'bold'))
empemail.place(x=30,y=130)

txtempemail=Entry(lblframe,bg="white",width=17,font=
                  ('time new roman',13,'bold'),bd=2,textvariable=em1)
txtempemail.place(x=160,y=130)

#emp marrital status

empmst=Label(lblframe,text="Married Status  :",bg="white",font=('constantia',13,'bold'))
empmst.place(x=350,y=130)

txtempmst=ttk.Combobox(lblframe,width=15,font=
                       ('time new roman',13,'bold')
                ,values=['Married','Unmarried'],textvariable=ms1)
txtempmst.place(x=490,y=130)


#emp qualification

empque=Label(lblframe,text="Qualification :",bg="white",font=('constantia',13,'bold'))
empque.place(x=680,y=130)

txtempque=ttk.Combobox(lblframe,width=15,font=
                       ('time new roman',13,'bold')
                ,values=['Software Engineer','IT Engineer','Mechanical Engineer','Computer Engineer','BCA','MCA','BSC','BTech','MBA','MCom'],textvariable=que1)
txtempque.place(x=810,y=130)

#emp gen

empgen=Label(lblframe,text="Gender :",bg="white",font=('constantia',13,'bold'))
empgen.place(x=30,y=190)

#txtempidprf=ttk.Combobox(lblframe,width=10,font=('time new roman',13,'bold')
                  #,values=['Aadhar Card','Pan Card','Voting Card']
                         #,textvariable=pan1)
#txtempidprf.place(x=30,y=190)

txtempgen=ttk.Combobox(lblframe,width=15,font=('time new roman',13,'bold')
                       ,values=['Male','Female','Other'],textvariable=gen22)
txtempgen.place(x=160,y=190)





#emp dept

empdept=Label(lblframe,text="Department  :",bg="white",font=('constantia',13,'bold'))
empdept.place(x=350,y=190)

txtempdept=ttk.Combobox(lblframe,width=15,font=('time new roman',13,'bold'),
                        values=['HR','Computer','Developer','Tester','Support Staff'],textvariable=dept1)
txtempdept.place(x=490,y=190)

#emp sal

empsal=Label(lblframe,text="Salary :",bg="white",font=('constantia',13,'bold'))
empsal.place(x=680,y=190)

txtempsal=Entry(lblframe,bg="white",width=17,font=
                ('time new roman',13,'bold'),bd=2,textvariable=sal78)
txtempsal.place(x=810,y=190)

#==================label ====================
#img5

img5=Image.open("D:/pictures/emp/download (9).jpg")
img5=img5.resize((210,225),Image.ANTIALIAS)
photoimg5=ImageTk.PhotoImage(img5)

label=ttk.Label(lblframe,image=photoimg5)
label.place(x=1020,y=15)


###########################################################################
ss='Welcome to Employee Management System'

count=0
text=""
#################################Slider label#######################################
sliderlabel=Label(root,text=ss,font=('constantia',25,'italic bold'),
                  relief=RIDGE,borderwidth=0,width=50,bg='white',fg='blue')
sliderlabel.place(x=230,y=3)

introlabel()





#========================Buttons ==============================


b2=Button(lblframe,text="INSERT",bg="blue",fg="white",width=7,
          font=('time new roman',13,'bold'),bd=2,command=insert)
b2.place(x=1400,y=35)


b3=Button(lblframe,text="UPDATE",bg="blue",fg="white",width=7,
          font=('time new roman',13,'bold'),bd=2,command=update)
b3.place(x=1400,y=90)


b4=Button(lblframe,text="DELETE",bg="blue",fg="white",width=7,
          font=('time new roman',13,'bold'),bd=2,command=delete)
b4.place(x=1400,y=150)

b5=Button(lblframe,text="EXIT",bg="blue",fg="white",width=7,
          font=('time new roman',13,'bold'),bd=2,command=root.destroy)
b5.place(x=1400,y=200)

#================================for database================================

#frame3

lblframe3=LabelFrame(lblframe,text="Search Info",font=('time new roman',10,'bold'),
                    width=1490, height=70,bg="white",fg="#EC7063",bd=6)
lblframe3.place(x=13, y=260)

#search label

search2=Label(lblframe3,text="Search By :",bg="orange",fg="black",font=
              ('constantia',14,'bold'),width=10)
search2.place(x=10,y=3)

#combosearch
search3=ttk.Combobox(lblframe3,font=('constantia',13,'bold')
                ,textvariable=combosearch1,width=15,values=["Id","Name","Mobile"])
search3.place(x=160,y=3)

txtsearch3=Entry(lblframe3,font=('constantia',13,'bold'),
                bd=2,textvariable=search1,width=15,)
txtsearch3.place(x=350,y=3)


#show button
b6=Button(lblframe3,text="Show",bg="blue",fg="white",
          font=('time new roman',13,'bold'),bd=2,command=Search,width=15)
b6.place(x=550,y=3)

#show all button

b1=Button(lblframe3,text="Show All",bg="blue",fg="white",width=15,
          font=('time new roman',13,'bold'),bd=2,command=ShowAllRecord)
b1.place(x=750,y=3)


#new  button

b1=Button(lblframe3,text="Clear",bg="blue",fg="white",width=15,
          font=('time new roman',13,'bold'),bd=2,command=new)
b1.place(x=1250,y=3)




l1=Label(lblframe3,text="Wear a Mask ",bg="white",fg="red",font=('constantia',19,'bold'))
l1.place(x=1020,y=0)





"""#frame5

lblframe4=LabelFrame(root,width=1518,height=270,font=
                     ('constantia',14,'bold'),bd=3)
lblframe4.place(x=5,y=565)"""







#####################################treeview##############################


tv['column']=('Id','Name','Mobile','Address','Dob','Country','Email','Marriedstatus','Qualification','Gender','Dept','Salary')

tv.place(x=8,y=10)

#for selectview method

tv.bind("<<TreeviewSelect>>",selectview)




# tv column


tv.column('#0',anchor=CENTER,width=0,minwidth=0)

tv.column('Id',anchor=CENTER,width=60)

tv.column('Name',anchor=CENTER,width=160)

tv.column('Mobile',anchor=CENTER,width=110)

tv.column('Address',anchor=CENTER,width=180)

tv.column('Dob',anchor=CENTER,width=100)

tv.column('Country',anchor=CENTER,width=100)

tv.column('Email',anchor=CENTER,width=240)

tv.column('Marriedstatus',anchor=CENTER,width=100)

tv.column('Qualification',anchor=CENTER,width=130)

tv.column('Gender',anchor=CENTER,width=100)

tv.column('Dept',anchor=CENTER,width=110)

tv.column('Salary',anchor=CENTER,width=100)


#tv heading



tv.heading('#0',anchor=CENTER,text='')

tv.heading('Id',anchor=CENTER,text='Id')

tv.heading('Name',anchor=CENTER,text='Name')

tv.heading('Mobile',anchor=CENTER,text='Mobile')

tv.heading('Address',anchor=CENTER,text='Address')

tv.heading('Dob',anchor=CENTER,text='DOB')

tv.heading('Country',anchor=CENTER,text='Country')

tv.heading('Email',anchor=CENTER,text='Email')

tv.heading('Marriedstatus',anchor=CENTER,text='Marriedstatus')


tv.heading('Qualification',anchor=CENTER,text='Qualification')

tv.heading('Gender',anchor=CENTER,text='Gender')

tv.heading('Dept',anchor=CENTER,text='Dept')

tv.heading('Salary',anchor=CENTER,text='Salary')



#tv.insert(parent='',index=0,value=('1','jayesh','jalgaon','Male'))


root.mainloop()
