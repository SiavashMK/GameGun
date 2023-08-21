#IMPORT
from tkinter import *
import jdatetime
import time
from fpdf import *
import sqlite3
import ast
#------window
w=Tk()
w.title('Holoo')
w.geometry('1364x716')
w.configure(bg='white')
#---------Sqlite
conn=sqlite3.connect('FormH3.db')
cur=conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
FactorNumber INTEGER PRIMARY KEY,
Orders TEXT,
TotalPrice TEXT,
DateTime TEXT);""")
conn.commit()
cur.execute("SELECT COUNT(*)FROM users")
fn=cur.fetchone()[0]+1
#---------------Def Date
def date():
    global time0
    global time01
    time0=jdatetime.date.today().strftime('%Y-%m-%d')
    time01=time.strftime('%H:%M:%S')
    lbtime.config(text=f'Date: {time0}_{time01}')
    w.after(1000,date)
#----------------------------Def pizza
def pizza():
    frs.grid_forget()
    frst.grid_forget()
    frsl.grid_forget()
    frd.grid_forget()
    btnm2.configure(relief='raised',bg='white',fg='black')
    btnm3.configure(relief='raised',bg='white',fg='black')
    btnm4.configure(relief='raised',bg='white',fg='black')
    btnm5.configure(relief='raised',bg='white',fg='black')
    btnm.config(relief='sunken',bg=btnm['activebackground'],fg=btnm['activeforeground'])
    frp.grid(row=2,column=2,sticky=E+N,padx=20,rowspan=60)
#------------values True,False
B=False;B2=False;B3=False;B4=False;B5=False;B6=False;B7=False;B8=False;B9=False;B10=False;B11=False
B12=False;B13=False;B14=False;B15=False;B16=False;B17=False;B18=False;B19=False;B20=False;B21=False;B22=False
list_factor=[]
global Total
Total=0
A=[]
#---------------------Frame,label,button american pizza
def AmericanPizza():
    #-----------------Global
    global Delete
    global Total
    global Tot1
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num;global B
    global f1;global listP;global l1;global l2;global l3;global l4;global l5;global l6;global E1;global Badd;global Badd2;global BDelete
#-------------------def +
    def add1():
        global Total
        global num
        global listP
        num+=1
        l4.config(text=f'{num}')
        l4.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6.config(text=f'{20*num}$')
        l6.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1.grid(row=row1+2,column=0,sticky=W+N)
        Total+=20
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP)
        listP=['01','American Pizza',f'{num}','20$',f'{20*num}$']
        A.append(listP)
#-------------------def -
    def add2():
        global Total
        global num
        global listP
        if num>1:
            Total-=20
        num-=1
        if num<=1:
            num=1
        l4.config(text=f'{num}')
        l4.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6.config(text=f'{20*num}$')
        l6.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1.grid(row=row1+2,column=0,sticky=W+N)
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP)
        listP=['01','American Pizza',f'{num}','20$',f'{20*num}$']
        A.append(listP)
#-------------------def delete
    def Delete():
        global Total
        global list_factor
        global num;global B
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        B=False
        A.remove(listP)
        E1.delete(0,'end')
        
        Total-=20*num
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        
        if 'American Pizza'in list_factor:
            list_factor.remove('American Pizza')
            
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()
#-----------------------first Click
    if B==False:
        num=1
        list_factor.append('American Pizza')
        row1=list_factor.index('American Pizza')+1
        listP=['01','American Pizza',f'{num}','20$',f'{20*num}$']
        A.append(listP)
        f1=Frame(w,bg='black')
        l1=Label(f1,text=f'{row1}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2=Label(f1,text=f'{listP[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3=Label(f1,text=f'{listP[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4=Label(f1,text=f'{num}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5=Label(f1,text=f'{listP[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6=Label(f1,text=f'{listP[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1=Entry(f1,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd=Button(f1,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1)
        Badd2=Button(f1,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2)
        BDelete=Button(f1,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete)
#-----------------------next Click
    else:
        A.remove(listP)
        num+=1
        listP=['01','American Pizza',f'{num}','20$',f'{20*num}$']
        A.append(listP)
        l1.config(text=f'{row1}')
        l4.config(text=f'{num}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6.config(text=f'{listP[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
#-----------------------grid
    l1.grid(row=0,column=0,pady=1,sticky=W+N)
    l2.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3.grid(row=0,column=2,pady=1,sticky=W+N)
    l4.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5.grid(row=0,column=4,pady=1,sticky=W+N)
    l6.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1.grid(row=row1+2,column=0,sticky=W+N)
    B=True
    Total+=20
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#---------------------Frame,label,button special pizza
def SpecialPizza():
    #---------------global
    global Delete_2
    global Total
    global Tot2
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num2;global B2
    global f1_2;global listP2;global l1_2;global l2_2;global l3_2;global l4_2;global l5_2;global l6_2;global E1_2;global Badd_2;global Badd2_2;global BDelete_2
#--------------------def +
    def add1_2():
        global Total
        global num2
        global listP2
        num2+=1
        l4_2.config(text=f'{num2}')
        l4_2.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_2.config(text=f'{22*num2}$')
        l6_2.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_2.grid(row=row2+2,column=0,sticky=W+N)
        Total+=22
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP2)
        listP2=['02','Special Pizza',f'{num2}','22$',f'{22*num2}$']
        A.append(listP2)
#---------------------def -
    def add2_2():
        global Total
        global num2
        global listP2
        if num2>1:
            Total-=22
        num2-=1
        if num2<=1:
            num2=1
        l4_2.config(text=f'{num2}')
        l4_2.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_2.config(text=f'{22*num2}$')
        l6_2.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_2.grid(row=row2+2,column=0,sticky=W+N)
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP2)
        listP2=['02','Special Pizza',f'{num2}','22$',f'{22*num2}$']
        A.append(listP2)
#----------------------def delete
    def Delete_2():
        global Total
        global list_factor
        global num2;global B2
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP2)
        E1_2.delete(0,'end')
        Total-=22*num2
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B2=False
        if('Special Pizza')in list_factor:
            list_factor.remove('Special Pizza')
            
        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_2.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()
#---------------------first Click
    if B2==False:
        num2=1
        list_factor.append('Special Pizza')
        row2=list_factor.index('Special Pizza')+1
        listP2=['02','Special Pizza',f'{num2}','22$',f'{22*num2}$']
        A.append(listP2)
        f1_2=Frame(w,bg='black')
        l1_2=Label(f1_2,text=f'{row2}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_2=Label(f1_2,text=f'{listP2[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_2=Label(f1_2,text=f'{listP2[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_2=Label(f1_2,text=f'{num2}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_2=Label(f1_2,text=f'{listP2[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_2=Label(f1_2,text=f'{listP2[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_2=Entry(f1_2,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_2=Button(f1_2,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_2)
        Badd2_2=Button(f1_2,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_2)
        BDelete_2=Button(f1_2,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_2)
#---------------------next Click
    else:
        A.remove(listP2)
        num2+=1
        listP2=['02','Special Pizza',f'{num2}','22$',f'{22*num2}$']
        A.append(listP2)
        l1_2.config(text=f'{row2}')
        l4_2.config(text=f'{num2}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_2.config(text=f'{listP2[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
#-----------------------grid
    l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_2.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_2.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_2.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_2.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_2.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_2.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_2.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_2.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_2.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_2.grid(row=row2+2,column=0,sticky=W+N)
    B2=True
    Total+=22
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#---------------------Frame,label,button italian pizza
def ItalianPizza():
    #---------------global
    global Delete_3
    global Total
    global Tot3
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num3;global B3
    global f1_3;global listP3;global l1_3;global l2_3;global l3_3;global l4_3;global l5_3;global l6_3;global E1_3;global Badd_3;global Badd2_3;global BDelete_3
#--------------------def +
    def add1_3():
        global Total
        global num3
        global listP3
        num3+=1
        l4_3.config(text=f'{num3}')
        l4_3.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_3.config(text=f'{18*num3}$')
        l6_3.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_3.grid(row=row3+2,column=0,sticky=W+N)
        Total+=18
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP3)
        listP3=['03','Italian Pizza',f'{num3}','18$',f'{18*num3}$']
        A.append(listP3)
#---------------------def -
    def add2_3():
        global Total
        global num3
        global listP3
        if num3>1:
            Total-=18
        num3-=1
        if num3<=1:
            num3=1
        l4_3.config(text=f'{num3}')
        l4_3.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_3.config(text=f'{18*num3}$')
        l6_3.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_3.grid(row=row3+2,column=0,sticky=W+N)
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP3)
        listP3=['03','Italian Pizza',f'{num3}','18$',f'{18*num3}$']
        A.append(listP3)
#----------------------def delete
    def Delete_3():
        global Total
        global list_factor
        global num3;global B3
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP3)
        E1_3.delete(0,'end')
        Total-=18*num3
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B3=False
        if('Italian Pizza')in list_factor:
            list_factor.remove('Italian Pizza')
        
        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)

        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_3.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()
#---------------------first Click
    if B3==False:
        num3=1
        list_factor.append('Italian Pizza')
        row3=list_factor.index('Italian Pizza')+1
        listP3=['03','Italian Pizza',f'{num3}','18$',f'{18*num3}$']
        f1_3=Frame(w,bg='black')
        l1_3=Label(f1_3,text=f'{row3}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_3=Label(f1_3,text=f'{listP3[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_3=Label(f1_3,text=f'{listP3[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_3=Label(f1_3,text=f'{num3}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_3=Label(f1_3,text=f'{listP3[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_3=Label(f1_3,text=f'{listP3[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_3=Entry(f1_3,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_3=Button(f1_3,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_3)
        Badd2_3=Button(f1_3,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_3)
        BDelete_3=Button(f1_3,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_3)
        A.append(listP3)
#---------------------next Click
    else:
        A.remove(listP3)
        num3+=1
        listP3=['02','Italian Pizza',f'{num3}','18$',f'{18*num3}$']
        l1_3.config(text=f'{row3}')
        l4_3.config(text=f'{num3}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_3.config(text=f'{listP3[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP3)
#-----------------------grid
    l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_3.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_3.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_3.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_3.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_3.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_3.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_3.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_3.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_3.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_3.grid(row=row3+2,column=0,sticky=W+N)
    B3=True
    Total+=18
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#---------------------Frame,label,button veg pizza        
def VegPizza():
    #---------------global
    global Delete_4
    global Total
    global Tot4
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num4;global B4
    global f1_4;global listP4;global l1_4;global l2_4;global l3_4;global l4_4;global l5_4;global l6_4;global E1_4;global Badd_4;global Badd2_4;global BDelete_4
#--------------------def +
    def add1_4():
        global Total
        global num4
        global listP4
        num4+=1
        l4_4.config(text=f'{num4}')
        l4_4.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_4.config(text=f'{15*num4}$')
        l6_4.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_4.grid(row=row4+2,column=0,sticky=W+N)
        Total+=15
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP4)
        listP4=['04','Veg Pizza',f'{num4}','15$',f'{15*num4}$']
        A.append(listP4)
#---------------------def -
    def add2_4():
        global Total
        global num4
        global listP4
        if num4>1:
            Total-=15
        num4-=1
        if num4<=1:
            num4=1
        l4_4.config(text=f'{num4}')
        l4_4.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_4.config(text=f'{15*num4}$')
        l6_4.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_4.grid(row=row4+2,column=0,sticky=W+N)
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP4)
        listP4=['04','Veg Pizza',f'{num4}','15$',f'{15*num4}$']
        A.append(listP4)
#----------------------def delete
    def Delete_4():
        global Total
        global list_factor
        global num4;global B4
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP4)
        E1_4.delete(0,'end')
        Total-=15*num4
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B4=False
        if('Veg Pizza')in list_factor:
            list_factor.remove('Veg Pizza')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_4.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()
#---------------------first Click
    if B4==False:
        num4=1
        list_factor.append('Veg Pizza')
        row4=list_factor.index('Veg Pizza')+1
        listP4=['04','Veg Pizza',f'{num4}','15$',f'{15*num4}$']
        f1_4=Frame(w,bg='black')
        l1_4=Label(f1_4,text=f'{row4}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_4=Label(f1_4,text=f'{listP4[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_4=Label(f1_4,text=f'{listP4[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_4=Label(f1_4,text=f'{num4}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_4=Label(f1_4,text=f'{listP4[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_4=Label(f1_4,text=f'{listP4[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_4=Entry(f1_4,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_4=Button(f1_4,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_4)
        Badd2_4=Button(f1_4,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_4)
        BDelete_4=Button(f1_4,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_4)
        A.append(listP4)
#---------------------next Click
    else:
        A.remove(listP4)
        num4+=1
        listP4=['04','Veg Pizza',f'{num4}','15$',f'{15*num4}$']
        l1_4.config(text=f'{row4}')
        l4_4.config(text=f'{num4}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_4.config(text=f'{listP4[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP4)
#-----------------------grid
    l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_4.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_4.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_4.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_4.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_4.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_4.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_4.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_4.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_4.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_4.grid(row=row4+2,column=0,sticky=W+N)
    B4=True
    Total+=15
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#---------------------Frame,label,button Chicken Pizza
def ChickenPizza():
    #---------------global
    global Delete_5
    global Total
    global Tot5
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num5;global B5
    global f1_5;global listP5;global l1_5;global l2_5;global l3_5;global l4_5;global l5_5;global l6_5;global E1_5;global Badd_5;global Badd2_5;global BDelete_5
#--------------------def +
    def add1_5():
        global Total
        global num5
        global listP5
        num5+=1
        l4_5.config(text=f'{num5}')
        l4_5.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_5.config(text=f'{16*num5}$')
        l6_5.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_5.grid(row=row5+2,column=0,sticky=W+N)
        Total+=16
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP5)
        listP5=['05','Chicken Pizza',f'{num5}','16$',f'{16*num5}$']
        A.append(listP5)
#---------------------def -
    def add2_5():
        global Total
        global num5
        global listP5
        if num5>1:
            Total-=16
        num5-=1
        if num5<=1:
            num5=1
        l4_5.config(text=f'{num5}')
        l4_5.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_5.config(text=f'{16*num5}$')
        l6_5.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_5.grid(row=row5+2,column=0,sticky=W+N)
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP5)
        listP5=['05','Chicken Pizza',f'{num5}','16$',f'{16*num5}$']
        A.append(listP5)
#----------------------def delete
    def Delete_5():
        global Total
        global list_factor
        global num5;global B5
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP5)
        E1_5.delete(0,'end')
        Total-=16*num5
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B5=False
        if('Chicken Pizza')in list_factor:
            list_factor.remove('Chicken Pizza')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)   
        f1_5.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()      
#---------------------first Click
    if B5==False:
        num5=1
        list_factor.append('Chicken Pizza')
        row5=list_factor.index('Chicken Pizza')+1
        listP5=['05','Chicken Pizza',f'{num5}','16$',f'{16*num5}$']
        f1_5=Frame(w,bg='black')
        l1_5=Label(f1_5,text=f'{row5}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_5=Label(f1_5,text=f'{listP5[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_5=Label(f1_5,text=f'{listP5[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_5=Label(f1_5,text=f'{num5}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_5=Label(f1_5,text=f'{listP5[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_5=Label(f1_5,text=f'{listP5[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_5=Entry(f1_5,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_5=Button(f1_5,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_5)
        Badd2_5=Button(f1_5,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_5)
        BDelete_5=Button(f1_5,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_5)
        A.append(listP5)
#---------------------next Click
    else:
        A.remove(listP5)
        num5+=1
        listP5=['05','Chicken Pizza',f'{num5}','16$',f'{16*num5}$']
        l1_5.config(text=f'{row5}')
        l4_5.config(text=f'{num5}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_5.config(text=f'{listP5[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP5)
#-----------------------grid
    l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_5.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_5.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_5.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_5.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_5.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_5.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_5.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_5.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_5.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_5.grid(row=row5+2,column=0,sticky=W+N)
    B5=True
    Total+=16
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)  
#---------------Def sandwich                
def sandwich():
    frp.grid_forget()
    frst.grid_forget()
    frsl.grid_forget()
    frd.grid_forget()
    btnm.configure(relief='raised',bg='white',fg='black')
    btnm3.configure(relief='raised',bg='white',fg='black')
    btnm4.configure(relief='raised',bg='white',fg='black')
    btnm5.configure(relief='raised',bg='white',fg='black')
    btnm2.config(relief='sunken',bg=btnm2['activebackground'],fg=btnm2['activeforeground'])
    frs.grid(row=2,column=2,sticky=E+N,padx=20,rowspan=60)
#-------------------Def Chicken filet
def Chickenfilet():
    #---------------global
    global Delete_6
    global Total
    global Tot6
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num6;global B6
    global f1_6;global listP6;global l1_6;global l2_6;global l3_6;global l4_6;global l5_6;global l6_6;global E1_6;global Badd_6;global Badd2_6;global BDelete_6
#--------------------def +
    def add1_6():
        global Total
        global num6
        global listP6
        num6+=1
        l4_6.config(text=f'{num6}')
        l4_6.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_6.config(text=f'{14*num6}$')
        l6_6.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_6.grid(row=row6+2,column=0,sticky=W+N)
        Total+=14
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP6)
        listP6=['06','Chicken filet',f'{num6}','14$',f'{14*num6}$']
        A.append(listP6)
#---------------------def -
    def add2_6():
        global Total
        global num6
        global listP6
        if num6>1:
            Total-=14
        num6-=1
        if num6<=1:
            num6=1
        l4_6.config(text=f'{num6}')
        l4_6.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_6.config(text=f'{14*num6}$')
        l6_6.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_6.grid(row=row6+2,column=0,sticky=W+N)
        
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP6)
        listP6=['06','Chicken filet',f'{num6}','14$',f'{14*num6}$']
        A.append(listP6)
#----------------------def delete
    def Delete_6():
        global Total
        global list_factor
        global num6;global B6
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP6)
        E1_6.delete(0,'end')
        Total-=14*num6
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B6=False
        if('Chicken filet')in list_factor:
            list_factor.remove('Chicken filet')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_6.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()
#---------------------first Click
    if B6==False:
        num6=1
        list_factor.append('Chicken filet')
        row6=list_factor.index('Chicken filet')+1
        listP6=['06','Chicken filet',f'{num6}','14$',f'{14*num6}$']
        f1_6=Frame(w,bg='black')
        l1_6=Label(f1_6,text=f'{row6}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_6=Label(f1_6,text=f'{listP6[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_6=Label(f1_6,text=f'{listP6[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_6=Label(f1_6,text=f'{num6}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_6=Label(f1_6,text=f'{listP6[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_6=Label(f1_6,text=f'{listP6[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_6=Entry(f1_6,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_6=Button(f1_6,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_6)
        Badd2_6=Button(f1_6,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_6)
        BDelete_6=Button(f1_6,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_6)
        A.append(listP6)
#---------------------next Click
    else:
        A.remove(listP6)
        num6+=1
        listP6=['06','Chicken filet',f'{num6}','14$',f'{14*num6}$']
        l1_6.config(text=f'{row6}')
        l4_6.config(text=f'{num6}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_6.config(text=f'{listP6[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP6)
#-----------------------grid
    l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_6.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_6.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_6.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_6.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_6.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_6.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_6.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_6.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_6.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_6.grid(row=row6+2,column=0,sticky=W+N)
    B6=True
    
    Total+=14
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#------------------------------def CheeseBurger
def CheeseBurger():
    #---------------global
    global Delete_7
    global Total
    global Tot7
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num7;global B7
    global f1_7;global listP7;global l1_7;global l2_7;global l3_7;global l4_7;global l5_7;global l6_7;global E1_7;global Badd_7;global Badd2_7;global BDelete_7
#--------------------def +
    def add1_7():
        global Total
        global num7
        global listP7
        num7+=1
        l4_7.config(text=f'{num7}')
        l4_7.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_7.config(text=f'{18*num7}$')
        l6_7.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_7.grid(row=row7+2,column=0,sticky=W+N)
        Total+=18
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP7)
        listP7=['07','CheeseBurger',f'{num7}','18$',f'{18*num7}$']
        A.append(listP7)
#---------------------def
    def add2_7():
        global Total
        global num7
        global listP7
        if num7>1:
            Total-=18
        num7-=1
        if num7<=1:
            num7=1
        l4_7.config(text=f'{num7}')
        l4_7.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_7.config(text=f'{18*num7}$')
        l6_7.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_7.grid(row=row7+2,column=0,sticky=W+N)
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP7)
        listP7=['07','CheeseBurger',f'{num7}','18$',f'{18*num7}$']
        A.append(listP7)
#----------------------def delete
    def Delete_7():
        global Total
        global list_factor
        global num7;global B7
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP7)
        E1_7.delete(0,'end')
        Total-=18*num7
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B7=False
        if('CheeseBurger')in list_factor:
            list_factor.remove('CheeseBurger')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N) 
        f1_7.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()
#---------------------first Click
    if B7==False:
        num7=1
        list_factor.append('CheeseBurger')
        row7=list_factor.index('CheeseBurger')+1
        listP7=['07','CheeseBurger',f'{num7}','18$',f'{18*num7}$']
        f1_7=Frame(w,bg='black')
        l1_7=Label(f1_7,text=f'{row7}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_7=Label(f1_7,text=f'{listP7[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_7=Label(f1_7,text=f'{listP7[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_7=Label(f1_7,text=f'{num7}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_7=Label(f1_7,text=f'{listP7[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_7=Label(f1_7,text=f'{listP7[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_7=Entry(f1_7,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_7=Button(f1_7,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_7)
        Badd2_7=Button(f1_7,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_7)
        BDelete_7=Button(f1_7,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_7)
        A.append(listP7)
#---------------------next Click
    else:
        A.remove(listP7)
        num7+=1
        listP7=['07','CheeseBurger',f'{num7}','18$',f'{18*num7}$']
        l1_7.config(text=f'{row7}')
        l4_7.config(text=f'{num7}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_7.config(text=f'{listP7[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP7)
#-----------------------grid
    l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_7.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_7.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_7.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_7.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_7.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_7.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_7.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_7.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_7.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_7.grid(row=row7+2,column=0,sticky=W+N)
    B7=True
    Total+=18
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#----------------------------------def Burger
def Burger():
    #---------------global
    global Delete_8
    global Total
    global Tot8
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num8;global B8
    global f1_8;global listP8;global l1_8;global l2_8;global l3_8;global l4_8;global l5_8;global l6_8;global E1_8;global Badd_8;global Badd2_8;global BDelete_8
#--------------------def +
    def add1_8():
        global Total
        global num8
        global listP8
        num8+=1
        l4_8.config(text=f'{num8}')
        l4_8.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_8.config(text=f'{16*num8}$')
        l6_8.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_8.grid(row=row8+2,column=0,sticky=W+N)
        Total+=16
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP8)
        listP8=['08','Burger',f'{num8}','16$',f'{16*num8}$']
        A.append(listP8)
#---------------------def
    def add2_8():
        global Total
        global num8
        global listP8
        if num8>1:
            Total-=16
        num8-=1
        if num8<=1:
            num8=1
        l4_8.config(text=f'{num8}')
        l4_8.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_8.config(text=f'{16*num8}$')
        l6_8.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_8.grid(row=row8+2,column=0,sticky=W+N)
        
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP8)
        listP8=['08','Burger',f'{num8}','16$',f'{16*num8}$']
        A.append(listP8)
#----------------------def delete
    def Delete_8():
        global Total
        global list_factor
        global num8;global B8
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP8)
        E1_8.delete(0,'end')
        Total-=16*num8
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B8=False
        if('Burger')in list_factor:
            list_factor.remove('Burger')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_8.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()
#---------------------first Click
    if B8==False:
        num8=1
        list_factor.append('Burger')
        row8=list_factor.index('Burger')+1
        listP8=['08','Burger',f'{num8}','16$',f'{16*num8}$']
        f1_8=Frame(w,bg='black')
        l1_8=Label(f1_8,text=f'{row8}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_8=Label(f1_8,text=f'{listP8[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_8=Label(f1_8,text=f'{listP8[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_8=Label(f1_8,text=f'{num8}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_8=Label(f1_8,text=f'{listP8[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_8=Label(f1_8,text=f'{listP8[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_8=Entry(f1_8,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_8=Button(f1_8,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_8)
        Badd2_8=Button(f1_8,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_8)
        BDelete_8=Button(f1_8,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_8)
        A.append(listP8)
#---------------------next Click
    else:
        A.remove(listP8)
        num8+=1
        listP8=['08','Burger',f'{num8}','16$',f'{16*num8}$']
        l1_8.config(text=f'{row8}')
        l4_8.config(text=f'{num8}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_8.config(text=f'{listP8[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP8)
#-----------------------grid
    l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_8.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_8.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_8.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_8.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_8.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_8.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_8.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_8.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_8.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_8.grid(row=row8+2,column=0,sticky=W+N)
    B8=True
    Total+=16
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#-----------------------def Turkish kebab
def Turkishkebab():
    #---------------global
    global Delete_9
    global Total
    global Tot9
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num9;global B9
    global f1_9;global listP9;global l1_9;global l2_9;global l3_9;global l4_9;global l5_9;global l6_9;global E1_9;global Badd_9;global Badd2_9;global BDelete_9
#--------------------def +
    def add1_9():
        global Total
        global num9
        global listP9
        num9+=1
        l4_9.config(text=f'{num9}')
        l4_9.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_9.config(text=f'{15*num9}$')
        l6_9.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_9.grid(row=row9+2,column=0,sticky=W+N)
        Total+=15
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP9)
        listP9=['09','Turkish kebab',f'{num9}','15$',f'{15*num9}$']
        A.append(listP9)
#---------------------def
    def add2_9():
        global Total
        global num9
        global listP9
        if num9>1:
            Total-=15
        num9-=1
        if num9<=1:
            num9=1
        l4_9.config(text=f'{num9}')
        l4_9.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_9.config(text=f'{15*num9}$')
        l6_9.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_9.grid(row=row9+2,column=0,sticky=W+N)
        
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP9)
        listP9=['09','Turkish kebab',f'{num9}','15$',f'{15*num9}$']
        A.append(listP9)
#----------------------def delete
    def Delete_9():
        global Total
        global list_factor
        global num9;global B9
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP9)
        E1_9.delete(0,'end')
        Total-=15*num9
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B9=False
        if('Turkish kebab')in list_factor:
            list_factor.remove('Turkish kebab')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_9.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()   
#---------------------first Click
    if B9==False:
        num9=1
        list_factor.append('Turkish kebab')
        row9=list_factor.index('Turkish kebab')+1
        listP9=['09','Turkish kebab',f'{num9}','15$',f'{15*num9}$']
        f1_9=Frame(w,bg='black')
        l1_9=Label(f1_9,text=f'{row9}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_9=Label(f1_9,text=f'{listP9[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_9=Label(f1_9,text=f'{listP9[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_9=Label(f1_9,text=f'{num9}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_9=Label(f1_9,text=f'{listP9[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_9=Label(f1_9,text=f'{listP9[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_9=Entry(f1_9,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_9=Button(f1_9,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_9)
        Badd2_9=Button(f1_9,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_9)
        BDelete_9=Button(f1_9,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_9)
        A.append(listP9)
#---------------------next Click
    else:
        A.remove(listP9)
        num9+=1
        listP9=['09','Turkish kebab',f'{num9}','15$',f'{15*num9}$']
        l1_9.config(text=f'{row9}')
        l4_9.config(text=f'{num9}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_9.config(text=f'{listP9[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP9)
#-----------------------grid
    l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_9.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_9.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_9.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_9.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_9.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_9.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_9.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_9.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_9.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_9.grid(row=row9+2,column=0,sticky=W+N)
    B9=True
    Total+=15
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#------------------------------def Hot Dog
def HotDog():
    #---------------global
    global Delete_10
    global Total
    global Tot10
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num10;global B10
    global f1_10;global listP10;global l1_10;global l2_10;global l3_10;global l4_10;global l5_10;global l6_10;global E1_10;global Badd_10;global Badd2_10;global BDelete_10
#--------------------def +
    def add1_10():
        global Total
        global num10
        global listP10
        num10+=1
        l4_10.config(text=f'{num10}')
        l4_10.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_10.config(text=f'{12*num10}$')
        l6_10.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_10.grid(row=row10+2,column=0,sticky=W+N)
        Total+=12
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP10)
        listP10=['010','Hot Dog',f'{num10}','12$',f'{12*num10}$']
        A.append(listP10)
#---------------------def
    def add2_10():
        global Total
        global num10
        global listP10
        if num10>1:
            Total-=12
        num10-=1
        if num10<=1:
            num10=1
        l4_10.config(text=f'{num10}')
        l4_10.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_10.config(text=f'{12*num10}$')
        l6_10.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_10.grid(row=row10+2,column=0,sticky=W+N) 
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP10)
        listP10=['010','Hot Dog',f'{num10}','12$',f'{12*num10}$']
        A.append(listP10)
#----------------------def delete
    def Delete_10():
        global Total
        global list_factor
        global num10;global B10
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP10)
        E1_10.delete(0,'end')
        Total-=12*num10
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B10=False
        if('Hot Dog')in list_factor:
            list_factor.remove('Hot Dog')
            
        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_10.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()
#---------------------first Click
    if B10==False:
        num10=1
        list_factor.append('Hot Dog')
        row10=list_factor.index('Hot Dog')+1
        listP10=['010','Hot Dog',f'{num10}','12$',f'{12*num10}$']
        f1_10=Frame(w,bg='black')
        l1_10=Label(f1_10,text=f'{row10}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_10=Label(f1_10,text=f'{listP10[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_10=Label(f1_10,text=f'{listP10[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_10=Label(f1_10,text=f'{num10}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_10=Label(f1_10,text=f'{listP10[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_10=Label(f1_10,text=f'{listP10[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_10=Entry(f1_10,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_10=Button(f1_10,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_10)
        Badd2_10=Button(f1_10,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_10)
        BDelete_10=Button(f1_10,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_10)
        A.append(listP10)
#---------------------next Click
    else:
        A.remove(listP10)
        num10+=1
        listP10=['010','Hot Dog',f'{num10}','12$',f'{12*num10}$']
        l1_10.config(text=f'{row10}')
        l4_10.config(text=f'{num10}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_10.config(text=f'{listP10[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP10)
#-----------------------grid
    l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_10.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_10.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_10.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_10.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_10.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_10.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_10.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_10.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_10.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_10.grid(row=row10+2,column=0,sticky=W+N)
    B10=True
    Total+=12
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)   
#---------------Def Steak
def steak():
    frs.grid_forget()
    frp.grid_forget()
    frsl.grid_forget()
    frd.grid_forget()
    btnm.configure(relief='raised',bg='white',fg='black')
    btnm2.configure(relief='raised',bg='white',fg='black')
    btnm4.configure(relief='raised',bg='white',fg='black')
    btnm5.configure(relief='raised',bg='white',fg='black')
    btnm3.config(relief='sunken',bg=btnm3['activebackground'],fg=btnm3['activeforeground'])
    frst.grid(row=2,column=2,sticky=E+N,padx=20,rowspan=60)
#--------------------def T-Bone
def TBone():
    #---------------global
    global Delete_11
    global Total
    global Tot11
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num11;global B11
    global f1_11;global listP11;global l1_11;global l2_11;global l3_11;global l4_11;global l5_11;global l6_11;global E1_11;global Badd_11;global Badd2_11;global BDelete_11
#--------------------def +
    def add1_11():
        global Total
        global num11
        global listP11
        num11+=1
        l4_11.config(text=f'{num11}')
        l4_11.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_11.config(text=f'{30*num11}$')
        l6_11.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_11.grid(row=row11+2,column=0,sticky=W+N)
        Total+=30
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP11)
        listP11=['011','T-Bone',f'{num11}','30$',f'{30*num11}$']
        A.append(listP11)
#---------------------def
    def add2_11():
        global Total
        global num11
        global listP11
        if num11>1:
            Total-=30
        num11-=1
        if num11<=1:
            num11=1
        l4_11.config(text=f'{num11}')
        l4_11.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_11.config(text=f'{30*num11}$')
        l6_11.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_11.grid(row=row11+2,column=0,sticky=W+N)
        
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP11)
        listP11=['011','T-Bone',f'{num11}','30$',f'{30*num11}$']
        A.append(listP11)
#----------------------def delete
    def Delete_11():
        global Total
        global list_factor
        global num11;global B11
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP11)
        E1_11.delete(0,'end')
        Total-=30*num11
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B11=False
        if('T-Bone')in list_factor:
            list_factor.remove('T-Bone')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_11.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()
#---------------------first Click
    if B11==False:
        num11=1
        list_factor.append('T-Bone')
        row11=list_factor.index('T-Bone')+1
        listP11=['011','T-Bone',f'{num11}','30$',f'{30*num11}$']
        f1_11=Frame(w,bg='black')
        l1_11=Label(f1_11,text=f'{row11}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_11=Label(f1_11,text=f'{listP11[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_11=Label(f1_11,text=f'{listP11[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_11=Label(f1_11,text=f'{num11}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_11=Label(f1_11,text=f'{listP11[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_11=Label(f1_11,text=f'{listP11[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_11=Entry(f1_11,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_11=Button(f1_11,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_11)
        Badd2_11=Button(f1_11,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_11)
        BDelete_11=Button(f1_11,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_11)
        A.append(listP11)
#---------------------next Click
    else:
        A.remove(listP11)
        num11+=1
        listP11=['011','T-Bone',f'{num11}','30$',f'{30*num11}$']
        l1_11.config(text=f'{row11}')
        l4_11.config(text=f'{num11}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_11.config(text=f'{listP11[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP11)
#-----------------------grid
    l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_11.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_11.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_11.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_11.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_11.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_11.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_11.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_11.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_11.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_11.grid(row=row11+2,column=0,sticky=W+N)
    B11=True
    Total+=30
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#--------------------def Filet Mignon
def FiletMignon():
    #---------------global
    global Delete_12
    global Total
    global Tot12
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num12;global B12
    global f1_12;global listP12;global l1_12;global l2_12;global l3_12;global l4_12;global l5_12;global l6_12;global E1_12;global Badd_12;global Badd2_12;global BDelete_12
#--------------------def +
    def add1_12():
        global Total
        global num12
        global listP12
        num12+=1
        l4_12.config(text=f'{num12}')
        l4_12.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_12.config(text=f'{28*num12}$')
        l6_12.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_12.grid(row=row12+2,column=0,sticky=W+N)
        Total+=28
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP12)
        listP12=['012','Filet Mignon',f'{num12}','28$',f'{28*num12}$']
        A.append(listP12)
#---------------------def
    def add2_12():
        global Total
        global num12
        global listP12
        if num12>1:
            Total-=28
        num12-=1
        if num12<=1:
            num12=1
        l4_12.config(text=f'{num12}')
        l4_12.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_12.config(text=f'{28*num12}$')
        l6_12.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_12.grid(row=row12+2,column=0,sticky=W+N)
        
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP12)
        listP12=['012','Filet Mignon',f'{num12}','28$',f'{28*num12}$']
        A.append(listP12)
#----------------------def delete
    def Delete_12():
        global Total
        global list_factor
        global num12;global B12
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP12)
        E1_12.delete(0,'end')
        Total-=28*num12
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B12=False
        if('Filet Mignon')in list_factor:
            list_factor.remove('Filet Mignon')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_12.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()
        
#---------------------first Click
    if B12==False:
        num12=1
        list_factor.append('Filet Mignon')
        row12=list_factor.index('Filet Mignon')+1
        listP12=['012','Filet Mignon',f'{num12}','28$',f'{28*num12}$']
        f1_12=Frame(w,bg='black')
        l1_12=Label(f1_12,text=f'{row12}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_12=Label(f1_12,text=f'{listP12[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_12=Label(f1_12,text=f'{listP12[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_12=Label(f1_12,text=f'{num12}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_12=Label(f1_12,text=f'{listP12[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_12=Label(f1_12,text=f'{listP12[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_12=Entry(f1_12,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_12=Button(f1_12,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_12)
        Badd2_12=Button(f1_12,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_12)
        BDelete_12=Button(f1_12,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_12)
        A.append(listP12)
#---------------------next Click
    else:
        A.remove(listP12)
        num12+=1
        listP12=['012','Filet Mignon',f'{num12}','28$',f'{28*num12}$']
        l1_12.config(text=f'{row12}')
        l4_12.config(text=f'{num12}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_12.config(text=f'{listP12[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP12)
#-----------------------grid
    l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_12.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_12.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_12.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_12.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_12.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_12.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_12.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_12.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_12.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_12.grid(row=row12+2,column=0,sticky=W+N)
    B12=True
    Total+=28
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#------------------------def Ribeye
def Ribeye():
    #---------------global
    global Delete_13
    global Total
    global Tot13
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num13;global B13
    global f1_13;global listP13;global l1_13;global l2_13;global l3_13;global l4_13;global l5_13;global l6_13;global E1_13;global Badd_13;global Badd2_13;global BDelete_13
#--------------------def +
    def add1_13():
        global Total
        global num13
        global listP13
        num13+=1
        l4_13.config(text=f'{num13}')
        l4_13.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_13.config(text=f'{25*num13}$')
        l6_13.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_13.grid(row=row13+2,column=0,sticky=W+N)
        Total+=25
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP13)
        listP13=['013','Ribeye',f'{num13}','25$',f'{25*num13}$']
        A.append(listP13)
#---------------------def
    def add2_13():
        global Total
        global num13
        global listP13
        if num13>1:
            Total-=25
        num13-=1
        if num13<=1:
            num13=1
        l4_13.config(text=f'{num13}')
        l4_13.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_13.config(text=f'{25*num13}$')
        l6_13.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_13.grid(row=row13+2,column=0,sticky=W+N)
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP13)
        listP13=['013','Ribeye',f'{num13}','25$',f'{25*num13}$']
        A.append(listP13)
#----------------------def delete
    def Delete_13():
        global Total
        global list_factor
        global num13;global B13
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP13)
        E1_13.delete(0,'end')
        Total-=25*num13
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B13=False
        if('Ribeye')in list_factor:
            list_factor.remove('Ribeye')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_13.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()
#---------------------first Click
    if B13==False:
        num13=1
        list_factor.append('Ribeye')
        row13=list_factor.index('Ribeye')+1
        listP13=['013','Ribeye',f'{num13}','25$',f'{25*num13}$']
        f1_13=Frame(w,bg='black')
        l1_13=Label(f1_13,text=f'{row13}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_13=Label(f1_13,text=f'{listP13[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_13=Label(f1_13,text=f'{listP13[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_13=Label(f1_13,text=f'{num13}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_13=Label(f1_13,text=f'{listP13[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_13=Label(f1_13,text=f'{listP13[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_13=Entry(f1_13,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_13=Button(f1_13,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_13)
        Badd2_13=Button(f1_13,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_13)
        BDelete_13=Button(f1_13,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_13)
        A.append(listP13)
#---------------------next Click
    else:
        A.remove(listP13)
        num13+=1
        listP13=['013','Ribeye',f'{num13}','25$',f'{25*num13}$']
        l1_13.config(text=f'{row13}')
        l4_13.config(text=f'{num13}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_13.config(text=f'{listP13[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP13)
#-----------------------grid
    l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_13.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_13.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_13.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_13.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_13.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_13.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_13.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_13.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_13.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_13.grid(row=row13+2,column=0,sticky=W+N)
    B13=True
    Total+=25
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#-----------------------def Tri-Tip
def TriTip():
    #---------------global
    global Delete_14
    global Total
    global Tot14
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num14;global B14
    global f1_14;global listP14;global l1_14;global l2_14;global l3_14;global l4_14;global l5_14;global l6_14;global E1_14;global Badd_14;global Badd2_14;global BDelete_14
#--------------------def +
    def add1_14():
        global Total
        global num14
        global listP14
        num14+=1
        l4_14.config(text=f'{num14}')
        l4_14.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_14.config(text=f'{20*num14}$')
        l6_14.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_14.grid(row=row14+2,column=0,sticky=W+N)
        Total+=20
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP14)
        listP14=['014','Tri-Tip',f'{num14}','20$',f'{20*num14}$']
        A.append(listP14)
#---------------------def
    def add2_14():
        global Total
        global num14
        global listP14
        if num14>1:
            Total-=20
        num14-=1
        if num14<=1:
            num14=1
        l4_14.config(text=f'{num14}')
        l4_14.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_14.config(text=f'{20*num14}$')
        l6_14.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_14.grid(row=row14+2,column=0,sticky=W+N)
        
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP14)
        listP14=['014','Tri-Tip',f'{num14}','20$',f'{20*num14}$']
        A.append(listP14)
#----------------------def delete
    def Delete_14():
        global Total
        global list_factor
        global num14;global B14
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP14)
        E1_14.delete(0,'end')
        Total-=20*num14
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B14=False
        if('Tri-Tip')in list_factor:
            list_factor.remove('Tri-Tip')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_14.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()
#---------------------first Click
    if B14==False:
        num14=1
        list_factor.append('Tri-Tip')
        row14=list_factor.index('Tri-Tip')+1
        listP14=['014','Tri-Tip',f'{num14}','20$',f'{20*num14}$']
        f1_14=Frame(w,bg='black')
        l1_14=Label(f1_14,text=f'{row14}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_14=Label(f1_14,text=f'{listP14[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_14=Label(f1_14,text=f'{listP14[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_14=Label(f1_14,text=f'{num14}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_14=Label(f1_14,text=f'{listP14[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_14=Label(f1_14,text=f'{listP14[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_14=Entry(f1_14,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_14=Button(f1_14,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_14)
        Badd2_14=Button(f1_14,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_14)
        BDelete_14=Button(f1_14,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_14)
        A.append(listP14)
#---------------------next Click
    else:
        A.remove(listP14)
        num14+=1
        listP14=['014','Tri-Tip',f'{num14}','20$',f'{20*num14}$']
        l1_14.config(text=f'{row14}')
        l4_14.config(text=f'{num14}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_14.config(text=f'{listP14[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP14)
#-----------------------grid
    l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_14.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_14.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_14.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_14.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_14.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_14.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_14.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_14.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_14.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_14.grid(row=row14+2,column=0,sticky=W+N)
    B14=True
    Total+=20
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#---------------Def Salad
def salad():
    frs.grid_forget()
    frp.grid_forget()
    frst.grid_forget()
    frd.grid_forget()
    btnm.configure(relief='raised',bg='white',fg='black')
    btnm2.configure(relief='raised',bg='white',fg='black')
    btnm3.configure(relief='raised',bg='white',fg='black')
    btnm5.configure(relief='raised',bg='white',fg='black')
    btnm4.config(relief='sunken',bg=btnm4['activebackground'],fg=btnm4['activeforeground'])
    frsl.grid(row=2,column=2,sticky=E+N,padx=20,rowspan=60)
#-----------------def Greek
def Greek():
    #---------------global
    global Delete_15
    global Total
    global Tot15
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num15;global B15
    global f1_15;global listP15;global l1_15;global l2_15;global l3_15;global l4_15;global l5_15;global l6_15;global E1_15;global Badd_15;global Badd2_15;global BDelete_15
#--------------------def +
    def add1_15():
        global Total
        global num15
        global listP15
        num15+=1
        l4_15.config(text=f'{num15}')
        l4_15.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_15.config(text=f'{10*num15}$')
        l6_15.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_15.grid(row=row15+2,column=0,sticky=W+N)
        Total+=10
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP15)
        listP15=['015','Greek',f'{num15}','10$',f'{10*num15}$']
        A.append(listP15)
#---------------------def
    def add2_15():
        global Total
        global num15
        global listP15
        if num15>1:
            Total-=10
        num15-=1
        if num15<=1:
            num15=1
        l4_15.config(text=f'{num15}')
        l4_15.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_15.config(text=f'{10*num15}$')
        l6_15.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_15.grid(row=row15+2,column=0,sticky=W+N)
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP15)
        listP15=['015','Greek',f'{num15}','10$',f'{10*num15}$']
        A.append(listP15)
#----------------------def delete
    def Delete_15():
        global Total
        global list_factor
        global num15;global B15
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP15)
        E1_15.delete(0,'end')
        Total-=10*num15
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B15=False
        if('Greek')in list_factor:
            list_factor.remove('Greek')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_15.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()
#---------------------first Click
    if B15==False:
        num15=1
        list_factor.append('Greek')
        row15=list_factor.index('Greek')+1
        listP15=['015','Greek',f'{num15}','10$',f'{10*num15}$']
        f1_15=Frame(w,bg='black')
        l1_15=Label(f1_15,text=f'{row15}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_15=Label(f1_15,text=f'{listP15[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_15=Label(f1_15,text=f'{listP15[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_15=Label(f1_15,text=f'{num15}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_15=Label(f1_15,text=f'{listP15[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_15=Label(f1_15,text=f'{listP15[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_15=Entry(f1_15,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_15=Button(f1_15,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_15)
        Badd2_15=Button(f1_15,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_15)
        BDelete_15=Button(f1_15,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_15)
        A.append(listP15)
#---------------------next Click
    else:
        A.remove(listP15)
        num15+=1
        listP15=['015','Greek',f'{num15}','10$',f'{10*num15}$']
        l1_15.config(text=f'{row15}')
        l4_15.config(text=f'{num15}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_15.config(text=f'{listP15[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP15)
#-----------------------grid
    l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_15.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_15.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_15.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_15.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_15.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_15.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_15.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_15.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_15.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_15.grid(row=row15+2,column=0,sticky=W+N)
    B15=True
    Total+=10
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#-----------------------def Caesar
def Caesar():
    #---------------global
    global Delete_16
    global Total
    global Tot16
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num16;global B16
    global f1_16;global listP16;global l1_16;global l2_16;global l3_16;global l4_16;global l5_16;global l6_16;global E1_16;global Badd_16;global Badd2_16;global BDelete_16
#--------------------def +
    def add1_16():
        global Total
        global num16
        global listP16
        num16+=1
        l4_16.config(text=f'{num16}')
        l4_16.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_16.config(text=f'{15*num16}$')
        l6_16.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_16.grid(row=row16+2,column=0,sticky=W+N)
        Total+=15
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP16)
        listP16=['016','Caesar',f'{num16}','15$',f'{15*num16}$']
        A.append(listP16)
#---------------------def
    def add2_16():
        global Total
        global num16
        global listP16
        if num16>1:
            Total-=15
        num16-=1
        if num16<=1:
            num16=1
        l4_16.config(text=f'{num16}')
        l4_16.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_16.config(text=f'{15*num16}$')
        l6_16.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_16.grid(row=row16+2,column=0,sticky=W+N)
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP16)
        listP16=['016','Caesar',f'{num16}','15$',f'{15*num16}$']
        A.append(listP16)
#----------------------def delete
    def Delete_16():
        global Total
        global list_factor
        global num16;global B16
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP16)
        E1_16.delete(0,'end')
        Total-=15*num16
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B16=False
        if('Caesar')in list_factor:
            list_factor.remove('Caesar')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_16.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()        
#---------------------first Click
    if B16==False:
        num16=1
        list_factor.append('Caesar')
        row16=list_factor.index('Caesar')+1
        listP16=['016','Caesar',f'{num16}','15$',f'{15*num16}$']
        f1_16=Frame(w,bg='black')
        l1_16=Label(f1_16,text=f'{row16}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_16=Label(f1_16,text=f'{listP16[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_16=Label(f1_16,text=f'{listP16[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_16=Label(f1_16,text=f'{num16}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_16=Label(f1_16,text=f'{listP16[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_16=Label(f1_16,text=f'{listP16[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_16=Entry(f1_16,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_16=Button(f1_16,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_16)
        Badd2_16=Button(f1_16,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_16)
        BDelete_16=Button(f1_16,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_16)
        A.append(listP16)
#---------------------next Click
    else:
        A.remove(listP16)
        num16+=1
        listP16=['016','Caesar',f'{num16}','15$',f'{15*num16}$']
        l1_16.config(text=f'{row16}')
        l4_16.config(text=f'{num16}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_16.config(text=f'{listP16[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP16)
#-----------------------grid
    l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_16.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_16.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_16.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_16.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_16.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_16.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_16.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_16.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_16.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_16.grid(row=row16+2,column=0,sticky=W+N)
    B16=True 
    Total+=15
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#---------------------------def Solterito
def Solterito():
    #---------------global
    global Delete_17
    global Total
    global Tot17
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num17;global B17
    global f1_17;global listP17;global l1_17;global l2_17;global l3_17;global l4_17;global l5_17;global l6_17;global E1_17;global Badd_17;global Badd2_17;global BDelete_17
#--------------------def +
    def add1_17():
        global Total
        global num17
        global listP17
        num17+=1
        l4_17.config(text=f'{num17}')
        l4_17.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_17.config(text=f'{12*num17}$')
        l6_17.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_17.grid(row=row17+2,column=0,sticky=W+N)
        Total+=12
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP17)
        listP17=['017','Solterito',f'{num17}','12$',f'{12*num17}$']
        A.append(listP17)
#---------------------def
    def add2_17():
        global Total
        global num17
        global listP17
        if num17>1:
            Total-=12
        num17-=1
        if num17<=1:
            num17=1
        l4_17.config(text=f'{num17}')
        l4_17.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_17.config(text=f'{12*num17}$')
        l6_17.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_17.grid(row=row17+2,column=0,sticky=W+N)
        
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP17)
        listP17=['017','Solterito',f'{num17}','12$',f'{12*num17}$']
        A.append(listP17)
#----------------------def delete
    def Delete_17():
        global Total
        global list_factor
        global num17;global B17
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP17)
        E1_17.delete(0,'end')
        Total-=12*num17
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B17=False
        if('Solterito')in list_factor:
            list_factor.remove('Solterito')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_17.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()       
#---------------------first Click
    if B17==False:
        num17=1
        list_factor.append('Solterito')
        row17=list_factor.index('Solterito')+1
        listP17=['017','Solterito',f'{num17}','12$',f'{12*num17}$']
        f1_17=Frame(w,bg='black')
        l1_17=Label(f1_17,text=f'{row17}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_17=Label(f1_17,text=f'{listP17[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_17=Label(f1_17,text=f'{listP17[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_17=Label(f1_17,text=f'{num17}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_17=Label(f1_17,text=f'{listP17[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_17=Label(f1_17,text=f'{listP17[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_17=Entry(f1_17,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_17=Button(f1_17,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_17)
        Badd2_17=Button(f1_17,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_17)
        BDelete_17=Button(f1_17,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_17)
        A.append(listP17)
#---------------------next Click
    else:
        A.remove(listP17)
        num17+=1
        listP17=['017','Solterito',f'{num17}','12$',f'{12*num17}$']
        l1_17.config(text=f'{row17}')
        l4_17.config(text=f'{num17}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_17.config(text=f'{listP17[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP17)
#-----------------------grid
    l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_17.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_17.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_17.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_17.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_17.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_17.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_17.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_17.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_17.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_17.grid(row=row17+2,column=0,sticky=W+N)
    B17=True   
    Total+=12
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#------------------------def Shirazi
def Shirazi():
    #---------------global
    global Delete_18
    global Total
    global Tot18
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num18;global B18
    global f1_18;global listP18;global l1_18;global l2_18;global l3_18;global l4_18;global l5_18;global l6_18;global E1_18;global Badd_18;global Badd2_18;global BDelete_18
#--------------------def +
    def add1_18():
        global Total
        global num18
        global listP18
        num18+=1
        l4_18.config(text=f'{num18}')
        l4_18.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_18.config(text=f'{8*num18}$')
        l6_18.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_18.grid(row=row18+2,column=0,sticky=W+N)
        Total+=8
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP18)
        listP18=['018','Shirazi',f'{num18}','8$',f'{8*num18}$']
        A.append(listP18)
#---------------------def
    def add2_18():
        global Total
        global num18
        global listP18
        if num18>1:
            Total-=8
        num18-=1
        if num18<=1:
            num18=1
        l4_18.config(text=f'{num18}')
        l4_18.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_18.config(text=f'{8*num18}$')
        l6_18.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_18.grid(row=row18+2,column=0,sticky=W+N)
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP18)
        listP18=['018','Shirazi',f'{num18}','8$',f'{8*num18}$']
        A.append(listP18)
#----------------------def delete
    def Delete_18():
        global Total
        global list_factor
        global num18;global B18
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP18)
        E1_18.delete(0,'end')
        Total-=8*num18
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B18=False
        if('Shirazi')in list_factor:
            list_factor.remove('Shirazi')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_18.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()       
#---------------------first Click
    if B18==False:
        num18=1
        list_factor.append('Shirazi')
        row18=list_factor.index('Shirazi')+1
        listP18=['018','Shirazi',f'{num18}','8$',f'{8*num18}$']
        f1_18=Frame(w,bg='black')
        l1_18=Label(f1_18,text=f'{row18}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_18=Label(f1_18,text=f'{listP18[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_18=Label(f1_18,text=f'{listP18[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_18=Label(f1_18,text=f'{num18}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_18=Label(f1_18,text=f'{listP18[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_18=Label(f1_18,text=f'{listP18[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_18=Entry(f1_18,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_18=Button(f1_18,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_18)
        Badd2_18=Button(f1_18,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_18)
        BDelete_18=Button(f1_18,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_18)
        A.append(listP18)
#---------------------next Click
    else:
        A.remove(listP18)
        num18+=1
        listP18=['018','Shirazi',f'{num18}','8$',f'{8*num18}$']
        l1_18.config(text=f'{row18}')
        l4_18.config(text=f'{num18}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_18.config(text=f'{listP18[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP18)
#-----------------------grid
    l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_18.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_18.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_18.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_18.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_18.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_18.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_18.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_18.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_18.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_18.grid(row=row18+2,column=0,sticky=W+N)
    B18=True 
    Total+=8
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#---------------Def Drink
def drink():
    frs.grid_forget()
    frp.grid_forget()
    frst.grid_forget()
    frsl.grid_forget()
    btnm.configure(relief='raised',bg='white',fg='black')
    btnm2.configure(relief='raised',bg='white',fg='black')
    btnm3.configure(relief='raised',bg='white',fg='black')
    btnm4.configure(relief='raised',bg='white',fg='black')
    btnm5.config(relief='sunken',bg=btnm5['activebackground'],fg=btnm5['activeforeground'])
    frd.grid(row=2,column=2,sticky=E+N,padx=20,rowspan=60)
#------------------------def Water
def Water():
    #---------------global
    global Delete_19
    global Total
    global Tot19
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num19;global B19
    global f1_19;global listP19;global l1_19;global l2_19;global l3_19;global l4_19;global l5_19;global l6_19;global E1_19;global Badd_19;global Badd2_19;global BDelete_19
#--------------------def +
    def add1_19():
        global Total
        global num19
        global listP19
        num19+=1
        l4_19.config(text=f'{num19}')
        l4_19.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_19.config(text=f'{1*num19}$')
        l6_19.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_19.grid(row=row19+2,column=0,sticky=W+N)
        Total+=1
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP19)
        listP19=['019','Water',f'{num19}','1$',f'{1*num19}$']
        A.append(listP19)
#---------------------def
    def add2_19():
        global Total
        global num19
        global listP19
        if num19>1:
            Total-=1
        num19-=1
        if num19<=1:
            num19=1
        l4_19.config(text=f'{num19}')
        l4_19.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_19.config(text=f'{1*num19}$')
        l6_19.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_19.grid(row=row19+2,column=0,sticky=W+N)
        
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP19)
        listP19=['019','Water',f'{num19}','1$',f'{1*num19}$']
        A.append(listP19)
#----------------------def delete
    def Delete_19():
        global Total
        global list_factor
        global num19;global B19
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP19)
        E1_19.delete(0,'end')
        Total-=1*num19
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B19=False
        if('Water')in list_factor:
            list_factor.remove('Water')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_19.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()
#---------------------first Click
    if B19==False:
        num19=1
        list_factor.append('Water')
        row19=list_factor.index('Water')+1
        listP19=['019','Water',f'{num19}','1$',f'{1*num19}$']
        f1_19=Frame(w,bg='black')
        l1_19=Label(f1_19,text=f'{row19}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_19=Label(f1_19,text=f'{listP19[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_19=Label(f1_19,text=f'{listP19[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_19=Label(f1_19,text=f'{num19}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_19=Label(f1_19,text=f'{listP19[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_19=Label(f1_19,text=f'{listP19[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_19=Entry(f1_19,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_19=Button(f1_19,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_19)
        Badd2_19=Button(f1_19,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_19)
        BDelete_19=Button(f1_19,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_19)
        A.append(listP19)
#---------------------next Click
    else:
        A.remove(listP19)
        num19+=1
        listP19=['019','Water',f'{num19}','1$',f'{1*num19}$']
        l1_19.config(text=f'{row19}')
        l4_19.config(text=f'{num19}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_19.config(text=f'{listP19[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP19)
#-----------------------grid
    l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_19.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_19.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_19.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_19.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_19.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_19.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_19.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_19.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_19.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_19.grid(row=row19+2,column=0,sticky=W+N)
    B19=True
    Total+=1
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#-----------------------------def Tea
def Tea():
    #---------------global
    global Delete_20
    global Total
    global Tot20
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num20;global B20
    global f1_20;global listP20;global l1_20;global l2_20;global l3_20;global l4_20;global l5_20;global l6_20;global E1_20;global Badd_20;global Badd2_20;global BDelete_20
#--------------------def +
    def add1_20():
        global Total
        global num20
        global listP20
        num20+=1
        l4_20.config(text=f'{num20}')
        l4_20.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_20.config(text=f'{1.5*num20}$')
        l6_20.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_20.grid(row=row20+2,column=0,sticky=W+N)
        Total+=1.5
        if num20%2==0:
            Total=int(Total)
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP20)
        listP20=['020','Tea',f'{num20}','1.5$',f'{1.5*num20}$']
        A.append(listP20)
#---------------------def
    def add2_20():
        global Total
        global num20
        global listP20
        if num20>1:
            Total-=1.5
        num20-=1
        if num20<=1:
            num20=1
        l4_20.config(text=f'{num20}')
        l4_20.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_20.config(text=f'{1.5*num20}$')
        l6_20.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_20.grid(row=row20+2,column=0,sticky=W+N)
        
        if num20%2==0:
            Total=int(Total)
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP20)
        listP20=['020','Tea',f'{num20}','1.5$',f'{1.5*num20}$']
        A.append(listP20)
#----------------------def delete
    def Delete_20():
        global Total
        global list_factor
        global num20;global B20
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP20)
        E1_20.delete(0,'end')
        Total-=1.5*num20
        
        Total=int(Total)
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B20=False
        if('Tea')in list_factor:
            list_factor.remove('Tea')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_20.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()
#---------------------first Click
    if B20==False:
        num20=1
        list_factor.append('Tea')
        row20=list_factor.index('Tea')+1
        listP20=['020','Tea',f'{num20}','1.5$',f'{1.5*num20}$']
        f1_20=Frame(w,bg='black')
        l1_20=Label(f1_20,text=f'{row20}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_20=Label(f1_20,text=f'{listP20[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_20=Label(f1_20,text=f'{listP20[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_20=Label(f1_20,text=f'{num20}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_20=Label(f1_20,text=f'{listP20[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_20=Label(f1_20,text=f'{listP20[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_20=Entry(f1_20,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_20=Button(f1_20,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_20)
        Badd2_20=Button(f1_20,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_20)
        BDelete_20=Button(f1_20,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_20)
        A.append(listP20)
#---------------------next Click
    else:
        A.remove(listP20)
        num20+=1
        listP20=['020','Tea',f'{num20}','1.5$',f'{1.5*num20}$']
        l1_20.config(text=f'{row20}')
        l4_20.config(text=f'{num20}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_20.config(text=f'{listP20[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP20)
#-----------------------grid
    l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_20.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_20.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_20.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_20.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_20.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_20.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_20.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_20.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_20.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_20.grid(row=row20+2,column=0,sticky=W+N)
    B20=True
    Total+=1.5
    if num20%2==0:
        Total=int(Total)
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#--------------------------------def CocaCola
def CocaCola():
    #---------------global
    global Delete_21
    global Total
    global Tot21
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num21;global B21
    global f1_21;global listP21;global l1_21;global l2_21;global l3_21;global l4_21;global l5_21;global l6_21;global E1_21;global Badd_21;global Badd2_21;global BDelete_21
#--------------------def +
    def add1_21():
        global Total
        global num21
        global listP21
        num21+=1
        l4_21.config(text=f'{num21}')
        l4_21.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_21.config(text=f'{2*num21}$')
        l6_21.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_21.grid(row=row21+2,column=0,sticky=W+N)
        Total+=2
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP21)
        listP21=['021','Coca Cola',f'{num21}','2$',f'{2*num21}$']
        A.append(listP21)
#---------------------def
    def add2_21():
        global Total
        global num21
        global listP21
        if num21>1:
            Total-=2
        num21-=1
        if num21<=1:
            num21=1
        l4_21.config(text=f'{num21}')
        l4_21.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_21.config(text=f'{2*num21}$')
        l6_21.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_21.grid(row=row21+2,column=0,sticky=W+N)

        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP21)
        listP21=['021','Coca Cola',f'{num21}','2$',f'{2*num21}$']
        A.append(listP21)
#----------------------def delete
    def Delete_21():
        global Total
        global list_factor
        global num21;global B21
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP21)
        E1_21.delete(0,'end')
        Total-=2*num21
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B21=False
        if('Coca Cola')in list_factor:
            list_factor.remove('Coca Cola')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Sprite'in list_factor:
            row22=list_factor.index('Sprite')+1
            l1_22.config(text=f'{row22}')
            l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_22.grid(row=row22+2,column=0,sticky=W+N)
        f1_21.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()  
#---------------------first Click
    if B21==False:
        num21=1
        list_factor.append('Coca Cola')
        row21=list_factor.index('Coca Cola')+1
        listP21=['021','Coca Cola',f'{num21}','2$',f'{2*num21}$']
        f1_21=Frame(w,bg='black')
        l1_21=Label(f1_21,text=f'{row21}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_21=Label(f1_21,text=f'{listP21[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_21=Label(f1_21,text=f'{listP21[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_21=Label(f1_21,text=f'{num21}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_21=Label(f1_21,text=f'{listP21[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_21=Label(f1_21,text=f'{listP21[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_21=Entry(f1_21,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_21=Button(f1_21,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_21)
        Badd2_21=Button(f1_21,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_21)
        BDelete_21=Button(f1_21,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_21)
        A.append(listP21)
#---------------------next Click
    else:
        A.remove(listP21)
        num21+=1
        listP21=['021','Coca Cola',f'{num21}','2$',f'{2*num21}$']
        l1_21.config(text=f'{row21}')
        l4_21.config(text=f'{num21}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_21.config(text=f'{listP21[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP21)
#-----------------------grid
    l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_21.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_21.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_21.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_21.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_21.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_21.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_21.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_21.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_21.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_21.grid(row=row21+2,column=0,sticky=W+N)
    B21=True
    Total+=2
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#--------------------------------def Sprite
def Sprite():
    #---------------global
    global Delete_22
    global Total
    global Tot22
    global list_factor
    global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
    global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
    global num22;global B22
    global f1_22;global listP22;global l1_22;global l2_22;global l3_22;global l4_22;global l5_22;global l6_22;global E1_22;global Badd_22;global Badd2_22;global BDelete_22
#--------------------def +
    def add1_22():
        global Total
        global num22
        global listP22
        num22+=1
        l4_22.config(text=f'{num22}')
        l4_22.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_22.config(text=f'{2*num22}$')
        l6_22.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_22.grid(row=row22+2,column=0,sticky=W+N)
        Total+=2
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP22)
        listP22=['022','Sprite',f'{num22}','2$',f'{2*num22}$']
        A.append(listP22)
#---------------------def
    def add2_22():
        global Total
        global num22
        global listP22
        if num22>1:
            Total-=2
        num22-=1
        if num22<=1:
            num22=1
        l4_22.config(text=f'{num22}')
        l4_22.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
        l6_22.config(text=f'{2*num22}$')
        l6_22.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
        f1_22.grid(row=row22+2,column=0,sticky=W+N)

        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        A.remove(listP22)
        listP22=['022','Sprite',f'{num22}','2$',f'{2*num22}$']
        A.append(listP22)
#----------------------def delete
    def Delete_22():
        global Total
        global list_factor
        global num22;global B22
        global row1;global row2;global row3;global row4;global row5;global row6;global row7;global row8;global row9;global row10;global row11
        global row12;global row13;global row14;global row15;global row16;global row17;global row18;global row19;global row20;global row21;global row22
        A.remove(listP22)
        E1_22.delete(0,'end')
        Total-=2*num22
        LT.config(text=f'Total Price:\t{Total}$')
        LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
        B22=False
        if('Sprite')in list_factor:
            list_factor.remove('Sprite')

        if 'American Pizza' in list_factor:
            row1=list_factor.index('American Pizza')+1
            l1.config(text=f'{row1}')
            l1.grid(row=0,column=0,pady=1,sticky=W+N)
            f1.grid(row=row1+2,column=0,sticky=W+N)
        if 'Special Pizza'in list_factor:
            row2=list_factor.index('Special Pizza')+1
            l1_2.config(text=f'{row2}')
            l1_2.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_2.grid(row=row2+2,column=0,sticky=W+N)
        if 'Italian Pizza'in list_factor:
            row3=list_factor.index('Italian Pizza')+1
            l1_3.config(text=f'{row3}')
            l1_3.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_3.grid(row=row3+2,column=0,sticky=W+N)
        if 'Veg Pizza'in list_factor:
            row4=list_factor.index('Veg Pizza')+1
            l1_4.config(text=f'{row4}')
            l1_4.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_4.grid(row=row4+2,column=0,sticky=W+N)
        if 'Chicken Pizza'in list_factor:
            row5=list_factor.index('Chicken Pizza')+1
            l1_5.config(text=f'{row5}')
            l1_5.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_5.grid(row=row5+2,column=0,sticky=W+N)
        if 'Chicken filet'in list_factor:
            row6=list_factor.index('Chicken filet')+1
            l1_6.config(text=f'{row6}')
            l1_6.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_6.grid(row=row6+2,column=0,sticky=W+N)
        if 'CheeseBurger'in list_factor:
            row7=list_factor.index('CheeseBurger')+1
            l1_7.config(text=f'{row7}')
            l1_7.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_7.grid(row=row7+2,column=0,sticky=W+N)
        if 'Burger'in list_factor:
            row8=list_factor.index('Burger')+1
            l1_8.config(text=f'{row8}')
            l1_8.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_8.grid(row=row8+2,column=0,sticky=W+N)
        if 'Turkish kebab'in list_factor:
            row9=list_factor.index('Turkish kebab')+1
            l1_9.config(text=f'{row9}')
            l1_9.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_9.grid(row=row9+2,column=0,sticky=W+N)
        if 'Hot Dog'in list_factor:
            row10=list_factor.index('Hot Dog')+1
            l1_10.config(text=f'{row10}')
            l1_10.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_10.grid(row=row10+2,column=0,sticky=W+N)
        if 'T-Bone'in list_factor:
            row11=list_factor.index('T-Bone')+1
            l1_11.config(text=f'{row11}')
            l1_11.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_11.grid(row=row11+2,column=0,sticky=W+N)
        if 'Filet Mignon'in list_factor:
            row12=list_factor.index('Filet Mignon')+1
            l1_12.config(text=f'{row12}')
            l1_12.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_12.grid(row=row12+2,column=0,sticky=W+N)
        if 'Ribeye'in list_factor:
            row13=list_factor.index('Ribeye')+1
            l1_13.config(text=f'{row13}')
            l1_13.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_13.grid(row=row13+2,column=0,sticky=W+N)
        if 'Tri-Tip'in list_factor:
            row14=list_factor.index('Tri-Tip')+1
            l1_14.config(text=f'{row14}')
            l1_14.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_14.grid(row=row14+2,column=0,sticky=W+N)
        if 'Greek'in list_factor:
            row15=list_factor.index('Greek')+1
            l1_15.config(text=f'{row15}')
            l1_15.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_15.grid(row=row15+2,column=0,sticky=W+N)
        if 'Caesar'in list_factor:
            row16=list_factor.index('Caesar')+1
            l1_16.config(text=f'{row16}')
            l1_16.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_16.grid(row=row16+2,column=0,sticky=W+N)
        if 'Solterito'in list_factor:
            row17=list_factor.index('Solterito')+1
            l1_17.config(text=f'{row17}')
            l1_17.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_17.grid(row=row17+2,column=0,sticky=W+N)
        if 'Shirazi'in list_factor:
            row18=list_factor.index('Shirazi')+1
            l1_18.config(text=f'{row18}')
            l1_18.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_18.grid(row=row18+2,column=0,sticky=W+N)
        if 'Water'in list_factor:
            row19=list_factor.index('Water')+1
            l1_19.config(text=f'{row19}')
            l1_19.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_19.grid(row=row19+2,column=0,sticky=W+N)
        if 'Tea'in list_factor:
            row20=list_factor.index('Tea')+1
            l1_20.config(text=f'{row20}')
            l1_20.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_20.grid(row=row20+2,column=0,sticky=W+N)
        if 'Coca Cola'in list_factor:
            row21=list_factor.index('Coca Cola')+1
            l1_21.config(text=f'{row21}')
            l1_21.grid(row=0,column=0,pady=1,sticky=W+N)
            f1_21.grid(row=row21+2,column=0,sticky=W+N)
        f1_22.grid_forget()
        if list_factor==[]:
            if B==True:
                f1.grid_forget()
            if B2==True:
                f1_2.grid_forget()
            if B3==True:
                f1_3.grid_forget()
            if B4==True:
                f1_4.grid_forget()
            if B5==True:
                f1_5.grid_forget()
            if B6==True:
                f1_6.grid_forget()
            if B7==True:
                f1_7.grid_forget()
            if B8==True:
                f1_8.grid_forget()
            if B9==True:
                f1_9.grid_forget()
            if B10==True:
                f1_10.grid_forget()
            if B11==True:
                f1_11.grid_forget()
            if B12==True:
                f1_12.grid_forget()
            if B13==True:
                f1_13.grid_forget()
            if B14==True:
                f1_14.grid_forget()
            if B15==True:
                f1_15.grid_forget()
            if B16==True:
                f1_16.grid_forget()
            if B17==True:
                f1_17.grid_forget()
            if B18==True:
                f1_18.grid_forget()
            if B19==True:
                f1_19.grid_forget()
            if B20==True:
                f1_20.grid_forget()
            if B21==True:
                f1_21.grid_forget()
            if B22==True:
                f1_22.grid_forget()       
#---------------------first Click
    if B22==False:
        num22=1
        list_factor.append('Sprite')
        row22=list_factor.index('Sprite')+1
        listP22=['022','Sprite',f'{num22}','2$',f'{2*num22}$']
        f1_22=Frame(w,bg='black')
        l1_22=Label(f1_22,text=f'{row22}',bg='white',fg='blue',font=('cooper 11'),width=3)
        l2_22=Label(f1_22,text=f'{listP22[0]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l3_22=Label(f1_22,text=f'{listP22[1]}',bg='white',fg='blue',font=('cooper 11'),width=11)
        l4_22=Label(f1_22,text=f'{num22}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l5_22=Label(f1_22,text=f'{listP22[3]}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_22=Label(f1_22,text=f'{listP22[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        E1_22=Entry(f1_22,width=25,bg='white',fg='blue',font=('cooper 11 bold'))
        Badd_22=Button(f1_22,text='+',bg='white',fg='green',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=add1_22)
        Badd2_22=Button(f1_22,text='—',bg='white',fg='red',font=('Btitr 10 bold'),width=7,height=1,pady=-50,command=add2_22)
        BDelete_22=Button(f1_22,text='×',bg='white',fg='red',font=('Btitr 10 bold'),width=6,height=1,pady=-50,command=Delete_22)
        A.append(listP22)
#---------------------next Click
    else:
        A.remove(listP22)
        num22+=1
        listP22=['022','Sprite',f'{num22}','2$',f'{2*num22}$']
        l1_22.config(text=f'{row22}')
        l4_22.config(text=f'{num22}',bg='white',fg='blue',font=('cooper 11'),width=6)
        l6_22.config(text=f'{listP22[4]}',bg='white',fg='blue',font=('cooper 11'),width=9)
        A.append(listP22)
#-----------------------grid
    l1_22.grid(row=0,column=0,pady=1,sticky=W+N)
    l2_22.grid(row=0,column=1,pady=1,padx=3,sticky=W+N)
    l3_22.grid(row=0,column=2,pady=1,sticky=W+N)
    l4_22.grid(row=0,column=3,pady=1,padx=3,sticky=W+N)
    l5_22.grid(row=0,column=4,pady=1,sticky=W+N)
    l6_22.grid(row=0,column=5,pady=1,padx=3,sticky=W+N)
    E1_22.grid(row=0,column=6,pady=1,sticky=W+N+E)
    Badd_22.grid(row=0,column=7,pady=0,padx=3,sticky=N)
    Badd2_22.grid(row=0,column=8,pady=0,padx=3,sticky=W+N)
    BDelete_22.grid(row=0,column=9,pady=0,padx=3,sticky=N)
    f1_22.grid(row=row22+2,column=0,sticky=W+N)
    B22=True
    Total+=2
    LT.config(text=f'Total Price:\t{Total}$')
    LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
n0=0
def PDF():
    if A!=[]:
        global fn
        global n0
        #---------------connect sqlite
        conn=sqlite3.connect('FormH3.db')
        cur=conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
        FactorNumber INTEGER PRIMARY KEY,
        Orders TEXT,
        TotalPrice TEXT,
        DateTime TEXT);""")
        conn.commit()
        #---------------PDF Add page
        pdf=FPDF()
        pdf.add_page()
        #---------------values
        a=1
        b=0
        c=len(list_factor)
        data=[]
        List0=[]
        #---------------Date
        pdf.set_font('Arial','B',15)
        pdf.set_text_color(255,255,255)
        header0=[f'Date: {time0}_{time01}                               Factor Number:{fn}']
        for column0 in header0:
            pdf.cell(190.2,10,column0,0,1,'L',True)
        #---------------column
        pdf.set_font('Arial','B',12)
        pdf.set_text_color(0,0,0)
        header=['Row','Food Name','Number','Price','Total Price']
        for column in header:
            pdf.cell(38,10,column,1,0,'C')
        #----------------Row values
        for A1 in A:
            List0.append(A1)
        for i in range(c):
            data+=[[f'{a}',f'{List0[b][1]}',f'{List0[b][2]}',f'{List0[b][3]}',f'{List0[b][4]}']]
            a+=1
            b+=1
        pdf.ln()
        pdf.set_font('Arial','',12)
        for row in data:
            for column in row:
                pdf.cell(38,10,column,1,0,'C')
            pdf.ln()    
        pdf.set_font('Arial','B',20)
        pdf.set_text_color(255,255,255)
        header2=[f'Total Price:\t\t\t\t\t\t\t{Total}$']
        for column2 in header2:
            pdf.cell(190,10,column2,1,0,'L',True)
        #-----------------Output PDF,SQlite
        pdf.output(f'ppf{str(fn)}.pdf')
        FactorNumber=fn
        FoodName=f'{str(List0)}'
        TotalPrice=f'{Total}$'
        DateTime=f'{time0}_{time01}'
        cur.execute("INSERT INTO users(FactorNumber,Orders,TotalPrice,DateTime) VALUES(?,?,?,?)",(FactorNumber,FoodName,TotalPrice,DateTime)) 
        conn.commit()
        #-----------------Delete
        if B==True:
            Delete()
        if B2==True:
            Delete_2()
        if B3==True:
            Delete_3()
        if B4==True:
            Delete_4()
        if B5==True:
            Delete_5()
        if B6==True:
            Delete_6()
        if B7==True:
            Delete_7()
        if B8==True:
            Delete_8()
        if B9==True:
            Delete_9()
        if B10==True:
            Delete_10()
        if B11==True:
            Delete_11()
        if B12==True:
            Delete_12()
        if B13==True:
            Delete_13()
        if B14==True:
            Delete_14()
        if B15==True:
            Delete_15()
        if B16==True:
            Delete_16()
        if B17==True:
            Delete_17()
        if B18==True:
            Delete_18()
        if B19==True:
            Delete_19()
        if B20==True:
            Delete_20()
        if B21==True:
            Delete_21()
        if B22==True:
            Delete_22()
        #-------------Factor Number   
        fn+=1
        lb.config(text=f'factor number: {fn}')
        lb.grid(row=1,column=0,sticky=W,pady=5)
