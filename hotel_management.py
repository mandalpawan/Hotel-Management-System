from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime


class Hotel:

    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.configure(bg="powder blue")
        self.root.geometry("1600x650")
        self.root.resizable(0, 0)

        Mainframe = Frame(self.root)
        Mainframe.grid()

        TopFrame = Frame(Mainframe, bd=14,width=1350,height=550 ,padx=20 ,relief=RIDGE,bg="cadet blue")
        TopFrame.pack(side=TOP)

        LeftFrame = Frame(TopFrame, bd=10,width=450,height=550 ,padx=2 ,relief=RIDGE,bg="powder blue")
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(TopFrame, bd=10,width=820,height=550 ,padx=2 ,relief=RIDGE,bg="cadet blue")
        RightFrame.pack(side=RIGHT)

        BottomFrame = Frame(Mainframe, bd=10,width=1350,height=150 ,padx=20 ,relief=RIDGE,bg="powder blue")
        BottomFrame.pack(side=BOTTOM)
        #==========================================================================================================

        def iExist():
            iExit=tkinter.messagebox.askyesno("Hotel Management System","Confirm if you want to Exit")
            if iExit>0:
                root.destroy()
                return

        def Receipt():
            self.txtReceipt.insert(END,"\t"+CustomerRef.get()+'\t\t'+Firstname.get()+'\t\t'+Surename.get()+'\t\t'+Address.get()+'\t\t'+
                                  PostCCode.get()+'\t\t'+ CheckIndate.get()+"\t\t"+CheckoutDate.get()+"\n")

        def Reset():
            CustomerRef.set("")
            Firstname.set("")
            Surename.set("")
            Address.set("")
            PostCCode.set("")
            Mobile.set("")
            Email.set("")
            Nationality.set("")
            DOB.set("")
            IDCard.set("")
            Gender.set("")
            CheckIndate.set("")
            CheckoutDate.set("")
            Meal.set("")
            RoomType.set("")
            RoomNo.set("")
            RoomExNo.set("")
            TotalCost.set("")
            SubTotal.set("")
            PadTax.set("")
            TotalDays.set("")
            self.txtReceipt.delete("1.0",END)

        def TotalCostDate():
            InDate=CheckIndate.get()
            OutDate=CheckoutDate.get()
            Room = RoomType.get()
            MealType = Meal.get()
            if (InDate or OutDate) == "":
                tkinter.messagebox.showwarning("Failed","Fill the Indate and Outdate")
            else:  
                InDate = datetime.strptime(InDate,"%d/%m/%Y")
                OutDate = datetime.strptime(OutDate,"%d/%m/%Y")
                Days = ((OutDate-InDate).days)
                TotalDays.set(((OutDate-InDate).days))

            if(Room=="Single" or MealType=="Breakfast"):
                Cost = float(3500)
                GrandTotal = ((Cost)*Days)
                GST = float(GrandTotal * 0.08)
                Total = GST + GrandTotal
                PadTax.set(GST)
                TotalCost.set(Total)
                SubTotal.set(GrandTotal)

            elif(Room=="Single" or MealType=="Lunch"):
                Cost = float(4500)
                GrandTotal = ((Cost)*Days)
                GST = float(GrandTotal * 0.08)
                Total = GST + GrandTotal
                PadTax.set(GST)
                TotalCost.set(Total)
                SubTotal.set(GrandTotal)

            elif(Room=="Single" or MealType=="Dinner"):
                Cost = float(7000)
                GrandTotal = ((Cost)*Days)
                GST = float(GrandTotal * 0.08)
                Total = GST + GrandTotal
                PadTax.set(GST)
                TotalCost.set(Total)
                SubTotal.set(GrandTotal)

            elif(Room=="Double" or MealType=="Breakfast"):
                Cost = float(5000)
                GrandTotal = ((Cost)*Days)
                GST = float(GrandTotal * 0.08)
                Total = GST + GrandTotal
                PadTax.set(GST)
                TotalCost.set(Total)
                SubTotal.set(GrandTotal)

            elif(Room=="Double" or MealType=="Lunch"):
                Cost = float(6000)
                GrandTotal = ((Cost)*Days)
                GST = float(GrandTotal * 0.08)
                Total = GST + GrandTotal
                PadTax.set(GST)
                TotalCost.set(Total)
                SubTotal.set(GrandTotal)

            elif(Room=="Double" or MealType=="Dinner"):
                Cost = float(8000)
                GrandTotal = ((Cost)*Days)
                GST = float(GrandTotal * 0.08)
                Total = GST + GrandTotal
                PadTax.set(GST)
                TotalCost.set(Total)
                SubTotal.set(GrandTotal)

            elif(Room=="Family" or MealType=="Breakfast"):
                Cost = float(7000)
                GrandTotal = ((Cost)*Days)
                GST = float(GrandTotal * 0.08)
                Total = GST + GrandTotal
                PadTax.set(GST)
                TotalCost.set(Total)
                SubTotal.set(GrandTotal)

            elif(Room=="Family" or MealType=="Lunch"):
                Cost = float(10000)
                GrandTotal = ((Cost)*Days)
                GST = float(GrandTotal * 0.08)
                Total = GST + GrandTotal
                PadTax.set(GST)
                TotalCost.set(Total)
                SubTotal.set(GrandTotal)

            elif(Room=="Family" or MealType=="Dinner"):
                Cost = float(15000)
                GrandTotal = ((Cost)*Days)
                GST = float(GrandTotal * 0.08)
                Total = GST + GrandTotal
                PadTax.set(GST)
                TotalCost.set(Total)
                SubTotal.set(GrandTotal)
            

            
            
        
        CustomerRef=StringVar()
        Firstname=StringVar()
        Surename= StringVar()
        Address =StringVar()
        PostCCode=StringVar()
        Mobile=StringVar()
        Email=StringVar()
        Nationality=StringVar()
        DOB=StringVar()
        IDCard=StringVar()
        Gender=StringVar()
        CheckIndate=StringVar()
        CheckoutDate=StringVar()
        Meal=StringVar()
        RoomType=StringVar()
        RoomNo=StringVar()
        RoomExNo=StringVar()
        TotalCost=StringVar()
        SubTotal=StringVar()
        PadTax=StringVar()
        TotalDays=StringVar()
                
        #=============================================widget==================================================================
        self.lblCustomber_Ref = Label(LeftFrame,font=('arial',12,'bold'),text='Customber Ref:',padx=2,bg="powder blue")
        self.lblCustomber_Ref.grid(row=0,column=0,sticky=W)
        self.txtCustomber_Ref = Entry(LeftFrame,font=('arial',12,'bold'),textvariable=CustomerRef,width=20)
        self.txtCustomber_Ref.grid(row=0,column=1,padx=20,pady=3)

        self.lblFirstname = Label(LeftFrame,font=('arial',12,'bold'),text='First Name:',padx=2,bg="powder blue")
        self.lblFirstname.grid(row=1,column=0,sticky=W)
        self.txtFirstname = Entry(LeftFrame,font=('arial',12,'bold'),textvariable=Firstname,width=20)
        self.txtFirstname.grid(row=1,column=1,padx=20,pady=3)

        self.lblSurename= Label(LeftFrame,font=('arial',12,'bold'),text='Sure Name:',padx=2,bg="powder blue")
        self.lblSurename.grid(row=2,column=0,sticky=W)
        self.txtSurename = Entry(LeftFrame,font=('arial',12,'bold'),textvariable=Surename,width=20)
        self.txtSurename.grid(row=2,column=1,padx=20,pady=3)

        self.lblAddress = Label(LeftFrame,font=('arial',12,'bold'),text='Address:',padx=2,bg="powder blue")
        self.lblAddress.grid(row=3,column=0,sticky=W)
        self.txtAddress = Entry(LeftFrame,font=('arial',12,'bold'),textvariable=Address,width=20)
        self.txtAddress.grid(row=3,column=1,padx=20,pady=3)

        self.lblPostCCode = Label(LeftFrame,font=('arial',12,'bold'),text='PostC Code:',padx=2,bg="powder blue")
        self.lblPostCCode.grid(row=4,column=0,sticky=W)
        self.txtPostCCode = Entry(LeftFrame,font=('arial',12,'bold'),textvariable=PostCCode,width=20)
        self.txtPostCCode.grid(row=4,column=1,padx=20,pady=3)

        self.lblMobile= Label(LeftFrame,font=('arial',12,'bold'),text='Mobile:',padx=2,bg="powder blue")
        self.lblMobile.grid(row=5,column=0,sticky=W)
        self.txtMobile = Entry(LeftFrame,font=('arial',12,'bold'),textvariable=Mobile,width=20)
        self.txtMobile.grid(row=5,column=1,padx=20,pady=3)

        self.lblEmail= Label(LeftFrame,font=('arial',12,'bold'),text='Email:',padx=2,bg="powder blue")
        self.lblEmail.grid(row=6,column=0,sticky=W)
        self.txtEmail = Entry(LeftFrame,font=('arial',12,'bold'),textvariable=Email,width=20)
        self.txtEmail.grid(row=6,column=1,padx=20,pady=3)

        self.lblNationality= Label(LeftFrame,font=('arial',12,'bold'),text='Nationality:',padx=2,pady=2,bg="powder blue")
        self.lblNationality.grid(row=7,column=0,sticky=W)
        self.cboNationality=ttk.Combobox(LeftFrame,textvariable=Nationality,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboNationality['value'] =('','India','Bangladeshi','British','other')
        self.cboNationality.current(0)
        self.cboNationality.grid(row=7,column=1,padx=3)

        self.lblDOB= Label(LeftFrame,font=('arial',12,'bold'),text='Date Of Birth:',padx=2,bg="powder blue")
        self.lblDOB.grid(row=8,column=0,sticky=W)
        self.txtDOB = Entry(LeftFrame,font=('arial',12,'bold'),textvariable=DOB,width=20)
        self.txtDOB.grid(row=8,column=1,padx=20,pady=3)

        self.lblIDCard= Label(LeftFrame,font=('arial',12,'bold'),text='Type of Id:',padx=2,bg="powder blue")
        self.lblIDCard.grid(row=9,column=0,sticky=W)
        self.cboIDCard=ttk.Combobox(LeftFrame,textvariable=IDCard,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboIDCard['value'] =('','Driving Licence','AADHAR','Voter','Passport')
        self.cboIDCard.current(0)
        self.cboIDCard.grid(row=9,column=1,padx=3,pady=5)

        self.lblGender= Label(LeftFrame,font=('arial',12,'bold'),text='Gender:',padx=2,bg="powder blue")
        self.lblGender.grid(row=10,column=0,sticky=W)
        self.cboGender=ttk.Combobox(LeftFrame,textvariable=Gender,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboGender['value'] =('','Male','Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=10,column=1,padx=3,pady=5)

        self.lblCheckIndate= Label(LeftFrame,font=('arial',12,'bold'),text='Check In Date:',padx=2,bg="powder blue")
        self.lblCheckIndate.grid(row=11,column=0,sticky=W)
        self.txtCheckIndate = Entry(LeftFrame,font=('arial',12,'bold'),textvariable=CheckIndate,width=20)
        self.txtCheckIndate.grid(row=11,column=1,padx=20,pady=5)

        self.lblCheckoutDate= Label(LeftFrame,font=('arial',12,'bold'),text='Check Out Date:',padx=2,bg="powder blue")
        self.lblCheckoutDate.grid(row=12,column=0,sticky=W)
        self.txtCheckoutDate = Entry(LeftFrame,font=('arial',12,'bold'),textvariable=CheckoutDate,width=20)
        self.txtCheckoutDate.grid(row=12,column=1,padx=20,pady=5)

        self.lblMeal= Label(LeftFrame,font=('arial',12,'bold'),text='Meal:',padx=2,bg="powder blue")
        self.lblMeal.grid(row=13,column=0,sticky=W)
        self.cboMeal=ttk.Combobox(LeftFrame,textvariable=Meal,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboMeal['value'] =('','Breakfast','Lunch','Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13,column=1,padx=20,pady=5)

        self.lblRoomType= Label(LeftFrame,font=('arial',12,'bold'),text='Room Type:',padx=2,bg="powder blue")
        self.lblRoomType.grid(row=14,column=0,sticky=W)
        self.cboRoomType=ttk.Combobox(LeftFrame,textvariable=RoomType,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboRoomType['value'] =('','Single','Double','Family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14,column=1,padx=3,pady=5)

        self.lblRoomNo= Label(LeftFrame,font=('arial',12,'bold'),text='Room Type:',padx=2,bg="powder blue")
        self.lblRoomNo.grid(row=15,column=0,sticky=W)
        self.cboRoomNo=ttk.Combobox(LeftFrame,textvariable=RoomType,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboRoomNo['value'] =('','001','002','003','004','005','006')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=15,column=1,padx=20,pady=5)

        self.lblRoomExNo= Label(LeftFrame,font=('arial',12,'bold'),text='Room Ex No:',padx=2,bg="powder blue")
        self.lblRoomExNo.grid(row=15,column=0,sticky=W)
        self.cboRoomExNo=ttk.Combobox(LeftFrame,textvariable=RoomExNo,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboRoomExNo['value'] =('','101','102','103','104','105','106')
        self.cboRoomExNo.current(0)
        self.cboRoomExNo.grid(row=15,column=1,padx=20,pady=5)


        #=============================================================================================================

        self.lblLabel=Label(RightFrame,font=('arial',12,'bold'),pady=10,bg='cadet Blue',
                            text="Customber Ref\tFirstName\tSurename\tAddress\tPostCode\tNationality\tCheckInDate\tCheckOutDate")
        self.lblLabel.grid(row=0,column=0,columnspan=17)
        self.txtReceipt =Text(RightFrame,height=15,width=122,bd=10,font=('arial',12,'bold'))
        self.txtReceipt.grid(row=1,column=0,columnspan=2,padx=2,pady=5)
        #=====================================================================================================================
        
        self.lblTotalDays= Label(RightFrame,font=('arial',12,'bold'),text='Total Days:',padx=2,bg="cadet blue")
        self.lblTotalDays.grid(row=2,column=0,sticky=W)
        self.txtTotalDays = Entry(RightFrame,font=('arial',14,'bold'),textvariable=TotalDays,width=67,justify=LEFT,bd=7)
        self.txtTotalDays.grid(row=2,column=1)

        self.lblPadTax= Label(RightFrame,font=('arial',12,'bold'),text='Pad Tax:',padx=2,bg="cadet blue")
        self.lblPadTax.grid(row=3,column=0,sticky=W)
        self.txtPadTax = Entry(RightFrame,font=('arial',14,'bold'),textvariable=PadTax,width=67,justify=LEFT,bd=7)
        self.txtPadTax.grid(row=3,column=1)

        self.lblSubTotal= Label(RightFrame,font=('arial',12,'bold'),text='Sub Total:',padx=2,bg="cadet blue")
        self.lblSubTotal.grid(row=4,column=0,sticky=W)
        self.txtSubTotal = Entry(RightFrame,font=('arial',14,'bold'),textvariable=SubTotal,width=67,justify=LEFT,bd=7)
        self.txtSubTotal.grid(row=4,column=1)

        self.lblTotalCost= Label(RightFrame,font=('arial',12,'bold'),text='Total Cost:',padx=2,bg="cadet blue")
        self.lblTotalCost.grid(row=5,column=0,sticky=W)
        self.txtTotalCost = Entry(RightFrame,font=('arial',14,'bold'),textvariable=TotalCost,width=67,justify=LEFT,bd=7)
        self.txtTotalCost.grid(row=5,column=1)

        #=====================================================================================================================

        self.btnTotal=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=22,height=2,
                    command=TotalCostDate,bg="powder blue",text="Total").grid(row=0,column=4,padx=4)

        self.btnReceipt=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=22,height=2,
                    command=Receipt,bg="powder blue",text="Receipe").grid(row=0,column=2,padx=5)

        self.btnReset=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=35,height=2,
                    command=Reset, bg="powder blue",text="Reset").grid(row=0,column=5,padx=5)

        self.btnEixt=Button(BottomFrame,padx=16,pady=1,fg="black",bd=4,font=('arial',16,'bold'),width=22,height=2,
                    command=iExist,bg="powder blue",text="Exit").grid(row=0,column=6,padx=5)

        
        

        

        

        

        
if __name__=='__main__':
    root=Tk()
    application=Hotel(root)
    root.mainloop()
