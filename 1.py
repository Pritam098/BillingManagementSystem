import matplotlib.pyplot as plt
import pymysql
import datetime
from tabulate import tabulate
#print("I'm running")
from tkinter import *
from tkinter import ttk
class Invoice:
	def __init__(self,root):
		self.root=root
		self.root.title("M/S ABC Enterprise")
		self.root.geometry("1350x700+0+0")

		title=Label(self.root,text="M/S ABC Enterprise",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
		title.pack(side=TOP,fill=X)

		####All Variables####
		self.invoiceno_var=StringVar()
		self.invoiceno2_var=StringVar()
		self.date_var=StringVar()
		self.date2_var=StringVar()
		self.cgst_var=StringVar()
		self.cgst2_var=StringVar()
		self.sgst_var=StringVar()
		self.sgst2_var=StringVar()
		self.cess_var=StringVar()
		self.taxable_var=StringVar()
		self.netbill_var=StringVar()
		self.grossbill_var=StringVar()
		self.purchasefrom_var=StringVar()
		self.searchparam_var=StringVar()
		self.searchby_var=StringVar()
		###Manage_Frame####
		Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
		Manage_Frame.place(x=20,y=100,width=600,height=590)


		m_title=Label(Manage_Frame,text="Manage Data",bg="blue",fg="white",font=("times new roman",20,"bold"))
		m_title.grid(row=0,columnspan=2,pady=10)

		lbl_invoiceno=Label(Manage_Frame,text="Invoice No.",bg="crimson",fg="white",font=("times new roman",15,"bold"))
		lbl_invoiceno.grid(row=1,column=0,pady=5,sticky="w")

		txt_invoiceno=Entry(Manage_Frame,textvariable=self.invoiceno_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
		txt_invoiceno.grid(row=1,column=1,pady=5,padx=10,sticky="w")

		lbl_date=Label(Manage_Frame,text="Date",bg="crimson",fg="white",font=("times new roman",15,"bold"))
		lbl_date.grid(row=1,column=2,pady=5,sticky="w")

		txt_date=Entry(Manage_Frame,textvariable=self.date_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
		txt_date.grid(row=1,column=3,pady=5,padx=10,sticky="w")

		lbl_netbill=Label(Manage_Frame,text="Net Bill",bg="crimson",fg="white",font=("times new roman",15,"bold"))
		lbl_netbill.grid(row=3,column=0,pady=5,sticky="w")

		txt_netbill=Entry(Manage_Frame,textvariable=self.netbill_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
		txt_netbill.grid(row=3,column=1,pady=5,padx=10,sticky="w")

		lbl_cgst=Label(Manage_Frame,text="CGST",bg="crimson",fg="white",font=("times new roman",15,"bold"))
		lbl_cgst.grid(row=4,column=0,pady=5,sticky="w")

		txt_cgst=Entry(Manage_Frame,textvariable=self.cgst_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
		txt_cgst.grid(row=4,column=1,pady=5,padx=10,sticky="w")

		lbl_sgst=Label(Manage_Frame,text="SGST",bg="crimson",fg="white",font=("times new roman",15,"bold"))
		lbl_sgst.grid(row=4,column=2,pady=10,sticky="w")

		txt_sgst=Entry(Manage_Frame,textvariable=self.sgst_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
		txt_sgst.grid(row=4,column=3,pady=10,padx=10,sticky="w",ipadx=0)

		lbl_cess=Label(Manage_Frame,text="Cess",bg="crimson",fg="white",font=("times new roman",15,"bold"))
		lbl_cess.grid(row=5,column=0,pady=10,sticky="w")

		txt_cess=Entry(Manage_Frame,textvariable=self.cess_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
		txt_cess.grid(row=5,column=1,pady=10,padx=10,sticky="w",ipadx=0)

		lbl_grossbill=Label(Manage_Frame,text="GrossBill",bg="crimson",fg="white",font=("times new roman",15,"bold"))
		lbl_grossbill.grid(row=6,column=0,pady=10,sticky="w")

		txt_grossbill=Entry(Manage_Frame,textvariable=self.grossbill_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
		txt_grossbill.grid(row=6,column=1,pady=10,padx=10,sticky="w")

		lbl_purchasebill=Label(Manage_Frame,text="PurchaseFrom",bg="crimson",fg="white",font=("times new roman",15,"bold"))
		lbl_purchasebill.grid(row=9,column=0,pady=10,sticky="w")

		txt_purchasebill=Entry(Manage_Frame,textvariable=self.purchasefrom_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
		txt_purchasebill.grid(row=9,column=1,pady=10,padx=10,sticky="w")

		lbl_invoiceno2=Label(Manage_Frame,text="Invoice No",bg="crimson",fg="white",font=("times new roman",15,"bold"))
		lbl_invoiceno2.grid(row=10,column=0,pady=10,sticky="w")

		txt_invoiceno2=Entry(Manage_Frame,textvariable=self.invoiceno2_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
		txt_invoiceno2.grid(row=10,column=1,pady=10,padx=10,sticky="w")
	
		lbl_invoicedate=Label(Manage_Frame,text="Date",bg="crimson",fg="white",font=("times new roman",15,"bold"))
		lbl_invoicedate.grid(row=10,column=2,pady=10,sticky="w")

		txt_invoicedate=Entry(Manage_Frame,textvariable=self.date2_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
		txt_invoicedate.grid(row=10,column=3,pady=10,padx=10,sticky="w")

		lbl_taxable=Label(Manage_Frame,text="TaxableValue",bg="crimson",fg="white",font=("times new roman",15,"bold"))
		lbl_taxable.grid(row=11,column=0,pady=10,sticky="w")

		txt_taxable=Entry(Manage_Frame,textvariable=self.taxable_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
		txt_taxable.grid(row=11,column=1,pady=10,padx=10,sticky="w")

		lbl_cgst2=Label(Manage_Frame,text="CGST",bg="crimson",fg="white",font=("times new roman",15,"bold"))
		lbl_cgst2.grid(row=12,column=0,pady=5,sticky="w")

		txt_cgst2=Entry(Manage_Frame,textvariable=self.cgst2_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
		txt_cgst2.grid(row=12,column=1,pady=5,padx=10,sticky="w")

		lbl_sgst2=Label(Manage_Frame,text="SGST",bg="crimson",fg="white",font=("times new roman",15,"bold"))
		lbl_sgst2.grid(row=12,column=2,pady=10,sticky="w")

		txt_sgst2=Entry(Manage_Frame,textvariable=self.sgst2_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
		txt_sgst2.grid(row=12,column=3,pady=10,padx=10,sticky="w",ipadx=0)

		######Button_Frame######

		Button_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
		Button_Frame.place(x=3,y=490,width=590)
		
		add_button=Button(Button_Frame,text="SAVE",font=("times new roman",10,"bold"),width=20,command=self.save).grid(row=0,column=1,padx=10,pady=10)
		new_button=Button(Button_Frame,text="CLEAR",font=("times new roman",10,"bold"),width=20,command=self.clear).grid(row=0,column=2,padx=10,pady=10)
		delete_button=Button(Button_Frame,text="DELETE",font=("times new roman",10,"bold"),width=20,command=self.delete).grid(row=0,column=3,padx=10,pady=10)
		update_button=Button(Button_Frame,text="UPDATE",font=("times new roman",10,"bold"),width=20,command=self.update_data).grid(row=1,column=2,padx=10,pady=10)
		
		####Detail_Frame###

		Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
		Detail_Frame.place(x=620,y=100,width=720,height=590)

		lbl_search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",18,"bold"))
		lbl_search.grid(row=1,column=0,pady=10,sticky="w")

		combo_search=ttk.Combobox(Detail_Frame,width=13,textvariable=self.searchby_var,font=("times new roman",13,"bold"),state="readonly")
		combo_search["values"]=("Month","Purchase From","Invoice No")
		combo_search.grid(row=1,column=1,padx=20,pady=10)

		search_param=Entry(Detail_Frame,textvariable=self.searchparam_var,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
		search_param.grid(row=1,column=2,pady=10,padx=10,sticky="w")

		search_button=Button(Detail_Frame,text="SEARCH",font=("times new roman",10,"bold"),width=20,command=self.search).grid(row=2,column=2,padx=10,pady=10)
		print_button=Button(Detail_Frame,text="PRINT",font=("times new roman",10,"bold"),width=20,command=self.print).grid(row=2,column=3,padx=10,pady=10)


		#####Table_Frame#####

		Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
		Table_Frame.place(x=10,y=96,width=700,height=480)

		scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
		scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
		self.data_table=ttk.Treeview(Table_Frame,columns=("invoiceno","date","netbill","cgst","sgst","cess","grossbill","purchasefrom","invoiceno2","date2","taxablevalue","cgst2","sgst2"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
		scroll_x.config(command=self.data_table.xview)
		scroll_y.config(command=self.data_table.yview)
		self.data_table.heading("invoiceno",text="Invoice No.")
		self.data_table.heading("date",text="Date")
		self.data_table.heading("netbill",text="Net Bill")
		self.data_table.heading("cgst",text="CGST")
		self.data_table.heading("sgst",text="SGST")
		self.data_table.heading("cess",text="Cess")
		self.data_table.heading("grossbill",text="GrossBill")
		self.data_table.heading("purchasefrom",text="PurchaseFrom")
		self.data_table.heading("invoiceno2",text="Invoice No.")
		self.data_table.heading("date2",text="Date")
		self.data_table.heading("taxablevalue",text="TaxableValue")
		self.data_table.heading("cgst2",text="CGST")
		self.data_table.heading("sgst2",text="SGST")

		self.data_table.column("invoiceno",width=100)
		self.data_table.column("invoiceno2",width=100)
		self.data_table.column("date",width=100)
		self.data_table.column("date2",width=100)
		self.data_table.column("cgst",width=120)
		self.data_table.column("cgst2",width=120)
		self.data_table.column("sgst",width=120)
		self.data_table.column("sgst2",width=120)
		self.data_table.pack(fill=BOTH,expand=1)
		self.data_table.bind("<ButtonRelease-1>",self.get_cursor)
		self.fetch_data()
	def save(self):
		con=pymysql.connect(host="localhost",user="root",password="Pritam@098",database="billingms")
		cur=con.cursor()
		cur.execute("insert into invoice_tbl values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
					self.invoiceno_var.get(),
					self.date_var.get(),
					self.netbill_var.get(),
					self.cgst_var.get(),
					self.sgst_var.get(),
					self.cess_var.get(),
					self.grossbill_var.get(),
					self.purchasefrom_var.get(),
					self.invoiceno2_var.get(),
					self.date2_var.get(),
					self.taxable_var.get(),
					self.cgst2_var.get(),
					self.sgst2_var.get()
					))
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()
	def delete(self):
		con=pymysql.connect(host="localhost",user="root",password="Pritam@098",database="billingms")
		cur=con.cursor()
		cur.execute("delete from invoice_tbl where invoiceno=%s",self.invoiceno_var.get())
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()

	def fetch_data(self):
		con=pymysql.connect(host="localhost",user="root",password="Pritam@098",database="billingms")
		cur=con.cursor()		
		cur.execute("select * from invoice_tbl")
		rows=cur.fetchall()
		if(len(rows)!=0):
			self.data_table.delete(*self.data_table.get_children())
			for row in rows:
				self.data_table.insert('',END,values=row)
			con.commit()
		con.close()
	def clear(self):
		self.invoiceno_var.set("")
		self.invoiceno2_var.set("")
		self.date_var.set("")
		self.date2_var.set("")
		self.cgst_var.set("")
		self.cgst2_var.set("")
		self.sgst_var.set("")
		self.sgst2_var.set("")
		self.cess_var.set("")
		self.taxable_var.set("")
		self.netbill_var.set("")
		self.grossbill_var.set("")
		self.purchasefrom_var.set("")
		self.searchparam_var.set("")
		self.searchby_var.set("")
	def get_cursor(self,ev):
		cursor_row=self.data_table.focus()
		contents=self.data_table.item(cursor_row)
		row=contents["values"]
		#print(row)
		self.invoiceno_var.set(row[0])
		self.invoiceno2_var.set(row[8])
		self.date_var.set(row[1])
		self.date2_var.set(row[9])
		self.cgst_var.set(row[3])
		self.cgst2_var.set(row[11])
		self.sgst_var.set(row[4])
		self.sgst2_var.set(row[12])
		self.cess_var.set(row[5])
		self.taxable_var.set(row[10])
		self.netbill_var.set(row[2])
		self.grossbill_var.set(row[6])
		self.purchasefrom_var.set(row[7])
	def update_data(self):
		con=pymysql.connect(host="localhost",user="root",password="Pritam@098",database="billingms")
		cur=con.cursor()
		cur.execute("update invoice_tbl set date=%s,netbill=%s,cgst=%s,sgst=%s,cess=%s,grossbill=%s,purchasefrom=%s,invoice2=%s,date2=%s,taxablevalue=%s,cgst2=%s,sgst2=%s where invoiceno=%s",(
					self.date_var.get(),
					self.netbill_var.get(),
					self.cgst_var.get(),
					self.sgst_var.get(),
					self.cess_var.get(),
					self.grossbill_var.get(),
					self.purchasefrom_var.get(),
					self.invoiceno2_var.get(),
					self.date2_var.get(),
					self.taxable_var.get(),
					self.cgst2_var.get(),
					self.sgst2_var.get(),
					self.invoiceno_var.get()
					))
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()
	def search(self):
		con=pymysql.connect(host="localhost",user="root",password="Pritam@098",database="billingms")
		cur=con.cursor()
		if(self.searchby_var.get()=='Month'):		
			cur.execute("select * from invoice_tbl where month(date)=%s",(self.searchparam_var.get()))
			rows=cur.fetchall()
			if(len(rows)!=0):
				self.data_table.delete(*self.data_table.get_children())
				for row in rows:
					self.data_table.insert('',END,values=row)
			con.commit()
		elif(self.searchby_var.get()=='Invoice No'):
			cur.execute("select * from invoice_tbl where invoiceno=%s",(self.searchparam_var.get()))
			rows=cur.fetchall()
			if(len(rows)!=0):
				self.data_table.delete(*self.data_table.get_children())
				for row in rows:
					self.data_table.insert('',END,values=row)
			con.commit()
		elif(self.searchby_var.get()=='Purchase From'):
			cur.execute("select * from invoice_tbl where purchasefrom=%s",(self.searchparam_var.get()))
			rows=cur.fetchall()
			if(len(rows)!=0):
				self.data_table.delete(*self.data_table.get_children())
				for row in rows:
					self.data_table.insert('',END,values=row)
			con.commit()

		con.close()
	def print(self):
		con=pymysql.connect(host="localhost",user="root",password="Pritam@098",database="billingms")
		cur=con.cursor()
		f=open("C:/Users/prita/OneDrive/Desktop/BabaShivEnterprise/t2.txt",'w+')
		##f.write("Invoice No    Date  		NetBill    CGST   SGST  Cess  GrossBill   	PurchaseFrom  		   Invoice No.  		Date  	TaxableValue  	CGST  	SGST\n")
		#f.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
		if(self.searchby_var.get()=='Month'):		
			cur.execute("select * from invoice_tbl where month(date)=%s",(self.searchparam_var.get()))
			rows=cur.fetchall()
			data=[]
			if(len(rows)!=0):
				for row in rows:
					x=[]
					for i in range(0,7):
						x.append(row[i])
					data.append(x)
				print(tabulate(data,headers=["InvoiceNo","Date","NetBill","CGST","SGST","Cess","GrossBill"]),file=f)
			con.commit()
		elif(self.searchby_var.get()=='Invoice No'):
			cur.execute("select * from invoice_tbl where invoiceno=%s",(self.searchparam_var.get()))
			rows=cur.fetchall()
			data=[]
			if(len(rows)!=0):
				for row in rows:
					x=[]
					for i in range(0,7):
						x.append(row[i])
					data.append(x)
				print(tabulate(data,headers=["InvoiceNo","Date","NetBill","CGST","SGST","Cess","GrossBill"]),file=f)
			con.commit()
		elif(self.searchby_var.get()=='Purchase From'):
			cur.execute("select * from invoice_tbl where purchasefrom=%s",(self.searchparam_var.get()))
			rows=cur.fetchall()
			data=[]
			if(len(rows)!=0):
				for row in rows:
					x=[]
					for i in range(7,13):
						x.append(row[i])
					data.append(x)
				print(tabulate(data,headers=["PurchaseFrom","InvoiceNo","Date","TaxableValue","CGST","SGST"]),file=f)
			con.commit()
		else:
			cur.execute("select * from invoice_tbl")
			rows=cur.fetchall()
			data=[]
			if(len(rows)!=0):
				for row in rows:
					x=[]
					for i in range(0,7):
						x.append(row[i])
					data.append(x)
				print(tabulate(data,headers=["InvoiceNo","Date","NetBill","CGST","SGST","Cess","GrossBill"]),file=f)
			con.commit()

		f.close()
		con.close()

root=Tk()
ob=Invoice(root)
root.mainloop()