def search():
    w2=Toplevel()
    w2.title('Factor')
    w2.geometry('800x716')
    w2.geometry('+200+14')
    w2.configure(bg='white')
    
    LabelS=Label(w2,text='Please Enter Factor Number:',bg='blue',fg='white',bd=10,font=('cooper 18 bold'))
    LabelS.pack()
    #----------------str filter(Just integer)
    def validate_input(new_value):
        if new_value.isdigit()and len(new_value)<=4 and int(new_value)>0:
            return True
        elif new_value=='':
            return True
        else:
            return False
    validate=w2.register(validate_input)
    Entry1=Entry(w2,bg='white',fg='black',bd=11,justify='center',font=('cooper 16 bold'),validate='key',validatecommand=(validate,'%P'))
    Entry1.pack()
    LabelS2=Label(w2,text='This Factor Number Was Not Found !!',bg='red',fg='white',bd=10,font=('cooper 18 bold'))#Error not found
    def Find():
        valFind=int(Entry1.get())
        cur.execute("SELECT COUNT(*)FROM users")
        countfactor=int(cur.fetchone()[0]+1)
        if valFind>=1 and valFind<countfactor:
            global l2_S
            global l3_S
            global l4_S
            global l5_S
            global l6_S
            global c
            global a1
            global lbtime2
            global fr1_S
            global fr1_S2
            global lbPrice
            lbtime2=Label(w2,text='',bg='black',fg='white',bd=4,font=('cooper 14 bold'),width=39,anchor=W)
            fr1_S=Frame(w2,bg='black')
            fr1_S2=Frame(w2,bg='black')
            lbPrice=Label(w2,text='',bg='black',fg='white',bd=4,font=('cooper 14 bold'),width=39,anchor=W)
            lbtime2.pack(pady=2)
            fr1_S.pack()
            fr1_S2.pack()
            lbPrice.pack(pady=2)

            lbf_S=Label(fr1_S,text='Row',bg='white',fg='blue',font=('cooper 13 bold'),width=5)
            lbf_S.grid(row=0,column=0,sticky=W,pady=4,padx=3)
            lbf3_S=Label(fr1_S,text='Food Name',bg='white',fg='blue',font=('cooper 13 bold'),width=13)
            lbf3_S.grid(row=0,column=2,sticky=W,pady=4)
            lbf4_S=Label(fr1_S,text='Number',bg='white',fg='blue',font=('cooper 13 bold'),width=7)
            lbf4_S.grid(row=0,column=3,sticky=W,pady=4,padx=3)
            lbf5_S=Label(fr1_S,text='Price',bg='white',fg='blue',font=('cooper 13 bold'),width=7)
            lbf5_S.grid(row=0,column=4,sticky=W,pady=4)
            lbf6_S=Label(fr1_S,text='Total Price',bg='white',fg='blue',font=('cooper 13 bold'),width=11)
            lbf6_S.grid(row=0,column=5,sticky=W,pady=4,padx=3)
        
            
            cur.execute(f"SELECT Orders FROM users WHERE rowid={valFind}")
            UU=[]
            for i in cur.fetchone():
                UU.append(i)
            UU0=UU[0]
            UU1=ast.literal_eval(UU0)
            c=len(UU1)
            cur.execute(f"SELECT DateTime FROM users WHERE rowid={valFind}")
            Time2=[]
            for i in cur.fetchone():
                Time2.append(i)
            lbtime2.config(text=f'Date:{str(Time2[0])}\t        Factor Number:{valFind}')

            cur.execute(f"SELECT TotalPrice FROM users WHERE rowid={valFind}")
            for i in cur.fetchone():
                Price=i
            lbPrice.config(text=f'Total Price:         {Price}')
            a1=1
            au=[]
            b=0
            S=1
            for i in range(c):
                au+=[[f'{UU1[b][1]}',f'{UU1[b][2]}',f'{UU1[b][3]}',f'{UU1[b][4]}']]
                l2_S=Label(fr1_S2,text=f'{a1}',bg='white',fg='red',font=('cooper 13 bold'),width=5)
                l2_S.grid(row=a1,column=0,pady=1,padx=3,sticky=W)
            
                l3_S=Label(fr1_S2,text=f'{au[b][0]}',bg='white',fg='black',font=('cooper 13 bold'),width=13)
                l3_S.grid(row=a1,column=1,pady=1,sticky=W+N)
            
                l4_S=Label(fr1_S2,text=f'{au[b][1]}',bg='white',fg='black',font=('cooper 13 bold'),width=7)
                l4_S.grid(row=a1,column=2,pady=1,padx=3,sticky=W+N)
            
                l5_S=Label(fr1_S2,text=f'{au[b][2]}',bg='white',fg='black',font=('cooper 13 bold'),width=7)
                l5_S.grid(row=a1,column=3,pady=1,sticky=W+N)
            
                l6_S=Label(fr1_S2,text=f'{au[b][3]}',bg='white',fg='black',font=('cooper 13 bold'),width=11)
                l6_S.grid(row=a1,column=4,pady=1,padx=3,sticky=W+N)
            
                a1+=1
                b+=1
            conn.commit()
            LabelS.pack_forget()
            Entry1.pack_forget()
            BtnS.pack_forget()
            BtnS2.pack()
            LabelS2.pack_forget()
        else:
            LabelS2.pack()
            
    def research2():
        
        LabelS.pack()
        Entry1.pack();Entry1.delete(0,'end')
        BtnS.pack()
        BtnS2.pack_forget()
        fr1_S.pack_forget()
        lbPrice.pack_forget()
        lbtime2.pack_forget()
        fr1_S2.destroy()
    BtnS=Button(w2,text='OK',bg='blue',fg='white',font=('cooper 11 bold'),bd=8,width=7,command=Find)
    BtnS2=Button(w2,text='Research',bg='blue',fg='white',font=('cooper 11 bold'),bd=8,width=7,command=research2)
    BtnS.pack()
