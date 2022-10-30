from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector as mcp
from tkinter import messagebox
import csv
import subprocess
import numpy
import pandas as pd
import time
global class1
#df.to_sql(con=con, name='table_name_for_df', if_exists='replace', flavor='mysql')
root=Tk()
root.geometry("1366x786")
mydb=mcp.connect(host='localhost',user='root',password='abc123*',port=3306)
mycursor=mydb.cursor()
mycursor.execute("create database if not exists pro")
mydb=mcp.connect(host='localhost',user='root',password='abc123*',port=3306,database="pro")
mycursor=mydb.cursor()
sql="create table if not exists classteachers ( uniqueid char(50),class char(5),sec char(5),filename char(50))"
mycursor.execute(sql)
def exit(): 
    root.destroy()    
##########TEACHER HOME PAGE ########################

def teacher_homepg( ):
    global class1
    def update_marks():
        def excel2():
            global df
            global tname
            df1 = pd.read_excel(tname+'.xlsx')
            print(df1.head())
            time.sleep(0.5)
            for row in df1.iterrows():
                tuple_data = row[1]
                print(list(tuple_data.values))
                
                
            #df1.to_sql(con=mydb, name=tname, if_exists='replace')

        def excel():
                
            global class4
            global sec4
            global tname
            exam=c.get()
            tname=str(class4+sec4+c.get())
            print(tname)
            global file4
            sql="create table if not exists "+tname+" ( select id, name from "+ file4+" ORDER BY ELECTIVE ,name)"
            print(sql)
            mycursor.execute(sql)
            mydb.commit()
            mycursor.execute("select internals from "+class4+"examslist where exams_in_class_"+class4+"='"+exam+"'")
            ab=(mycursor.fetchall())[0][0]
            print(ab)
            mycursor.execute("select * from "+ class4+sec4+"defaultsubjects")
            check=[]
            for i in mycursor.fetchall():
                check.append(i[0])                            
            for i in check:
                sql= "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='"+tname+"'"
                mycursor.execute(sql)
                if (i,) not in mycursor.fetchall():
                    sql="alter table "+class4+sec4+c.get()+ " add ("+i+" integer(20))"
                    print(sql)
                    mycursor.execute(sql)
                    mydb.commit()
                    if ab.lower()=="yes":
                        sql="alter table "+class4+sec4+c.get()+ " add ( internals"+i+" integer(20))"
                        print(sql)
                        mycursor.execute(sql)
                        mydb.commit()
                        print("sarah")
            sql= "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='"+class4+sec4+"elective'"
            mycursor.execute(sql)
            
            #mycursor.execute("select * from "+class4+sec4+"elective")
            elec=[]
            for j in (mycursor.fetchall()):
                #print(j)                
                mycursor.execute("select "+j[0]+" from "+class4+sec4+"elective")
                elec2=""

                for m in mycursor.fetchall():
                    for k in m:
                        #print(m,"ele in column")
                        if k !=None:
                            #elec2.append(k)
                            #elec2.append("or")
                            elec2+=(k)
                            elec2+=("_or_")
                #print(elec2)
                elec2=elec2[:len(elec2)-3]
                elec.append(elec2)
            #print(elec,"electives")
                for i in elec:
                    sql= "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='"+tname+"'"
                    mycursor.execute(sql)
                    if (i,) not in mycursor.fetchall():
                        sql="alter table "+class4+sec4+c.get()+ " add ("+i+" integer(20))"
                        #print(sql)
                        mycursor.execute(sql)
                        mydb.commit()
                        if ab.lower()=="yes":
                            sql="alter table "+class4+sec4+c.get()+ " add ( internals_"+i+" integer(20))"
                            #print(sql)
                            mycursor.execute(sql)
                            mydb.commit()
                            #print("sarah")       
            time.sleep(3)
            global df
            df = pd.read_sql('SELECT * FROM '+tname, con=mydb)
            print("Sucess")
            df.to_excel(str(tname+".xlsx"),index=False)
            time.sleep(3)
            print("sucess2")
            #exl=str("'start D:\AAPYTHON\project\)" + tnmae + ".xlsx'"
            subprocess.Popen('start D:\AAPYTHON\project\\'+tname+'.xlsx' ,shell=True)
            print("hi")
            #global class4
            #global sec4           
        sql="select uniqueid from classteachers"
        mycursor.execute(sql)        
        if (username,)in mycursor.fetchall():
            sql="select class,sec,filename from classteachers where uniqueid='"+username+"'"
            mycursor.execute(sql)
            class3=mycursor.fetchall()
            global class4
            global sec4
            global file4
            class4=class3[0][0]
            sec4=class3[0][1]
            file4=class3[0][2]
            def stubck2():
                root.destroy()
                teacher_homepg()
            try:
                global root
                root.destroy()
            except():
                pass
            root=Tk()
            root.geometry("1366x786")
            global class1
            frame5=Frame(root,bg='turquoise2',width=1340, height=700, highlightbackground="salmon", highlightcolor="salmon" ,highlightthickness=15)
            frame5.place(relwidth=1,relheight=1)
            load=Image.open('D:\AAPYTHON\project\pic (in use)\harshh.jpg')
            bg=ImageTk.PhotoImage(load)
            bglabel=Label(frame5,image=bg)
            bglabel.image = bg
            bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
            global class1
            global sec1
            #global class4
            #global sec4
            label = Label(frame5, text=" UPDATE MARKS "+class4+" -"+ sec4, relief=RAISED ,font=('segoe script', 17,'bold'),bg='orange',fg='snow' ,bd=8)
            label.place(relx=0.35,rely=0.01)
            label = Label(frame5, text="Select the exam", relief=RAISED ,font=('dubai light', 17,'bold'),bg='red',fg='snow' ,bd=8)
            label.place(relx=0.30,rely=0.22)
            sql=("show tables like '"+ class4+"examslist"+"' ")
            mycursor.execute(sql)
            lst=mycursor.fetchall()
            if len(lst)!=0:            
                mycursor.execute("SELECT Exams_in_Class_" +class4+" FROM "+class4+"examslist" )                        
                lst=mycursor.fetchall()
                if lst==[]:
                    label = Label(frame5, text=" NO EXAMS SO FAR !", relief=RAISED ,font=('dubai light', 15,'bold'),bg='red',fg='snow' ,bd=8)
                    label.place(relx=0.27,rely=0.65)
                else:
                    lst2=[]
                    for i in lst:
                        lst2+=[i[0]]
                    c=StringVar()
                    droplist=OptionMenu(frame5,c, *lst2)
                    droplist.config(width=15)
                    c.set('Select the exam')
                    droplist.place(relx=0.50,rely=0.23)
            bck_bt=Button(frame5,text=' HOME PAGE ',font=('dubai light', 15,'bold'),command=stubck2,bd=5)
            bck_bt.place(relx=0.0,rely=0.00)
            button=Button(frame5,text='   IMPORT TO EXCEL   ',bd=7,bg="thistle3",font=('dubai light', 15,'bold'),command=excel)
            button.place(relx=0.43,rely=0.38)
            button=Button(frame5,text='   IMPORT FROM EXCEL   ',bd=7,bg="thistle3",font=('dubai light', 15,'bold'),command=excel2)
            button.place(relx=0.42,rely=0.48)

            
        else:
            messagebox.showinfo("ERROR","KINDLY FILL YOUR ACADEMIC \n YEAR DETAILS TO ACCESS THIS PAGE")
        def bck():
            global root1
            root1.destroy()
            teacher_homepg()
    def update_tea_aca():
        def subject_page():
            def stubck2():
                    root.destroy()
                    teacher_homepg()
            root=Tk()
            root.geometry("1366x786")
            def electives():
                def ok():
                    try:
                        global num
                        num=file.get()
                        frame9.destroy()
                    except:
                        pass
                    def electives1():
                        global thing
                        global mister
                        if mister ==1:
                                    global M,lst1
                                    global chk
                                    M=[mm.get() for mm in M]
                                    chk=[sub for yes,sub in zip(M,lst1) if yes]
                                    print(chk)
                                    mycursor.execute("drop table if exists "+class4+sec4+"elective")
                                    mydb.commit()
                                    mycursor.execute("create table "+class4+sec4+"elective( elec1 char(25))")
                                    mydb.commit()
                                    for i in chk:
                                        sql="insert into "+class4+sec4+"elective values('"+i+"')"
                                        mycursor.execute(sql)
                                        mydb.commit()
                                        mister=2
                                        thing=2
                                    messagebox.showinfo("INFO","SUCESSFULLY UPDATED \n ELECTIVE SUBJECTS")
                                    ok()
                        else:
                                    sql="alter table "+ class4+sec4+"elective add (elec" +str(mister)+" char(25))"
                                    print(sql)
                                    mycursor.execute(sql)
                                    mydb.commit()
                                    #global M,lst1
                                    #global chk
                                    M=[mm.get() for mm in M]
                                    chk=[sub for yes,sub in zip(M,lst1) if yes]
                                    print(chk)
                                    for i in chk:
                                        sql="insert into "+class4+sec4+"elective (elec"+str(mister)+") values('"+i+"')"
                                        mycursor.execute(sql)
                                        mydb.commit()
                                    messagebox.showinfo("INFO","SUCESSFULLY UPDATED \n ELECTIVE SUBJECTS")
                                    mister+=1
                                    thing=mister
                                    ok()
                    global thing
                    global mister
                #    thing=1
                    while thing< int(num)+1:
                                mister=thing
                                print(thing)
                                main_frame=Frame(frame5,width=500,height=1500)
                                #main_frame.pack(fill=BOTH,expand=1)
                                main_frame.place(relx=0.5,rely=0.12)
                                my_canvas=Canvas(main_frame,width=500)
                                my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
                                my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
                                my_scrollbar.pack(side=RIGHT,fill=Y)
                                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                                my_canvas.bind('<Configure>',lambda e :my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                                frame7=Frame(my_canvas,bg='pink',width=500)
                                #frame7=Frame(my_canvas,bg='pink',width=500,height=600,highlightbackground="pink", highlightcolor="salmon" ,highlightthickness=15)
                                my_canvas.create_window((0,0),window=frame7,anchor ="nw")
                                sm="yes"
                                while sm=="yes":
                                    load=Image.open('D:\AAPYTHON\project\pic (in use)\harsh1.jpg')
                                    bg=ImageTk.PhotoImage(load)
                                    bglabel=Label(frame7,image=bg)
                                    bglabel.image = bg
                                    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
                

                                    label = Label(frame7, text="SELECT THE ELECTIVES -"+str(thing), relief=RAISED ,font=('dubai light', 17,'bold'),bg='red',fg='snow' ,bd=8)
                                    label.grid(row=0)
                                    sm="no"                    
                                global M

                                M=[0 for _ in lst1]
                                C3=[0 for _ in lst1]
                                count=1
                                for i, sub in zip(range(len(lst1)), lst1):
                                    M[i]= IntVar()                
                                    C3[i] = Checkbutton(frame7, text = sub, onvalue = 1, offvalue = 0,font=('dubai light', 17,'bold'),variable=M[i])
                                    C3[i].grid(row=count)
                                    count+=1
                                stud_bt=Button(frame7,text='UPDATE ELECTIVES -'+str(thing),font=('dubai light', 13 ,'bold'),bg='thistle3',fg='snow',bd=7,command=electives1)
                                stud_bt.grid(row=count+1)
                                thing=int(num)+1
                    else:
                        if mister>int(num):
                            root.destroy()
                            teacher_homepg()
                    
                global m,lst1
                m = [mm.get() for mm in m]
                check = [sub for yes,sub in zip(m,lst1) if yes]
                print(check)
                global username
                sql="select class,sec from classteachers where uniqueid='"+username+"'"
                mycursor.execute(sql)
                class3=mycursor.fetchall()
                global class4
                global sec4
                class4=class3[0][0]
                sec4=class3[0][1]
                mycursor.execute("delete from "+class4+sec4+"defaultsubjects")
                mydb.commit()
                for i in check:
                    print(i)
              
                    sql="insert into "+class4+sec4+"defaultsubjects(default_subjects) values('"+i+"')"
                    mycursor.execute(sql)
                    mydb.commit()
                
                messagebox.showinfo("INFO","SUCESSFULLY UPDATED \n DEFAULT SUBJECTS")                
                global main_frame
                main_frame.destroy()
                global thing
                thing=1
                frame9=Frame(frame5,bg='turquoise2',width=500, height=500, highlightbackground="salmon", highlightcolor="salmon" ,highlightthickness=15)
                frame9.place(relx=0.5,rely=0.12)
                load=Image.open('D:\AAPYTHON\project\pic (in use)\harsh1.jpg')
                bg=ImageTk.PhotoImage(load)
                bglabel=Label(frame9,image=bg)
                bglabel.image = bg
                bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
                


                
                label = Label(frame9, text="Type the number of elective(s) (if any)", relief=RAISED ,font=('dubai light', 17,'bold'),bg='red',fg='snow' ,bd=8)
                label.place(relx=0.08,rely=0.05)
                file= Entry(frame9, bd =7,width=4,selectborderwidth=1,relief='groove',font=('dubai light', 14,'bold'),fg='black')
                file.place(relx=0.40,rely=0.41)
                sql=("select Subjects_in_Class_"+str(class4)+" from "+ str(class4)+"subjectslist")
                mycursor.execute(sql)
                lst=mycursor.fetchall()
                #global lst1
                lst1=[]
                for i in lst:
                    lst1.append(i[0])
                stud_bt=Button(frame9,text='ok',font=('dubai light', 18 ,'bold'),bg='thistle3',fg='snow',bd=7,command=ok,width=6)
                stud_bt.place(relx=0.44,rely=0.6)
            frame5=Frame(root,bg='turquoise2',width=1340, height=700, highlightbackground="salmon", highlightcolor="salmon" ,highlightthickness=15)
            frame5.place(relwidth=1,relheight=1)
            load=Image.open('D:\AAPYTHON\project\pic (in use)\space.jpg')
            bg=ImageTk.PhotoImage(load)
            bglabel=Label(frame5,image=bg)
            bglabel.image = bg
            bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
                

            global class1
            global sec1
            if class1.get()!="Select your class":
                label = Label(frame5, text="UPDATE SUBJECTS of "+ class1.get()+"-"+sec1.get(), relief=RAISED ,font=('dubai light', 17,'bold'),bg='red',fg='snow' ,bd=8)
                label.place(relx=0.25,rely=0.01)
            else:
                label = Label(frame5, text="UPDATE SUBJECTS of your class", relief=RAISED ,font=('dubai light', 17,'bold'),bg='red',fg='snow' ,bd=8)
                label.place(relx=0.25,rely=0.01)
                
            sql=("select Subjects_in_Class_"+str(class1.get())+" from "+ str(class1.get())+"subjectslist")
            mycursor.execute(sql)
            lst=mycursor.fetchall()
            global lst1
            lst1=[]
            for i in lst:
                lst1.append(i[0])
            global main_frame
            main_frame=Frame(frame5,width=500,height=1500)
            #main_frame.pack(fill=BOTH,expand=1)
            main_frame.place(relx=0.05,rely=0.12)
            my_canvas=Canvas(main_frame,width=500)
            my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
            my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT,fill=Y)
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>',lambda e :my_canvas.configure(scrollregion=my_canvas.bbox("all")))
            frame6=Frame(my_canvas,bg='pink')
            #frame7=Frame(my_canvas,bg='pink',width=500,height=600,highlightbackground="pink", highlightcolor="salmon" ,highlightthickness=15)
            my_canvas.create_window((0,0),window=frame6,anchor ="nw")
            sm="yes"
            while sm=="yes":                    
                load=Image.open('D:\AAPYTHON\project\pic (in use)\harsh1.jpg')
                bg=ImageTk.PhotoImage(load)
                bglabel=Label(frame6,image=bg)
                bglabel.image = bg
                bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
                

                label = Label(frame6, text="SELECT THE DEFAULT SUBJECTS", relief=RAISED ,font=('segoe script', 17,'bold'),bg='red',fg='snow' ,bd=8)
                    #label.place(relx=0.0,rely=0.01)
                label.grid(row=0)
                    #stud_bt.pack()
                sm="no"                    
            '''
            frame6=Frame(frame5,bg='pink',width=500, height=700, highlightbackground="pink", highlightcolor="salmon" ,highlightthickness=15)
            frame6.place(relx=0.0,rely=0.09)
            label = Label(frame6, text="SELECT THE DEFAULT SUBJECTS", relief=RAISED ,font=('segoe script', 17,'bold'),bg='red',fg='snow' ,bd=8)
            label.place(relx=0.0,rely=0.01)
            j=0.05
            '''
            global m
            m=[0 for _ in lst1]
            c1=[0 for _ in lst1]
            count=1
            for i, sub in zip(range(len(lst1)), lst1):
                
                #j+=0.07
                m[i]= IntVar()
                c1[i]= Checkbutton(frame6, text = sub, onvalue = 1, offvalue = 0,font=('segoe script', 17,'bold'),width=15,variable=m[i])
                #c1[i].place(relx=0.01,rely=j)
                c1[i].grid(row=count)
                count+=1
            bck_bt=Button(frame5,text=' HOME PAGE ',font=('segoe print', 15,'bold'),command=stubck2,bd=5)
            bck_bt.place(relx=0.0,rely=0.00)           
            stud_bt=Button(frame6,text='  UPDATE DEFAULT SUBJECTS   ',font=('dubai light', 13 ,'bold'),bg='thistle3',fg='snow',bd=7,command=electives)
            #stud_bt.place(relx=0.44,rely=0.85)
            stud_bt.grid(row=count)
        def submit():
            filename=file.get()
            global class1
            if len(filename)!=0 and class1.get()!="Select your class" and sec1.get()!="Select your sec":
                fh=open(file.get(),"r")
                redr=csv.reader(fh)
                m=len(filename)
                file2=filename[:m-4]
                try:
                    sql=("delete from "+str(file2));
                    mycursor.execute(sql)
                    mydb.commit()
                except:
                    pass
                for rec in redr:
                    id1=rec[0]
                    name=rec[1]
                    class2=rec[2]
                    group=rec[3]
                    electives=rec[4]
                    dob=rec[5]
                    bgroup=rec[6]
                    address=rec[7]
                    fname=rec[8]
                    mname=rec[9]
                    mail1=rec[10]
                    mail2=rec[11]
                    m=len(filename)
                    file2=filename[:m-4]
                    sql=("create table IF NOT EXISTS " + str(file2) + " (id char(20),name char(50),class char(20),grp char(20),elective char(30),dob char(20),bgroup char(20),address char(200),fname char(30),mname char(30),mail1 char(50),mail2 char(50))")
                    mycursor.execute(sql)
                    mydb.commit()                   
                    sql= "insert into "+str(file2)+" values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    stud=(id1,name,class2,group,electives,dob,bgroup,address,fname,mname,mail1,mail2)
                    mycursor.execute(sql,stud)
                    mydb.commit()## student's biodata is written to sql .
                messagebox.showinfo("INFO","SUCESSFULLY UPDATED \n STUDENTS' BIO DATA")
                sql="create table if not exists classteachers ( uniqueid char(50),class char(5),sec char(50),filename char(20))"
                mycursor.execute(sql)
                mycursor.execute("select uniqueid from classteachers")
                if ( (username,) not in mycursor.fetchall()):
                    sql="insert into classteachers values ('" +username +"','"+class1.get()+"','"+sec1.get()+"','"+file2+"')"
                    mycursor.execute(sql)
                else:
                    sql="update classteachers set class='"+class1.get()+"',sec='"+sec1.get()+"',filename='"+file2+"' where uniqueid='"+username+"'"                    
                    mycursor.execute(sql)               
                sql=("create table if not exists  " + str(class1.get()) + str(sec1.get()) +"defaultsubjects" + " (Default_Subjects char(100))")
                mycursor.execute(sql)
                sql=("create table if not exists  " + str(class1.get()) + str(sec1.get()) +"elective" + " (electives char(100))")
                mycursor.execute(sql)
                
                mydb.commit()
                root.destroy()
                subject_page()
            else:
                    messagebox.showinfo("ERROR","ENTRY ERROR")
        def stubck1():
            root.destroy()
            teacher_homepg()

        frame5=Frame(root,bg='turquoise2',width=1340, height=700, highlightbackground="salmon", highlightcolor="salmon" ,highlightthickness=15)
        frame5.place(relwidth=1,relheight=1)
        load=Image.open('D:\AAPYTHON\project\pic (in use)\harsh3.jpg')
        bg=ImageTk.PhotoImage(load)
        bglabel=Label(frame5,image=bg)
        bglabel.image = bg
        bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
        label = Label(frame5, text="CLASS TEACHER OF :", relief=RAISED ,font=('dubai light', 20,'bold'),bg='red',fg='snow' ,bd=8)
        label.place(relx=0.30,rely=0.01)
        label = Label(frame5, text="    Select your class & section    ", relief=RAISED ,font=('dubai light', 17,'bold'),bg='red',fg='snow' ,bd=8)
        label.place(relx=0.10,rely=0.22)
        global class1
        global filename
        global sec1
        Class =["XI","XII"]
        class1=StringVar()
        droplist=OptionMenu(root,class1, *Class)
        droplist.config(width=20)
        class1.set('Select your class')
        droplist.place(relx=0.45,rely=0.24)
        list_of_section=[ 'A','B','C','D']
        sec1=StringVar()
        droplist=OptionMenu(root,sec1, *list_of_section)
        droplist.config(width=20)
        sec1.set('Select your sec')
        droplist.place(relx=0.60,rely=0.24)
        label=Label(frame5, text="Enter the name of your file", relief=RAISED ,font=('dubai light', 16,'bold'),bg='red',fg='snow',bd=10)
        label.place(relx=0.10,rely=0.40)
        file= Entry(frame5, bd =7,width=15,selectborderwidth=1,relief='groove',font=('dubai light', 14,'bold'),fg='black')
        file.place(relx=0.40,rely=0.41)
        stud_bt=Button(frame5,text='   UPDATE   ',font=('segoe print', 15 ,'bold'),width=9,bg='thistle3',fg='black',bd=9,command=submit)
        stud_bt.place(relx=0.44,rely=0.55)
        bck_bt=Button(frame5,text='  BACK  ',font=('dubai light', 15,'bold'),command=stubck1,bd=5)
        bck_bt.place(relx=0.80,rely=0.05)
        ext_bt=Button(frame5,text='  QUIT  ',font=('dubai light', 15,'bold'),command=exit,bd=5)
        ext_bt.place(relx=0.90,rely=0.05)
    def teabck():
        root.destroy()
        teacher_homepg()
    def update1():
            def update():                
                field=c.get()
                if field== "Name" :
                    field="name"
                elif field== 'Father"S Name':
                    field="fname"
                elif field== "Mother's Name":
                    field='mname'
                elif field =="Address":
                    field='addr'
                elif field ==" Spouses's Name ":
                    field='sanme'
                elif field == "  Email address ":
                    field='email'
                elif field == "Contact number":
                    field= 'contact'
                elif field == "Emergency contact number":
                    field='emerph'
                elif field =="Degrees":
                    filed='degrees'
                v1=E1.get()
                if len(v1)==0:
                    messagebox.showinfo("ERROR",'NO ENTRY FOUND')
                else:
                    if field !='Select The Field':
                        global username
                        sql="UPDATE teabiodata SET "+ field +'= "' + v1 +'" WHERE id1 = "' + username +'"'
                        mycursor.execute(sql)
                        mydb.commit( )
                        messagebox.showinfo("INFO",'BIO DATA SUCESSFULLY UPDATED')
                        update1()
                    else:
                        messagebox.showinfo("ERROR",'NO FIELD SELECTED')

            frame2 = Frame(displayframe, highlightbackground="skyblue1", highlightcolor="red", highlightthickness=10, width=600, height=400, bd= 0,bg='gray1')
            frame2.place(relx=0.18,rely=0.28)
            load=Image.open('D:\AAPYTHON\project\pic (in use)\harsh1.jpg')
            bg=ImageTk.PhotoImage(load)
            bglabel=Label(frame2,image=bg)
            bglabel.image = bg
            bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
            label = Label( frame2, text=" UPDATE YOUR BIO DATA ", relief=RAISED ,font=('dubai light', 18,'bold'),bg='gray1',fg='deep pink' ,bd=9)
            label.place(relx=0.1,rely=0.09 )
            list_of_field=[ 'Name','Father"S Name',"Mother's Name","Address"," Spouses's Name "," Email address ","Contact number","Emergency contact number","Degrees"]
            c=StringVar()
            droplist=OptionMenu(frame2,c, *list_of_field)
            droplist.config(width=15)
            c.set('Select The Field')
            droplist.place(relx=0.1,rely=0.42)
            E1 = Entry(frame2, bd =7,width=22,selectborderwidth=2,relief='groove',font=('dubai light', 14,'bold'),fg='black')
            E1.place(relx=0.35,rely=0.42)
            bck_bt=Button(frame2,text='  BACK  ',font=('segoe script', 11,'bold'),command=teabck,bd=6)
            bck_bt.place(relx=0.8,rely=0.08)
            Button(frame2, text='UPDATE',relief ='raised',bd=10,width=15,fg="black",bg='white',command=update,font=('segoe script', 13 ,'bold')).place(relx=0.35,rely=0.7)
            frame5.destroy()  
    ## root should be inside this loop for image to come.
    global root
    root=Tk()
    root.geometry("1366x786")
    frame5=Frame(root,bg='cadet blue')
    frame5.place(relx=0,rely=0,relheight=1,relwidth=0.18)
    global displayframe
    displayframe=Frame(root,bg="brown3")
    displayframe.place(relx=0.19,rely=0.00,relheight=1,relwidth=0.85)
    load=Image.open('D:\AAPYTHON\project\pic (in use)\Teacher bg.jpg')
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(frame5,image=bg)
    bglabel.image = bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    label=Label(displayframe, text=" DAV SR SECONDARY SCHOOL,CHENNAI.", relief=RAISED ,font=('segoe script', 20,'bold'),bg='brown3',fg='snow' ,bd=10)
    label.place(relx=0.28,rely=0.01)
    label=Label(displayframe, text=" TEACHER'S HOME PAGE ", relief=RAISED ,font=('segoe script', 20,'bold'),bg='brown3',fg='snow' ,bd=10)
    label.place(relx=0.35,rely=0.10)

    label=Label(frame5, text="I want to ", relief=RAISED ,font=('segoe script', 20,'bold'),bg='brown3',fg='snow' ,bd=10)
    label.place(relx=0.012,rely=0.10)

    img1=ImageTk.PhotoImage(Image.open ("D:\\AAPYTHON\\project\\pic (in use)\\centum.jpg"))
    stud_bt=Button(frame5,compound='left',text="ACCESS MARKS",font=('segoe script', 13 ,'bold'),bg='brown3',fg='snow',bd=5,cursor="hand2",image=img1)
    stud_bt.place(relx=0.015,rely=0.20)

    img2=ImageTk.PhotoImage(Image.open ("D:\\AAPYTHON\\project\\pic (in use)\\mark logo.jpg"))
    stud_bt=Button(frame5,compound='left',text="UPDATE MARKS",font=('segoe script', 13 ,'bold'),bg='brown3',fg='snow',bd=5,cursor='hand2',image=img2,command=update_marks)
    stud_bt.place(relx=0.015,rely=0.30)
    img3=ImageTk.PhotoImage(Image.open ("D:\\AAPYTHON\\project\\pic (in use)\\report card logo.png"))
    stud_bt=Button(frame5,compound='left', text="GERNERATE \n REPORT CARD",font=('segoe script', 13 ,'bold'),bg='brown3',fg='snow',bd=5,cursor='hand2',image=img3)
    stud_bt.place(relx=0.015,rely=0.40)
    img4=ImageTk.PhotoImage(Image.open ("D:\\AAPYTHON\\project\\pic (in use)\\profile logo.png"))
    stud_bt=Button(frame5, text="MODIFY MY PROFILE",font=('segoe script', 13 ,'bold'),bg='brown3',command=update1,fg='snow',cursor='hand2',image=img4, compound='left')
    stud_bt.place(relx=0.015,rely=0.550)
    img5=ImageTk.PhotoImage(Image.open ("D:\\AAPYTHON\\project\\pic (in use)\\bio data logo.png"))
    stud_bt=Button(frame5, text="UPDATE MY \n ACADEMIC YR \n DETAILS",command=update_tea_aca,font=('segoe script', 13 ,'bold'),bg='brown3',fg='snow',cursor='hand2',image=img5, compound='left')
    stud_bt.place(relx=0.015,rely=0.65)
    img=ImageTk.PhotoImage(Image.open ("D:\\AAPYTHON\\project\\pic (in use)\\sign out img.jpg"))
    button=Button(frame5,text=' SIGN OUT',command=root.destroy,cursor='hand2',fg='snow',bg='brown3',compound="left",font=('segoe script', 15,'bold'),image=img)
    button.place(relx=0.0,rely=0.85)
    root.mainloop( )    