#---------------Label
fr0=Frame(w,bg='black')
fr0.grid(row=0,column=0,sticky=W,pady=5)
lbtime=Label(fr0,width=22,bg='white',fg='blue',font=('cooper 15 bold'),anchor=W)
lbtime.grid(row=0,column=0,sticky=W,pady=5)
date()
lb=Label(w,text=f'factor number: {fn}',bg='black',fg='white',font=('cooper 15 bold'))
lb.grid(row=1,column=0,sticky=W,pady=5)
#---------------Frame
fr1=Frame(w,bg='black')
fr1.grid(row=2,column=0,sticky=W)
#---------------labelfr1
lbf=Label(fr1,text='Row',bg='white',fg='blue',font=('cooper 11 bold'),width=3)
lbf.grid(row=0,column=0,sticky=W,pady=4)
lbf2=Label(fr1,text='Food Code',bg='white',fg='blue',font=('cooper 11 bold'),width=11)
lbf2.grid(row=0,column=1,sticky=W,pady=4,padx=3)
lbf3=Label(fr1,text='Food Name',bg='white',fg='blue',font=('cooper 11 bold'),width=11)
lbf3.grid(row=0,column=2,sticky=W,pady=4)
lbf4=Label(fr1,text='Number',bg='white',fg='blue',font=('cooper 11 bold'),width=6)
lbf4.grid(row=0,column=3,sticky=W,pady=4,padx=3)
lbf5=Label(fr1,text='Price',bg='white',fg='blue',font=('cooper 11 bold'),width=6)
lbf5.grid(row=0,column=4,sticky=W,pady=4)
lbf6=Label(fr1,text='Total Price',bg='white',fg='blue',font=('cooper 11 bold'),width=9)
lbf6.grid(row=0,column=5,sticky=W,pady=4,padx=3)
lbf7=Label(fr1,text='Description',bg='white',fg='blue',font=('cooper 11 bold'),width=22)
lbf7.grid(row=0,column=6,sticky=W,pady=4)
lbf8=Label(fr1,text='add',bg='white',fg='blue',font=('cooper 11 bold'),width=6)
lbf8.grid(row=0,column=7,sticky=W,pady=4,padx=3)
lbf9=Label(fr1,text='diminish',bg='white',fg='blue',font=('cooper 11 bold'),width=7)
lbf9.grid(row=0,column=8,sticky=W,pady=4)
lbf10=Label(fr1,text='delete',bg='white',fg='blue',font=('cooper 11 bold'),width=6)
lbf10.grid(row=0,column=9,sticky=W,pady=4,padx=3)
#---------------Frame Total
frtotal=Frame(w,bg='black')
frtotal.grid(row=25,column=0,sticky=W,pady=10)
#---------------label
LT=Label(frtotal,text=f'Total Price:\t{Total}$',bg='white',fg='green',font=('cooper 16 bold'),width=60,anchor=W)
LT.grid(row=0,column=0,sticky=W,pady=5,padx=4)
#----------------Button Save.pdf
Btnsave=Button(frtotal,text='Save',font=('cooper 11 bold'),bg='white',fg='green',bd=2,width=7,command=PDF)
Btnsave.grid(row=0,column=1,sticky=E,pady=5,padx=2)
#---------------Frame2menu
fr2=Frame(w,bg='black')
fr2.grid(row=1,column=2,sticky=E+S,padx=20,pady=2)
#---------------buttn menu
btnm=Button(fr2,text='Pizza',bg='white',activebackground='#e0115f',activeforeground='white',fg='black',font=('cooper 9 bold'),width=7,bd=5,command=pizza)
btnm.grid(row=0,column=0,sticky=W,pady=4,padx=3)
btnm2=Button(fr2,text='Sandwich',bg='white',activebackground='#e0115f',activeforeground='white',fg='black',font=('cooper 9 bold'),bd=5,width=7,command=sandwich)
btnm2.grid(row=0,column=1,sticky=W,pady=4,padx=3)
btnm3=Button(fr2,text='Steak',bg='white',activebackground='#e0115f',activeforeground='white',fg='black',font=('cooper 9 bold'),bd=5,width=7,command=steak)
btnm3.grid(row=0,column=2,sticky=W,pady=4,padx=3)
btnm4=Button(fr2,text='Salad',bg='white',activebackground='#e0115f',activeforeground='white',fg='black',font=('cooper 9 bold'),bd=5,width=7,command=salad)
btnm4.grid(row=0,column=3,sticky=W,pady=4,padx=3)
btnm5=Button(fr2,text='Drink',bg='white',activebackground='#e0115f',activeforeground='white',fg='black',font=('cooper 9 bold'),bd=5,width=7,command=drink)
btnm5.grid(row=0,column=4,sticky=W,pady=4,padx=3)
#---------------Frame pizza
frp=Frame(w,bg='black')
#---------------Button pizza
btnP=Button(frp,text='American Pizza',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=AmericanPizza)
btnP.grid(row=0,column=0,sticky=W,pady=4,padx=3)
btnP2=Button(frp,text='Special Pizza',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=SpecialPizza)
btnP2.grid(row=0,column=1,sticky=W,pady=4,padx=3)
btnP3=Button(frp,text='Italian Pizza',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=10,command=ItalianPizza)
btnP3.grid(row=0,column=2,sticky=W,pady=4,padx=3)
btnP4=Button(frp,text='Veg Pizza',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=VegPizza)
btnP4.grid(row=1,column=0,sticky=W,pady=4,padx=3)
btnP5=Button(frp,text='Chicken Pizza',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=ChickenPizza)
btnP5.grid(row=1,column=1,sticky=W,pady=4,padx=3)
#---------------Frame sandwich
frs=Frame(w,bg='black')
#---------------Button sandwich
btnS=Button(frs,text='Chicken filet',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=Chickenfilet)
btnS.grid(row=0,column=0,sticky=W,pady=4,padx=3)
btnS2=Button(frs,text='CheeseBurger',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=CheeseBurger)
btnS2.grid(row=0,column=1,sticky=W,pady=4,padx=3)
btnS3=Button(frs,text='Burger',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=10,command=Burger)
btnS3.grid(row=0,column=2,sticky=W,pady=4,padx=3)
btnS4=Button(frs,text='Turkish kebab',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=Turkishkebab)
btnS4.grid(row=1,column=0,sticky=W,pady=4,padx=3)
btnS5=Button(frs,text='Hot Dog',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=HotDog)
btnS5.grid(row=1,column=1,sticky=W,pady=4,padx=3)
#---------------Frame Steak
frst=Frame(w,bg='black')
#---------------Button Steak
btnSt=Button(frst,text='T-Bone',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=TBone)
btnSt.grid(row=0,column=0,sticky=W,pady=4,padx=3)
btnSt2=Button(frst,text='Filet Mignon',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=FiletMignon)
btnSt2.grid(row=0,column=1,sticky=W,pady=4,padx=3)
btnSt3=Button(frst,text='Ribeye',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=10,command=Ribeye)
btnSt3.grid(row=0,column=2,sticky=W,pady=4,padx=3)
btnSt4=Button(frst,text='Tri-Tip',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=TriTip)
btnSt4.grid(row=1,column=0,sticky=W,pady=4,padx=3)
#---------------Frame Salad
frsl=Frame(w,bg='black')
#---------------Button Salad
btnSl=Button(frsl,text='Greek',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=Greek)
btnSl.grid(row=0,column=0,sticky=W,pady=4,padx=3)
btnSl2=Button(frsl,text='Caesar',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=Caesar)
btnSl2.grid(row=0,column=1,sticky=W,pady=4,padx=3)
btnSl3=Button(frsl,text='Solterito',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=10,command=Solterito)
btnSl3.grid(row=0,column=2,sticky=W,pady=4,padx=3)
btnSl4=Button(frsl,text='Shirazi',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=Shirazi)
btnSl4.grid(row=1,column=0,sticky=W,pady=4,padx=3)
#---------------Frame Drink
frd=Frame(w,bg='black')
#---------------Button Drink
btnD=Button(frd,text='Water',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=Water)
btnD.grid(row=0,column=0,sticky=W,pady=4,padx=3)
btnD2=Button(frd,text='Tea',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=Tea)
btnD2.grid(row=0,column=1,sticky=W,pady=4,padx=3)
btnD3=Button(frd,text='Coca Cola',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=10,command=CocaCola)
btnD3.grid(row=0,column=2,sticky=W,pady=4,padx=3)
btnD4=Button(frd,text='Sprite',bg='#e0115f',fg='white',font=('cooper 11 bold'),bd=5,width=11,command=Sprite)
btnD4.grid(row=1,column=0,sticky=W,pady=4,padx=3)
#--------------Frame Search
frsearch=Frame(w,bg='black')
frsearch.grid(row=0,column=2,sticky=N+W+E,padx=20,rowspan=60,columnspan=60)
btnsearch=Button(frsearch,text='Search Factor',bg='white',fg='red',font=('cooper 11 bold'),bd=5,command=search)
btnsearch.grid(row=0,column=0,pady=4,padx=118)

w.mainloop()