###### TEACHER BIO DATA  ######################
def tea_bio():
    global username
    def stubck1():
        frame5.destroy
        #mnfrm()
    mycursor.execute("CREATE TABLE IF NOT EXISTS teabiodata ( name char(50),id1 char(10),fname char(50),mname char(50),sanme char(50),dob char(20),bgroup char(20),email char(50),contact char(15),addr char(80),yrjn char(10),degrees char(50),emerph char(15),mainsub char(50))")
    def submit():
        global username
        name_var=tk.StringVar() 
        yrjn_var=tk.StringVar() 
        name=E1.get()
        fname=E2.get()
        mname=E3.get()
        sanme=E4.get()
        #dob=E5.get()
        dob=(str(m.get())+'.'+ str(t.get())+'.20'+str(u.get()))
        bgroup=E6.get()
        email=E7.get()
        contact=E8.get()
        addr=E9.get()
        yrjn=E10.get()
        degrees=E11.get()
        emerph=E12.get()
        mainsub=E13.get()
        id1=E14.get()

        name_var.set("") 
        yrjn_var.set("")

        if len(name)!=0 and len(fname)!=0 and len(mname) !=0 and len(sanme)!=0 and len(bgroup)!=0 and len(email)!=0 and len(contact)!=0 and len(addr)!=0 and len(yrjn)!=0 and len(degrees)!=0 and len(emerph)!=0 and len(mainsub)!=0 and len(id1)!=0 and m.get()!= "Select your date"and  t.get()!="Select your month" and u.get()!="Select your year":       
            global username
            if id1 != username:
                messagebox.showinfo("ERROR",'wrong UNIQUE ID')
            else:    
                sqlformula="INSERT INTO teabiodata VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                stud=(name,id1,fname,mname,sanme,dob,bgroup,email,contact,addr,yrjn,degrees,emerph ,mainsub)
                mycursor.execute(sqlformula,stud)
                mydb.commit()
                root.destroy()
                teacher_homepg( )
        else:
            messagebox.showinfo("ERROR",'INCOMPLETE FORM') 
            root.destroy()

    frame5=Frame(root,bg='cadet blue',width=1340, height=700, highlightbackground="salmon", highlightcolor="salmon" ,highlightthickness=15)
    frame5.place(relwidth=1,relheight=1)      
    load=Image.open('D:\AAPYTHON\project\pic (in use)\page.jpg')
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(frame5,image=bg)
    bglabel.image = bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    label = Label(frame5, text="       TEACHER BIO DATA       ", relief=RAISED ,font=('segoe print', 20,'bold'),bg='blue',fg='black' ,bd=15)
    label.place(relx=0.33,rely=0.03)
    L1 = Label(frame5, text=" TEACHER'S NAME ",font=('dubai light', 18,'bold'),bg='ivory3',fg='black',relief='raised',bd=8)
    L1.place(relx=0.02,rely=0.15)
    E1 = Entry(frame5, bd =9,width=19,selectborderwidth=2,relief='groove',font=('dubai light', 18,'bold'),fg='black')
    E1.place(relx=0.21,rely=0.15)

    L1 = Label(frame5, text=" UNIQUE ID ",font=('dubai light', 18,'bold'),bg='ivory3',fg='black',relief='raised',bd=8)
    L1.place(relx=0.48,rely=0.15)
    E14 = Entry(frame5, bd =9,width=19,selectborderwidth=2,relief='groove',font=('dubai light', 18,'bold'),fg='black')
    E14.place(relx=0.78,rely=0.15)
    global username
    E14.insert(END, username)
    L1 = Label(frame5, text="FATHER'S NAME",font=('dubai light', 18,'bold'),bg='ivory3',fg='black',relief='raised',bd=8)
    L1.place(relx=0.02,rely=0.25)
    E2 = Entry(frame5, bd =9,width=19,selectborderwidth=2,relief='groove',font=('dubai light', 18,'bold'),fg='black')
    E2.place(relx=0.19,rely=0.25)

    L1 = Label(frame5, text=" MOTHER'S NAME ",font=('dubai light', 18,'bold'),bg='ivory3',fg='black',relief='raised',bd=8)
    L1.place(relx=0.02,rely=0.35)
    E3 = Entry(frame5, bd =9,width=19,selectborderwidth=2,relief='groove',font=('dubai light', 18,'bold'),fg='black')
    E3.place(relx=0.20,rely=0.35)

    L1 = Label(frame5, text="SPOUSE'S NAME ",font=('dubai light', 18,'bold'),bg='ivory3',fg='black',relief='raised',bd=8)
    L1.place(relx=0.02,rely=0.45)
    E4 = Entry(frame5, bd =9,width=19,selectborderwidth=2,relief='groove',font=('dubai light', 18,'bold'),fg='black')
    E4.place(relx=0.19,rely=0.45)

    L1 = Label(frame5, text="DATE OF BIRTH",font=('dubai light', 18,'bold'),bg='ivory3',fg='black',relief='raised',bd=8)
    L1.place(relx=0.02,rely=0.55)
    # options for Date
    list_of_dates=[ '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    m=StringVar()
    droplist=OptionMenu(root,m, *list_of_dates)
    droplist.config(width=15)
    m.set('Select your date')
    droplist.place(relx=0.17,rely=0.55)
    # OPTIONS FOR MONTH
    list_of_months=[ '1','2','3','4','5','6','7','8','9','10','11','12']
    t=StringVar()
    droplist=OptionMenu(root,t, *list_of_months)
    droplist.config(width=15)
    t.set('Select your month')
    droplist.place(relx=0.27,rely=0.55)
    #option fr yr   #keep years from 1965 - 2000
    list_of_years=['60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91']
    u=StringVar()
    droplist=OptionMenu(root,u, *list_of_years)
    droplist.config(width=15)
    u.set('Select your year')
    droplist.place(relx=0.37,rely=0.55)

    L1 = Label(frame5, text="BLOOD GROUP",font=('dubai light', 18,'bold'),bg='ivory3',fg='black',relief='raised',bd=8)
    L1.place(relx=0.02,rely=0.65)
    E6 = Entry(frame5, bd =9,width=19,selectborderwidth=2,relief='groove',font=('dubai light', 18,'bold'),fg='black')
    E6.place(relx=0.19,rely=0.65)

    L1 = Label(frame5, text="EMAIL ADDRESS",font=('dubai light', 18,'bold'),bg='ivory3',fg='black',relief='raised',bd=8)
    L1.place(relx=0.02,rely=0.75)
    E7 = Entry(frame5, bd =9,width=19,selectborderwidth=2,relief='groove',font=('dubai light', 18,'bold'),fg='black')
    E7.place(relx=0.19,rely=0.75)

    L1 = Label(frame5, text="CONTACT NO",font=('dubai light', 18,'bold'),bg='ivory3',fg='black',relief='raised',bd=8)
    L1.place(relx=0.48,rely=0.55)
    E8 = Entry(frame5, bd =9,width=19,selectborderwidth=2,relief='groove',font=('dubai ligjht', 18,'bold'),fg='black')
    E8.place(relx=0.78,rely=0.55)
    L1 = Label(frame5, text="POSTAL ADDRESS",font=('dubai light', 18,'bold'),bg='ivory3',fg='black',relief='raised',bd=8)
    L1.place(relx=0.48,rely=0.35)
    E9 = Entry(frame5, bd =20,width=19,selectborderwidth=1,relief='groove',font=('dubai light', 17,'bold'),fg='black')
    E9.place(relx=0.78,rely=0.35)
    L1 = Label(frame5, text="YEAR OF JOINING",font=('dubai light', 18,'bold'),bg='ivory3',fg='black',relief='raised',bd=8)
    L1.place(relx=0.48,rely=0.65)
    E10 = Entry(frame5, bd =9,width=19,selectborderwidth=2,relief='groove',font=('dubai light', 18,'bold'),fg='black')
    E10.place(relx=0.78,rely=0.65)
    L1 = Label(frame5, text="DEGREES ",font=('dubai light', 18,'bold'),bg='ivory3',fg='black',relief='raised',bd=8)
    L1.place(relx=0.48,rely=0.75)
    E11 = Entry(frame5, bd =9,width=19,selectborderwidth=2,relief='groove',font=('dubai light', 18,'bold'),fg='black')
    E11.place(relx=0.78,rely=0.75)

    L1 = Label(frame5, text="EMERGENCY CONTACT NUMBER ",font=('dubai light', 18,'bold'),bg='ivory3',fg='black',relief='raised',bd=8)
    L1.place(relx=0.48,rely=0.25)
    E12 = Entry(frame5, bd =9,width=19,selectborderwidth=2,relief='groove',font=('dubai light', 18,'bold'),fg='black')
    E12.place(relx=0.78,rely=0.25)

    L1 = Label(frame5, text="MAIN SUBJECT",font=('dubai light', 18,'bold'),bg='ivory3',fg='black',relief='raised',bd=8)
    L1.place(relx=0.48,rely=0.45)
    E13 = Entry(frame5, bd =9,width=19,selectborderwidth=2,relief='groove',font=('dubai light', 18,'bold'),fg='black')
    E13.place(relx=0.78,rely=0.45)

    stud_bt=Button(frame5,text='   UPDATE   ',font=('segoe print', 13 ,'bold'),width=9,bg='thistle3',fg='snow',bd=7,command=submit)
    stud_bt.place(relx=0.44,rely=0.85)

    bck_bt=Button(frame5,text='  BACK  ',font=('segoe print', 15,'bold'),command=stubck1,bd=5)
    bck_bt.place(relx=0.80,rely=0.05)

    ext_bt=Button(frame5,text='  QUIT  ',font=('segoe print', 15,'bold'),command=exit,bd=5)
    ext_bt.place(relx=0.90,rely=0.05)

####################END OF TEACHER BIODATA##############
#==================================================================================================================    
# tea create acc
def tea_ca():
    global username
    def teabck1():
        frame7.destroy
        teachpg()

    def submit():
        global username        
        a=username1.get()
        d=E3.get()
        b=E2.get()
        c=E4.get()#passcode or teacher check code
        global username
        username=a
        if c != "GURU27":
                        messagebox.showinfo("ERROR",'invalid username or passcode')                                               
        else:
                        if b==d and len(b )!=0:
                            mycursor.execute("CREATE TABLE IF NOT EXISTS tea_ca (uname char(20) primary key,pswd char(10))")
                            mydb.commit()
                            mycursor.execute('select uname from tea_ca')
                            lst1=mycursor.fetchall()
                            mycursor.execute('select pswd from tea_ca')
                            lst2=mycursor.fetchall()
                            tea=(a,str(b))
                            if (a,) not in lst1 and (b,) not in lst2:                            
                                    sqlformula="INSERT INTO tea_ca VALUES (%s,%s)"                            
                                    mycursor.execute(sqlformula,tea)
                                    mydb.commit()
                                    tea_bio()
                            else:
                                messagebox.showinfo("ERROR",'account already exists or \n try with a new pswd. \n or try signing in!!') 
                        else:
                            messagebox.showinfo("ERROR",'no matches btw the pwds or \n no pswd entered')
    frame7 = Frame(root, highlightbackground="skyblue1", highlightcolor="skyblue1" ,highlightthickness=20, width=1340, height=700, bd= 0,bg='gray1')
    frame7.place(relx=0.01,rely=0.02)
    label = Label( frame7, text=" TEACHER CREATE ACCOUNT", relief=RAISED ,font=('segoe script', 25,'bold'),bg='gray1',fg='deep pink' ,bd=0)
    label.place(relx=0.27,rely=0.1 )

    L1 = Label(frame7, text=" USERNAME ",font=('segoe print', 20,'bold'),bg='plum1',fg='brown4',relief='raised',bd=9)
    L1.place(relx=0.18,rely=0.3)
    username1 = Entry(frame7, bd =10,width=20,selectborderwidth=2,relief='groove',font=('segoe script', 20,'bold'),fg='blue2')
    username1.place(relx=0.35,rely=0.3)

    L4 = Label(frame7, text=" TEACHER CHECK CODE ",font=('segoe print', 20,'bold'),bg='plum1',fg='brown4',relief='raised',bd=9)
    L4.place(relx=0.18,rely=0.45)
    E4 = Entry(frame7, bd =10,width=10,selectborderwidth=2,relief='groove',font=('segoe script', 20,'bold'),fg='blue2')
    E4.place(relx=0.49,rely=0.45)

    L2 = Label(frame7, text=" PASSWORD ",font=('segoe script', 20,'bold'),bg='plum1',fg='brown4',relief='raised',bd=9)
    L2.place(relx=0.18,rely=0.60)
    E2 = Entry(frame7, bd =10, width=15, selectborderwidth=2,relief='groove',font=('segoe script', 20,'bold'),fg='blue2',show='*')
    E2.place(relx=0.35,rely=0.60)


    L3 = Label(frame7, text="CONFIRM PASSWORD ",font=('segoe script', 20,'bold'),bg='plum1',fg='brown4',relief='raised',bd=9)
    L3.place(relx=0.18,rely=0.75)
    E3 = Entry(frame7, bd =10, width=15, selectborderwidth=2,relief='groove',font=('segoe script', 20,'bold'),fg='blue2',show='*')
    E3.place(relx=0.46,rely=0.75)

    stud_bt=Button(frame7,text=' CREATE ',font=('segoe script', 17,'bold'),height=1,width=15,bg='thistle1',fg='gray1',bd=8,command=submit)
    stud_bt.place(relx=0.4,rely=0.88)

    bck_bt=Button(frame7,text='BACK',font=('segoe script', 15,'bold'),command=teabck1,bd=5)
    bck_bt.place(relx=0.08,rely=0.08)

    ext_bt=Button(frame7,text='QUIT',font=('segoe script', 17,'bold'),command=exit,bd=5)
    ext_bt.place(relx=0.08,rely=0.2)
    
################tea sign in##########  
def tea_signin():
    def submit1():
        conn=mcp.connect(host='localhost',user='root',password='abc123*',port=3306,database='pro')
        cur=conn.cursor()
        sql=("show tables like 'tea_ca'")
        mycursor.execute(sql)
        lst=mycursor.fetchall()
        if len(lst) != 0:

            cur.execute('select * from tea_ca')
            lst=cur.fetchall()

            uname=username1.get()
            global username
            username=uname
            pswd=E2.get()

            details=(username,pswd)
            if details in lst:
                           messagebox.showinfo("INFO",'Correct teacher id ')
                           root.destroy()
                           teacher_homepg()
            else:
                            messagebox.showinfo("ERROR",'WRONG TEACHER ID OR PSWD')
        else:
            messagebox.showinfo("ERROR",'NO ACCOUNTS YET !! \n create an account and try signing in')
    def teabck1(): #3rd pg sign in
        frame4.destroy
        teachpg()
        
    frame4=Frame(root,bg='cadet blue')
    frame4.place(relwidth=1,relheight=1)

    load=Image.open('D:\AAPYTHON\project\pic (in use)\Teacher bg.jpg')
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(frame4,image=bg)
    bglabel.image = bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    label = Label( frame4, text=" DAV SR SECONDARY SCHOOL,CHENNAI.", relief=RAISED ,font=('segoe script', 27,'bold'),bg='brown3' ,bd=5)
    label.place(relx=0.20,rely=0.05)

    label_ = Label( frame4, text=" TEACHER SIGN IN ", relief=RAISED ,font=('segoe script', 23,'bold'),bg='brown3',bd=8 )
    label_.place(relx=0.33,rely=0.18 )

    load=Image.open('D:\AAPYTHON\project\pic (in use)\Teacher sign in.jpg')
    t_icon=ImageTk.PhotoImage(load)
    iconlabe=Label(frame4,image=t_icon)
    iconlabe.image = t_icon
    iconlabe.place(relx=0.4,rely=0.3)

    L1 = Label(frame4, text=" USERNAME ",font=('dubai light', 20,'bold'),bg='brown3',relief='raised',bd=9)
    L1.place(relx=0.18,rely=0.55)
    username1 = Entry(frame4, bd =10,width=20,selectborderwidth=2,relief='groove',font=('segoe script', 20,'bold'),fg='blue2')
    username1.place(relx=0.35,rely=0.55)

    L2 = Label(frame4, text=" PASSWORD ",font=('dubai light', 20,'bold'),bg='brown3',relief='raised',bd=9)
    L2.place(relx=0.18,rely=0.65)
    E2 = Entry(frame4, bd =10, width=15, selectborderwidth=2,relief='groove',font=('segoe script', 20,'bold'),fg='blue2',show='*')
    E2.place(relx=0.35,rely=0.65)

    stud_bt=Button(frame4,text=' SIGN IN ',font=('segoe script', 12,'bold'),height=2,width=12,bg='brown3',command=submit1,bd=8)
    stud_bt.place(relx=0.39,rely=0.75)

    bck_bt=Button(frame4,text='BACK',font=('segoe script', 15,'bold'),command=teabck1,bd=5,bg="thistle3")
    bck_bt.place(relx=0.08,rely=0.08)

    ext_bt=Button(frame4,text='QUIT',font=('segoe script', 15,'bold'),command=exit,bd=5,bg="thistle3")
    ext_bt.place(relx=0.08,rely=0.2)

###############tea sign in over###################
###################################TEACHER PG###################################################
def teachpg():
            def teabck():  # 2nd pg
                frame2.destroy
                mnfrm()
    
            MainFrame.destroy()
            frame2=Frame(root,bg='cadet blue')
            frame2.place(relwidth=1,relheight=1)

            load3=Image.open('D:\AAPYTHON\project\pic (in use)\sarah 2 nd bg.jpg')
            bg3=ImageTk.PhotoImage(load3)
            bglabel3=Label(frame2,image=bg3)
            bglabel3.image = bg3
            bglabel3.place(relx=0,rely=0,relwidth=1,relheight=1)
            
            load4=Image.open('D:\\AAPYTHON\\project\\pic (in use)\\teacher.jpg')
            t_icon=ImageTk.PhotoImage(load4)
            iconlabel=Label(frame2,image=t_icon)
            iconlabel.image = t_icon
            iconlabel.place(relx=0.4,rely=0.22)
            
            label = Label( frame2, text="  DAV SR SECONDARY SCHOOL,CHENNAI.", relief=RAISED ,font=('segoe script', 30,'bold'),bg='lawn green',fg='brown4' )
            label.place(relx=0.17,rely=0.09 )

            teac_bt=Button(frame2,text='CREATE NEW ACCOUNT',font=('segoe script', 11,'bold'),height=2,width=25,bg='gray11', fg='floral white',bd=8,command=tea_ca)
            teac_bt.place(relx=0.25,rely=0.7)

            stud_bt=Button(frame2,text='SIGN IN ',font=('segoe script', 11,'bold'),height=2,width=25,bg='dark orchid4',fg='floralwhite',bd=8,command=tea_signin)
            stud_bt.place(relx=0.55,rely=0.7)

            bck_bt=Button(frame2,text='BACK',font=('segoe script', 15,'bold'),command=teabck,bd=5,bg="thistle3")
            bck_bt.place(relx=0.08,rely=0.1)

            ext_bt=Button(frame2,text='QUIT',font=('segoe script', 17,'bold'),command=exit,bd=5,bg="thistle3")
            ext_bt.place(relx=0.08,rely=0.23)
######################################END OF TEACHER PG###############################################             
def admin():
    def okie():
        if E1.get()=="admin274":
            admin_homepg()
        else:
            messagebox.showinfo("INFO",' WRONG CODE  ')
    def admin_homepg():
        def exam_portal():
            global root
            root.destroy()
            root=Tk()
            root.geometry("1366x786")
            def add_exam():
                def addexam():
                    a=E1.get()
                    a=a.replace(" ","_")
                    if len(E1.get())!=0 and c.get()!='Select your Option'and c1.get()!='Select your Class':
                            sql=("CREATE TABLE IF NOT EXISTS " +str(str(c1.get())+"examslist" ) +" ( Exams_in_Class_" +str(c1.get())+ " char(50),Internals char(5))")
                            mycursor.execute(sql)
                            mydb.commit()
                            sql="Select LOWER(Exams_in_Class_" +str(c1.get())+") from "+str(c1.get())+"examslist"
                            #print(sql)
                            mycursor.execute(sql)
                            
                            b=mycursor.fetchall()
                            if (a.lower(),) not in b:
                                sqlformula="INSERT INTO " +str(c1.get())+"examslist" +" VALUES ('"+a+"','"+c.get()+"')"
                                mycursor.execute(sqlformula)
                                mydb.commit()
                                messagebox.showinfo("INFO",'Exam ADDED')
                                add_exam()
                            else:
                                messagebox.showinfo("ERROR",'EXAM ALREADY EXISTS')
                                add_exam()
                                
                    else:
                            messagebox.showinfo("ERROR",'INCOMPLETE FORM')
                frame6=Frame(frame5,bg="thistle3",width=900,height=150,highlightbackground="salmon", highlightcolor="salmon",highlightthickness=15)
                frame6.place(relwidth=0.44,relheight=0.6)
                frame6.place(relx=0.01,rely=0.33)
                label = Label(frame6, text=" Enter the \n name of the exam ", relief=RAISED ,font=('segoe script', 18,'bold'),bg='red',fg='snow' ,bd=8)
                label.place(relx=0.02,rely=0.07)
                E1 = Entry(frame6, bd =8,width=15,selectborderwidth=2,relief='groove',font=('segoe script', 15,'bold'),fg='blue2')
                E1.place(relx=0.56,rely=0.09)

                label = Label(frame6, text=" Any internals? ", relief=RAISED ,font=('segoe script', 18,'bold'),bg='red',fg='snow' ,bd=8)
                label.place(relx=0.02,rely=0.36)
                list_of_opt=[ 'YES','NO']
                c=StringVar()
                droplist=OptionMenu(frame6,c, *list_of_opt)
                droplist.config(width=15)
                c.set('Select your Option')
                droplist.place(relx=0.65,rely=0.35)

                label = Label(frame6, text=" For which standard would \n you like to add this exam ", relief=RAISED ,font=('segoe script', 18,'bold'),bg='red',fg='snow' ,bd=8)
                label.place(relx=0.02,rely=0.55)
                list_of_class=[ 'XI','XII']
                c1=StringVar()
                droplist=OptionMenu(frame6,c1, *list_of_class)
                droplist.config(width=15)
                c1.set('Select your Class')
                droplist.place(relx=0.72,rely=0.6)
                button=Button(frame6,text='ADD THIS EXAM ',bd=8,command=addexam,font=('segoe script', 15,'bold'),bg="thistle3")
                button.place(relx=0.35,rely=0.81)


            def view_exam():
                
                def viewexam():
                    a=c.get()
                    if a!='Select your Class':                      
                                sql=("show tables like '"+ str(str(c.get())+"examslist"+"' "))
                                mycursor.execute(sql)
                                lst1=mycursor.fetchall()
                                if len(lst1) != 0:
                                    mycursor.execute("SELECT Exams_in_Class_" +str(c.get() +" FROM "+str(str(c.get())+"examslist" )))                        
                                    lst1=mycursor.fetchall()
                                    button2['state']='disabled'
                                    label = Label(frame7, text=" LIST OF EXAMS IN CLASS"+c.get(), relief=RAISED ,font=('segoe script', 18,'bold'),bg='hotpink2',fg='purple4' )
                                    label.place(relx=0.15,rely=0.4)
                                    if lst1==[]:
                                        label = Label(frame7, text=" NO EXAMS SO FAR !", relief=RAISED ,font=('segoe script', 25,'bold'),bg='hotpink2',fg='green2')
                                        label.place(relx=0.32,rely=0.6)
                                    
                                    else:                                        
                                        frame=Frame(frame7)
                                        sb=Scrollbar(frame,orient=VERTICAL)
                                        lst=Listbox(frame,yscrollcommand=sb.set,height=5,width=13,font=('segoe script', 15,'bold'),bg='red',fg='snow' ,bd=8)
                                        sb.config(command=lst.yview)
                                        sb.pack(side=RIGHT,fill=Y)
                                        lst.pack()
                                        frame.place(relx=0.02,rely=0.52)                                        
                                        for i in lst1:                                            
                                            a=i[0]
                                            lst.insert(END,a)
                                else:
                                        button2['state']='disabled'
                                        label = Label(frame7, text=" NO EXAMSS SO FAR !!!", relief=RAISED ,font=('segoe script', 25,'bold'),bg='hotpink2',fg='green2' )
                                        label.place(relx=0.1,rely=0.6)
                                                              
                    else:
                                  messagebox.showinfo("ERROR",'INCOMPLETE FORM ')
                    
                frame7=Frame (frame5,bg="hotpink2",width=900,highlightbackground="salmon", highlightcolor="salmon",highlightthickness=15)
                frame7.place(relwidth=0.45,relheight=0.6)
                frame7.place(relx=0.50,rely=0.33)
                
                label = Label(frame7, text=" For which standard would you \n  like to view the exam list ", relief=RAISED ,font=('segoe script', 15,'bold'),bg='green2' ,bd=8)
                label.place(relx=0.02,rely=0.01)
                list_of_class=[ 'XI','XII']
                c=StringVar()
                droplist=OptionMenu(frame7,c, *list_of_class)
                droplist.config(width=15)
                c.set('Select your Class')
                droplist.place(relx=0.68,rely=0.01)
                button2=Button(frame7,text='VIEW',bd=8,command=viewexam,font=('segoe script', 15,'bold'),bg="thistle3")
                button2.place(relx=0.45,rely=0.25)

            frame5=Frame(root,bg='turquoise2',width=1340, height=700, highlightbackground="salmon", highlightcolor="salmon" ,highlightthickness=15)
            frame5.place(relwidth=1,relheight=1) 
            load=Image.open('D:\AAPYTHON\project\pic (in use)\sarah bg pic.jpg')
            bg=ImageTk.PhotoImage(load)
            bglabel=Label(frame5,image=bg)
            bglabel.image = bg
            bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
            label = Label(frame5, text=" EXAM  PORTAL ", relief=RAISED ,font=('segoe print bold', 37,'bold'),bg='red',fg='snow' ,bd=8)
            label.place(relx=0.3,rely=0.01)
            button=Button(frame5,text='access \n home page',command=admin_homepg,bg='thistle3',bd=10,relief='raised',font=('segoe script', 15,'bold'))
            button.place(relx=0.85,rely=0.01)
            button=Button(frame5,text='ADD EXAM ',command=add_exam,font=('segoe print bold',16),bg='thistle3',bd=10,relief='raised')
            button.place(relx=0.20,rely=0.2)
            button=Button(frame5,text='VIEW EXAMS LIST',command=view_exam,font=('segoe print bold',16),bg='thistle3',bd=10,relief='raised')
            button.place(relx=0.60,rely=0.2)
            bck_bt=Button(frame5,text='EXIT',font=('segoe script', 15,'bold'),command=exit,bg='thistle3',bd=10,relief='raised')
            bck_bt.place(relx=0.06,rely=0.05)

        def subject_portal():
            global root
            root.destroy()
            root=Tk()
            root.geometry("1366x786")
            def add_sub():
                def addsubject():
                    a=E1.get()
                    a=a.replace(" ","_")
                    if len(a) != 0 and c.get() != 'Select your Class':
                            sql=("CREATE TABLE IF NOT EXISTS " +str(str(c.get())+"subjectslist" ) +" ( Subjects_in_Class_" +str(c.get())+ " char(50))")
                            #print(sql)
                            mycursor.execute(sql)
                            mydb.commit()
                            mycursor.execute("SELECT LOWER (Subjects_in_Class_" +str(c.get())+") FROM "+str(str(c.get())+"subjectslist" ))
                            if (a.lower(),) not in mycursor.fetchall():
                                
                                sqlformula="INSERT INTO " +str(c.get())+"subjectslist" +" VALUES ('"+a+"')"
                                mycursor.execute(sqlformula)
                                mydb.commit()
                                messagebox.showinfo("INFO",'SUBJECT ADDED')
                                add_sub()
                            else:
                                messagebox.showinfo("ERROR",'SUBJECT ALREADY EXISTS')
                                
                    else:
                            messagebox.showinfo("ERROR",'INCOMPLETE FORM')             
                frame6=Frame (frame5,bg="thistle3",width=900,height=150,highlightbackground="salmon", highlightcolor="salmon" ,highlightthickness=15)
                frame6.place(relwidth=0.43,relheight=0.6)
                frame6.place(relx=0.06,rely=0.3)

                label = Label(frame6, text="Enter the name of the subject", relief=RAISED ,font=('segoe script', 15,'bold'),bg='red',fg='snow' ,bd=7)
                label.place(relx=0.01,rely=0.02)
                E1 = Entry(frame6, bd =7,width=10,selectborderwidth=1,relief='groove',font=('segoe script', 15,'bold'),fg='blue2')
                E1.place(relx=0.66,rely=0.02)

                label = Label(frame6, text=" For which standard would \n you like to add this ", relief=RAISED ,font=('segoe script', 18,'bold'),bg='red',fg='cyan2' ,bd=7)
                label.place(relx=0.02,rely=0.32)
                list_of_class=[ 'XI','XII']
                c=StringVar()
                droplist=OptionMenu(frame6,c, *list_of_class)
                droplist.config(width=15)
                c.set('Select your Class')
                droplist.place(relx=0.74,rely=0.35)

                button=Button(frame6,text='ADD THIS SUBJECT ',font=('segoe script', 18,'bold'),bg='thistle3',command=addsubject,bd=8)
                button.place(relx=0.3,rely=0.75)

            def view_sub():
                def viewsubject():
                    a=c.get()
                    if a!='Select your Class':                      
                                sql=("show tables like '"+ str(str(c.get())+"subjectslist"+"' "))
                                mycursor.execute(sql)
                                lst1=mycursor.fetchall()
                                if len(lst1) != 0:
                                    mycursor.execute("SELECT * FROM "+str(str(c.get())+"subjectslist" ))                                    
                                    lst1=mycursor.fetchall()
                                    button2['state']='disabled'
                                    label = Label(frame7, text=" LIST OF SUBJECTS IN CLASS"+c.get(), relief=RAISED ,font=('segoe script', 17,'bold'),bg='red',fg='snow' ,bd=8)
                                    label.place(relx=0.02,rely=0.4)
                                    if lst1==[]:
                                        label = Label(frame7, text=" NO SUBJECTS SO FAR !", relief=RAISED ,font=('segoe script', 15,'bold'),bg='red',fg='snow' ,bd=8)
                                        label.place(relx=0.32,rely=0.45)
                                    else:                                        
                                        frame=Frame(frame7)
                                        sb=Scrollbar(frame,orient=VERTICAL)
                                        lst=Listbox(frame,yscrollcommand=sb.set,height=5,width=13,font=('segoe script', 15,'bold'),bg='red',fg='snow' ,bd=8)
                                        sb.config(command=lst.yview)
                                        sb.pack(side=RIGHT,fill=Y)
                                        lst.pack()
                                        frame.place(relx=0.02,rely=0.52)                                        
                                        for i in lst1:                                            
                                            a=i[0]
                                            lst.insert(END,a)
                                else:
                                        button2['state']='disabled'
                                        label = Label(frame7, text=" NO SUBJECTS SO FAR !!!", relief=RAISED ,font=('segoe script', 17,'bold'),bg='red',fg='cyan2' ,bd=8)
                                        label.place(relx=0.02,rely=0.85)                                                              
                    else:
                                  messagebox.showinfo("ERROR",'NO CLASS SELECTED ')
                frame7=Frame (frame5,bg="thistle3",width=900,highlightbackground="salmon", highlightcolor="salmon" ,highlightthickness=15)
                frame7.place(relwidth=0.45,relheight=0.6)
                frame7.place(relx=0.50,rely=0.3)
                label = Label(frame7, text=" Which standard's subject \n list would you require ?", relief=RAISED ,font=('segoe script', 18,'bold'),bg='red',fg='cyan2' ,bd=7)
                label.place(relx=0.02,rely=0.02)
                list_of_class=[ 'XI','XII']
                c=StringVar()
                droplist=OptionMenu(frame7,c, *list_of_class)
                droplist.config(width=15)
                c.set('Select your Class')
                droplist.place(relx=0.68,rely=0.02)
                button2=Button(frame7,text='VIEW Subject List',command=viewsubject,bd=8,font=('segoe script',13,'bold'),bg='thistle3')
                button2.place(relx=0.4,rely=0.3)
                
            frame5=Frame(root,bg='turquoise2',width=1340, height=700, highlightbackground="salmon", highlightcolor="salmon" ,highlightthickness=15)
            frame5.place(relwidth=1,relheight=1)

            load=Image.open('D:\AAPYTHON\project\pic (in use)\sarah bg picture.jpg')
            bg=ImageTk.PhotoImage(load)
            bglabel=Label(frame5,image=bg)
            bglabel.image = bg
            bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
            label = Label(frame5, text=" SUBJECT PORTAL ",font=('segoe script', 25,'bold'),bg='red',bd=10,relief='raised')
            label.place(relx=0.36,rely=0.02)
            button=Button(frame5,text='Access \n Home Page ',command=admin_homepg,bd=10,font=('segoe script', 15,'bold'),bg='thistle3',relief='raised')
            button.place(relx=0.85,rely=0.02)
            button=Button(frame5,text=' ADD SUBJECT ',command=add_sub,font=('segoe script', 18,'bold'),bg='thistle3',bd=10,relief='raised')
            button.place(relx=0.20,rely=0.15)
            button=Button(frame5,text='VIEW SUBJECTS LIST',command=view_sub,font=('segoe script', 18,'bold'),bg='thistle3',bd=10,relief='raised')
            button.place(relx=0.60,rely=0.15)
            bck_bt=Button(frame5,text='EXIT',font=('segoe script', 20,'bold'),command=exit,bg='thistle3',bd=10,relief='raised')
            bck_bt.place(relx=0.08,rely=0.08)
        global root
        try:
            root.destroy()
        except:
            pass
        root=Tk()
        root.geometry("1366x786")

        frame5=Frame(root,bg='orange',width=1340, height=700, highlightbackground="salmon", highlightcolor="salmon" ,highlightthickness=15)
        frame5.place(relwidth=1,relheight=1)

        load=Image.open('D:\AAPYTHON\project\pic (in use)\harshh.jpg')
        bg=ImageTk.PhotoImage(load)
        bglabel=Label(frame5,image=bg)
        bglabel.image = bg
        bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        label = Label(frame5, text=" WELCOME TO ADMIN HOME PAGE ", relief=RAISED ,font=('segoe script', 30,'bold'),bg='orangered',fg='gray1' ,bd=8)
        label.place(relx=0.20,rely=0.03)
        button=Button(frame5,text='Access Subject Portal ',command=subject_portal,bd=10,relief=RAISED,font=('segoe script', 18,'bold'),bg="cyan2",fg="red")
        button.place(relx=0.25,rely=0.37)
        button=Button(frame5,text='Access Exams Portal',width=18,command=exam_portal,bd=10,bg="cyan2",fg="red",relief=RAISED,font=('segoe script', 18,'bold'))
        button.place(relx=0.65,rely=0.37)
        button=Button(frame5,text='Deletions Portal',width=18,bd=10,bg="cyan2",fg="red",relief=RAISED,font=('segoe script', 18,'bold'))
        button.place(relx=0.65,rely=0.23)
        button=Button(frame5,text='Additions Portal',width=18,bd=10,bg="cyan2",fg="red",relief=RAISED,font=('segoe script', 18,'bold'))
        button.place(relx=0.25,rely=0.23)        
    
        bck_bt=Button(frame5,text='EXIT',font=('segoe script', 18,'bold'),command=exit,bg='thistle3',bd=10,relief='raised')
        bck_bt.place(relx=0.08,rely=0.08)
           
    frame5=Frame(root,bg='pink',width=1340, height=700, highlightbackground="salmon", highlightcolor="salmon" ,highlightthickness=15)
    frame5.place(relwidth=1,relheight=1)
      
    load=Image.open('D:\AAPYTHON\project\pic (in use)\harsh.jpg')
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(frame5,image=bg)
    bglabel.image = bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    label = Label(frame5, text=" CHECK PAGE ",font=('segoe print bold', 37,'bold'),bg='thistle3' ,bd=8,relief=RAISED,width=18)
    label.place(relx=0.30,rely=0.05)
    label = Label(frame5, text=" Enter the admin's access code  ", relief=RAISED ,font=('segoe print bold',18),bg="blue2",fg='snow' ,bd=8)
    label.place(relx=0.22,rely=0.22)
    E1 = Entry(frame5, bd =8,width=12,selectborderwidth=2,relief='groove',font=('segoe print bold',18),fg='blue2')
    E1.place(relx=0.55,rely=0.22)
    button=Button(frame5,text='access ADMIN  portal',command=okie,bd=10,width=19,bg="hotpink1",font=('segoe print bold',18))
    button.place(relx=0.43,rely=0.35)
    button=Button(frame5,text='BACK TO \n START PAGE ',command=mnfrm,bd=10,font=('segoe print bold',18))
    button.place(relx=0.01,rely=0.01)
            
#####################################FIRST PG####################################################
def mnfrm():
    global MainFrame
    MainFrame = Frame(root, bg="cadet blue")
    MainFrame.place(relwidth=1,relheight=1)

    load=Image.open('D:\AAPYTHON\project\pic (in use)\sarah bg pic.jpg')
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(MainFrame,image=bg)
    bglabel.image = bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    TitFrame = Frame(MainFrame, bd=2,  padx=54,  bg='Ghost White', relief = RIDGE)
    TitFrame.pack(side=TOP)

    lblTit=Label(TitFrame ,font=('segoe print bold', 37,'bold'),text=" DAV Sr. SECONDARY SCHOOL \n Student Database Management System ",bg='Ghost White')
    lblTit.pack()

    load2=Image.open('D:\AAPYTHON\project\pic (in use)\harrshithaa bg pic.PNG')
    bg2=ImageTk.PhotoImage(load2)
    bglabel2=Label(MainFrame,image=bg2)
    bglabel2.image = bg2
    bglabel2.place(relx=0.3,rely=0.25)

    lbl2=Label(MainFrame,font=('segoe script',28),text='You are a',bg='white')
    lbl2.place(relx=0.38,rely=0.58)
            
    admin1=Button(MainFrame,text='ADMIN',font=('segoe print bold',16),height=2,width=12,bg='thistle3',bd=10,relief='raised',command=admin)
    admin1.place(relx=0.5,rely=0.7)

    teacherb=Button(MainFrame,text='TEACHER',font=('segoe print bold',16),height=2,width=12,bg='thistle3',bd=10,relief='raised',command=teachpg)
    teacherb.place(relx=0.3,rely=0.7)

    ext_bt=Button(MainFrame,text=' QUIT ',font=('segoe script', 18,'bold'),command=exit,bg='thistle3',bd=10,relief='raised')
    ext_bt.place(relx=0.06,rely=0.23)
#################################OVER 1ST PG###################################################
mnfrm()
root.mainloop()
    
