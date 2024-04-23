import sqlite3
from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import Progressbar
import random
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image
from tkinter.ttk import Notebook, Style
from time import sleep
import datetime
import time
import os
import customtkinter as ctk
# from tabulate import tabulate #  This library is for Printing Documents with lines table creations
from prettytable import PrettyTable
import prettytable
from tkinter import filedialog

from tkcalendar import Calendar
import configparser  # This mudole is for creating config file in any settings
from serial import *
import tempfile
import win32api
import win32print
import smtplib  # for sending E-Mail
from email.mime.text import MIMEText as MMT
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageGrab, ImageFilter, ImageTk
from persiantools.jdatetime import JalaliDate
import persiantools
from PIL import Image
from tkcalendar import DateEntry

# import imageio #THis is for gif images

# ----- Config file -----------------
CAppTitle = "Space4 Software (Printing Press Management System v.1.3)"
AppNameVar = "سیستم مدیریت اطلاعات  و پروژه های مطبعه (فضای4)"


# ============================ Colors =========================
DEFAULTHCRBG = "#4B4B4B"  # 72959F
CTKLIGHT = "#EBEBEB"
CTKDARK = "#242424"
TKDARK = "#4B4B4B"
mygreen = "#d2ffd2"
myred = "#dd0505"
mylightblue = "light blue"
DEFAULTHCRBG = "#4B4B4B"  # 72959F
BGCOL1 = "#003A45"
BGCOL2 = "#2f2f2f"
FGCOL1 = "#FFFFFF"
FGCOL2 = "#6f7f3f"
FGCOL3 = "#ffffff"
FGCOL4 = "dark red"
BGCOL4 = "white"
BGGRAY = "#6f8f9f"
BGLIGHTBLUE = "light blue"
BGBLUE = "blue"
BGBLACK = "black"
BGYELLOW = "yellow"
BGGREEN = "green"
BGRED = "red"
BGLIGHTYELLOW = "light yellow"
BGDEFAULT = "DFDFDF"
BGORANGE = "orange"
BGLIGHTGREEN = "light green"
BGWHITE = "white"
BGLIGHTGRAY = "light gray"
BGDARKSKY = "#0F1F3F"
MODERNBACK = "#420052"
MODERNFORGROUND = "#8F49A6"
MODERNBACKBLUE = "#5D96A1"
MODERNFORGROUNDBLUE = "#454D9C"
MODERNLIGHTBLUE = "#5D96A1"
MODERNPINK = "#410070"
CTKDARK_ENT = "#2B2B2B"
DarkBlue = "#39003D"
MikroTik = "#7A949A"
DARKENTRY = "#343638"
GRAY_NEW = "#ADADAD"
S4DARK = "#1F1F1F"
S4LIGHT = "#2B2B2B"
S4ORANGE = "#FFC800"

BTN_HOVER = "#FFA500"
BTN_VENDOR = "#A9A900"
# ============ Root Systme ================

root = ctk.CTk()
root.title(CAppTitle)
root.iconbitmap("Space4.ico")
root.state("zoomed")
# root.call('tk', 'scaling', -1)
root.call("set", "encoding", "utf-8")
default_font_bold1 = ("Tahoma", 10, "bold")
default_font_bold = ("Tahoma", 12, "bold")
default_font = ("Tahoma", 12, "normal")
default_font_bold2 = ("Tahoma", 8, "bold")
ctk.set_appearance_mode("Dark")
# root.attributes("-alpha", 0.8)


# ========== Images ===========

Img00 = Image.open("PsysDataDir/PersonImg.png")
Img0_0 = Img00.resize((50, 50))
PersonImg = ImageTk.PhotoImage(Img0_0)

Img0_1 = Image.open("PsysDataDir/OrderImg.png")
Img0_2 = Img0_1.resize((50, 50))
OrderImg = ImageTk.PhotoImage(Img0_2)

Img0_3 = Image.open("PsysDataDir/FinanceImg.png")
Img0_4 = Img0_3.resize((50, 50))
FinanceImg = ImageTk.PhotoImage(Img0_4)

Img0_5 = Image.open("PsysDataDir/GraphImg.png")
Img0_6 = Img0_5.resize((50, 50))
GraphImg = ImageTk.PhotoImage(Img0_6)

Img0_7 = Image.open("PsysDataDir/RecordImg.png")
Img0_8 = Img0_7.resize((50, 50))
RecordImg = ImageTk.PhotoImage(Img0_8)

Img0_9 = Image.open("PsysDataDir/StoreImg.png")
Img0_10 = Img0_9.resize((50, 50))
StoreImg = ImageTk.PhotoImage(Img0_10)

Img0_11 = Image.open("PsysDataDir/Space4Img.png")
Img0_12 = Img0_11.resize((50, 50))
Space4Img1 = ImageTk.PhotoImage(Img0_12)



Img1_0 = Image.open("PsysDataDir/SellImg.png")
Img1_1 = Img1_0.resize((20, 20))
SellImg_1 = ImageTk.PhotoImage(Img1_1)

Img1_2 = Image.open("PsysDataDir/EditImg.png")
Img1_3 = Img1_2.resize((20, 20))
EditImg_1 = ImageTk.PhotoImage(Img1_3)

Img1_4 = Image.open("PsysDataDir/DeleteImg.png")
Img1_5 = Img1_4.resize((20, 20))
DeleteImg_1 = ImageTk.PhotoImage(Img1_5)

Img1_6 = Image.open("PsysDataDir/RefreshImg.png")
Img1_7 = Img1_6.resize((20, 20))
RefreshImg_1 = ImageTk.PhotoImage(Img1_7)

Img1_8 = Image.open("PsysDataDir/UpdateImg.png")
Img1_9 = Img1_8.resize((20, 20))
UpdateImg_1 = ImageTk.PhotoImage(Img1_9)

Img1_10 = Image.open("PsysDataDir/ShowImg.png")
Img1_11 = Img1_10.resize((20, 20))
ShowImg_1 = ImageTk.PhotoImage(Img1_11)

Img1_12 = Image.open("PsysDataDir/ReceiveImg.png")
Img1_13 = Img1_12.resize((20, 20))
PriceImg1 = ImageTk.PhotoImage(Img1_13)

Img1_14 = Image.open("PsysDataDir/PrintImg.png")
Img1_15 = Img1_14.resize((20, 20))
PrintImg_1 = ImageTk.PhotoImage(Img1_15)
"""
TabImg5 = Image.open('PsysDataDir/Space4Img.png')
TabImg1_5 = TabImg5.resize((50,50),Image.ANTIALIAS)
Space4TitleLogo = ImageTk.PhotoImage(TabImg1_5)
"""
Space4TitleLogo = ctk.CTkImage(dark_image=Image.open("PsysDataDir/Space4Img.png"))
SaveImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/SaveImg.png"))
EditImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/EditImg.png"))
DeleteImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/DeleteImg.png"))
ClearImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/ClearImg.png"))
RefreshImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/RefreshImg.png"))
PrintImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/PrintImg.png"))
ReceiveImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/ReceiveImg.png"))
RefundImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/RefundImg.png"))
UpdateImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/UpdateImg.png"))
VendorImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/VendorImg.png"))
# ======== String Variables ==========

THEMVARIABLE = StringVar()
EmpVar1 = StringVar()
EmpVar2 = StringVar()
EmpVar3 = StringVar()
EmpVar4 = StringVar()
EmpVar5 = StringVar()

DateNow = datetime.date.today()


# ========================= Functions and Database ==========================
# ========================= Functions and Database ==========================

with sqlite3.connect("DataBaseDir/PressDb.db") as db:
    cur = db.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS EmployeeTable(
        ETID INTEGER PRIMARY KEY AUTOINCREMENT,
        ENAME TEXT NOT NULL,
        EFNAME TEXT NOT NULL,
        EPHONENO INTEGER NOT NULL,
        EEMAIL TEXT NOT NULL,
        EADDRESS TEXT NOT NULL,
        EIDCARDNO INTEGER NOT NULL,
        EGENDER TEXT NOT NULL,
        EPOSITION TEXT NOT NULL,
        EEDUCATION TEXT NOT NULL,
        EJOINDATE DATE,
        EENDDATE DATE,
        EACTIVETIME TEXT NOT NULL,
        ESALARY REAL NOT NULL,
        ERECSALL REAL NOT NULL,
        ENEWPAYDATE REAL NOT NULL);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS EmployeeTableDone(
        DONE_ETID INTEGER PRIMARY KEY AUTOINCREMENT,
        DONE_ENAME TEXT NOT NULL,
        DONE_EFNAME TEXT NOT NULL,
        DONE_EPHONENO INTEGER NOT NULL,
        DONE_EEMAIL TEXT NOT NULL,
        DONE_EADDRESS TEXT NOT NULL,
        DONE_EIDCARDNO INTEGER NOT NULL,
        DONE_EGENDER TEXT NOT NULL,
        DONE_EPOSITION TEXT NOT NULL,
        DONE_EEDUCATION TEXT NOT NULL,
        DONE_EJOINDATE DATE,
        DONE_EENDDATE DATE,
        DONE_EACTIVETIME TEXT NOT NULL,
        DONE_ESALARY REAL NOT NULL,
        DONE_EDATE DATE,
        DONE_ENEWPAYDATE REAL NOT NULL);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS LaserTable3D(
        OTID INTEGER PRIMARY KEY AUTOINCREMENT,
        OORDERTYPE TEXT NOT NULL,
        OLENGTH INTEGER NOT NULL,
        OWIDTH INTEGER NOT NULL,
        OQUNTITY INTEGER NOT NULL,
        OMATERIALTYPE TEXT NOT NULL,
        OTEXT TEXT NOT NULL,
        OCURRENTTIME DATE,
        OFINISHTIME DATE,
        OPRICE REAL NOT NULL,
        OPREPAY REAL NOT NULL,
        OCUSTOMERNAME TEXT NOT NULL,
        OCUSTOMERPHONE INTEGER NOT NULL,
        OCUSTADDRESS TEXT NOT NULL,
        ODELIVERYPRICE REAL NOT NULL,
        ONOTE TEXT NOT NULL,
        OREFUND REAL NOT NULL,
        OUSAGE REAL NOT NULL);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS LaserTableEngrave(
        O_ENGR_TID INTEGER PRIMARY KEY AUTOINCREMENT,
        O_ENGR_ORDERTYPE TEXT NOT NULL,
        O_ENGR_LENGTH INTEGER NOT NULL,
        O_ENGR_WIDTH INTEGER NOT NULL,
        O_ENGR_QUNTITY INTEGER NOT NULL,
        O_ENGR_MATERIALTYPE TEXT NOT NULL,
        O_ENGR_TEXT TEXT NOT NULL,
        O_ENGR_CURRENTTIME DATE,
        O_ENGR_FINISHTIME DATE,
        O_ENGR_PRICE REAL NOT NULL,
        O_ENGR_PREPAY REAL NOT NULL,
        O_ENGR_CUSTOMERNAME TEXT NOT NULL,
        O_ENGR_CUSTOMERPHONE INTEGER NOT NULL,
        O_ENGR_CUSTADDRESS TEXT NOT NULL,
        O_ENGR_DELIVERYPRICE REAL NOT NULL,
        O_ENGR_NOTE TEXT NOT NULL,
        O_ENGR_REFUND REAL NOT NULL,
        O_ENGR_USAGE REAL NOT NULL);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS LaserTableEngraveDone(
        DONE_O_ENGR_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DONE_O_ENGR_ORDERTYPE TEXT NOT NULL,
        DONE_O_ENGR_SIZE INTEGER NOT NULL,
        DONE_O_ENGR_QUNTITY INTEGER NOT NULL,
        DONE_O_ENGR_MTLTYPE TEXT NOT NULL,
        DONE_O_ENGR_TEXT TEXT NOT NULL,
        DONE_O_ENGR_CURTIME DATE,
        DONE_O_ENGR_FINTIME DATE,
        DONE_O_ENGR_TTLPID REAL NOT NULL,
        DONE_O_ENGR_NAME TEXT NOT NULL,
        DONE_O_ENGR_PHONE INTEGER NOT NULL,
        DONE_O_ENGR_ADDR TEXT NOT NULL,
        DONE_O_ENGR_NOTE TEXT NOT NULL,
        DONE_O_ENGR_USAGE REAL NOT NULL,
        DONE_O_ENGR_DATE DATE);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS LaserTableCut(
        O_CUT_TID INTEGER PRIMARY KEY AUTOINCREMENT,
        O_CUT_ORDERTYPE TEXT NOT NULL,
        O_CUT_LENGTH INTEGER NOT NULL,
        O_CUT_WIDTH INTEGER NOT NULL,
        O_CUT_QUNTITY INTEGER NOT NULL,
        O_CUT_MATERIALTYPE TEXT NOT NULL,
        O_CUT_TEXT TEXT NOT NULL,
        O_CUT_CURRENTTIME DATE,
        O_CUT_FINISHTIME DATE,
        O_CUT_PRICE REAL NOT NULL,
        O_CUT_PREPAY REAL NOT NULL,
        O_CUT_CUSTOMERNAME TEXT NOT NULL,
        O_CUT_CUSTOMERPHONE INTEGER NOT NULL,
        O_CUT_CUSTADDRESS TEXT NOT NULL,
        O_CUT_DELIVERYPRICE REAL NOT NULL,
        O_CUT_NOTE TEXT NOT NULL,
        O_CUT_REFUND REAL NOT NULL,
        O_CUT_USAGE REAL NOT NULL);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS LaserTableCutDone(
        DONE_O_CUT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DONE_O_CUT_ORDERTYPE TEXT NOT NULL,
        DONE_O_CUT_SIZE INTEGER NOT NULL,
        DONE_O_CUT_QUNTITY INTEGER NOT NULL,
        DONE_O_CUT_MTLTYPE TEXT NOT NULL,
        DONE_O_CUT_TEXT TEXT NOT NULL,
        DONE_O_CUT_CURTIME DATE,
        DONE_O_CUT_FINTIME DATE,
        DONE_O_CUT_TTLPID REAL NOT NULL,
        DONE_O_CUT_NAME TEXT NOT NULL,
        DONE_O_CUT_PHONE INTEGER NOT NULL,
        DONE_O_CUT_ADDR TEXT NOT NULL,
        DONE_O_CUT_NOTE TEXT NOT NULL,
        DONE_O_CUT_USAGE REAL NOT NULL,
        DONE_O_CUT_DATE DATE);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS DigitalTable(
        DTID INTEGER PRIMARY KEY AUTOINCREMENT,
        DORDERTYPE TEXT NOT NULL,
        DLENGTH INTEGER NOT NULL,
        DWIDTH INTEGER NOT NULL,
        DQUNTITY INTEGER NOT NULL,
        DMATERIALTYPE TEXT NOT NULL,
        DTEXT TEXT NOT NULL,
        DCURRENTTIME DATE,
        DFINISHTIME DATE,
        DPRICE REAL NOT NULL,
        DPREPAY REAL NOT NULL,
        DCUSTOMERNAME TEXT NOT NULL,
        DCUSTOMERPHONE INTEGER NOT NULL,
        DCUSTADDRESS TEXT NOT NULL,
        DDELIVERYPRICE REAL NOT NULL,
        DNOTE TEXT NOT NULL,
        DREFUND REAL NOT NULL,
        DUSAGE REAL NOT NULL);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS LSTTable(
        STL_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STL_ORDERTYPE TEXT NOT NULL,
        STL_SIZE INTEGER NOT NULL,
        STL_QUNTITY INTEGER NOT NULL,
        STL_MTLTYPE TEXT NOT NULL,
        STL_TEXT TEXT NOT NULL,
        STL_CURTIME DATE,
        STL_FINTIME DATE,
        STL_TTLPID REAL NOT NULL,
        STL_NAME TEXT NOT NULL,
        STL_PHONE INTEGER NOT NULL,
        STL_ADDR TEXT NOT NULL,
        STL_NOTE TEXT NOT NULL,
        STL_USAGE REAL NOT NULL,
        STL_DATE DATE);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS DSTTable(
        DST_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DST_ORDERTYPE TEXT NOT NULL,
        DST_SIZE INTEGER NOT NULL,
        DST_QUNTITY INTEGER NOT NULL,
        DST_MTLTYPE TEXT NOT NULL,
        DST_TEXT TEXT NOT NULL,
        DST_CURTIME DATE,
        DST_FINTIME DATE,
        DST_TTLPID REAL NOT NULL,
        DST_NAME TEXT NOT NULL,
        DST_PHONE INTEGER NOT NULL,
        DST_ADDR TEXT NOT NULL,
        DST_NOTE TEXT NOT NULL,
        DST_USAGE REAL NOT NULL,
        DST_DATE DATE);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS FCostTable(
        FTID INTEGER PRIMARY KEY AUTOINCREMENT,
        FTYPE REAL NOT NULL,
        FCOSTTYPE REAL NOT NULL,
        FAMOUNT REAL NOT NULL,
        FDATE DATE,
        FNOTE TEXT NOT NULL);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS IncomeTable(
        ITID INTEGER PRIMARY KEY AUTOINCREMENT,
        ITYPE REAL NOT NULL,
        IINCTYPE REAL NOT NULL,
        IAMOUNT REAL NOT NULL,
        IDATE DATE,
        INOTE TEXT NOT NULL);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS StorageTable(
        SRID INTEGER PRIMARY KEY AUTOINCREMENT,
        SRMODEL TEXT NOT NULL,
        SRTYPE TEXT NOT NULL,
        SRGROUP TEXT NOT NULL,
        SRPRICE REAL NOT NULL,
        SRQTT INTEGER NOT NULL,
        SRDATE DATE,
        SRNOTE TEXT NOT NULL);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS StorageSoldTable(
        SOLDID INTEGER PRIMARY KEY AUTOINCREMENT,
        SOLDMODEL TEXT NOT NULL,
        SOLDTYPE TEXT NOT NULL,
        SOLDGROUP TEXT NOT NULL,
        SOLDPRICE REAL NOT NULL,
        SOLDQTT INTEGER NOT NULL,
        SOLDDATE DATE,
        SOLDNOTE TEXT NOT NULL,
        SOLDREALPRICE REAL NOT NULL);
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS LenderTable(
        LDRID INTEGER PRIMARY KEY AUTOINCREMENT,
        LDRLENDER TEXT NOT NULL,
        LDRBEHALF TEXT NOT NULL,
        LDRAMOUNT REAL NOT NULL,
        LDRDATE DATE,
        LDRNOTE TEXT NOT NULL);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS DebtorTable(
        DBTID INTEGER PRIMARY KEY AUTOINCREMENT,
        DBTDEBTOR TEXT NOT NULL,
        DBTBEHALF TEXT NOT NULL,
        DBTAMOUNT REAL NOT NULL,
        DBDATE DATE,
        DBTNOTE TEXT NOT NULL);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS SellingDebtTable(
        SLID INTEGER PRIMARY KEY AUTOINCREMENT,
        SLNAME TEXT NOT NULL,
        SLFNAME TEXT NOT NULL,
        SLADDR TEXT NOT NULL,
        SLMTYPE TEXT NOT NULL,
        SLQTTY INTEGER NOT NULL,
        SLPRICE REAL NOT NULL,
        SLDAMOUNT REAL NOT NULL,
        SLDATE DATE,
        SLNOTE TEXT NOT NULL);
        """
    )
"""
JanTable
FebTable
MarTable
AprTable
MayTable
JunTable
JulTable
AugTable
SepTable
OctTable
NovTable
DecTable
"""


# ========================= Style ==========================


style = Style(root)
style.theme_use(
    "default"
)  # >>>>>>> TNotebook.Tab anchor is for placing the tab title and image
style.configure(
    "TNotebook.Tab",
    background=S4DARK,
    anchor="nsew",
    borderwidth=0,
    foreground="#ffffff",
    width=11,
    padding=[10, 10],
    tabmargins=[0, 0, 0, 0],
    font=default_font_bold1,
    bd=0,
)
style.configure("TNotebook", background=CTKDARK, borderwidth=0, padding=[10, 10])
style.map(
    "TNotebook.Tab",
    background=[("selected", S4LIGHT)],
    foreground=[("selected", S4ORANGE)],
)
style.layout("cb.TNotebook.Tab", [("TNotebook.Tab", {"side": "right", "sticky": "ne"})])
style.configure("TCombobox", font=default_font_bold)
style.configure("righttab.TNotebook", tabposition="en", sticky="ne")
style.configure(
    "Custom.DateEntry",
    fieldbackground=S4DARK,
    foreground=CTKLIGHT,
    borderwidth=0,
    relief=SOLID,
)
# TreeView Part
style.configure(
    "Treeview.Heading",
    background=CTKDARK,
    borderwidth=0,
    anchor=E,
    foreground=BGWHITE,
    padding=[3, 4],
    tabmargins=[2, 5, 2, 0],
    font=default_font_bold2,
)
style.configure(
    "Treeview",
    background="#333333",
    anchor=E,
    foreground="#ffffff",
    font=default_font_bold2,
    rowheight=27,
    fieldbackground="#33333",
)
style.map(
    "Treeview",
    background=[("selected", BGORANGE)],
    foreground=[("selected", "#000000")],
)
style.layout(
    "cb.Treeview.Row",
    [
        ("Treeitme.row", {"sticky": "e"}),
        ("Treeitme.image", {"side": "right", "sticky": "e"}),
    ],
)


tabControl = ttk.Notebook(root, style="righttab.TNotebook")
tab1 = ctk.CTkFrame(tabControl, border_width=0, corner_radius=7)
tab2 = ctk.CTkFrame(tabControl, border_width=0, corner_radius=7)
tab3 = ctk.CTkFrame(tabControl, border_width=0, corner_radius=7)
tab4 = ctk.CTkFrame(tabControl, border_width=0, corner_radius=7)
tab5 = ctk.CTkFrame(tabControl, border_width=0, corner_radius=7)
tab6 = ctk.CTkFrame(tabControl, border_width=0, corner_radius=7)

tabControl.add(tab1, text="مدیریت کارمند", image=PersonImg, compound=TOP, sticky=NE)
tabControl.add(tab2, text="ثبت سفارش", image=OrderImg, compound=TOP, sticky=NE)
tabControl.add(tab3, text="مدیریت مالی", image=FinanceImg, compound=TOP, sticky=NE)
tabControl.add(tab4, text="عملکرد ها", image=GraphImg, compound=TOP, sticky=NE)
tabControl.add(tab5, text="همه اطلاعات", image=RecordImg, compound=TOP, sticky=NE)
tabControl.add(tab6, text="گدام", image=StoreImg, compound=TOP, sticky=NE)
tabControl.select(tab1)
tabControl.grid(row=0, column=1, padx=30, pady=50, sticky=E)


# ============== Mini Tab2_1 =========================
tabControlMini = ttk.Notebook(tab2, style="RTL.TNotebook")
tab2_1 = ctk.CTkFrame(tabControlMini, border_width=0, corner_radius=0)
tab2_2 = ctk.CTkFrame(tabControlMini, border_width=0, corner_radius=0)

tabControlMini.add(tab2_2, text="بخش دیجیتل", compound=TOP, sticky=NE)
tabControlMini.add(tab2_1, text="بخش لیزر", compound=TOP, sticky=NE)
tabControlMini.select(tab2_1)
tabControlMini.pack(side="right")

style1 = Style(tabControlMini)
style1.configure("RTL.TNotebook", tabposition="ne")


# ============== Mini Tab2_1 =========================
tabFinance = ttk.Notebook(tab3, style="RTL.TNotebook")
tab3_1 = ctk.CTkFrame(tabFinance, border_width=0, corner_radius=0)
tab3_2 = ctk.CTkFrame(tabFinance, border_width=0, corner_radius=0)
tab3_3 = ctk.CTkFrame(tabFinance, border_width=0, corner_radius=0)

tabFinance.add(tab3_3, text="طی سال", compound=TOP, sticky=NE)
tabFinance.add(tab3_2, text="بدهی ها", compound=TOP, sticky=NE)
tabFinance.add(tab3_1, text="محاسبات", compound=TOP, sticky=NE)
tabFinance.select(tab3_1)
tabFinance.pack(side="right")

# ============== Mini Tab6_1 =========================
tabControlMini = ttk.Notebook(tab6, style="RTL.TNotebook")
tab1_1 = ctk.CTkFrame(tabControlMini, border_width=0, corner_radius=0)
tab1_2 = ctk.CTkFrame(tabControlMini, border_width=0, corner_radius=0)

tabControlMini.add(tab1_2, text="باقیات", compound=TOP, sticky=NE)
tabControlMini.add(tab1_1, text="خرید و فروش", compound=TOP, sticky=NE)
tabControlMini.select(tab1_1)
tabControlMini.pack(side="right")

style1 = Style(tabControlMini)
style1.configure("RTL.TNotebook", tabposition="ne")

style2 = Style(tabFinance)
style2.configure("RTL.TNotebook", tabposition="ne")


# ========== Date, Time, Exit Button ==========
""" #Thisi is the Jalali Date & Time ----
current_date = JalaliDate.today()
formatted_date = current_date.strftime('%Y-%m-%d')
DateLabel_1 = ctk.CTkLabel(root,text=formatted_date,font=("Nexa Heavy",20),text_color=(DarkBlue,BGORANGE))
DateLabel_1.place(x=100,y=1)
#------ Time -------
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    time_label.configure(text=current_time)
    time_label.after(1000, update_time)

time_label = ctk.CTkLabel(root, font=("Nexa Heavy",20),text_color=(DarkBlue,BGLIGHTYELLOW))
time_label.place(x=250,y=1)
update_time()
"""


def VendorSetFunc():
    import os

    VenRoot = ctk.CTkToplevel(root)
    VenRoot.title(CAppTitle)
    VenRoot.geometry("200,200+100+100")

    default_font_bold5 = ("Tahoma", VenRoot.winfo_width())
    # VenRoot.resizable()

    def delete_database():
        file_path = "DataBaseDir/PressDb.db"
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                messagebox.showinfo("Space4", "همه اطلاعات حذف گردید ")
            except Exception as err:
                messagebox.showerror("خطا ", f"حذف نشدن به علت  : {str(err)}")

    BackupBtn = ctk.CTkButton(
        VenRoot,
        text="پشتیبان گیری همه داده ها",
        font=default_font_bold,
        fg_color=CTKDARK,
        hover_color=BTN_HOVER,
        text_color=CTKLIGHT,
        width=VenRoot.winfo_width(),
        corner_radius=0,
        height=30,
    )
    BackupBtn.pack(fill=BOTH, expand=True)

    FactoryBtn = ctk.CTkButton(
        VenRoot,
        text="حذف همه داده ها",
        font=default_font_bold,
        fg_color=CTKDARK,
        hover_color=BTN_HOVER,
        text_color=CTKLIGHT,
        width=VenRoot.winfo_width(),
        corner_radius=0,
        height=30,
        command=delete_database,
    )
    FactoryBtn.pack(fill=BOTH, expand=True)
    VenRoot.update()

    VenRoot.mainloop()


def timshow1():
    from time import strftime

    string = strftime("%I:%M : %S %p")  # "%H:%M:%S %p" (I 12 and H 24)
    stringdate = strftime("%Y-%m-%d - %a")
    time_label.configure(text=string)
    DateLabel_1.configure(text=stringdate)
    time_label.after(1000, timshow1)


DateLabel_1 = ctk.CTkLabel(
    root, font=("Nexa Heavy", 20), text_color=(DarkBlue, BGORANGE)
)
DateLabel_1.place(x=100, y=1)
time_label = ctk.CTkLabel(
    root, font=("Nexa Heavy", 20), text_color=(DarkBlue, BGLIGHTYELLOW)
)
time_label.place(x=310, y=1)
timshow1()

ComName1 = ctk.CTkLabel(
    root, text=AppNameVar, font=("B Titr", 20, "bold"), text_color=(DarkBlue, BGORANGE)
)
ComName1.place(x=600, y=1)

VendorSetBtn = ctk.CTkButton(
    root,
    text="",
    image=VendorImg,
    width=15,
    height=15,
    fg_color=CTKDARK,
    hover_color=BTN_VENDOR,
    command=VendorSetFunc,
)
VendorSetBtn.place(x=5, y=1)

ComLogo1 = Label(root, image=Space4Img1, bg=CTKDARK)
ComLogo1.place(x=1200, y=1)


# ----- End ------


# ========================= Tab1 Employee Reg ==========================
# ========================= Tab1 Employee Reg ==========================
# ========================= Tab1 Employee Reg ==========================
# ========================= Tab1 Employee Reg ==========================
# ========================= Tab1 Employee Reg ==========================
# ========================= Tab1 Employee Reg ==========================
# ========================= Tab1 Employee Reg ==========================
# -------- Employee Table Variables -----------
ENAME = StringVar()
EFNAME = StringVar()
EPHONENO = StringVar()
EEMAIL = StringVar()
EADDRESS = StringVar()
EIDCARDNO = StringVar()
EGENDER = StringVar()
EPOSITION = StringVar()
EEDUCATION = StringVar()
EJOINDATE = StringVar()
EENDDATE = StringVar()
EACTIVETIME = StringVar()
ESALARY = StringVar()
ERECSALL = StringVar()
ENEWPAYDATE = StringVar()


def Employee_Auto_Done_Func():
    # ------- Get Data -----------
    for s_itm0 in Tree0.selection():
        GetConn1 = sqlite3.connect("DataBaseDir/PressDb.db")
        GetCor0 = GetConn1.execute(
            "SELECT ESALARY,ERECSALL FROM EmployeeTable"
            # "SELECT SUM(ESALARY-ERECSALL) AS SUM1 FROM EmployeeTable WHERE (ESALARY-ERECSALL) = 0"
        )
        fetch0 = GetCor0.fetchall()
        selected_item = Tree0.selection()[0]
        for data0 in fetch0:
            dt0 = data0[0]
            dt1 = data0[1]
            try:
                if int(dt0) == int(dt1):
                    DateNow1 = datetime.date.today()
                    GetCor1 = GetConn1.execute(
                        """
                        SELECT
                        ENAME,
                        EFNAME,
                        EPHONENO,
                        EEMAIL,
                        EADDRESS,
                        EIDCARDNO,
                        EGENDER,
                        EPOSITION,
                        EEDUCATION,
                        EJOINDATE,
                        EENDDATE,
                        EACTIVETIME,
                        ESALARY,
                        ENEWPAYDATE
                        FROM EmployeeTable
                        WHERE ETID=?""",
                        (Tree0.set(selected_item, "#14"),),
                    )

                    GetFetch1 = GetCor1.fetchall()
                    for Getdata1 in GetFetch1:
                        row0 = Getdata1[0]
                        row1 = Getdata1[1]
                        row2 = Getdata1[2]
                        row3 = Getdata1[3]
                        row4 = Getdata1[4]
                        row5 = Getdata1[5]
                        row6 = Getdata1[6]
                        row7 = Getdata1[7]
                        row8 = Getdata1[8]
                        row9 = Getdata1[9]
                        row10 = Getdata1[10]
                        row11 = Getdata1[11]
                        row12 = Getdata1[12]
                        row13 = Getdata1[13]

                        SCor1 = GetConn1.cursor()
                        SCor1.execute(
                            f"insert into EmployeeTableDone (DONE_ENAME,DONE_EFNAME,DONE_EPHONENO,DONE_EEMAIL,\
                                    DONE_EADDRESS,DONE_EIDCARDNO,DONE_EGENDER,DONE_EPOSITION,DONE_EEDUCATION,\
                                    DONE_EJOINDATE,DONE_EENDDATE,DONE_EACTIVETIME,DONE_ESALARY,DONE_EDATE,DONE_ENEWPAYDATE) values (\
                                    '{row0}','{row1}',\
                                    '{row2}','{row3}','{row4}','{row5}',\
                                    '{row6}','{row7}','{row8}','{row9}',\
                                    '{row10}','{row11}','{row12}','{DateNow1}','{row13}')"
                        )
                        GetConn1.commit()
                        GetCor1.close()

                        conn = sqlite3.connect("DataBaseDir/PressDb.db")
                        cur = conn.cursor()
                        cur.execute(
                            "UPDATE EmployeeTable SET ERECSALL=?,ENEWPAYDATE=? WHERE (ESALARY-ERECSALL) = 0",
                            (0,DateNow1),


                            # "DELETE FROM EmployeeTable WHERE (ESALARY-ERECSALL) = 0"
                        )
                        conn.commit()
                        conn.close()
                        root.after(2000, ERef)
            except:
                messagebox.showerror("خطای کاربر", "لطفاً اطلاعات را بصورت درست درج نمایید")

        GetCor0.close()
        GetConn1.close()


def ESubmit():
    DateNow2 = datetime.date.today()
    EConn1 = sqlite3.connect("DataBaseDir/PressDb.db")
    cur1 = EConn1.cursor()
    if (
        Employee_MngEntry1.get() == ""
        or Employee_MngEntry3.get() == ""
        or Employee_MngEntry6.get() == ""
        or Employee_MngEntry8.get() == ""
        or Employee_MngEntry12.get() == ""
    ):
        messagebox.showwarning("ببخشید", "الزامی است که ورودی ها قبل از ذخیره پر شود.")
    else:
        cur1.execute(
            f"""
            insert into EmployeeTable (
            ENAME,
            EFNAME,
            EPHONENO,
            EEMAIL,
            EADDRESS,
            EIDCARDNO,
            EGENDER,
            EPOSITION,
            EEDUCATION,
            EJOINDATE,
            EENDDATE,
            EACTIVETIME,
            ESALARY,
            ERECSALL,
            ENEWPAYDATE
            )
            values (
            '{ENAME.get()}',
            '{EFNAME.get()}',
            '{EPHONENO.get()}',
            '{EEMAIL.get()}',
            '{EADDRESS.get()}',
            '{EIDCARDNO.get()}',
            '{EGENDER.get()}',
            '{EPOSITION.get()}',
            '{EEDUCATION.get()}',
            '{EJOINDATE.get()}',
            '{EENDDATE.get()}',
            '{EACTIVETIME.get()}',
            '{ESALARY.get()}',
            0,
            '{DateNow2}'
            )
            """
        )

    EConn1.commit()
    EConn1.close()

    Employee_MngEntry1.delete(0, END)
    Employee_MngEntry2.delete(0, END)
    Employee_MngEntry3.delete(0, END)
    Employee_MngEntry4.delete(0, END)
    Employee_MngEntry5.delete(0, END)
    Employee_MngEntry6.delete(0, END)
    Employee_MngEntry7.delete(0, END)
    Employee_MngEntry9.delete(0, END)
    Employee_MngEntry13.delete(0, END)
    Employee_MngEntry1.focus()
    ERef()


def EClear():
    Employee_MngEntry1.delete(0, END)
    Employee_MngEntry2.delete(0, END)
    Employee_MngEntry3.delete(0, END)
    Employee_MngEntry4.delete(0, END)
    Employee_MngEntry5.delete(0, END)
    Employee_MngEntry6.delete(0, END)
    Employee_MngEntry7.delete(0, END)
    Employee_MngEntry9.delete(0, END)
    Employee_MngEntry13.delete(0, END)
    Employee_MngEntry1.focus()


def ERef():
    Employee_Auto_Done_Func()
    Tree0.delete(*Tree0.get_children())
    Tree0Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    Tree0Cor = Tree0Conn.execute(
        """
        SELECT
        ENEWPAYDATE,
        ERECSALL,
        ESALARY,
        EENDDATE,
        EEDUCATION,
        EPOSITION,
        EGENDER,
        EIDCARDNO,
        EADDRESS,
        EEMAIL,
        EPHONENO,
        ENAME,
        EJOINDATE,
        ETID
        FROM EmployeeTable
        """
    )

    fetchTree0 = Tree0Cor.fetchall()
    for dataTree0 in fetchTree0:
        Tree0.insert("", "end", values=(dataTree0))
    Tree0Cor.close()
    Tree0Conn.close()

    #--------------------------------------
    Tree0_1.delete(*Tree0_1.get_children())
    Tree0_1Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    Tree0_1Cor = Tree0_1Conn.execute(
        """
        SELECT
        DONE_ENEWPAYDATE,
        DONE_EDATE,
        DONE_ESALARY,
        DONE_EENDDATE,
        DONE_EEDUCATION,
        DONE_EPOSITION,
        DONE_EIDCARDNO,
        DONE_EADDRESS,
        DONE_EEMAIL,
        DONE_EPHONENO,
        DONE_ENAME,
        DONE_EJOINDATE,
        DONE_ETID
        FROM
        EmployeeTableDone
        """
    )

    fetchTree0_1 = Tree0_1Cor.fetchall()
    for dataTree0_1 in fetchTree0_1:
        Tree0_1.insert("", "end", values=(dataTree0_1))
    Tree0_1Cor.close()
    Tree0_1Conn.close()


def EDelete():
    conn = sqlite3.connect("DataBaseDir/PressDb.db")
    cur = conn.cursor()
    messageDelete = messagebox.askyesno("هشدار", "؟آیا میخواهید این داده را حذف کنید")
    if messageDelete > 0:
        selected_item = Tree0.selection()[0]
        for selected_item in Tree0.selection():
            cur.execute(
                "DELETE FROM EmployeeTable WHERE ETID=?",
                (Tree0.set(selected_item, "#14"),),
            )
        conn.commit()
        Tree0.delete(selected_item)
    conn.close()
    ERef()


def SalaryPayFunc():
    if SalaryPaEntry.get() == "":
        messagebox.showerror("Space4", "لطفاً مقدار را وارد کنید")
    else:
        if SalaryPaEntry.get() != "":
            dt1 = ERECSALL.get()
            for selected_item in Tree0.selection():
                conn = sqlite3.connect("DataBaseDir/PressDb.db")
                cur = conn.cursor()
                conn1 = cur.execute(
                    "SELECT ERECSALL FROM EmployeeTable WHERE ETID=?",
                    (Tree0.set(selected_item, "#14"),),
                )
                fetch = cur.fetchall()
                for data in fetch:
                    data0 = data[0]
                    addm = int(data0) + int(dt1)

                    cur.execute(
                        "UPDATE EmployeeTable SET ERECSALL=? WHERE ETID=?",
                        (addm, Tree0.set(selected_item, "#14")),
                    )

                    SalaryPaEntry.delete(0, END)
                    messagebox.showinfo(
                        "Space4 Software", "! عملیه پرداخت موفقانه انجام شد"
                    )
                    conn.commit()
                    conn1.close()
                    conn.close()
                    root.after(1000, ERef)

        else:
            messagebox.showinfo("اوووه", "!!!ریکارد ذخیره نشد")


def EditingFunction():
    conn = sqlite3.connect("DataBaseDir/PressDb.db")
    cur1 = conn.cursor()
    selected_item = Tree0.selection()[0]
    for selected_item in Tree0.selection():
        EQueryEdit = """
        SELECT
        ENAME,
        EFNAME,
        EPHONENO,
        EEMAIL,
        EADDRESS,
        EIDCARDNO,
        EGENDER,
        EPOSITION,
        EEDUCATION,
        EJOINDATE,
        EENDDATE,
        EACTIVETIME,
        ESALARY
        FROM EmployeeTable
        WHERE ETID=?
        """
        cur1.execute(
            EQueryEdit,
            (Tree0.set(selected_item, "#14"),),
        )
        fetch1 = cur1.fetchall()
        for Row in fetch1:
            data1 = Row[0]
            data2 = Row[1]
            data3 = Row[2]
            data4 = Row[3]
            data5 = Row[4]
            data6 = Row[5]
            data7 = Row[6]
            data8 = Row[7]
            data9 = Row[8]
            data10 = Row[9]
            data11 = Row[10]
            data12 = Row[11]
            data13 = Row[12]
            EClear()
            Employee_MngEntry10.delete(0, END)
            Employee_MngEntry11.delete(0, END)

            Employee_MngEntry1.insert(0, data1)
            Employee_MngEntry2.insert(0, data2)
            Employee_MngEntry3.insert(0, data3)
            Employee_MngEntry4.insert(0, data4)
            Employee_MngEntry5.insert(0, data5)
            Employee_MngEntry6.insert(0, data6)
            Employee_MngEntry7.insert(0, data7)
            Employee_MngEntry8.set(data8)
            Employee_MngEntry9.insert(0, data9)
            Employee_MngEntry10.insert(0, data10)
            Employee_MngEntry11.insert(0, data11)
            Employee_MngEntry12.set(data12)
            Employee_MngEntry13.insert(0, data13)

    cur1.close()
    conn.close()
    Employee_MngEntry1.focus()


def SaveUpdateFunc():
    if Employee_MngEntry1.get() == "" or Employee_MngEntry13.get() == "":
        messagebox.showerror("Space4", "ورودی ها خالی است")
    else:
        if Employee_MngEntry1.get() != "":
            dt1 = Employee_MngEntry1.get()
            dt2 = Employee_MngEntry2.get()
            dt3 = Employee_MngEntry3.get()
            dt4 = Employee_MngEntry4.get()
            dt5 = Employee_MngEntry5.get()
            dt6 = Employee_MngEntry6.get()
            dt7 = Employee_MngEntry7.get()
            dt8 = Employee_MngEntry8.get()
            dt9 = Employee_MngEntry9.get()
            dt10 = Employee_MngEntry10.get()
            dt11 = Employee_MngEntry11.get()
            dt12 = Employee_MngEntry12.get()
            dt13 = Employee_MngEntry13.get()
            for selected_item in Tree0.selection():
                conn = sqlite3.connect("DataBaseDir/PressDb.db")
                cur = conn.cursor()
                UpdQueryE = """
                UPDATE EmployeeTable
                SET
                ENAME=?,
                EFNAME=?,
                EPHONENO=?,
                EEMAIL=?,
                EADDRESS=?,
                EIDCARDNO=?,
                EGENDER=?,
                EPOSITION=?,
                EEDUCATION=?,
                EJOINDATE=?,
                EENDDATE=?,
                EACTIVETIME=?,
                ESALARY=?
                WHERE ETID=?
                """
                cur.execute(
                    UpdQueryE,
                    (
                        dt1,
                        dt2,
                        dt3,
                        dt4,
                        dt5,
                        dt6,
                        dt7,
                        dt8,
                        dt9,
                        dt10,
                        dt11,
                        dt12,
                        dt13,
                        Tree0.set(selected_item, "#14"),
                    ),
                )

                EClear()
                messagebox.showinfo("Space4 Software", "! آپدیت موفقانه انجام شد")
                conn.commit()
                conn.close()
                ERef()
        else:
            messagebox.showinfo("اوووه", "!!!ریکارد ذخیره نشد")


# =========== Main Frames Opened ===========

MainFrame_L_Top_T1 = ctk.CTkFrame(tab1, corner_radius=10)
MainFrame_L_Top_T1.grid(row=1, column=0, padx=10, pady=10, sticky=NE)
Tree0Frame = ctk.CTkFrame(MainFrame_L_Top_T1, corner_radius=10)
Tree0Frame.grid(row=0, column=0, padx=10, pady=10, sticky=NE)
Tree0_1Frame = ctk.CTkFrame(MainFrame_L_Top_T1, corner_radius=10)
Tree0_1Frame.grid(row=1, column=0, padx=10, pady=50, sticky=NE)

Main_BtnFrameEmp = ctk.CTkFrame(MainFrame_L_Top_T1)
Main_BtnFrameEmp.place(x=10, y=250)

MainFrame_RIGHT_T1 = ctk.CTkFrame(tab1, corner_radius=10)
MainFrame_RIGHT_T1.grid(row=1, column=1, rowspan=2, padx=10, pady=10, sticky=NE)

# =========== Main Frames Closed ===========


Employee_MngLabel0 = ctk.CTkLabel(
    MainFrame_RIGHT_T1,
    text="ثبت مشخصات",
    font=default_font_bold,
    text_color=("teal", "orange"),
    justify=RIGHT,
)
Employee_MngLabel0.grid(row=0, column=3, sticky=E, padx=10, pady=10)


Employee_MngLabel1 = ctk.CTkLabel(
    MainFrame_RIGHT_T1, text="نام ", font=default_font_bold, justify=RIGHT
)
Employee_MngLabel1.grid(row=1, column=3, sticky=E, padx=10, pady=5)
Employee_MngLabel2 = ctk.CTkLabel(
    MainFrame_RIGHT_T1, text="تخلص", font=default_font_bold, justify=RIGHT
)
Employee_MngLabel2.grid(row=2, column=3, sticky=E, padx=10, pady=5)
Employee_MngLabel3 = ctk.CTkLabel(
    MainFrame_RIGHT_T1, text="تلفن", font=default_font_bold, justify=RIGHT
)
Employee_MngLabel3.grid(row=3, column=3, sticky=E, padx=10, pady=5)
Employee_MngLabel4 = ctk.CTkLabel(
    MainFrame_RIGHT_T1, text="ایمیل", font=default_font_bold, justify=RIGHT
)
Employee_MngLabel4.grid(row=4, column=3, sticky=E, padx=10, pady=5)
Employee_MngLabel5 = ctk.CTkLabel(
    MainFrame_RIGHT_T1, text="آدرس مکمل", font=default_font_bold, justify=RIGHT
)
Employee_MngLabel5.grid(row=5, column=3, sticky=E, padx=10, pady=5)
Employee_MngLabel6 = ctk.CTkLabel(
    MainFrame_RIGHT_T1, text="نمبر تذکره", font=default_font_bold, justify=RIGHT
)
Employee_MngLabel6.grid(row=6, column=3, sticky=E, padx=10, pady=5)
Employee_MngLabel7 = ctk.CTkLabel(
    MainFrame_RIGHT_T1, text="جنسیت", font=default_font_bold, justify=RIGHT
)
Employee_MngLabel7.grid(row=7, column=3, sticky=E, padx=10, pady=5)
Employee_MngLabel8 = ctk.CTkLabel(
    MainFrame_RIGHT_T1, text="بخش فعالیت", font=default_font_bold, justify=RIGHT
)
Employee_MngLabel8.grid(row=8, column=3, sticky=E, padx=10, pady=5)
Employee_MngLabel9 = ctk.CTkLabel(
    MainFrame_RIGHT_T1, text="تحصیلات", font=default_font_bold, justify=RIGHT
)
Employee_MngLabel9.grid(row=9, column=3, sticky=E, padx=10, pady=5)
Employee_MngLabel10 = ctk.CTkLabel(
    MainFrame_RIGHT_T1, text="تاریخ قرارداد", font=default_font_bold, justify=RIGHT
)
Employee_MngLabel10.grid(row=10, column=3, sticky=E, padx=10, pady=5)
Employee_MngLabel11 = ctk.CTkLabel(
    MainFrame_RIGHT_T1, text="ختم  قرارداد", font=default_font_bold, justify=RIGHT
)
Employee_MngLabel11.grid(row=11, column=3, sticky=E, padx=10, pady=5)
Employee_MngLabel12 = ctk.CTkLabel(
    MainFrame_RIGHT_T1, text="اوقات کاری", font=default_font_bold, justify=RIGHT
)
Employee_MngLabel12.grid(row=12, column=3, sticky=E, padx=10, pady=5)
Employee_MngLabel13 = ctk.CTkLabel(
    MainFrame_RIGHT_T1, text="معاش ماهوار", font=default_font_bold, justify=RIGHT
)
Employee_MngLabel13.grid(row=13, column=3, sticky=E, padx=10, pady=5)


Employee_MngEntry1 = ctk.CTkEntry(
    MainFrame_RIGHT_T1,
    textvariable=ENAME,
    width=130,
    font=default_font_bold,
    justify=RIGHT,
)
Employee_MngEntry1.grid(row=1, column=2, padx=10, sticky=E)
Employee_MngEntry1.focus()
Employee_MngEntry2 = ctk.CTkEntry(
    MainFrame_RIGHT_T1,
    textvariable=EFNAME,
    width=130,
    font=default_font_bold,
    justify=RIGHT,
)
Employee_MngEntry2.grid(row=2, column=2, padx=10, sticky=E)
Employee_MngEntry3 = ctk.CTkEntry(
    MainFrame_RIGHT_T1,
    textvariable=EPHONENO,
    width=130,
    font=default_font_bold,
    justify=RIGHT,
)
Employee_MngEntry3.grid(row=3, column=2, padx=10, sticky=E)
Employee_MngEntry4 = ctk.CTkEntry(
    MainFrame_RIGHT_T1,
    textvariable=EEMAIL,
    width=130,
    font=default_font_bold,
    justify=RIGHT,
)
Employee_MngEntry4.grid(row=4, column=2, padx=10, sticky=E)
Employee_MngEntry5 = ctk.CTkEntry(
    MainFrame_RIGHT_T1,
    textvariable=EADDRESS,
    width=130,
    font=default_font_bold,
    justify=RIGHT,
)
Employee_MngEntry5.grid(row=5, column=2, padx=10, sticky=E)
Employee_MngEntry6 = ctk.CTkEntry(
    MainFrame_RIGHT_T1,
    textvariable=EIDCARDNO,
    width=130,
    font=default_font_bold,
    justify=RIGHT,
)
Employee_MngEntry6.grid(row=6, column=2, padx=10, sticky=E)
Employee_MngEntry7 = ctk.CTkEntry(
    MainFrame_RIGHT_T1,
    textvariable=EGENDER,
    width=130,
    font=default_font_bold,
    justify=RIGHT,
)
Employee_MngEntry7.grid(row=7, column=2, padx=10, sticky=E)
Pospartval = [
    "مدیر",
    "انجنیر تخنیکی",
    "دیزاینر",
    "ماشینکار",
    "سیلک کار",
    "ctp کار",
    "صفاکار",
    "آشپز",
    "دلیور",
]
EPOSITION.set("بخش فعالیت")
Employee_MngEntry8 = ctk.CTkComboBox(
    MainFrame_RIGHT_T1,
    width=130,
    font=default_font_bold,
    justify=RIGHT,
    values=Pospartval,
    variable=EPOSITION,
)
Employee_MngEntry8.grid(row=8, column=2, padx=10, sticky=E)
Employee_MngEntry9 = ctk.CTkEntry(
    MainFrame_RIGHT_T1,
    textvariable=EEDUCATION,
    width=130,
    font=default_font_bold,
    justify=RIGHT,
)
Employee_MngEntry9.grid(row=9, column=2, padx=10, sticky=E)
Employee_MngEntry10 = DateEntry(
    MainFrame_RIGHT_T1,
    textvariable=EJOINDATE,
    font=("Arial", 10, "bold"),
    justify=RIGHT,
    width=15,
    date_pattern="yyyy-mm-dd",
)
Employee_MngEntry10.grid(row=10, column=2, padx=10, sticky=E)
Employee_MngEntry11 = DateEntry(
    MainFrame_RIGHT_T1,
    textvariable=EENDDATE,
    font=("Arial", 10, "bold"),
    justify=RIGHT,
    width=15,
    date_pattern="yyyy-mm-dd",
)

Employee_MngEntry11.grid(row=11, column=2, padx=10, sticky=E)
ActivTime = ["تمام روز", "نصف روز"]
EACTIVETIME.set("انتخاب تایم")
Employee_MngEntry12 = ctk.CTkComboBox(
    MainFrame_RIGHT_T1,
    width=130,
    font=default_font_bold,
    justify=RIGHT,
    values=ActivTime,
    variable=EACTIVETIME,
)
Employee_MngEntry12.grid(row=12, column=2, padx=10, sticky=E)
Employee_MngEntry13 = ctk.CTkEntry(
    MainFrame_RIGHT_T1,
    textvariable=ESALARY,
    width=130,
    font=default_font_bold,
    justify=RIGHT,
)
Employee_MngEntry13.grid(row=13, column=2, padx=10, sticky=E)


# ----------- Buttons --------------
SaveBtn1 = ctk.CTkButton(
    Main_BtnFrameEmp,
    image=SaveImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#333333",
    text="ذخیره",
    width=40,
    font=default_font_bold2,
    command=ESubmit,
)
SaveBtn1.grid(row=0, column=9, padx=10, pady=2)

EditBtnE1 = ctk.CTkButton(
    Main_BtnFrameEmp,
    image=EditImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#333333",
    text="ویرایش",
    width=40,
    font=default_font_bold2,
    command=EditingFunction,
)
EditBtnE1.grid(row=0, column=8, padx=10, pady=2)

UpdateBtnE1 = ctk.CTkButton(
    Main_BtnFrameEmp,
    image=UpdateImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#333333",
    text="آپدیت",
    width=40,
    font=default_font_bold2,
    command=SaveUpdateFunc,
)
UpdateBtnE1.grid(row=0, column=7, padx=10, pady=2)

ClearBtn1 = ctk.CTkButton(
    Main_BtnFrameEmp,
    image=ClearImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#333333",
    text="پاک کردن",
    width=40,
    font=default_font_bold2,
    command=EClear,
)
ClearBtn1.grid(row=0, column=6, padx=10, pady=2)
RefreshBtn1 = ctk.CTkButton(
    Main_BtnFrameEmp,
    image=RefreshImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#333333",
    text="تجدید ",
    width=40,
    font=default_font_bold2,
    command=ERef,
)
RefreshBtn1.grid(row=0, column=5, padx=10, pady=2)
DeleteBtn1 = ctk.CTkButton(
    Main_BtnFrameEmp,
    image=DeleteImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#333333",
    text="حذف",
    width=40,
    font=default_font_bold2,
    command=EDelete,
)
DeleteBtn1.grid(row=0, column=4, padx=10, pady=2)


# ---------------- Salary Pay ------------------
SalaryPayBtn = ctk.CTkButton(
    Main_BtnFrameEmp,
    hover_color=BTN_HOVER,
    # fg_color="#2B2B2B",
    font=default_font_bold,
    width=80,
    text="پرداخت معاش",
    command=SalaryPayFunc,
)
SalaryPayBtn.grid(row=0, column=3, padx=10, pady=5, sticky=NE)

SalaryPaEntry = ctk.CTkEntry(
    Main_BtnFrameEmp,
    width=125,
    justify=RIGHT,
    placeholder_text="وارد کردن مقدار پرداختی",
    font=default_font_bold1,
    textvariable=ERECSALL,
)
SalaryPaEntry.grid(row=0, column=2, padx=10, pady=5, sticky=NE)


# -------------- Tree View Tab1 Up --------------------
Tree0 = ctk.CTkFrame(Tree0Frame, border_width=0)
Tree0.grid(row=0, column=0, padx=10, sticky=NE)
ScrolbarXTree0 = ctk.CTkScrollbar(Tree0Frame, orientation=HORIZONTAL)
ScrolbarYTree0 = ctk.CTkScrollbar(Tree0Frame, orientation=VERTICAL)
Tree0 = ttk.Treeview(
    Tree0,
    columns=(
        "TV1",
        "TV2",
        "TV3",
        "TV4",
        "TV5",
        "TV6",
        "TV7",
        "TV8",
        "TV9",
        "TV10",
        "TV11",
        "TV12",
        "TV13",
        "TV14"
    ),
    selectmode="extended",
    height=7,
    yscrollcommand=ScrolbarYTree0.set,
    xscrollcommand=ScrolbarXTree0.set,
)
ScrolbarYTree0.configure(command=Tree0.yview)
ScrolbarYTree0.grid(row=0, column=1, ipady=10, sticky=NE)
ScrolbarXTree0.configure(command=Tree0.xview)
ScrolbarXTree0.grid(row=1, column=0, ipadx=240, sticky=W)

# =====setting headings for the columns
Tree0.heading("TV14", text="ID", anchor=E)
Tree0.heading("TV13", text="شروع قرارداد", anchor=E)
Tree0.heading("TV12", text="نام", anchor=E)
Tree0.heading("TV11", text="تلفن", anchor=E)
Tree0.heading("TV10", text="ایمیل", anchor=E)
Tree0.heading("TV9", text="آدرس", anchor=E)
Tree0.heading("TV8", text="نمبر تذکره", anchor=E)
Tree0.heading("TV7", text="موادیت", anchor=E)
Tree0.heading("TV6", text="بخش فعالیت", anchor=E)
Tree0.heading("TV5", text="تحصیلات", anchor=E)
Tree0.heading("TV4", text="ختم قرارداد", anchor=E)
Tree0.heading("TV3", text="معاش", anchor=E)
Tree0.heading("TV2", text="پرداخت", anchor=E)
Tree0.heading("TV1", text="ماه جاری", anchor=E)

# setting width of the columns
Tree0.column("#0", stretch=NO, minwidth=0, width=0, anchor=E)
Tree0.column("#1", stretch=NO, minwidth=0, width=45, anchor=E)
Tree0.column("#2", stretch=NO, minwidth=0, width=45, anchor=E)
Tree0.column("#3", stretch=NO, minwidth=0, width=70, anchor=E)
Tree0.column("#4", stretch=NO, minwidth=0, width=60, anchor=E)
Tree0.column("#5", stretch=NO, minwidth=0, width=70, anchor=E)
Tree0.column("#6", stretch=NO, minwidth=0, width=60, anchor=E)
Tree0.column("#7", stretch=NO, minwidth=0, width=60, anchor=E)
Tree0.column("#8", stretch=NO, minwidth=0, width=70, anchor=E)
Tree0.column("#9", stretch=NO, minwidth=0, width=70, anchor=E)
Tree0.column("#10", stretch=NO, minwidth=0, width=60, anchor=E)
Tree0.column("#11", stretch=NO, minwidth=0, width=60, anchor=E)
Tree0.column("#12", stretch=NO, minwidth=0, width=70, anchor=E)
Tree0.column("#13", stretch=NO, minwidth=0, width=30, anchor=E)
Tree0.column("#14", stretch=NO, minwidth=0, width=30, anchor=E)

Tree0.grid()

"""
EGENDER
EJOINDATE
EACTIVETIME
"""
Tree0.delete(*Tree0.get_children())
Tree0Conn = sqlite3.connect("DataBaseDir/PressDb.db")
Tree0Cor = Tree0Conn.execute(
    """
    SELECT
    ENEWPAYDATE,
    ERECSALL,
    ESALARY,
    EENDDATE,
    EEDUCATION,
    EPOSITION,
    EGENDER,
    EIDCARDNO,
    EADDRESS,
    EEMAIL,
    EPHONENO,
    ENAME,
    EJOINDATE,
    ETID
    FROM EmployeeTable
    """
)

fetchTree0 = Tree0Cor.fetchall()
for dataTree0 in fetchTree0:
    Tree0.insert("", "end", values=(dataTree0))
Tree0Cor.close()
Tree0Conn.close()


Tree0Title = ctk.CTkLabel(
    master=Tree0Frame, text="تصفیه نشده", font=default_font_bold, text_color=BGORANGE
)
Tree0Title.place(x=695, y=210)




Tree0_1 = ctk.CTkFrame(Tree0_1Frame, border_width=0)
Tree0_1.grid(row=0, column=0, padx=10, sticky=NE)
ScrolbarXTree0_1 = ctk.CTkScrollbar(Tree0_1Frame, orientation=HORIZONTAL)
ScrolbarYTree0_1 = ctk.CTkScrollbar(Tree0_1Frame, orientation=VERTICAL)
Tree0_1 = ttk.Treeview(
    Tree0_1,
    columns=(
        "TV1",
        "TV2",
        "TV3",
        "TV4",
        "TV5",
        "TV6",
        "TV7",
        "TV8",
        "TV9",
        "TV10",
        "TV11",
        "TV12",
        "TV13"
    ),
    selectmode="browse",
    height=7,
    yscrollcommand=ScrolbarYTree0_1.set,
    xscrollcommand=ScrolbarXTree0_1.set,
)
ScrolbarYTree0_1.configure(command=Tree0_1.yview)
ScrolbarYTree0_1.grid(row=0, column=1, ipady=10, sticky=NE)
ScrolbarXTree0_1.configure(command=Tree0_1.xview)
ScrolbarXTree0_1.grid(row=1, column=0, ipadx=240, sticky=W)

# =====setting headings for the columns
Tree0_1.heading("TV13", text="ID", anchor=E)
Tree0_1.heading("TV12", text="شروع قرارداد", anchor=E)
Tree0_1.heading("TV11", text="نام", anchor=E)
Tree0_1.heading("TV10", text="تلفن", anchor=E)
Tree0_1.heading("TV9", text="ایمیل", anchor=E)
Tree0_1.heading("TV8", text="آدرس", anchor=E)
Tree0_1.heading("TV7", text="نمبر تذکره", anchor=E)
Tree0_1.heading("TV6", text="بخش فعالیت", anchor=E)
Tree0_1.heading("TV5", text="تحصیلات", anchor=E)
Tree0_1.heading("TV4", text="ختم قرارداد", anchor=E)
Tree0_1.heading("TV3", text="معاش", anchor=E)
Tree0_1.heading("TV2", text="تصفیه", anchor=E)
Tree0_1.heading("TV1", text="تصفیه طی", anchor=E)


# setting width of the columns
Tree0_1.column("#0", stretch=NO, minwidth=0, width=0, anchor=E)
Tree0_1.column("#1", stretch=NO, minwidth=0, width=50, anchor=E)
Tree0_1.column("#2", stretch=NO, minwidth=0, width=50, anchor=E)
Tree0_1.column("#3", stretch=NO, minwidth=0, width=60, anchor=E)
Tree0_1.column("#4", stretch=NO, minwidth=0, width=80, anchor=E)
Tree0_1.column("#5", stretch=NO, minwidth=0, width=60, anchor=E)
Tree0_1.column("#6", stretch=NO, minwidth=0, width=80, anchor=E)
Tree0_1.column("#7", stretch=NO, minwidth=0, width=70, anchor=E)
Tree0_1.column("#8", stretch=NO, minwidth=0, width=60, anchor=E)
Tree0_1.column("#9", stretch=NO, minwidth=0, width=60, anchor=E)
Tree0_1.column("#10", stretch=NO, minwidth=0, width=60, anchor=E)
Tree0_1.column("#11", stretch=NO, minwidth=0, width=60, anchor=E)
Tree0_1.column("#12", stretch=NO, minwidth=0, width=80, anchor=E)
Tree0_1.column("#13", stretch=NO, minwidth=0, width=30, anchor=E)
Tree0_1.grid()

Tree0_1.delete(*Tree0_1.get_children())
Tree0_1Conn = sqlite3.connect("DataBaseDir/PressDb.db")
Tree0_1Cor = Tree0_1Conn.execute(
    """
    SELECT
    DONE_ENEWPAYDATE,
    DONE_EDATE,
    DONE_ESALARY,
    DONE_EENDDATE,
    DONE_EEDUCATION,
    DONE_EPOSITION,
    DONE_EIDCARDNO,
    DONE_EADDRESS,
    DONE_EEMAIL,
    DONE_EPHONENO,
    DONE_ENAME,
    DONE_EJOINDATE,
    DONE_ETID
    FROM
    EmployeeTableDone
    """
)

fetchTree0_1 = Tree0_1Cor.fetchall()
for dataTree0_1 in fetchTree0_1:
    Tree0_1.insert("", "end", values=(dataTree0_1))
Tree0_1Cor.close()
Tree0_1Conn.close()

Tree0_1Title = ctk.CTkLabel(
    master=Tree0_1Frame, text="تصفیه شده", font=default_font_bold, text_color=BGORANGE
)
Tree0_1Title.place(x=700, y=210)
# ========================= Tab2 Orders ==========================
# ========================= Tab2 Orders ==========================
# ========================= Tab2 Orders ==========================
# ========================= Tab2 Orders ==========================
# ========================= Tab2 Orders ==========================
# ========================= Tab2 Orders ==========================
# ========================= Tab2 Orders ==========================


# ============ Settled Table String Variables ==========
"""
    #------- Get Data -----------
    GetConn1 = sqlite3.connect('DataBaseDir/PressDb.db')
    selected_item = Tree1.selection()[0]
    for selected_item in Tree1.selection():
        GetCor1 = GetConn1.execute("SELECT OORDERTYPE,SUM(OLENGTH*OWIDTH)AS OSIZE,OQUNTITY,\
            OMATERIALTYPE,OTEXT,OCURRENTTIME,OFINISHTIME,SUM(OPRICE*(OLENGTH*OWIDTH)*OQUNTITY)AS OTOTALPAID,OCUSTOMERNAME,\
            OCUSTOMERPHONE,OCUSTADDRESS,ONOTE FROM LaserTable3D WHERE OCUSTOMERPHONE=?",(Tree1.set(selected_item, "#1"),))

    GetFetch1 = GetCor1.fetchall()
    for Getdata1 in GetFetch1:
        print(Getdata1)
        GetConn1.commit()
        GetCor1.close()
    GetConn1.close()

    #----- Separated ------------
"""
STL_ORDERTYPE = StringVar()
STL_SIZE = StringVar()
STL_QUNTITY = StringVar()
STL_MTLTYPE = StringVar()
STL_TEXT = StringVar()
STL_CURTIME = StringVar()
STL_FINTIME = StringVar()
STL_TTLPID = StringVar()
STL_NAME = StringVar()
STL_PHONE = StringVar()
STL_ADDR = StringVar()
STL_NOTE = StringVar()
STL_USAGE = StringVar()


def Settled_Auto_Done_Func():
    if OORDERTYPE.get() == O_3D:
        # ------- Get Data -----------
        GetConn1 = sqlite3.connect("DataBaseDir/PressDb.db")
        GetCor0 = GetConn1.execute(
            """
            SELECT
            SUM((OPRICE*(OLENGTH*OWIDTH)*OQUNTITY)-(OPREPAY+OREFUND))AS OSETTLED
            FROM LaserTable3D
            WHERE ((OPREPAY+OREFUND)-(OPRICE*(OLENGTH*OWIDTH)*OQUNTITY)) = 0"""
        )
        fetch1 = GetCor0.fetchall()
        for data0 in fetch1:
            dt = data0[0]

            if dt == 0:
                DateNow1 = datetime.date.today()
                GetCor1 = GetConn1.execute(
                    """
                    SELECT
                    OORDERTYPE,
                    SUM(OLENGTH*OWIDTH)AS OSIZE,
                    OQUNTITY,
                    OMATERIALTYPE,
                    OTEXT,
                    OCURRENTTIME,
                    OFINISHTIME,
                    SUM(OPRICE*(OLENGTH*OWIDTH)*OQUNTITY)AS OTOTALPAID,
                    OCUSTOMERNAME,
                    OCUSTOMERPHONE,
                    OCUSTADDRESS,
                    ONOTE,
                    OUSAGE AS OSG
                    FROM LaserTable3D
                    """
                )

                GetFetch1 = GetCor1.fetchall()
                for Getdata1 in GetFetch1:
                    row0 = Getdata1[0]
                    row1 = Getdata1[1]
                    row2 = Getdata1[2]
                    row3 = Getdata1[3]
                    row4 = Getdata1[4]
                    row5 = Getdata1[5]
                    row6 = Getdata1[6]
                    row7 = Getdata1[7]
                    row8 = Getdata1[8]
                    row9 = Getdata1[9]
                    row10 = Getdata1[10]
                    row11 = Getdata1[11]
                    row12 = Getdata1[12]

                    SCor1 = GetConn1.cursor()
                    SCor1.execute(
                        f"insert into LSTTable (STL_ORDERTYPE,STL_SIZE,STL_QUNTITY,STL_MTLTYPE,\
                                STL_TEXT,STL_CURTIME,STL_FINTIME,STL_TTLPID,STL_NAME,\
                                STL_PHONE,STL_ADDR,STL_NOTE,STL_USAGE,STL_DATE) values ('{row0}','{row1}',\
                                '{row2}','{row3}','{row4}','{row5}',\
                                '{row6}','{row7}','{row8}','{row9}',\
                                '{row10}','{row11}','{row12}','{DateNow1}')"
                    )
                    GetConn1.commit()
                    GetCor1.close()

                    conn = sqlite3.connect("DataBaseDir/PressDb.db")
                    cur = conn.cursor()
                    cur.execute(
                        "DELETE FROM LaserTable3D WHERE ((OPREPAY+OREFUND)-(OPRICE*(OLENGTH*OWIDTH)*OQUNTITY)) = 0"
                    )
                    conn.commit()
                    conn.close()
                    ORef()
        GetCor0.close()
        GetConn1.close()

    #----------------------------------------------------------
    elif OORDERTYPE.get() == O_ENGRAVE:
        # ------- Get Data -----------
        GetConn2 = sqlite3.connect("DataBaseDir/PressDb.db")
        GetCor0_2 = GetConn2.execute(
            """
            SELECT
            SUM((O_ENGR_PRICE*(O_ENGR_LENGTH*O_ENGR_WIDTH)*O_ENGR_QUNTITY)-
                (O_ENGR_PREPAY+O_ENGR_REFUND))AS O_ENGR_SETTLED
            FROM LaserTableEngrave
            WHERE ((O_ENGR_PREPAY+O_ENGR_REFUND)-
                (O_ENGR_PRICE*(O_ENGR_LENGTH*O_ENGR_WIDTH)*O_ENGR_QUNTITY)) = 0
            """
        )
        fetch2 = GetCor0_2.fetchall()
        for data0 in fetch2:
            dt = data0[0]

            if dt == 0:
                DateNow1 = datetime.date.today()
                GetCor1_2 = GetConn2.execute(
                    """
                    SELECT
                    O_ENGR_ORDERTYPE,
                    SUM(O_ENGR_LENGTH*O_ENGR_WIDTH)AS O_ENGR_SIZE,
                    O_ENGR_QUNTITY,
                    O_ENGR_MATERIALTYPE,
                    O_ENGR_TEXT,
                    O_ENGR_CURRENTTIME,
                    O_ENGR_FINISHTIME,
                    SUM(O_ENGR_PRICE*(O_ENGR_LENGTH*O_ENGR_WIDTH)*
                        O_ENGR_QUNTITY)AS O_ENGR_TOTALPAID,
                    O_ENGR_CUSTOMERNAME,
                    O_ENGR_CUSTOMERPHONE,
                    O_ENGR_CUSTADDRESS,
                    O_ENGR_NOTE,
                    O_ENGR_USAGE AS O_ENGR_SG
                    FROM LaserTableEngrave
                    """
                )

                GetFetch1 = GetCor1_2.fetchall()
                for Getdata1 in GetFetch1:
                    row0 = Getdata1[0]
                    row1 = Getdata1[1]
                    row2 = Getdata1[2]
                    row3 = Getdata1[3]
                    row4 = Getdata1[4]
                    row5 = Getdata1[5]
                    row6 = Getdata1[6]
                    row7 = Getdata1[7]
                    row8 = Getdata1[8]
                    row9 = Getdata1[9]
                    row10 = Getdata1[10]
                    row11 = Getdata1[11]
                    row12 = Getdata1[12]

                    SCor1 = GetConn2.cursor()
                    SCor1.execute(
                        f"""
                        insert into LaserTableEngraveDone (
                        DONE_O_ENGR_ORDERTYPE,
                        DONE_O_ENGR_SIZE,
                        DONE_O_ENGR_QUNTITY,
                        DONE_O_ENGR_MTLTYPE,
                        DONE_O_ENGR_TEXT,
                        DONE_O_ENGR_CURTIME,
                        DONE_O_ENGR_FINTIME,
                        DONE_O_ENGR_TTLPID,
                        DONE_O_ENGR_NAME,
                        DONE_O_ENGR_PHONE,
                        DONE_O_ENGR_ADDR,
                        DONE_O_ENGR_NOTE,
                        DONE_O_ENGR_USAGE,
                        DONE_O_ENGR_DATE
                        )
                        values(
                        '{row0}',
                        '{row1}',
                        '{row2}',
                        '{row3}',
                        '{row4}',
                        '{row5}',
                        '{row6}',
                        '{row7}',
                        '{row8}',
                        '{row9}',
                        '{row10}',
                        '{row11}',
                        '{row12}',
                        '{DateNow1}'
                        )
                        """
                    )
                    GetConn2.commit()
                    GetCor1_2.close()

                    conn = sqlite3.connect("DataBaseDir/PressDb.db")
                    cur = conn.cursor()
                    cur.execute(
                        """
                        DELETE FROM LaserTableEngrave
                        WHERE ((O_ENGR_PREPAY+O_ENGR_REFUND)-
                            (O_ENGR_PRICE*(O_ENGR_LENGTH*O_ENGR_WIDTH)*
                                O_ENGR_QUNTITY)) = 0
                        """
                    )
                    conn.commit()
                    conn.close()
                    ORef()
        GetCor0_2.close()
        GetConn2.close()


    #----------------------------------------------------------
    elif OORDERTYPE.get() == O_CUTTING:
        # ------- Get Data -----------
        GetConn3 = sqlite3.connect("DataBaseDir/PressDb.db")
        GetCor0_3 = GetConn3.execute(
            """
            SELECT
            SUM((O_CUT_PRICE*(O_CUT_LENGTH*O_CUT_WIDTH)*O_CUT_QUNTITY)-
                (O_CUT_PREPAY+O_CUT_REFUND))AS O_CUT_SETTLED
            FROM LaserTableCut
            WHERE ((O_CUT_PREPAY+O_CUT_REFUND)-
                (O_CUT_PRICE*(O_CUT_LENGTH*O_CUT_WIDTH)*O_CUT_QUNTITY)) = 0
            """
        )
        fetch3 = GetCor0_3.fetchall()
        for data0 in fetch3:
            dt = data0[0]

            if dt == 0:
                DateNow1 = datetime.date.today()
                GetCor1_3 = GetConn3.execute(
                    """
                    SELECT
                    O_CUT_ORDERTYPE,
                    SUM(O_CUT_LENGTH*O_CUT_WIDTH)AS O_CUT_SIZE,
                    O_CUT_QUNTITY,
                    O_CUT_MATERIALTYPE,
                    O_CUT_TEXT,
                    O_CUT_CURRENTTIME,
                    O_CUT_FINISHTIME,
                    SUM(O_CUT_PRICE*(O_CUT_LENGTH*O_CUT_WIDTH)*
                        O_CUT_QUNTITY)AS O_CUT_TOTALPAID,
                    O_CUT_CUSTOMERNAME,
                    O_CUT_CUSTOMERPHONE,
                    O_CUT_CUSTADDRESS,
                    O_CUT_NOTE,
                    O_CUT_USAGE AS O_CUT_SG
                    FROM LaserTableCut
                    """
                )

                GetFetch3 = GetCor1_3.fetchall()
                for Getdata3 in GetFetch3:
                    row0 = Getdata3[0]
                    row1 = Getdata3[1]
                    row2 = Getdata3[2]
                    row3 = Getdata3[3]
                    row4 = Getdata3[4]
                    row5 = Getdata3[5]
                    row6 = Getdata3[6]
                    row7 = Getdata3[7]
                    row8 = Getdata3[8]
                    row9 = Getdata3[9]
                    row10 = Getdata3[10]
                    row11 = Getdata3[11]
                    row12 = Getdata3[12]
                    print(row1,row2,row3,row5)

                    SCor3 = GetConn3.cursor()
                    SCor3.execute(
                        f"""
                        insert into LaserTableCutDone (
                        DONE_O_CUT_ORDERTYPE,
                        DONE_O_CUT_SIZE,
                        DONE_O_CUT_QUNTITY,
                        DONE_O_CUT_MTLTYPE,
                        DONE_O_CUT_TEXT,
                        DONE_O_CUT_CURTIME,
                        DONE_O_CUT_FINTIME,
                        DONE_O_CUT_TTLPID,
                        DONE_O_CUT_NAME,
                        DONE_O_CUT_PHONE,
                        DONE_O_CUT_ADDR,
                        DONE_O_CUT_NOTE,
                        DONE_O_CUT_USAGE,
                        DONE_O_CUT_DATE
                        )
                        values(
                        '{row0}',
                        '{row1}',
                        '{row2}',
                        '{row3}',
                        '{row4}',
                        '{row5}',
                        '{row6}',
                        '{row7}',
                        '{row8}',
                        '{row9}',
                        '{row10}',
                        '{row11}',
                        '{row12}',
                        '{DateNow1}'
                        )
                        """
                    )
                    GetConn3.commit()
                    GetCor1_3.close()

                    conn3 = sqlite3.connect("DataBaseDir/PressDb.db")
                    cur3 = conn3.cursor()
                    cur3.execute(
                        """
                        DELETE FROM LaserTableCut
                        WHERE ((O_CUT_PREPAY+O_CUT_REFUND)-
                            (O_CUT_PRICE*(O_CUT_LENGTH*O_CUT_WIDTH)*
                                O_CUT_QUNTITY)) = 0
                        """
                    )
                    conn3.commit()
                    conn3.close()
                    ORef()
        GetCor0_3.close()
        GetConn3.close()


# --------------- Settled Finished ------------------------
# --------- Table Order Variables ------------

OORDERTYPE = StringVar()
OLENGTH = StringVar()
OWIDTH = StringVar()
OQUNTITY = StringVar()
OMATERIALTYPE = StringVar()
OTEXT = StringVar()
OCURRENTTIME = StringVar()
OFINISHTIME = StringVar()
OPRICE = StringVar()
OPREPAY = StringVar()
OCUSTOMERNAME = StringVar()
OCUSTOMERPHONE = StringVar()
OCUSTADDRESS = StringVar()
ODELIVERYPRICE = StringVar()
ONOTE = StringVar()
OREFUND = StringVar()
OUSAGE = StringVar()

ProjectTypeVar = StringVar()


def UpdateFunction():
    if OORDERTYPE.get() == O_3D:
        if RefundEntry1.get() == "":
            messagebox.showerror("Space4", "لطفاً مقدار را وارد کنید")
        else:
            if RefundEntry1.get() != "":
                dt1 = OREFUND.get()
                for selected_item in Tree1.selection():
                    conn = sqlite3.connect("DataBaseDir/PressDb.db")
                    cur = conn.cursor()
                    conn1 = cur.execute(
                        "SELECT OREFUND FROM LaserTable3D WHERE OTID=?",
                        (Tree1.set(selected_item, "#17"),),
                    )
                    fetch = cur.fetchall()
                    for data in fetch:
                        data0 = data[0]
                        addm = int(data0) + int(dt1)
                        cur.execute(
                            "UPDATE LaserTable3D SET OREFUND=? WHERE OTID=?",
                            (addm, Tree1.set(selected_item, "#17")),
                        )
                        RefundEntry1.delete(0, END)
                        messagebox.showinfo("Space4 Software", "!رسید موفقانه  درج گردید")
                        conn.commit()
                        conn1.close()
                        conn.close()
                        ORef()
            else:
                messagebox.showinfo("اوووه", "!!!ریکارد ذخیره نشد")

    if OORDERTYPE.get() == O_ENGRAVE:
        if RefundEntry1.get() == "":
            messagebox.showerror("Space4", "لطفاً مقدار را وارد کنید")
        else:
            if RefundEntry1.get() != "":
                dt1 = OREFUND.get()
                for selected_item in Tree1.selection():
                    conn = sqlite3.connect("DataBaseDir/PressDb.db")
                    cur = conn.cursor()
                    conn1 = cur.execute(
                        "SELECT O_ENGR_REFUND FROM LaserTableEngrave WHERE O_ENGR_TID=?",
                        (Tree1.set(selected_item, "#17"),),
                    )
                    fetch = cur.fetchall()
                    for data in fetch:
                        data0 = data[0]
                        addm = int(data0) + int(dt1)
                        cur.execute(
                            "UPDATE LaserTableEngrave SET O_ENGR_REFUND=? WHERE O_ENGR_TID=?",
                            (addm, Tree1.set(selected_item, "#17")),
                        )
                        RefundEntry1.delete(0, END)
                        messagebox.showinfo("Space4 Software", "!رسید موفقانه  درج گردید")
                        conn.commit()
                        conn1.close()
                        conn.close()
                        ORef()
            else:
                messagebox.showinfo("اوووه", "!!!ریکارد ذخیره نشد")


    if OORDERTYPE.get() == O_CUTTING:
        if RefundEntry1.get() == "":
            messagebox.showerror("Space4", "لطفاً مقدار را وارد کنید")
        else:
            if RefundEntry1.get() != "":
                dt1 = OREFUND.get()
                for selected_item in Tree1.selection():
                    conn = sqlite3.connect("DataBaseDir/PressDb.db")
                    cur = conn.cursor()
                    conn1 = cur.execute(
                        "SELECT O_CUT_REFUND FROM LaserTableCut WHERE O_CUT_TID=?",
                        (Tree1.set(selected_item, "#17"),),
                    )
                    fetch = cur.fetchall()
                    for data in fetch:
                        data0 = data[0]
                        addm = int(data0) + int(dt1)
                        cur.execute(
                            "UPDATE LaserTableCut SET O_CUT_REFUND=? WHERE O_CUT_TID=?",
                            (addm, Tree1.set(selected_item, "#17")),
                        )
                        RefundEntry1.delete(0, END)
                        messagebox.showinfo("Space4 Software", "!رسید موفقانه  درج گردید")
                        conn.commit()
                        conn1.close()
                        conn.close()
                        ORef()
            else:
                messagebox.showinfo("اوووه", "!!!ریکارد ذخیره نشد")



def ProjUsageFunc():
    if OORDERTYPE.get() == O_3D:
        if UsageEntry1.get() == "":
            messagebox.showerror("Space4", "لطفاً مقدار مصرف مواد خام را وارد کنید")
        else:
            if UsageEntry1.get() != "":
                Udt1 = OUSAGE.get()
                for selected_item in Tree1.selection():
                    Uconn = sqlite3.connect("DataBaseDir/PressDb.db")
                    Ucur = Uconn.cursor()
                    Uconn1 = Ucur.execute(
                        "SELECT OUSAGE FROM LaserTable3D WHERE OTID=?",
                        (Tree1.set(selected_item, "#17"),),
                    )
                    fetch = Ucur.fetchall()
                    for data in fetch:
                        data0 = data[0]
                        addm = int(data0) + int(Udt1)
                        Ucur.execute(
                            "UPDATE LaserTable3D SET OUSAGE=? WHERE OTID=?",
                            (addm, Tree1.set(selected_item, "#17")),
                        )
                        UsageEntry1.delete(0, END)
                        messagebox.showinfo(
                            "Space4 Software", "!مصارف پروژه مورد نظر موفقانه درج گردید"
                        )
                        Uconn.commit()
                        Uconn1.close()
                        Uconn.close()
                        ORef()
            else:
                messagebox.showinfo("اوووه", "!!!مصارف پروژه ذخیره نشد")


    elif OORDERTYPE.get() == O_ENGRAVE:
        if UsageEntry1.get() == "":
            messagebox.showerror("Space4", "لطفاً مقدار مصرف مواد خام را وارد کنید")
        else:
            if UsageEntry1.get() != "":
                Udt1 = OUSAGE.get()
                for selected_item in Tree1.selection():
                    Uconn = sqlite3.connect("DataBaseDir/PressDb.db")
                    Ucur = Uconn.cursor()
                    Uconn1 = Ucur.execute(
                        "SELECT O_ENGR_USAGE FROM LaserTableEngrave WHERE O_ENGR_TID=?",
                        (Tree1.set(selected_item, "#17"),),
                    )
                    fetch = Ucur.fetchall()
                    for data in fetch:
                        data0 = data[0]
                        addm = int(data0) + int(Udt1)
                        Ucur.execute(
                            "UPDATE LaserTableEngrave SET O_ENGR_USAGE=? WHERE O_ENGR_TID=?",
                            (addm, Tree1.set(selected_item, "#17")),
                        )
                        UsageEntry1.delete(0, END)
                        messagebox.showinfo(
                            "Space4 Software", "!مصارف پروژه مورد نظر موفقانه درج گردید"
                        )
                        Uconn.commit()
                        Uconn1.close()
                        Uconn.close()
                        ORef()
            else:
                messagebox.showinfo("اوووه", "!!!مصارف پروژه ذخیره نشد")


    elif OORDERTYPE.get() == O_CUTTING:
        if UsageEntry1.get() == "":
            messagebox.showerror("Space4", "لطفاً مقدار مصرف مواد خام را وارد کنید")
        else:
            if UsageEntry1.get() != "":
                Udt1 = OUSAGE.get()
                for selected_item in Tree1.selection():
                    Uconn = sqlite3.connect("DataBaseDir/PressDb.db")
                    Ucur = Uconn.cursor()
                    Uconn1 = Ucur.execute(
                        "SELECT O_CUT_USAGE FROM LaserTableCut WHERE O_CUT_TID=?",
                        (Tree1.set(selected_item, "#17"),),
                    )
                    fetch = Ucur.fetchall()
                    for data in fetch:
                        data0 = data[0]
                        addm = int(data0) + int(Udt1)
                        Ucur.execute(
                            "UPDATE LaserTableCut SET O_CUT_USAGE=? WHERE O_CUT_TID=?",
                            (addm, Tree1.set(selected_item, "#17")),
                        )
                        UsageEntry1.delete(0, END)
                        messagebox.showinfo(
                            "Space4 Software", "!مصارف پروژه مورد نظر موفقانه درج گردید"
                        )
                        Uconn.commit()
                        Uconn1.close()
                        Uconn.close()
                        ORef()
            else:
                messagebox.showinfo("اوووه", "!!!مصارف پروژه ذخیره نشد")
# ============= Laser Part all options ===================



def OSubmit():
    OConn1 = sqlite3.connect("DataBaseDir/PressDb.db")
    Ocur1 = OConn1.cursor()
    if (
        Order_MngEntry4.get() == ""
        or Order_MngEntry10.get() == ""
    ):
        messagebox.showwarning("ببخشید", "الزامی است که ورودی ها قبل از ذخیره پر شود.")
    else:
        if OORDERTYPE.get() == O_3D:
            Ocur1.execute(
                f"""
                insert into LaserTable3D (
                OORDERTYPE,
                OLENGTH,
                OWIDTH,
                OQUNTITY,
                OMATERIALTYPE,
                OTEXT,
                OCURRENTTIME,
                OFINISHTIME,
                OPRICE,
                OPREPAY,
                OCUSTOMERNAME,
                OCUSTOMERPHONE,
                OCUSTADDRESS,
                ODELIVERYPRICE,
                ONOTE,
                OREFUND,
                OUSAGE
                )
                values(
                '{OORDERTYPE.get()}',
                '{OLENGTH.get()}',
                '{OWIDTH.get()}',
                '{OQUNTITY.get()}',
                '{OMATERIALTYPE.get()}',
                '{Order_MngEntry6.get()}',
                '{OCURRENTTIME.get()}',
                '{OFINISHTIME.get()}',
                '{OPRICE.get()}',
                '{OPREPAY.get()}',
                '{OCUSTOMERNAME.get()}',
                '{OCUSTOMERPHONE.get()}',
                '{OCUSTADDRESS.get()}',
                '{ODELIVERYPRICE.get()}',
                '{ONOTE.get()}',0,0
                )
                """
            )
            OClear()

        elif OORDERTYPE.get() == O_ENGRAVE:
            Ocur1.execute(
                f"""
                insert into LaserTableEngrave (
                O_ENGR_ORDERTYPE,
                O_ENGR_LENGTH,
                O_ENGR_WIDTH,
                O_ENGR_QUNTITY,
                O_ENGR_MATERIALTYPE,
                O_ENGR_TEXT,
                O_ENGR_CURRENTTIME,
                O_ENGR_FINISHTIME,
                O_ENGR_PRICE,
                O_ENGR_PREPAY,
                O_ENGR_CUSTOMERNAME,
                O_ENGR_CUSTOMERPHONE,
                O_ENGR_CUSTADDRESS,
                O_ENGR_DELIVERYPRICE,
                O_ENGR_NOTE,
                O_ENGR_REFUND,
                O_ENGR_USAGE
                )
                values(
                '{OORDERTYPE.get()}',
                '{OLENGTH.get()}',
                '{OWIDTH.get()}',
                '{OQUNTITY.get()}',
                '{OMATERIALTYPE.get()}',
                '{Order_MngEntry6.get()}',
                '{OCURRENTTIME.get()}',
                '{OFINISHTIME.get()}',
                '{OPRICE.get()}',
                '{OPREPAY.get()}',
                '{OCUSTOMERNAME.get()}',
                '{OCUSTOMERPHONE.get()}',
                '{OCUSTADDRESS.get()}',
                '{ODELIVERYPRICE.get()}',
                '{ONOTE.get()}',0,0
                )
                """
            )
            OClear()

        elif OORDERTYPE.get() == O_CUTTING:
            Ocur1.execute(
                f"""
                insert into LaserTableCut (
                O_CUT_ORDERTYPE,
                O_CUT_LENGTH,
                O_CUT_WIDTH,
                O_CUT_QUNTITY,
                O_CUT_MATERIALTYPE,
                O_CUT_TEXT,
                O_CUT_CURRENTTIME,
                O_CUT_FINISHTIME,
                O_CUT_PRICE,
                O_CUT_PREPAY,
                O_CUT_CUSTOMERNAME,
                O_CUT_CUSTOMERPHONE,
                O_CUT_CUSTADDRESS,
                O_CUT_DELIVERYPRICE,
                O_CUT_NOTE,
                O_CUT_REFUND,
                O_CUT_USAGE
                )
                values(
                '{OORDERTYPE.get()}',
                '{OLENGTH.get()}',
                '{OWIDTH.get()}',
                '{OQUNTITY.get()}',
                '{OMATERIALTYPE.get()}',
                '{Order_MngEntry6.get()}',
                '{OCURRENTTIME.get()}',
                '{OFINISHTIME.get()}',
                '{OPRICE.get()}',
                '{OPREPAY.get()}',
                '{OCUSTOMERNAME.get()}',
                '{OCUSTOMERPHONE.get()}',
                '{OCUSTADDRESS.get()}',
                '{ODELIVERYPRICE.get()}',
                '{ONOTE.get()}',0,0
                )
                """
            )
            OClear()
        else:
            messagebox.showerror("Space4", "لطفاً نوعیت را انتخاب کنید")

    OConn1.commit()
    OConn1.close()
    ORef()


def OClear():
    Order_MngEntry2.delete(0, END)
    Order_MngEntry3.delete(0, END)
    Order_MngEntry4.delete(0, END)
    Order_MngEntry5.delete(0, END)
    Order_MngEntry6.delete(0, END)
    Order_MngEntry9.delete(0, END)
    Order_MngEntry10.delete(0, END)
    Order_MngEntry11.delete(0, END)
    Order_MngEntry12.delete(0, END)
    Order_MngEntry13.delete(0, END)
    Order_MngEntry14.delete(0, END)
    Order_MngEntry2.focus()


def ORef():
    if OORDERTYPE.get() == O_3D:
        Tree1.delete(*Tree1.get_children())
        Tree1Conn = sqlite3.connect("DataBaseDir/PressDb.db")
        Tree1Cor = Tree1Conn.execute(
            """
            SELECT
            OUSAGE,
            OREFUND,
            ONOTE,
            ODELIVERYPRICE,
            OCUSTADDRESS,
            OCUSTOMERPHONE,
            OCUSTOMERNAME,
            OPREPAY,
            OPRICE,
            OFINISHTIME,
            OCURRENTTIME,
            OTEXT,
            OQUNTITY,
            OWIDTH,
            OLENGTH,
            OORDERTYPE,
            OTID
            FROM LaserTable3D"""
        )
        fetchTree1 = Tree1Cor.fetchall()
        for dataTree1 in fetchTree1:
            Tree1.insert("", "end", values=(dataTree1))
        Tree1Cor.close()
        Tree1Conn.close()
        Settled_Auto_Done_Func()

        # ====== Separate Tree Refresh ==========
        Tree2.delete(*Tree2.get_children())
        Tree2Conn = sqlite3.connect("DataBaseDir/PressDb.db")
        Tree2Cor = Tree2Conn.execute(
            """
            SELECT
            STL_DATE,
            STL_USAGE,
            STL_ADDR,
            STL_PHONE,
            STL_TTLPID,
            STL_NAME,
            STL_FINTIME,
            STL_TEXT,
            STL_QUNTITY,
            STL_SIZE,
            STL_ORDERTYPE
            FROM LSTTable
            """
        )
        fetchTree2 = Tree2Cor.fetchall()
        for dataTree2 in fetchTree2:
            Tree2.insert("", "end", values=(dataTree2))
        Tree2Cor.close()
        Tree2Conn.close()

    elif OORDERTYPE.get() == O_ENGRAVE:
        Tree1.delete(*Tree1.get_children())
        Tree1Conn = sqlite3.connect("DataBaseDir/PressDb.db")
        Tree1Cor = Tree1Conn.execute(
            """
            SELECT
            O_ENGR_USAGE,
            O_ENGR_REFUND,
            O_ENGR_NOTE,
            O_ENGR_DELIVERYPRICE,
            O_ENGR_CUSTADDRESS,
            O_ENGR_CUSTOMERPHONE,
            O_ENGR_CUSTOMERNAME,
            O_ENGR_PREPAY,
            O_ENGR_PRICE,
            O_ENGR_FINISHTIME,
            O_ENGR_CURRENTTIME,
            O_ENGR_TEXT,
            O_ENGR_QUNTITY,
            O_ENGR_WIDTH,
            O_ENGR_LENGTH,
            O_ENGR_ORDERTYPE,
            O_ENGR_TID
            FROM LaserTableEngrave"""
        )
        fetchTree1 = Tree1Cor.fetchall()
        for dataTree1 in fetchTree1:
            Tree1.insert("", "end", values=(dataTree1))
        Tree1Cor.close()
        Tree1Conn.close()
        Settled_Auto_Done_Func()

        # ====== Separate Tree Refresh ==========
        Tree2.delete(*Tree2.get_children())
        Tree2Conn = sqlite3.connect("DataBaseDir/PressDb.db")
        Tree2Cor = Tree2Conn.execute(
            """
            SELECT
            DONE_O_ENGR_DATE,
            DONE_O_ENGR_USAGE,
            DONE_O_ENGR_ADDR,
            DONE_O_ENGR_PHONE,
            DONE_O_ENGR_TTLPID,
            DONE_O_ENGR_NAME,
            DONE_O_ENGR_FINTIME,
            DONE_O_ENGR_TEXT,
            DONE_O_ENGR_QUNTITY,
            DONE_O_ENGR_SIZE,
            DONE_O_ENGR_ORDERTYPE
            FROM LaserTableEngraveDone
            """
        )
        fetchTree2 = Tree2Cor.fetchall()
        for dataTree2 in fetchTree2:
            Tree2.insert("", "end", values=(dataTree2))
        Tree2Cor.close()
        Tree2Conn.close()


    elif OORDERTYPE.get() == O_CUTTING:
        Tree1.delete(*Tree1.get_children())
        Tree1Conn = sqlite3.connect("DataBaseDir/PressDb.db")
        Tree1Cor = Tree1Conn.execute(
            """
            SELECT
            O_CUT_USAGE,
            O_CUT_REFUND,
            O_CUT_NOTE,
            O_CUT_DELIVERYPRICE,
            O_CUT_CUSTADDRESS,
            O_CUT_CUSTOMERPHONE,
            O_CUT_CUSTOMERNAME,
            O_CUT_PREPAY,
            O_CUT_PRICE,
            O_CUT_FINISHTIME,
            O_CUT_CURRENTTIME,
            O_CUT_TEXT,
            O_CUT_QUNTITY,
            O_CUT_WIDTH,
            O_CUT_LENGTH,
            O_CUT_ORDERTYPE,
            O_CUT_TID
            FROM LaserTableCut"""
        )
        fetchTree1 = Tree1Cor.fetchall()
        for dataTree1 in fetchTree1:
            Tree1.insert("", "end", values=(dataTree1))
        Tree1Cor.close()
        Tree1Conn.close()
        Settled_Auto_Done_Func()

        # ====== Separate Tree Refresh ==========
        Tree2.delete(*Tree2.get_children())
        Tree2Conn = sqlite3.connect("DataBaseDir/PressDb.db")
        Tree2Cor = Tree2Conn.execute(
            """
            SELECT
            DONE_O_CUT_DATE,
            DONE_O_CUT_USAGE,
            DONE_O_CUT_ADDR,
            DONE_O_CUT_PHONE,
            DONE_O_CUT_TTLPID,
            DONE_O_CUT_NAME,
            DONE_O_CUT_FINTIME,
            DONE_O_CUT_TEXT,
            DONE_O_CUT_QUNTITY,
            DONE_O_CUT_SIZE,
            DONE_O_CUT_ORDERTYPE
            FROM LaserTableCutDone
            """
        )
        fetchTree2 = Tree2Cor.fetchall()
        for dataTree2 in fetchTree2:
            Tree2.insert("", "end", values=(dataTree2))
        Tree2Cor.close()
        Tree2Conn.close()


def ODelete():
    try:
        if OORDERTYPE.get() == O_3D:
            selected_item = Tree1.selection()[0]
            for selected_item in Tree1.selection():
                conn = sqlite3.connect("DataBaseDir/PressDb.db")
                cur = conn.cursor()
                messageDelete = messagebox.askyesno(
                    "هشدار", "؟آیا میخواهید این داده را حذف کنید"
                )
                if messageDelete > 0:
                    cur.execute(
                        "DELETE FROM LaserTable3D WHERE OTID=?",
                        (Tree1.set(selected_item, "#17"),),
                    )
                    conn.commit()
                    Tree1.delete(selected_item)
                conn.close()


        elif OORDERTYPE.get() == O_ENGRAVE:
            selected_item = Tree1.selection()[0]
            for selected_item in Tree1.selection():
                conn = sqlite3.connect("DataBaseDir/PressDb.db")
                cur = conn.cursor()
                messageDelete = messagebox.askyesno(
                    "هشدار", "؟آیا میخواهید این داده را حذف کنید"
                )
                if messageDelete > 0:
                    cur.execute(
                        "DELETE FROM LaserTableEngrave WHERE O_ENGR_TID=?",
                        (Tree1.set(selected_item, "#17"),),
                    )
                    conn.commit()
                    Tree1.delete(selected_item)
                conn.close()


        elif OORDERTYPE.get() == O_CUTTING:
            selected_item = Tree1.selection()[0]
            for selected_item in Tree1.selection():
                conn = sqlite3.connect("DataBaseDir/PressDb.db")
                cur = conn.cursor()
                messageDelete = messagebox.askyesno(
                    "هشدار", "؟آیا میخواهید این داده را حذف کنید"
                )
                if messageDelete > 0:
                    cur.execute(
                        "DELETE FROM LaserTableCut WHERE O_CUT_TID=?",
                        (Tree1.set(selected_item, "#17"),),
                    )
                    conn.commit()
                    Tree1.delete(selected_item)
                conn.close()

    except:
        messagebox.showerror("اووووه", "عدم شناسایی ریکارد\nدرصورت موجودیت ریکارد لطفاً انتخاب نموده و بعد حذف کنید")



def EditingFunctionLaser():
    try:
        if OORDERTYPE.get() == O_3D:
            conn = sqlite3.connect("DataBaseDir/PressDb.db")
            cur1 = conn.cursor()
            selected_item = Tree1.selection()[0]
            for selected_item in Tree1.selection():
                LrQueryEdit = """
                SELECT
                OLENGTH,
                OWIDTH,
                OPRICE,
                OQUNTITY,
                OTEXT,
                OCURRENTTIME,
                OFINISHTIME,
                OCUSTOMERNAME,
                OCUSTOMERPHONE,
                OCUSTADDRESS,
                OPREPAY,
                ODELIVERYPRICE,
                ONOTE
                FROM LaserTable3D
                WHERE OTID=?
                """
                cur1.execute(
                    LrQueryEdit,
                    (Tree1.set(selected_item, "#17"),),
                )
                fetch1 = cur1.fetchall()
                for Row in fetch1:
                    data1 = Row[0]
                    data2 = Row[1]
                    data3 = Row[2]
                    data4 = Row[3]
                    data5 = Row[4]
                    data6 = Row[5]
                    data7 = Row[6]
                    data8 = Row[7]
                    data9 = Row[8]
                    data10 = Row[9]
                    data11 = Row[10]
                    data12 = Row[11]
                    data13 = Row[12]
                    OClear()
                    Order_MngEntry7.delete(0, END)
                    Order_MngEntry8.delete(0, END)

                    Order_MngEntry2.insert(0, data1)
                    Order_MngEntry3.insert(0, data2)
                    Order_MngEntry4.insert(0, data3)
                    Order_MngEntry5.insert(0, data4)
                    Order_MngEntry6.insert(0, data5)
                    Order_MngEntry7.insert(0, data6)
                    Order_MngEntry8.insert(0, data7)
                    Order_MngEntry9.insert(0, data8)
                    Order_MngEntry10.insert(0, data9)
                    Order_MngEntry11.insert(0, data10)
                    Order_MngEntry12.insert(0, data11)
                    Order_MngEntry13.insert(0, data12)
                    Order_MngEntry14.insert(0, data13)

            cur1.close()
            conn.close()
            Order_MngEntry2.focus()

        elif OORDERTYPE.get() == O_ENGRAVE:
            conn = sqlite3.connect("DataBaseDir/PressDb.db")
            cur1 = conn.cursor()
            selected_item = Tree1.selection()[0]
            for selected_item in Tree1.selection():
                LrQueryEdit = """
                SELECT
                O_ENGR_LENGTH,
                O_ENGR_WIDTH,
                O_ENGR_PRICE,
                O_ENGR_QUNTITY,
                O_ENGR_TEXT,
                O_ENGR_CURRENTTIME,
                O_ENGR_FINISHTIME,
                O_ENGR_CUSTOMERNAME,
                O_ENGR_CUSTOMERPHONE,
                O_ENGR_CUSTADDRESS,
                O_ENGR_PREPAY,
                O_ENGR_DELIVERYPRICE,
                O_ENGR_NOTE
                FROM LaserTableEngrave
                WHERE O_ENGR_TID=?
                """
                cur1.execute(
                    LrQueryEdit,
                    (Tree1.set(selected_item, "#17"),),
                )
                fetch1 = cur1.fetchall()
                for Row in fetch1:
                    data1 = Row[0]
                    data2 = Row[1]
                    data3 = Row[2]
                    data4 = Row[3]
                    data5 = Row[4]
                    data6 = Row[5]
                    data7 = Row[6]
                    data8 = Row[7]
                    data9 = Row[8]
                    data10 = Row[9]
                    data11 = Row[10]
                    data12 = Row[11]
                    data13 = Row[12]
                    OClear()
                    Order_MngEntry7.delete(0, END)
                    Order_MngEntry8.delete(0, END)

                    Order_MngEntry2.insert(0, data1)
                    Order_MngEntry3.insert(0, data2)
                    Order_MngEntry4.insert(0, data3)
                    Order_MngEntry5.insert(0, data4)
                    Order_MngEntry6.insert(0, data5)
                    Order_MngEntry7.insert(0, data6)
                    Order_MngEntry8.insert(0, data7)
                    Order_MngEntry9.insert(0, data8)
                    Order_MngEntry10.insert(0, data9)
                    Order_MngEntry11.insert(0, data10)
                    Order_MngEntry12.insert(0, data11)
                    Order_MngEntry13.insert(0, data12)
                    Order_MngEntry14.insert(0, data13)

            cur1.close()
            conn.close()
            Order_MngEntry2.focus()


        elif OORDERTYPE.get() == O_CUTTING:
            conn = sqlite3.connect("DataBaseDir/PressDb.db")
            cur1 = conn.cursor()
            selected_item = Tree1.selection()[0]
            for selected_item in Tree1.selection():
                LrQueryEdit = """
                SELECT
                O_CUT_LENGTH,
                O_CUT_WIDTH,
                O_CUT_PRICE,
                O_CUT_QUNTITY,
                O_CUT_TEXT,
                O_CUT_CURRENTTIME,
                O_CUT_FINISHTIME,
                O_CUT_CUSTOMERNAME,
                O_CUT_CUSTOMERPHONE,
                O_CUT_CUSTADDRESS,
                O_CUT_PREPAY,
                O_CUT_DELIVERYPRICE,
                O_CUT_NOTE
                FROM LaserTableCut
                WHERE O_CUT_TID=?
                """
                cur1.execute(
                    LrQueryEdit,
                    (Tree1.set(selected_item, "#17"),),
                )
                fetch1 = cur1.fetchall()
                for Row in fetch1:
                    data1 = Row[0]
                    data2 = Row[1]
                    data3 = Row[2]
                    data4 = Row[3]
                    data5 = Row[4]
                    data6 = Row[5]
                    data7 = Row[6]
                    data8 = Row[7]
                    data9 = Row[8]
                    data10 = Row[9]
                    data11 = Row[10]
                    data12 = Row[11]
                    data13 = Row[12]
                    OClear()
                    Order_MngEntry7.delete(0, END)
                    Order_MngEntry8.delete(0, END)

                    Order_MngEntry2.insert(0, data1)
                    Order_MngEntry3.insert(0, data2)
                    Order_MngEntry4.insert(0, data3)
                    Order_MngEntry5.insert(0, data4)
                    Order_MngEntry6.insert(0, data5)
                    Order_MngEntry7.insert(0, data6)
                    Order_MngEntry8.insert(0, data7)
                    Order_MngEntry9.insert(0, data8)
                    Order_MngEntry10.insert(0, data9)
                    Order_MngEntry11.insert(0, data10)
                    Order_MngEntry12.insert(0, data11)
                    Order_MngEntry13.insert(0, data12)
                    Order_MngEntry14.insert(0, data13)

            cur1.close()
            conn.close()
            Order_MngEntry2.focus()
        else:
            messagebox.showerror("اوووه", "هیچ فایلی انتخاب نشده")
    except:
        messagebox.showerror("اوووه", "ریکارد منتخب شناسایی نشد")



def SaveUpdateFuncLaser():
    if OORDERTYPE.get() == O_3D:
        if Order_MngEntry4.get() == "":
            messagebox.showerror("Space4", "مشکل در انتخاب ریکارد  یا عدم تعیین قیمت")
        else:
            dt2 = Order_MngEntry2.get()
            dt3 = Order_MngEntry3.get()
            dt4 = Order_MngEntry4.get()
            dt5 = Order_MngEntry5.get()
            dt6 = Order_MngEntry6.get()
            dt7 = Order_MngEntry7.get()
            dt8 = Order_MngEntry8.get()
            dt9 = Order_MngEntry9.get()
            dt10 = Order_MngEntry10.get()
            dt11 = Order_MngEntry11.get()
            dt12 = Order_MngEntry12.get()
            dt13 = Order_MngEntry13.get()
            dt14 = Order_MngEntry14.get()
            for selected_item in Tree1.selection():
                conn = sqlite3.connect("DataBaseDir/PressDb.db")
                cur = conn.cursor()
                UpdQueryL1 = """
                UPDATE LaserTable3D
                SET
                OLENGTH=?,
                OWIDTH=?,
                OPRICE=?,
                OQUNTITY=?,
                OTEXT=?,
                OCURRENTTIME=?,
                OFINISHTIME=?,
                OCUSTOMERNAME=?,
                OCUSTOMERPHONE=?,
                OCUSTADDRESS=?,
                OPREPAY=?,
                ODELIVERYPRICE=?,
                ONOTE=?
                WHERE OTID=?
                """
                cur.execute(
                    UpdQueryL1,
                    (
                        dt2,
                        dt3,
                        dt4,
                        dt5,
                        dt6,
                        dt7,
                        dt8,
                        dt9,
                        dt10,
                        dt11,
                        dt12,
                        dt13,
                        dt14,
                        Tree1.set(selected_item, "#17"),
                    ),
                )

                OClear()
                messagebox.showinfo("Space4 Software", "! آپدیت موفقانه انجام شد")
                conn.commit()
                conn.close()
                ORef()


    elif OORDERTYPE.get() == O_ENGRAVE:
        if Order_MngEntry4.get() == "":
            messagebox.showerror("Space4", "مشکل در انتخاب ریکارد  یا عدم تعیین قیمت")
        else:
            dt2 = Order_MngEntry2.get()
            dt3 = Order_MngEntry3.get()
            dt4 = Order_MngEntry4.get()
            dt5 = Order_MngEntry5.get()
            dt6 = Order_MngEntry6.get()
            dt7 = Order_MngEntry7.get()
            dt8 = Order_MngEntry8.get()
            dt9 = Order_MngEntry9.get()
            dt10 = Order_MngEntry10.get()
            dt11 = Order_MngEntry11.get()
            dt12 = Order_MngEntry12.get()
            dt13 = Order_MngEntry13.get()
            dt14 = Order_MngEntry14.get()
            for selected_item in Tree1.selection():
                conn = sqlite3.connect("DataBaseDir/PressDb.db")
                cur = conn.cursor()
                UpdQueryL2 = """
                UPDATE LaserTableEngrave
                SET
                O_ENGR_LENGTH=?,
                O_ENGR_WIDTH=?,
                O_ENGR_PRICE=?,
                O_ENGR_QUNTITY=?,
                O_ENGR_TEXT=?,
                O_ENGR_CURRENTTIME=?,
                O_ENGR_FINISHTIME=?,
                O_ENGR_CUSTOMERNAME=?,
                O_ENGR_CUSTOMERPHONE=?,
                O_ENGR_CUSTADDRESS=?,
                O_ENGR_PREPAY=?,
                O_ENGR_DELIVERYPRICE=?,
                O_ENGR_NOTE=?
                WHERE O_ENGR_TID=?
                """
                cur.execute(
                    UpdQueryL2,
                    (
                        dt2,
                        dt3,
                        dt4,
                        dt5,
                        dt6,
                        dt7,
                        dt8,
                        dt9,
                        dt10,
                        dt11,
                        dt12,
                        dt13,
                        dt14,
                        Tree1.set(selected_item, "#17"),
                    ),
                )

                OClear()
                messagebox.showinfo("Space4 Software", "! آپدیت موفقانه انجام شد")
                conn.commit()
                conn.close()
                ORef()


    elif OORDERTYPE.get() == O_CUTTING:
        if Order_MngEntry4.get() == "":
            messagebox.showerror("Space4", "مشکل در انتخاب ریکارد  یا عدم تعیین قیمت")
        else:
            dt2 = Order_MngEntry2.get()
            dt3 = Order_MngEntry3.get()
            dt4 = Order_MngEntry4.get()
            dt5 = Order_MngEntry5.get()
            dt6 = Order_MngEntry6.get()
            dt7 = Order_MngEntry7.get()
            dt8 = Order_MngEntry8.get()
            dt9 = Order_MngEntry9.get()
            dt10 = Order_MngEntry10.get()
            dt11 = Order_MngEntry11.get()
            dt12 = Order_MngEntry12.get()
            dt13 = Order_MngEntry13.get()
            dt14 = Order_MngEntry14.get()
            for selected_item in Tree1.selection():
                conn = sqlite3.connect("DataBaseDir/PressDb.db")
                cur = conn.cursor()
                UpdQueryL3 = """
                UPDATE LaserTableCut
                SET
                O_CUT_LENGTH=?,
                O_CUT_WIDTH=?,
                O_CUT_PRICE=?,
                O_CUT_QUNTITY=?,
                O_CUT_TEXT=?,
                O_CUT_CURRENTTIME=?,
                O_CUT_FINISHTIME=?,
                O_CUT_CUSTOMERNAME=?,
                O_CUT_CUSTOMERPHONE=?,
                O_CUT_CUSTADDRESS=?,
                O_CUT_PREPAY=?,
                O_CUT_DELIVERYPRICE=?,
                O_CUT_NOTE=?
                WHERE O_CUT_TID=?
                """
                cur.execute(
                    UpdQueryL3,
                    (
                        dt2,
                        dt3,
                        dt4,
                        dt5,
                        dt6,
                        dt7,
                        dt8,
                        dt9,
                        dt10,
                        dt11,
                        dt12,
                        dt13,
                        dt14,
                        Tree1.set(selected_item, "#17"),
                    ),
                )

                OClear()
                messagebox.showinfo("Space4 Software", "! آپدیت موفقانه انجام شد")
                conn.commit()
                conn.close()
                ORef()


def O_RadioFunc1():
    Order_MngLabel2.configure(text="M/طول",font=default_font_bold)
    Order_MngLabel3.configure(text="M/عرض",font=default_font_bold)
    Tree1.delete(*Tree1.get_children())
    Tree1Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    Tree1Cor = Tree1Conn.execute(
        """
        SELECT
        OUSAGE,
        OREFUND,
        ONOTE,
        ODELIVERYPRICE,
        OCUSTADDRESS,
        OCUSTOMERPHONE,
        OCUSTOMERNAME,
        OPREPAY,
        OPRICE,
        OFINISHTIME,
        OCURRENTTIME,
        OTEXT,
        OQUNTITY,
        OWIDTH,
        OLENGTH,
        OORDERTYPE,
        OTID
        FROM LaserTable3D
        """
    )
    fetchTree1 = Tree1Cor.fetchall()
    for dataTree1 in fetchTree1:
        Tree1.insert("", "end", values=(dataTree1))
    Tree1Cor.close()
    Tree1Conn.close()

    # ====== Separate Tree Refresh ==========
    Tree2.delete(*Tree2.get_children())
    Tree2Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    Tree2Cor = Tree2Conn.execute(
        """
        SELECT
        STL_DATE,
        STL_USAGE,
        STL_ADDR,
        STL_PHONE,
        STL_TTLPID,
        STL_NAME,
        STL_FINTIME,
        STL_TEXT,
        STL_QUNTITY,
        STL_SIZE,
        STL_ORDERTYPE
        FROM LSTTable
        """
    )
    fetchTree2 = Tree2Cor.fetchall()
    for dataTree2 in fetchTree2:
        Tree2.insert("", "end", values=(dataTree2))
    Tree2Cor.close()
    Tree2Conn.close()


def O_RadioFunc2():
    Order_MngLabel2.configure(text="cm/طول",font=default_font_bold)
    Order_MngLabel3.configure(text="cm/عرض",font=default_font_bold)
    Tree1.delete(*Tree1.get_children())
    Tree1Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    Tree1Cor = Tree1Conn.execute(
        """
        SELECT
        O_ENGR_USAGE,
        O_ENGR_REFUND,
        O_ENGR_NOTE,
        O_ENGR_DELIVERYPRICE,
        O_ENGR_CUSTADDRESS,
        O_ENGR_CUSTOMERPHONE,
        O_ENGR_CUSTOMERNAME,
        O_ENGR_PREPAY,
        O_ENGR_PRICE,
        O_ENGR_FINISHTIME,
        O_ENGR_CURRENTTIME,
        O_ENGR_TEXT,
        O_ENGR_QUNTITY,
        O_ENGR_WIDTH,
        O_ENGR_LENGTH,
        O_ENGR_ORDERTYPE,
        O_ENGR_TID
        FROM LaserTableEngrave
        """
    )
    fetchTree1 = Tree1Cor.fetchall()
    for dataTree1 in fetchTree1:
        Tree1.insert("", "end", values=(dataTree1))
    Tree1Cor.close()
    Tree1Conn.close()

    # ====== Separate Tree Refresh ==========
    Tree2.delete(*Tree2.get_children())
    Tree2Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    Tree2Cor = Tree2Conn.execute(
        """
        SELECT
        DONE_O_ENGR_DATE,
        DONE_O_ENGR_USAGE,
        DONE_O_ENGR_ADDR,
        DONE_O_ENGR_PHONE,
        DONE_O_ENGR_TTLPID,
        DONE_O_ENGR_NAME,
        DONE_O_ENGR_FINTIME,
        DONE_O_ENGR_TEXT,
        DONE_O_ENGR_QUNTITY,
        DONE_O_ENGR_SIZE,
        DONE_O_ENGR_ORDERTYPE
        FROM LaserTableEngraveDone
        """
    )
    fetchTree2 = Tree2Cor.fetchall()
    for dataTree2 in fetchTree2:
        Tree2.insert("", "end", values=(dataTree2))
    Tree2Cor.close()
    Tree2Conn.close()



def O_RadioFunc3():
    Order_MngLabel2.configure(text="M/طول",font=default_font_bold)
    Order_MngLabel3.configure(text="M/عرض",font=default_font_bold)
    Tree1.delete(*Tree1.get_children())
    Tree1Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    Tree1Cor = Tree1Conn.execute(
        """
        SELECT
        O_CUT_USAGE,
        O_CUT_REFUND,
        O_CUT_NOTE,
        O_CUT_DELIVERYPRICE,
        O_CUT_CUSTADDRESS,
        O_CUT_CUSTOMERPHONE,
        O_CUT_CUSTOMERNAME,
        O_CUT_PREPAY,
        O_CUT_PRICE,
        O_CUT_FINISHTIME,
        O_CUT_CURRENTTIME,
        O_CUT_TEXT,
        O_CUT_QUNTITY,
        O_CUT_WIDTH,
        O_CUT_LENGTH,
        O_CUT_ORDERTYPE,
        O_CUT_TID
        FROM LaserTableCut
        """
    )
    fetchTree1 = Tree1Cor.fetchall()
    for dataTree1 in fetchTree1:
        Tree1.insert("", "end", values=(dataTree1))
    Tree1Cor.close()
    Tree1Conn.close()

    #------------------------------------
    Tree2.delete(*Tree2.get_children())
    Tree2Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    Tree2Cor = Tree2Conn.execute(
        """
        SELECT
        DONE_O_CUT_DATE,
        DONE_O_CUT_USAGE,
        DONE_O_CUT_ADDR,
        DONE_O_CUT_PHONE,
        DONE_O_CUT_TTLPID,
        DONE_O_CUT_NAME,
        DONE_O_CUT_FINTIME,
        DONE_O_CUT_TEXT,
        DONE_O_CUT_QUNTITY,
        DONE_O_CUT_SIZE,
        DONE_O_CUT_ORDERTYPE
        FROM LaserTableCutDone
        """
    )
    fetchTree2 = Tree2Cor.fetchall()
    for dataTree2 in fetchTree2:
        Tree2.insert("", "end", values=(dataTree2))
    Tree2Cor.close()
    Tree2Conn.close()


#---------------- Display Price Tree1 -----------
def TtlPrcTree1Func():
    if OORDERTYPE.get() == O_3D:
        for selected_item in Tree1.selection():
            conn = sqlite3.connect("DataBaseDir/PressDb.db")
            cur = conn.cursor()
            Cur1 = cur.execute(
                """
                SELECT
                OCUSTOMERNAME,
                ((OLENGTH*OWIDTH)*(OQUNTITY)*(OPRICE)) AS SM0,
                (((OLENGTH*OWIDTH)*(OQUNTITY)*(OPRICE))-(OPREPAY+OREFUND)) AS SM1
                FROM LaserTable3D
                WHERE OTID=?
                """,
                (Tree1.set(selected_item, "#17"),),
            )
            fetchT1 = Cur1.fetchall()
            for T1Row in fetchT1:
                row0 = T1Row[0]
                row1 = T1Row[1]
                row2 = T1Row[2]
                messagebox.showinfo("Space4", f" سفارش دهنده: {row0}\n{row1} : قیمت کل\n{row2} : باقی حساب")
            conn.close()


    elif OORDERTYPE.get() == O_ENGRAVE:
        for selected_item in Tree1.selection():
            conn = sqlite3.connect("DataBaseDir/PressDb.db")
            cur = conn.cursor()
            Cur1 = cur.execute(
                """
                SELECT
                O_ENGR_CUSTOMERNAME,
                ((O_ENGR_LENGTH*O_ENGR_WIDTH)*(O_ENGR_QUNTITY)*(O_ENGR_PRICE)) AS SM0,
                (((O_ENGR_LENGTH*O_ENGR_WIDTH)*(O_ENGR_QUNTITY)*(O_ENGR_PRICE))-(O_ENGR_PREPAY+O_ENGR_REFUND)) AS SM1
                FROM LaserTableEngrave
                WHERE O_ENGR_TID=?
                """,
                (Tree1.set(selected_item, "#17"),),
            )
            fetchT1 = Cur1.fetchall()
            for T1Row in fetchT1:
                row0 = T1Row[0]
                row1 = T1Row[1]
                row2 = T1Row[2]
                messagebox.showinfo("Space4", f" سفارش دهنده: {row0}\n{row1} : قیمت کل\n{row2} : باقی حساب")
            conn.close()


    elif OORDERTYPE.get() == O_CUTTING:
        for selected_item in Tree1.selection():
            conn = sqlite3.connect("DataBaseDir/PressDb.db")
            cur = conn.cursor()
            Cur1 = cur.execute(
                """
                SELECT
                O_CUT_CUSTOMERNAME,
                ((O_CUT_LENGTH*O_CUT_WIDTH)*(O_CUT_QUNTITY)*(O_CUT_PRICE)) AS SM0,
                (((O_CUT_LENGTH*O_CUT_WIDTH)*(O_CUT_QUNTITY)*(O_CUT_PRICE))-(O_CUT_PREPAY+O_CUT_REFUND)) AS SM1
                FROM LaserTableCut
                WHERE O_CUT_TID=?
                """,
                (Tree1.set(selected_item, "#17"),),
            )
            fetchT1 = Cur1.fetchall()
            for T1Row in fetchT1:
                row0 = T1Row[0]
                row1 = T1Row[1]
                row2 = T1Row[2]
                messagebox.showinfo("Space4", f" سفارش دهنده: {row0}\n{row1} : قیمت کل\n{row2} : باقی حساب")
            conn.close()

#--------- ----------------------- ---------------------------- ---



# def Tree_RadioFunc1():
#     Tree1.delete(*Tree1.get_children())
#     Tree1Conn = sqlite3.connect("DataBaseDir/PressDb.db")
#     Tree1Cor = Tree1Conn.execute(
#         """
#         SELECT
#         OUSAGE,
#         OREFUND,
#         ONOTE,
#         ODELIVERYPRICE,
#         OCUSTADDRESS,
#         OCUSTOMERPHONE,
#         OCUSTOMERNAME,
#         OPREPAY,
#         OPRICE,
#         OFINISHTIME,
#         OCURRENTTIME,
#         OTEXT,
#         OQUNTITY,
#         OWIDTH,
#         OLENGTH,
#         OORDERTYPE,
#         OTID
#         FROM LaserTable3D
#         """
#     )
#     fetchTree1 = Tree1Cor.fetchall()
#     for dataTree1 in fetchTree1:
#         Tree1.insert("", "end", values=(dataTree1))
#     Tree1Cor.close()
#     Tree1Conn.close()


# def Tree_RadioFunc2():
#     Tree1.delete(*Tree1.get_children())
#     Tree1Conn = sqlite3.connect("DataBaseDir/PressDb.db")
#     Tree1Cor = Tree1Conn.execute(
#         """
#         SELECT
#         O_ENGR_USAGE,
#         O_ENGR_REFUND,
#         O_ENGR_NOTE,
#         O_ENGR_DELIVERYPRICE,
#         O_ENGR_CUSTADDRESS,
#         O_ENGR_CUSTOMERPHONE,
#         O_ENGR_CUSTOMERNAME,
#         O_ENGR_PREPAY,
#         O_ENGR_PRICE,
#         O_ENGR_FINISHTIME,
#         O_ENGR_CURRENTTIME,
#         O_ENGR_TEXT,
#         O_ENGR_QUNTITY,
#         O_ENGR_WIDTH,
#         O_ENGR_LENGTH,
#         O_ENGR_ORDERTYPE,
#         O_ENGR_TID
#         FROM LaserTableEngrave
#         """
#     )
#     fetchTree1 = Tree1Cor.fetchall()
#     for dataTree1 in fetchTree1:
#         Tree1.insert("", "end", values=(dataTree1))
#     Tree1Cor.close()
#     Tree1Conn.close()


# def Tree_RadioFunc3():
#     Tree1.delete(*Tree1.get_children())
#     Tree1Conn = sqlite3.connect("DataBaseDir/PressDb.db")
#     Tree1Cor = Tree1Conn.execute(
#         """
#         SELECT
#         O_CUT_USAGE,
#         O_CUT_REFUND,
#         O_CUT_NOTE,
#         O_CUT_DELIVERYPRICE,
#         O_CUT_CUSTADDRESS,
#         O_CUT_CUSTOMERPHONE,
#         O_CUT_CUSTOMERNAME,
#         O_CUT_PREPAY,
#         O_CUT_PRICE,
#         O_CUT_FINISHTIME,
#         O_CUT_CURRENTTIME,
#         O_CUT_TEXT,
#         O_CUT_QUNTITY,
#         O_CUT_WIDTH,
#         O_CUT_LENGTH,
#         O_CUT_ORDERTYPE,
#         O_CUT_TID
#         FROM LaserTableCut
#         """
#     )
#     fetchTree1 = Tree1Cor.fetchall()
#     for dataTree1 in fetchTree1:
#         Tree1.insert("", "end", values=(dataTree1))
#     Tree1Cor.close()
#     Tree1Conn.close()





# =========== Main Frames Opened ===========

MainFrame_BOT_L_T2 = ctk.CTkFrame(tab2_1)
MainFrame_BOT_L_T2.grid(row=0, column=0, padx=10, pady=10, sticky=NE)
MainFrame_CENTER_T2 = ctk.CTkFrame(tab2_1)
MainFrame_CENTER_T2.grid(row=0, column=1, padx=10, pady=10, sticky=NE)
MainFrame_BOT_R_T2 = ctk.CTkFrame(tab2_1)
MainFrame_BOT_R_T2.grid(row=1, column=0, padx=10, pady=10, sticky=NE, columnspan=2)

MainFrame_RIGHT_T2 = ctk.CTkFrame(MainFrame_BOT_R_T2)
MainFrame_RIGHT_T2.place(x=480, y=5)
MainFrame_BOTTOM_T2 = ctk.CTkFrame(MainFrame_BOT_R_T2)
MainFrame_BOTTOM_T2.place(x=5, y=5)
TreeViewBtnFrame1 = ctk.CTkFrame(MainFrame_BOT_R_T2, fg_color="#333333")
TreeViewBtnFrame1.place(x=880, y=5)# there is still nothing
# =========== Main Frames Closed ===========


# Order_MngLabel1 = ctk.CTkLabel(
#     MainFrame_CENTER_T2, text="نوع مواد", font=default_font_bold,
#     justify=RIGHT
# )
# Order_MngLabel1.grid(row=1, column=3, sticky=E, padx=10, pady=5)
Order_MngLabel2 = ctk.CTkLabel(
    MainFrame_CENTER_T2, text="M/طول", font=default_font_bold,
    justify=RIGHT
)
Order_MngLabel2.grid(row=2, column=3, sticky=E, padx=10, pady=5)
Order_MngLabel3 = ctk.CTkLabel(
    MainFrame_CENTER_T2, text="M/عرض", font=default_font_bold,
    justify=RIGHT
)
Order_MngLabel3.grid(row=3, column=3, sticky=E, padx=10, pady=5)
Order_MngLabel4 = ctk.CTkLabel(
    MainFrame_CENTER_T2, text="قیمت فی", font=default_font_bold,
    justify=RIGHT
)
Order_MngLabel4.grid(row=4, column=3, sticky=E, padx=10, pady=5)
Order_MngLabel5 = ctk.CTkLabel(
    MainFrame_CENTER_T2, text="تعداد", font=default_font_bold,
    justify=RIGHT
)
Order_MngLabel5.grid(row=5, column=3, sticky=E, padx=10, pady=5)
Order_MngLabel6 = ctk.CTkLabel(
    MainFrame_CENTER_T2, text="متن", font=default_font_bold,
    justify=RIGHT
)
Order_MngLabel6.grid(row=6, column=3, sticky=E, padx=10, pady=5)
Order_MngLabel7 = ctk.CTkLabel(
    MainFrame_CENTER_T2, text="تاریخ فعلی", font=default_font_bold,
    justify=RIGHT
)
Order_MngLabel7.grid(row=7, column=3, sticky=E, padx=10, pady=5)
Order_MngLabel8 = ctk.CTkLabel(
    MainFrame_CENTER_T2, text="تاریخ تحویل", font=default_font_bold,
    justify=RIGHT
)
Order_MngLabel8.grid(row=1, column=1, sticky=E, padx=10, pady=5)
Order_MngLabel9 = ctk.CTkLabel(
    MainFrame_CENTER_T2, text="نام مشتری", font=default_font_bold,
    justify=RIGHT
)
Order_MngLabel9.grid(row=2, column=1, sticky=E, padx=10, pady=5)
Order_MngLabel10 = ctk.CTkLabel(
    MainFrame_CENTER_T2, text="نمبر تماس", font=default_font_bold,
    justify=RIGHT
)
Order_MngLabel10.grid(row=3, column=1, sticky=E, padx=10, pady=5)
Order_MngLabel11 = ctk.CTkLabel(
    MainFrame_CENTER_T2, text="آدرس مشتری", font=default_font_bold,
    justify=RIGHT
)
Order_MngLabel11.grid(row=4, column=1, sticky=E, padx=10, pady=5)
Order_MngLabel12 = ctk.CTkLabel(
    MainFrame_CENTER_T2, text="پیش پرداخت", font=default_font_bold,
    justify=RIGHT
)
Order_MngLabel12.grid(row=5, column=1, sticky=E, padx=10, pady=5)
Order_MngLabel13 = ctk.CTkLabel(
    MainFrame_CENTER_T2, text="هزینه انتقال", font=default_font_bold,
    justify=RIGHT
)
Order_MngLabel13.grid(row=6, column=1, sticky=E, padx=10, pady=5)
Order_MngLabel14 = ctk.CTkLabel(
    MainFrame_CENTER_T2, text="نوت", font=default_font_bold,
    justify=RIGHT
)
Order_MngLabel14.grid(row=7, column=1, sticky=E, padx=10, pady=5)


#------ O Laser Radiobuttons -----------

O_3D = "برجسته"
O_ENGRAVE = "حکاکی"
O_CUTTING = "برش"

ORadioTypeFrame = ctk.CTkFrame(
    MainFrame_CENTER_T2,
    corner_radius=5
)
ORadioTypeFrame.grid(row=1, column=2, padx=10, sticky=E, columnspan=2)
#Radio Main Frame
ORadio1_1 = ctk.CTkRadioButton(
    ORadioTypeFrame,
    variable=OORDERTYPE,
    font=default_font_bold1,
    text="برجسته",
    width=20,
    hover_color=BGYELLOW,
    fg_color=BGORANGE,
    command=O_RadioFunc1,
    value=O_3D,
)
ORadio1_1.grid(row=0, column=0, sticky=E, padx=5)
ORadio1_2 = ctk.CTkRadioButton(
    ORadioTypeFrame,
    variable=OORDERTYPE,
    font=default_font_bold1,
    text="حکاکی",
    width=20,
    hover_color=BGYELLOW,
    fg_color=BGORANGE,
    command=O_RadioFunc2,
    value=O_ENGRAVE,
)
ORadio1_2.grid(row=0, column=1, sticky=E, padx=5)
ORadio1_3 = ctk.CTkRadioButton(
    ORadioTypeFrame,
    variable=OORDERTYPE,
    font=default_font_bold1,
    text="برش",
    width=20,
    hover_color=BGYELLOW,
    fg_color=BGORANGE,
    command=O_RadioFunc3,
    value=O_CUTTING,
)
ORadio1_3.grid(row=0, column=2, sticky=E, padx=5)



# ---------- O Entries and Date Entries -------------

# MatType = ["لوحه برجسته", "حکاکی", "برش مواد"]
# OORDERTYPE.set("انتخاب نوعیت")
# Order_MngEntry1 = ctk.CTkComboBox(
#     MainFrame_CENTER_T2,
#     width=140,
#     font=default_font_bold,
#     justify=RIGHT,
#     values=MatType,
#     variable=OORDERTYPE,
# )
# Order_MngEntry1.grid(row=1, column=2, sticky=E)

Order_MngEntry2 = ctk.CTkEntry(
    MainFrame_CENTER_T2,
    textvariable=OLENGTH,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
Order_MngEntry2.grid(row=2, column=2, sticky=E)
Order_MngEntry2.focus()
Order_MngEntry3 = ctk.CTkEntry(
    MainFrame_CENTER_T2,
    textvariable=OWIDTH,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
Order_MngEntry3.grid(row=3, column=2, sticky=E)
Order_MngEntry4 = ctk.CTkEntry(
    MainFrame_CENTER_T2,
    textvariable=OPRICE,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
Order_MngEntry4.grid(row=4, column=2, sticky=E)
Order_MngEntry5 = ctk.CTkEntry(
    MainFrame_CENTER_T2,
    textvariable=OQUNTITY,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
Order_MngEntry5.grid(row=5, column=2, sticky=E)
Order_MngEntry6 = ctk.CTkEntry(
    MainFrame_CENTER_T2,
    textvariable=OTEXT,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
Order_MngEntry6.grid(row=6, column=2, sticky=E)
Order_MngEntry7 = DateEntry(
    MainFrame_CENTER_T2,
    textvariable=OCURRENTTIME,
    font=("Arial", 10, "bold"),
    justify=RIGHT,
    width=14,
    date_pattern="yyyy-mm-dd",
)
Order_MngEntry7.grid(row=7, column=2, sticky=E)
Order_MngEntry8 = DateEntry(
    MainFrame_CENTER_T2,
    textvariable=OFINISHTIME,
    font=("Arial", 10, "bold"),
    justify=RIGHT,
    width=14,
    date_pattern="yyyy-mm-dd",
)
Order_MngEntry8.grid(row=1, column=0, sticky=E)
Order_MngEntry9 = ctk.CTkEntry(
    MainFrame_CENTER_T2,
    textvariable=OCUSTOMERNAME,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
Order_MngEntry9.grid(row=2, column=0, sticky=E)
Order_MngEntry10 = ctk.CTkEntry(
    MainFrame_CENTER_T2,
    textvariable=OCUSTOMERPHONE,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
Order_MngEntry10.grid(row=3, column=0, sticky=E)
Order_MngEntry11 = ctk.CTkEntry(
    MainFrame_CENTER_T2,
    textvariable=OCUSTADDRESS,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
Order_MngEntry11.grid(row=4, column=0, sticky=E)
Order_MngEntry12 = ctk.CTkEntry(
    MainFrame_CENTER_T2,
    textvariable=OPREPAY,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
Order_MngEntry12.grid(row=5, column=0, sticky=E)
Order_MngEntry13 = ctk.CTkEntry(
    MainFrame_CENTER_T2,
    textvariable=ODELIVERYPRICE,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
Order_MngEntry13.grid(row=6, column=0, sticky=E)
Order_MngEntry14 = ctk.CTkEntry(
    MainFrame_CENTER_T2,
    textvariable=ONOTE,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
Order_MngEntry14.grid(row=7, column=0, sticky=E)


# ------------ Refund --------------
RefundBtn1 = ctk.CTkButton(
    MainFrame_BOTTOM_T2,
    image=RefundImg,
    compound=RIGHT,
    hover_color=BTN_HOVER,
    # fg_color="#2B2B2B",
    font=default_font_bold,
    width=80,
    text="درج رسید",
    command=UpdateFunction,
)
RefundBtn1.grid(row=0, column=1, padx=10, pady=5, sticky=NE)

RefundEntry1 = ctk.CTkEntry(
    MainFrame_BOTTOM_T2, width=100, textvariable=OREFUND, justify=RIGHT
)
RefundEntry1.grid(row=0, column=0, padx=10, pady=5, sticky=NE)


# ------------ Usages --------------
UsageBtn1 = ctk.CTkButton(
    MainFrame_BOTTOM_T2,
    image=ReceiveImg,
    compound=RIGHT,
    hover_color=BTN_HOVER,
    # fg_color="#2B2B2B",
    font=default_font_bold,
    width=80,
    text="مصرف",
    command=ProjUsageFunc,
)
UsageBtn1.grid(row=0, column=3, padx=10, pady=5, sticky=NE)

UsageEntry1 = ctk.CTkEntry(
    MainFrame_BOTTOM_T2, width=100, textvariable=OUSAGE, justify=RIGHT
)
UsageEntry1.grid(row=0, column=2, padx=10, pady=5, sticky=NE)


# -------------------- Buttons Tab2 -------------------
SaveBtn1 = ctk.CTkButton(
    MainFrame_RIGHT_T2,
    text="ذخیره",
    font=default_font_bold2,
    compound=TOP,
    text_color=BGORANGE,
    image=SaveImg,
    hover_color=BTN_HOVER,
    width=20,
    fg_color="#333333",
    command=OSubmit,
)
SaveBtn1.grid(row=0, column=6, padx=5, pady=1)
UpdateBtnL1 = ctk.CTkButton(
    MainFrame_RIGHT_T2,
    text="Update",
    font=default_font_bold2,
    compound=TOP,
    text_color=BGORANGE,
    image=UpdateImg,
    hover_color=BTN_HOVER,
    width=20,
    fg_color="#333333",
    command=SaveUpdateFuncLaser,
)
UpdateBtnL1.grid(row=0, column=5, padx=5, pady=1)
ClearBtn1 = ctk.CTkButton(
    MainFrame_RIGHT_T2,
    text="پاک کردن",
    font=default_font_bold2,
    compound=TOP,
    text_color=BGORANGE,
    image=ClearImg,
    hover_color=BTN_HOVER,
    width=20,
    fg_color="#333333",
    command=OClear,
)
ClearBtn1.grid(row=0, column=4, padx=5, pady=1)
EditBtn1 = ctk.CTkButton(
    MainFrame_RIGHT_T2,
    text="ویرایش",
    font=default_font_bold2,
    compound=TOP,
    text_color=BGORANGE,
    image=EditImg,
    hover_color=BTN_HOVER,
    width=20,
    fg_color="#333333",
    command=EditingFunctionLaser,
)
EditBtn1.grid(row=0, column=3, padx=5, pady=1)
BillGenBtn1 = ctk.CTkButton(
    MainFrame_RIGHT_T2,
    text="صدور بل",
    font=default_font_bold2,
    compound=TOP,
    text_color=BGORANGE,
    image=PrintImg,
    hover_color=BTN_HOVER,
    width=20,
    fg_color="#333333",
)
BillGenBtn1.grid(row=0, column=2, padx=5, pady=1)
RefreshBtn1 = ctk.CTkButton(
    MainFrame_RIGHT_T2,
    text="تجدید",
    font=default_font_bold2,
    compound=TOP,
    text_color=BGORANGE,
    image=RefreshImg,
    hover_color=BTN_HOVER,
    width=20,
    fg_color="#333333",
    command=ORef,
)
RefreshBtn1.grid(row=0, column=1, padx=5, pady=1)
DeleteBtn1 = ctk.CTkButton(
    MainFrame_RIGHT_T2,
    text="حذف",
    font=default_font_bold2,
    compound=TOP,
    text_color=BGORANGE,
    image=DeleteImg,
    hover_color=BTN_HOVER,
    width=20,
    fg_color="#333333",
    command=ODelete,
)
DeleteBtn1.grid(row=0, column=0, padx=5, pady=1)




# -------------- TreeView Right Title Name --------------
TreeVTitle1 = ctk.CTkLabel(
    MainFrame_BOT_R_T2,
    text=":اولویت",
    font=default_font_bold,
    text_color=(
        "teal",
        "orange"
    ),
    justify=RIGHT
)
TreeVTitle1.grid(row=0, column=0, sticky=E, padx=10, pady=12)
#----------- Display Change Buttons-------------

# DispTypeVar = StringVar()
# TreeRadio_1 = ctk.CTkRadioButton(
#     TreeViewBtnFrame1,
#     variable=DispTypeVar,
#     font=default_font_bold2,
#     text="برجسته",
#     width=20,
#     hover_color=BGYELLOW,
#     fg_color=BGORANGE,
#     command=Tree_RadioFunc1,
# )
# TreeRadio_1.grid(row=0, column=0, sticky=E, padx=5)
# TreeRadio_2 = ctk.CTkRadioButton(
#     TreeViewBtnFrame1,
#     variable=DispTypeVar,
#     font=default_font_bold2,
#     text="حکاکی",
#     width=20,
#     hover_color=BGYELLOW,
#     fg_color=BGORANGE,
#     command=Tree_RadioFunc2,
# )
# TreeRadio_2.grid(row=0, column=1, sticky=E, padx=5)
# TreeRadio_3 = ctk.CTkRadioButton(
#     TreeViewBtnFrame1,
#     variable=DispTypeVar,
#     font=default_font_bold2,
#     text="برش",
#     width=20,
#     hover_color=BGYELLOW,
#     fg_color=BGORANGE,
#     command=Tree_RadioFunc3,
# )
# TreeRadio_3.grid(row=0, column=2, sticky=E, padx=5)


#
#------ Sum Price Tree1
SumPriceTree1Label = ctk.CTkLabel(
    master=MainFrame_BOT_R_T2,
    text="Nothing yet :)",
    text_color=BGYELLOW,
    font=default_font_bold
)
SumPriceTree1Label.place(x=930, y=10)

#----- TreeViews ----------


Tree1Frame = ctk.CTkFrame(MainFrame_BOT_R_T2)
Tree1Frame.grid(row=1, column=0, padx=5, sticky=W)
Tree1 = ttk.Treeview(
    Tree1Frame,
    columns=(
        "L1",
        "L2",
        "L3",
        "L4",
        "L5",
        "L6",
        "L7",
        "L8",
        "L9",
        "L10",
        "L11",
        "L12",
        "L13",
        "L14",
        "L15",
        "L16",
        "L17",
    ),
    selectmode="extended",
    height=7,
)
Tree1.heading("L17", text="آیدی", anchor=E)
Tree1.heading("L16", text="نوعیت", anchor=E)
Tree1.heading("L15", text="طول", anchor=E)
Tree1.heading("L14", text="عرض", anchor=E)
Tree1.heading("L13", text="تعداد", anchor=E)
Tree1.heading("L12", text="متن", anchor=E)
Tree1.heading("L11", text="گرفت", anchor=E)
Tree1.heading("L10", text="تحویل", anchor=E)
Tree1.heading("L9", text="قیمت فی", anchor=E)
Tree1.heading("L8", text="بیانیه", anchor=E)
Tree1.heading("L7", text="نام مشتری", anchor=E)
Tree1.heading("L6", text="تلفن", anchor=E)
Tree1.heading("L5", text="آدرس", anchor=E)
Tree1.heading("L4", text="دلیوری", anchor=E)
Tree1.heading("L3", text="نوت", anchor=E)
Tree1.heading("L2", text="رسید", anchor=E)
Tree1.heading("L1", text="مصرف", anchor=E)


Tree1.column("#0", stretch=NO, minwidth=0, width=0, anchor=E)
Tree1.column("#1", stretch=NO, minwidth=0, width=60, anchor=E)
Tree1.column("#2", stretch=NO, minwidth=0, width=70, anchor=E)
Tree1.column("#3", stretch=NO, minwidth=0, width=60, anchor=E)
Tree1.column("#4", stretch=NO, minwidth=0, width=70, anchor=E)
Tree1.column("#5", stretch=NO, minwidth=0, width=70, anchor=E)
Tree1.column("#6", stretch=NO, minwidth=0, width=70, anchor=E)
Tree1.column("#7", stretch=NO, minwidth=0, width=70, anchor=E)
Tree1.column("#8", stretch=NO, minwidth=0, width=70, anchor=E)
Tree1.column("#9", stretch=NO, minwidth=0, width=60, anchor=E)
Tree1.column("#10", stretch=NO, minwidth=0, width=80, anchor=E)
Tree1.column("#11", stretch=NO, minwidth=0, width=80, anchor=E)
Tree1.column("#12", stretch=NO, minwidth=0, width=50, anchor=E)
Tree1.column("#13", stretch=NO, minwidth=0, width=50, anchor=E)
Tree1.column("#14", stretch=NO, minwidth=0, width=50, anchor=E)
Tree1.column("#15", stretch=NO, minwidth=0, width=50, anchor=E)
Tree1.column("#16", stretch=NO, minwidth=0, width=80, anchor=E)
Tree1.column("#17", stretch=NO, minwidth=0, width=50, anchor=E)
Tree1.grid()


# Tree1.delete(*Tree1.get_children())
# Tree1Conn = sqlite3.connect("DataBaseDir/PressDb.db")
# Tree1Cor = Tree1Conn.execute(
#     "SELECT OUSAGE,OREFUND,ONOTE,ODELIVERYPRICE,OCUSTADDRESS,\
#         OCUSTOMERPHONE,OCUSTOMERNAME,OPREPAY,OPRICE,OFINISHTIME,OCURRENTTIME,OTEXT,\
#         OQUNTITY,OWIDTH,OLENGTH,OORDERTYPE,OTID FROM LaserTable3D"
# )
# fetchTree1 = Tree1Cor.fetchall()
# for dataTree1 in fetchTree1:
#     Tree1.insert("", "end", values=(dataTree1))
# Tree1Cor.close()
# Tree1Conn.close()


#============= View Sum Popup =============
def ViewSumPopFuncTree1(event):
    try:
        selectedRowT1 = Tree1.selection()[0]
        Tree1PopMenu = Menu(
            master=Tree1,
            tearoff=0,
            font=default_font_bold1,
            bg=CTKDARK,
            fg=CTKLIGHT,
            activebackground=BGORANGE,
        )
        Tree1PopMenu.add_command(
            compound=LEFT,
            image=ShowImg_1,
            label="مشاهده قیمت",
            command=TtlPrcTree1Func
        )
        Tree1PopMenu.add_command(
            compound=LEFT,
            image=DeleteImg_1,
            label="حذف",
            command=ODelete
        )
        Tree1PopMenu.add_command(
            compound=LEFT,
            image=RefreshImg_1,
            label="تجدید",
            command=ORef
        )
        Tree1PopMenu.add_command(
            compound=LEFT,
            image=EditImg_1,
            label="ویرایش",
            command=EditingFunctionLaser
        )
        Tree1PopMenu.add_command(
            compound=LEFT,
            image=UpdateImg_1,
            label="ذخیره تغییرات",
            command=SaveUpdateFuncLaser
            )
        try:
            Tree1PopMenu.tk_popup(event.x_root, event.y_root)
        finally:
            Tree1PopMenu.grab_release()
    except:
        messagebox.showinfo("اوووه", "! ریکارد را انتخاب کنید لطفاً")


Tree1.bind("<Button-3>", ViewSumPopFuncTree1)

# -------------- TreeView Left Title Name --------------
TreeVTitle2 = ctk.CTkLabel(
    MainFrame_BOT_L_T2,
    text="تصفیه شده",
    font=default_font_bold,
    text_color=("teal", "orange"),
    justify=RIGHT,
)
TreeVTitle2.grid(row=0, column=0, sticky=E, padx=10, pady=10)


Tree2Frame = ctk.CTkFrame(MainFrame_BOT_L_T2)
Tree2Frame.grid(row=1, column=0, padx=5, sticky=W)
Tree2 = ttk.Treeview(
    Tree2Frame,
    columns=(
        "OL1",
        "OL2",
        "OL3",
        "OL4",
        "OL5",
        "OL6",
        "OL7",
        "OL8",
        "OL9",
        "OL10",
        "OL11",
    ),
    selectmode="browse",
    height=7,
)
Tree2.heading("OL11", text="نوعیت", anchor=E)
Tree2.heading("OL10", text="اندازه", anchor=E)
Tree2.heading("OL9", text="تعداد", anchor=E)
Tree2.heading("OL8", text="متن", anchor=E)
Tree2.heading("OL7", text="تحویل", anchor=E)
Tree2.heading("OL6", text="نام", anchor=E)
Tree2.heading("OL5", text="قیمت", anchor=E)
Tree2.heading("OL4", text="تلفن", anchor=E)
Tree2.heading("OL3", text="آدرس", anchor=E)
Tree2.heading("OL2", text="مصرف", anchor=E)
Tree2.heading("OL1", text="تاریخ", anchor=E)

Tree2.column("#0", stretch=NO, minwidth=0, anchor=E, width=0)
Tree2.column("#1", stretch=NO, minwidth=0, anchor=E, width=50)
Tree2.column("#2", stretch=NO, minwidth=0, anchor=E, width=50)
Tree2.column("#3", stretch=NO, minwidth=0, anchor=E, width=50)
Tree2.column("#4", stretch=NO, minwidth=0, anchor=E, width=50)
Tree2.column("#5", stretch=NO, minwidth=0, anchor=E, width=50)
Tree2.column("#6", stretch=NO, minwidth=0, anchor=E, width=50)
Tree2.column("#7", stretch=NO, minwidth=0, anchor=E, width=50)
Tree2.column("#8", stretch=NO, minwidth=0, anchor=E, width=50)
Tree2.column("#9", stretch=NO, minwidth=0, anchor=E, width=50)
Tree2.column("#10", stretch=NO, minwidth=0, anchor=E, width=50)
Tree2.column("#11", stretch=NO, minwidth=0, anchor=E, width=50)
Tree2.grid()


# Tree2.delete(*Tree2.get_children())
# Tree2Conn = sqlite3.connect("DataBaseDir/PressDb.db")
# Tree2Cor = Tree2Conn.execute(
#     """
#     SELECT
#     STL_DATE,
#     STL_USAGE,
#     STL_ADDR,
#     STL_PHONE,
#     STL_TTLPID,
#     STL_NAME,
#     STL_FINTIME,
#     STL_TEXT,
#     STL_QUNTITY,
#     STL_SIZE,
#     STL_ORDERTYPE
#     FROM LSTTable
#     """
# )
# fetchTree2 = Tree2Cor.fetchall()
# for dataTree2 in fetchTree2:
#     Tree2.insert("", "end", values=(dataTree2))
# Tree2Cor.close()
# Tree2Conn.close()


# ============= Digital Part all options ===================

DORDERTYPE = StringVar()
DLENGTH = StringVar()
DWIDTH = StringVar()
DQUNTITY = StringVar()
DMATERIALTYPE = StringVar()
DTEXT = StringVar()
DINSERTFILE = StringVar()
DCURRENTTIME = StringVar()
DFINISHTIME = StringVar()
DPRICE = StringVar()
DPREPAY = StringVar()
DCUSTOMERNAME = StringVar()
DCUSTOMERPHONE = StringVar()
DCUSTADDRESS = StringVar()
DDELIVERYPRICE = StringVar()
DNOTE = StringVar()


def DSubmit():
    DConn1 = sqlite3.connect("DataBaseDir/PressDb.db")
    Dcur1 = DConn1.cursor()
    if D_MngEntry10.get() == "" or D_MngEntry12.get() == "" or D_MngEntry13.get() == "":
        messagebox.showwarning("ببخشید", "الزامی است که ورودی ها قبل از ذخیره پر شود.")
    else:
        Dcur1.execute(
            f"""
            insert into DigitalTable (
            DORDERTYPE,
            DLENGTH,
            DWIDTH,
            DQUNTITY,
            DMATERIALTYPE,
            DTEXT,
            DCURRENTTIME,
            DFINISHTIME,
            DPRICE,
            DPREPAY,
            DCUSTOMERNAME,
            DCUSTOMERPHONE,
            DCUSTADDRESS,
            DDELIVERYPRICE,
            DNOTE
            )
            values (
            '{DORDERTYPE.get()}',
            '{DLENGTH.get()}',
            '{DWIDTH.get()}',
            '{DQUNTITY.get()}',
            '{DMATERIALTYPE.get()}',
            '{DTEXT.get()}',
            '{DCURRENTTIME.get()}',
            '{DFINISHTIME.get()}',
            '{DPRICE.get()}',
            '{DPREPAY.get()}',
            '{DCUSTOMERNAME.get()}',
            '{DCUSTOMERPHONE.get()}',
            '{DCUSTADDRESS.get()}',
            '{DDELIVERYPRICE.get()}',
            '{DNOTE.get()}')
            """
        )

    DConn1.commit()
    DConn1.close()

    D_MngEntry2.delete(0, END)
    D_MngEntry3.delete(0, END)
    D_MngEntry4.delete(0, END)
    D_MngEntry6.delete(0, END)
    D_MngEntry9.delete(0, END)
    D_MngEntry10.delete(0, END)
    D_MngEntry11.delete(0, END)
    D_MngEntry12.delete(0, END)
    D_MngEntry13.delete(0, END)
    D_MngEntry14.delete(0, END)
    D_MngEntry1.focus()
    DRef()


def DClear():
    D_MngEntry2.delete(0, END)
    D_MngEntry3.delete(0, END)
    D_MngEntry4.delete(0, END)
    D_MngEntry5.delete(0, END)
    D_MngEntry6.delete(0, END)
    D_MngEntry9.delete(0, END)
    D_MngEntry10.delete(0, END)
    D_MngEntry11.delete(0, END)
    D_MngEntry12.delete(0, END)
    D_MngEntry13.delete(0, END)
    D_MngEntry14.delete(0, END)
    D_MngEntry1.focus()


def DRef():
    DTree1.delete(*DTree1.get_children())
    DTree1Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    """
    DTree1Cor = DTree1Conn.execute("SELECT OTID,ONOTE,ODELIVERYPRICE,OCUSTADDRESS,OCUSTOMERPHONE,OCUSTOMERNAME,OPREPAY,OPRICE,\
    OFINISHTIME,OCURRENTTIME,OINSERTFILE,OTEXT,OMATERIALTYPE,OQUNTITY,OWIDTH,OLENGTH,OORDERTYPE FROM OrdersTable")"""
    DTree1Cor = DTree1Conn.execute(
        "SELECT DCUSTOMERPHONE,DCUSTOMERNAME,DPRICE,\
        DFINISHTIME,DPREPAY,DQUNTITY,DCUSTADDRESS,DORDERTYPE FROM DigitalTable"
    )

    fetchDTree1 = DTree1Cor.fetchall()
    for dataDTree1 in fetchDTree1:
        DTree1.insert("", "end", values=(dataDTree1))
    DTree1Cor.close()
    DTree1Conn.close()


def DDelete():
    selected_item = DTree1.selection()[0]
    for selected_item in DTree1.selection():
        conn = sqlite3.connect("DataBaseDir/PressDb.db")
        cur = conn.cursor()
        messageDelete = messagebox.askyesno(
            "هشدار", "؟آیا میخواهید این داده را حذف کنید"
        )
        if messageDelete > 0:
            cur.execute(
                "DELETE FROM DigitalTable WHERE DCUSTOMERPHONE=?",
                (DTree1.set(selected_item, "#1"),),
            )
        conn.commit()
        DTree1.delete(selected_item)
        conn.close()


# =========== Main Frames Opened ===========

DMainFrame_BOT_R_T2 = ctk.CTkFrame(tab2_2)
DMainFrame_BOT_R_T2.grid(row=0, column=0, padx=10, pady=10, sticky=NE)
DMainFrame_BOT_L_T2 = ctk.CTkFrame(tab2_2)
DMainFrame_BOT_L_T2.grid(row=1, column=0, padx=10, pady=10, sticky=NE)

DMainFrame_CENTER_T2 = ctk.CTkFrame(tab2_2)
DMainFrame_CENTER_T2.grid(row=0, column=1, padx=10, pady=10, sticky=NE)
DMainFrame_RIGHT_T2 = ctk.CTkFrame(tab2_2)
DMainFrame_RIGHT_T2.grid(row=1, column=1, padx=10, pady=10, sticky=NE)
# =========== Main Frames Closed ===========


D_MngLabel1 = ctk.CTkLabel(
    DMainFrame_CENTER_T2,
    text="نوع مواد",
    font=default_font_bold,
    justify=RIGHT
)
D_MngLabel1.grid(row=1, column=3, sticky=E, padx=10, pady=5)
D_MngLabel2 = ctk.CTkLabel(
    DMainFrame_CENTER_T2,
    text="M/طول",
    font=default_font_bold,
    justify=RIGHT
)
D_MngLabel2.grid(row=2, column=3, sticky=E, padx=10, pady=5)
D_MngLabel3 = ctk.CTkLabel(
    DMainFrame_CENTER_T2,
    text="M/عرض",
    font=default_font_bold,
    justify=RIGHT
)
D_MngLabel3.grid(row=3, column=3, sticky=E, padx=10, pady=5)
D_MngLabel4 = ctk.CTkLabel(
    DMainFrame_CENTER_T2,
    text="قیمت فی",
    font=default_font_bold,
    justify=RIGHT
)
D_MngLabel4.grid(row=4, column=3, sticky=E, padx=10, pady=5)
D_MngLabel5 = ctk.CTkLabel(
    DMainFrame_CENTER_T2,
    text="تعداد",
    font=default_font_bold,
    justify=RIGHT
)
D_MngLabel5.grid(row=5, column=3, sticky=E, padx=10, pady=5)
D_MngLabel6 = ctk.CTkLabel(
    DMainFrame_CENTER_T2,
    text="متن",
    font=default_font_bold,
    justify=RIGHT
)
D_MngLabel6.grid(row=6, column=3, sticky=E, padx=10, pady=5)
D_MngLabel7 = ctk.CTkLabel(
    DMainFrame_CENTER_T2,
    text="تاریخ فعلی",
    font=default_font_bold,
    justify=RIGHT
)
D_MngLabel7.grid(row=7, column=3, sticky=E, padx=10, pady=5)
D_MngLabel8 = ctk.CTkLabel(
    DMainFrame_CENTER_T2,
    text="تاریخ تحویل",
    font=default_font_bold,
    justify=RIGHT
)
D_MngLabel8.grid(row=1, column=1, sticky=E, padx=10, pady=5)
D_MngLabel9 = ctk.CTkLabel(
    DMainFrame_CENTER_T2,
    text="نام مشتری",
    font=default_font_bold,
    justify=RIGHT
)
D_MngLabel9.grid(row=2, column=1, sticky=E, padx=10, pady=5)
D_MngLabel10 = ctk.CTkLabel(
    DMainFrame_CENTER_T2,
    text="نمبر تماس",
    font=default_font_bold,
    justify=RIGHT
)
D_MngLabel10.grid(row=3, column=1, sticky=E, padx=10, pady=5)
D_MngLabel11 = ctk.CTkLabel(
    DMainFrame_CENTER_T2,
    text="آدرس مشتری",
    font=default_font_bold,
    justify=RIGHT
)
D_MngLabel11.grid(row=4, column=1, sticky=E, padx=10, pady=5)
D_MngLabel12 = ctk.CTkLabel(
    DMainFrame_CENTER_T2,
    text="پیش پرداخت",
    font=default_font_bold,
    justify=RIGHT
)
D_MngLabel12.grid(row=5, column=1, sticky=E, padx=10, pady=5)
D_MngLabel13 = ctk.CTkLabel(
    DMainFrame_CENTER_T2,
    text="هزینه انتقال",
    font=default_font_bold,
    justify=RIGHT
)
D_MngLabel13.grid(row=6, column=1, sticky=E, padx=10, pady=5)
D_MngLabel14 = ctk.CTkLabel(
    DMainFrame_CENTER_T2,
    text="نوت",
    font=default_font_bold,
    justify=RIGHT
)
D_MngLabel14.grid(row=7, column=1, sticky=E, padx=10, pady=5)


MatType = ["لوحه برجسته", "حکاکی", "برش مواد"]
DORDERTYPE.set("انتخاب نوعیت")
D_MngEntry1 = ctk.CTkComboBox(
    DMainFrame_CENTER_T2,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
    values=MatType,
    variable=DORDERTYPE,
)
D_MngEntry1.grid(row=1, column=2, sticky=E)
D_MngEntry1.focus()
D_MngEntry2 = ctk.CTkEntry(
    DMainFrame_CENTER_T2,
    textvariable=DLENGTH,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
D_MngEntry2.grid(row=2, column=2, sticky=E)
D_MngEntry3 = ctk.CTkEntry(
    DMainFrame_CENTER_T2,
    textvariable=DWIDTH,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
D_MngEntry3.grid(row=3, column=2, sticky=E)
D_MngEntry4 = ctk.CTkEntry(
    DMainFrame_CENTER_T2,
    textvariable=DPRICE,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
D_MngEntry4.grid(row=4, column=2, sticky=E)
D_MngEntry5 = ctk.CTkEntry(
    DMainFrame_CENTER_T2,
    textvariable=DQUNTITY,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
D_MngEntry5.grid(row=5, column=2, sticky=E)
D_MngEntry6 = ctk.CTkEntry(
    DMainFrame_CENTER_T2,
    textvariable=DTEXT,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
D_MngEntry6.grid(row=6, column=2, sticky=E)
D_MngEntry7 = DateEntry(
    DMainFrame_CENTER_T2,
    textvariable=DCURRENTTIME,
    font=("Arial", 10, "bold"),
    justify=RIGHT,
    width=15,
    date_pattern="yyyy-mm-dd",
)
D_MngEntry7.grid(row=7, column=2, sticky=E)
D_MngEntry8 = DateEntry(
    DMainFrame_CENTER_T2,
    textvariable=DFINISHTIME,
    font=("Arial", 10, "bold"),
    justify=RIGHT,
    width=15,
    date_pattern="yyyy-mm-dd",
)
D_MngEntry8.grid(row=1, column=0, sticky=E)
D_MngEntry9 = ctk.CTkEntry(
    DMainFrame_CENTER_T2,
    textvariable=DCUSTOMERNAME,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
D_MngEntry9.grid(row=2, column=0, sticky=E)
D_MngEntry10 = ctk.CTkEntry(
    DMainFrame_CENTER_T2,
    textvariable=DCUSTOMERPHONE,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
D_MngEntry10.grid(row=3, column=0, sticky=E)
D_MngEntry11 = ctk.CTkEntry(
    DMainFrame_CENTER_T2,
    textvariable=DCUSTADDRESS,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
D_MngEntry11.grid(row=4, column=0, sticky=E)
D_MngEntry12 = ctk.CTkEntry(
    DMainFrame_CENTER_T2,
    textvariable=DPREPAY,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
D_MngEntry12.grid(row=5, column=0, sticky=E)
D_MngEntry13 = ctk.CTkEntry(
    DMainFrame_CENTER_T2,
    textvariable=DDELIVERYPRICE,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
D_MngEntry13.grid(row=6, column=0, sticky=E)
D_MngEntry14 = ctk.CTkEntry(
    DMainFrame_CENTER_T2,
    textvariable=DNOTE,
    width=140,
    font=default_font_bold,
    justify=RIGHT,
)
D_MngEntry14.grid(row=7, column=0, sticky=E)


# -------------------- Buttons Tab2 -------------------
DSaveBtn1 = ctk.CTkButton(
    DMainFrame_RIGHT_T2,
    fg_color="#333333",
    compound=TOP,
    hover_color=BTN_HOVER,
    text="ذخیره",
    image=SaveImg,
    width=60,
    font=default_font_bold,
    command=DSubmit,
)
DSaveBtn1.grid(row=0, column=5, padx=5, pady=10)
DClearBtn1 = ctk.CTkButton(
    DMainFrame_RIGHT_T2,
    fg_color="#333333",
    compound=TOP,
    hover_color=BTN_HOVER,
    text="پاک کردن",
    image=ClearImg,
    width=70,
    font=default_font_bold,
    command=DClear,
)
DClearBtn1.grid(row=0, column=4, padx=5, pady=10)
DEditBtn1 = ctk.CTkButton(
    DMainFrame_RIGHT_T2,
    fg_color="#333333",
    compound=TOP,
    hover_color=BTN_HOVER,
    text="ویرایش",
    image=EditImg,
    width=70,
    font=default_font_bold,
)
DEditBtn1.grid(row=0, column=3, padx=5, pady=10)
DBillGenBtn1 = ctk.CTkButton(
    DMainFrame_RIGHT_T2,
    fg_color="#333333",
    compound=TOP,
    hover_color=BTN_HOVER,
    text="صدور بل",
    image=PrintImg,
    width=70,
    font=default_font_bold,
)
DBillGenBtn1.grid(row=0, column=2, padx=5, pady=10)
DRefreshBtn1 = ctk.CTkButton(
    DMainFrame_RIGHT_T2,
    fg_color="#333333",
    compound=TOP,
    hover_color=BTN_HOVER,
    text="تجدید ",
    image=RefreshImg,
    width=70,
    font=default_font_bold,
    command=DRef,
)
DRefreshBtn1.grid(row=0, column=1, padx=5, pady=10)
DDeleteBtn1 = ctk.CTkButton(
    DMainFrame_RIGHT_T2,
    fg_color="#333333",
    compound=TOP,
    hover_color=BTN_HOVER,
    text="حذف",
    image=DeleteImg,
    width=70,
    font=default_font_bold,
    command=DDelete,
)
DDeleteBtn1.grid(row=0, column=0, padx=5, pady=10)


# -------------- TreeView Right Title Name --------------
DTreeVTitle1 = ctk.CTkLabel(
    DMainFrame_BOT_R_T2,
    text="اولویت پروژه های دیجیتل",
    font=default_font_bold,
    text_color=("teal", "orange"),
    justify=RIGHT,
)
DTreeVTitle1.grid(row=0, column=0, sticky=E, padx=10, pady=10)

DTree1Frame = ctk.CTkFrame(DMainFrame_BOT_R_T2)
DTree1Frame.grid(row=1, column=0, padx=5, sticky=W)
DTree1 = ttk.Treeview(
    DTree1Frame,
    columns=(
        "L1",
        "L2",
        "L3",
        "L4",
        "L5",
        "L6",
        "L7",
        "L8",
        "L9",
        "L10",
        "L11",
        "L12",
        "L13",
        "L14",
        "L15",
        "L16",
    ),
    selectmode="browse",
    height=7,
)

DTree1.heading("L16", text="آیدی", anchor=E)
DTree1.heading("L15", text="نوعیت", anchor=E)
DTree1.heading("L14", text="طول", anchor=E)
DTree1.heading("L13", text="عرض", anchor=E)
DTree1.heading("L12", text="تعداد", anchor=E)
DTree1.heading("L11", text="متن", anchor=E)
DTree1.heading("L10", text="گرفت", anchor=E)
DTree1.heading("L9", text="تحویل", anchor=E)
DTree1.heading("L8", text="قیمت فی", anchor=E)
DTree1.heading("L7", text="پیش پرداخت", anchor=E)
DTree1.heading("L6", text="نام مشتری", anchor=E)
DTree1.heading("L5", text="تلفن", anchor=E)
DTree1.heading("L4", text="آدرس", anchor=E)
DTree1.heading("L3", text="دلیوری", anchor=E)
DTree1.heading("L2", text="نوت", anchor=E)
DTree1.heading("L1", text="رسید", anchor=E)


DTree1.column("#0", stretch=NO, minwidth=0, width=0, anchor=E)
DTree1.column("#1", stretch=NO, minwidth=0, width=30, anchor=E)
DTree1.column("#2", stretch=NO, minwidth=0, width=35, anchor=E)
DTree1.column("#3", stretch=NO, minwidth=0, width=30, anchor=E)
DTree1.column("#4", stretch=NO, minwidth=0, width=35, anchor=E)
DTree1.column("#5", stretch=NO, minwidth=0, width=30, anchor=E)
DTree1.column("#6", stretch=NO, minwidth=0, width=30, anchor=E)
DTree1.column("#7", stretch=NO, minwidth=0, width=30, anchor=E)
DTree1.column("#8", stretch=NO, minwidth=0, width=30, anchor=E)
DTree1.column("#9", stretch=NO, minwidth=0, width=30, anchor=E)
DTree1.column("#10", stretch=NO, minwidth=0, width=20, anchor=E)
DTree1.column("#11", stretch=NO, minwidth=0, width=20, anchor=E)
DTree1.column("#12", stretch=NO, minwidth=0, width=20, anchor=E)
DTree1.column("#13", stretch=NO, minwidth=0, width=20, anchor=E)
DTree1.column("#14", stretch=NO, minwidth=0, width=20, anchor=E)
DTree1.column("#15", stretch=NO, minwidth=0, width=20, anchor=E)
DTree1.column("#16", stretch=NO, minwidth=0, width=20, anchor=E)
DTree1.grid()


"""
DTree1.delete(*DTree1.get_children())
DTree1Conn = sqlite3.connect('DataBaseDir/PressDb.db')
DTree1Cor = DTree1Conn.execute("SELECT OREFUND,ONOTE,ODELIVERYPRICE,OCUSTADDRESS,\
        OCUSTOMERPHONE,OCUSTOMERNAME,OPREPAY,OPRICE,OFINISHTIME,OCURRENTTIME,OTEXT,OQUNTITY,OWIDTH,OLENGTH,OORDERTYPE,OTID FROM DigitalTable")
fetchDTree1 = DTree1Cor.fetchall()
for dataDTree1 in fetchDTree1:
    DTree1.insert('','end', values=(dataDTree1))
DTree1Cor.close()
DTree1Conn.close()
"""


# -------------- TreeView Left Title Name --------------
DTreeVTitle2 = ctk.CTkLabel(
    DMainFrame_BOT_L_T2,
    text="همه پروژه ها",
    font=default_font_bold,
    text_color=("teal", "orange"),
    justify=RIGHT,
)
DTreeVTitle2.grid(row=0, column=0, sticky=E, padx=10, pady=10)


DTree2Frame = ctk.CTkFrame(DMainFrame_BOT_L_T2)
DTree2Frame.grid(row=1, column=0, padx=5, sticky=W)
DTree2 = ttk.Treeview(
    DTree2Frame,
    columns=("L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8"),
    selectmode="browse",
    height=7,
)
DTree2.heading("L1", text="نوعیت", anchor=E)
DTree2.heading("L2", text="اندازه", anchor=E)
DTree2.heading("L3", text="تعداد", anchor=E)
DTree2.heading("L4", text="مواد", anchor=E)
DTree2.heading("L5", text="تحویل", anchor=E)
DTree2.heading("L6", text="قیمت", anchor=E)
DTree2.heading("L7", text="مشتری", anchor=E)
DTree2.heading("L8", text="تلفن", anchor=E)

DTree2.column("#0", stretch=NO, minwidth=0, width=0)
DTree2.column("#1", stretch=NO, minwidth=0, width=50)
DTree2.column("#2", stretch=NO, minwidth=0, width=50)
DTree2.column("#3", stretch=NO, minwidth=0, width=50)
DTree2.column("#4", stretch=NO, minwidth=0, width=50)
DTree2.column("#5", stretch=NO, minwidth=0, width=50)
DTree2.column("#6", stretch=NO, minwidth=0, width=50)
DTree2.column("#7", stretch=NO, minwidth=0, width=50)
DTree2.column("#8", stretch=NO, minwidth=0, width=50)
DTree2.grid()

"""
DTree2.delete(*DTree2.get_children())
DTree2Conn = sqlite3.connect('DataBaseDir/ExtraScale.db')
DTree2Cor = DTree2Conn.execute("SELECT TRUCK_NUMBER,TRUCK_MODEL,DRIVER_NAME,REG_DATE,REG_MOOD FROM RegTruck")
fetchDTree2 = DTree2Cor.fetchall()
for dataDTree2 in fetchDTree2:
    DTree2.insert('','end', values=(dataDTree2))
DTree2Cor.close()
DTree2Conn.close()
"""


# ========================= Tab3_1 Financial ==========================
# ========================= Tab3_1 Financial ==========================
# ========================= Tab3_1 Financial ==========================
# ========================= Tab3_1 Financial ==========================
# ========================= Tab3_1 Financial ==========================
# ========================= Tab3_1 Financial ==========================
# ========================= Tab3_1 Financial ==========================


FTYPE = StringVar()
FCOSTTYPE = StringVar()
FAMOUNT = StringVar()
FNOTE = StringVar()
TREE7_SHOW_BY_DATE_FROM = StringVar()
TREE7_SHOW_BY_DATE_TO = StringVar()

ITYPE = StringVar()
IINCTYPE = StringVar()
IAMOUNT = StringVar()
IDATE = StringVar()
INOTE = StringVar()

FDATE = StringVar()
REGTYPE_VAR = StringVar()
INCTYPE_VAR = StringVar()
# ================ Rent,Tax,ElecBill,etc contents ================
# ================ Rent,Tax,ElecBill,etc contents ================
# ================ Rent,Tax,ElecBill,etc contents ================


# ============== This is for the income table to ===============


def Income_Submit():
    import datetime

    DateNow = datetime.date.today()
    FConn1 = sqlite3.connect("DataBaseDir/PressDb.db")
    Fcur1 = FConn1.cursor()
    if Inc_Entry1.get() == "":
        messagebox.showerror("Space4", "نوعیت نمیتواند خالی باشد")
    else:
        if INCTYPE_VAR.get() == DAILY_VAL:
            Fcur1.execute(
                f"insert into IncomeTable (ITYPE,\
                IINCTYPE,IAMOUNT,IDATE,INOTE) values ('{INCTYPE_VAR.get()}',\
                '{IINCTYPE.get()}','{IAMOUNT.get()}',\
                '{IDATE.get()}','{INOTE.get()}')"
            )
            messagebox.showinfo("Space4", "ثبت انجام شد")

        if INCTYPE_VAR.get() == MONTHLY_VAL:
            Fcur1.execute(
                f"insert into IncomeTable (ITYPE,\
                IINCTYPE,IAMOUNT,IDATE,INOTE) values ('{INCTYPE_VAR.get()}',\
                '{IINCTYPE.get()}','{IAMOUNT.get()}',\
                '{IDATE.get()}','{INOTE.get()}')"
            )
            messagebox.showinfo("Space4", "ثبت انجام شد")

        if INCTYPE_VAR.get() == YEARLY_VAL:
            Fcur1.execute(
                f"insert into IncomeTable (ITYPE,\
                IINCTYPE,IAMOUNT,IDATE,INOTE) values ('{INCTYPE_VAR.get()}',\
                '{IINCTYPE.get()}','{IAMOUNT.get()}',\
                '{IDATE.get()}','{INOTE.get()}')"
            )
            messagebox.showinfo("Space4", "ثبت انجام شد")
    FConn1.commit()
    FConn1.close()
    MFInClearFunc()
    MFInRef()


def MFInRef():
    MTree7_0.delete(*MTree7_0.get_children())
    MTree7_0Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    MTree7_0Cor = MTree7_0Conn.execute(
        """
        SELECT
        INOTE,
        IDATE,
        IAMOUNT,
        IINCTYPE,
        ITYPE,
        ITID 
        FROM IncomeTable"""
    )
    fetchMTree7_0 = MTree7_0Cor.fetchall()
    for dataMTree7_0 in fetchMTree7_0:
        MTree7_0.insert("", "end", values=(dataMTree7_0))
    MTree7_0Cor.close()
    MTree7_0Conn.close()


def MFRef():
    Tree7.delete(*Tree7.get_children())
    Tree7Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    Tree7Cor = Tree7Conn.execute(
        """
        SELECT
        FNOTE,
        FDATE,
        FAMOUNT,
        FCOSTTYPE,
        FTYPE,
        FTID
        FROM FCostTable
        """
    )
    fetchTree7 = Tree7Cor.fetchall()
    for dataTree7 in fetchTree7:
        Tree7.insert("", "end", values=(dataTree7))
    Tree7Cor.close()
    Tree7Conn.close()


def MFInClearFunc():
    Inc_Entry1.delete(0, END)
    Inc_Entry2.delete(0, END)
    Inc_Entry3.delete(0, END)
    Inc_Entry4.delete(0, END)
    Inc_Entry1.focus()


# ================ Rent,Tax,ElecBill,etc contents ================
# ================ Rent,Tax,ElecBill,etc contents ================
# ================ Rent,Tax,ElecBill,etc contents ================
def FSubmit():
    import datetime

    DateNow = datetime.date.today()
    FConn1 = sqlite3.connect("DataBaseDir/PressDb.db")
    Fcur1 = FConn1.cursor()
    if Finance_MngEntry3.get() == "":
        messagebox.showerror("Space4", "مقدار نمیتواند خالی باشد")
    else:
        if REGTYPE_VAR.get() == DAILY_VAL:
            Fcur1.execute(
                f"insert into FCostTable (FTYPE,\
                FCOSTTYPE,FAMOUNT,FDATE,FNOTE) values ('{REGTYPE_VAR.get()}',\
                '{FCOSTTYPE.get()}','{FAMOUNT.get()}',\
                '{FDATE.get()}','{FNOTE.get()}')"
            )
            messagebox.showinfo("Space4", "ثبت انجام شد")

        if REGTYPE_VAR.get() == MONTHLY_VAL:
            Fcur1.execute(
                f"insert into FCostTable (FTYPE,\
                FCOSTTYPE,FAMOUNT,FDATE,FNOTE) values ('{REGTYPE_VAR.get()}',\
                '{FCOSTTYPE.get()}','{FAMOUNT.get()}',\
                '{FDATE.get()}','{FNOTE.get()}')"
            )
            messagebox.showinfo("Space4", "ثبت انجام شد")

        if REGTYPE_VAR.get() == YEARLY_VAL:
            Fcur1.execute(
                f"insert into FCostTable (FTYPE,\
                FCOSTTYPE,FAMOUNT,FDATE,FNOTE) values ('{REGTYPE_VAR.get()}',\
                '{FCOSTTYPE.get()}','{FAMOUNT.get()}',\
                '{FDATE.get()}','{FNOTE.get()}')"
            )
            messagebox.showinfo("Space4", "ثبت انجام شد")

    FConn1.commit()
    FConn1.close()

    Finance_MngEntry4.delete(0, END)
    Finance_MngEntry3.delete(0, END)
    Finance_MngEntry5.delete(0, END)
    Finance_MngEntry2.focus()
    FRef()
    Finance_MngEntry4.insert(0, DateNow)


def FClearFunc():
    Finance_MngEntry4.delete(0, END)
    Finance_MngEntry2.set("انتخاب نوع")
    Finance_MngEntry3.delete(0, END)
    Finance_MngEntry5.delete(0, END)
    Finance_MngEntry2.focus()
    Finance_MngEntry4.insert(0, DateNow)


# notworking.fix(this one please! search in poe for JOIN table and select between two entry.get() date )
def FRef():
    Tree3.delete(*Tree3.get_children())
    Tree3Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    query3 = """
    SELECT
    strftime('%Y-%m-%d', FCostTable.FDATE) AS Month,
    SUM(FCostTable.FAMOUNT)AS SM0,
    SUM(EmployeeTable.ESALARY)AS SM1
    FROM
    FCostTable
    JOIN EmployeeTable ON EmployeeTable.EJOINDATE = FCostTable.FDATE
    WHERE FDATE BETWEEN date(?, '-1 month') AND date(?,'+1 day')
    AND FTYPE LIKE '%' || ? || '%'
    """
    Tree3Cor = Tree3Conn.execute(
        query3, (A_Between_EntryFrom.get(), A_Between_EntryFrom.get(), "ماهانه")
    )
    fetchTree3 = Tree3Cor.fetchall()
    for dataTree3 in fetchTree3:
        dt1 = dataTree3[1]
        dt2 = dataTree3[2]
        try:
            data1 = int(dt1 + dt2)
            Tree3.insert("", "end", values=data1)
        except:
            Tree3.insert("", "end", values="هیچ")
    Tree3Cor.close()
    Tree3Conn.close()

    # -------------------------------------
    # -------------------------------------
    Tree4.delete(*Tree4.get_children())
    Tree4Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    query4 = """
    SELECT
        SUM(FAMOUNT) AS SM0
    FROM
        FCostTable
    WHERE
        FDATE BETWEEN date(?, '-1 month') AND date(?, '+1 day')
        AND FTYPE LIKE '%' || ? || '%'
    """

    Tree4Cor = Tree4Conn.execute(
        query4,
        (
            B_Between_EntryFrom.get(),
            B_Between_EntryFrom.get(),
            "روزانه"
        )
    )
    fetchTree4 = Tree4Cor.fetchall()
    for dataTree4 in fetchTree4:
        try:
            CalcProfit = int(dataTree4[0])
            Tree4.insert("", "end", values=(CalcProfit,))
        except:
            Tree4.insert("", "end", values=("هیچ",))
    Tree4Cor.close()
    Tree4Conn.close()

    # -------------------------------------
    # -------------------------------------
    Tree4_0.delete(*Tree4_0.get_children())
    Tree4_0Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    query4_0 = """
    SELECT
        SUM(FAMOUNT) AS SM00
    FROM
        FCostTable
    WHERE
        FDATE BETWEEN date(?, '-12 month') AND date(?, '+1 day')
        AND FTYPE LIKE '%' || ? || '%'
    """
    Tree4_0Cor = Tree4_0Conn.execute(
        query4_0,(C_Between_EntryFrom.get(),C_Between_EntryFrom.get(),"سالانه")
    )
    fetchTree4_0 = Tree4_0Cor.fetchall()
    for dataTree4_0 in fetchTree4_0:
        Tree4_0.insert("", "end", values=(dataTree4_0))
    Tree4_0Cor.close()
    Tree4_0Conn.close()

    # -------------------------------------
    # -------------------------------------
    Tree5.delete(*Tree5.get_children())
    Tree5Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    query5 = """
    SELECT 
    SUM(ESALARY),
    COUNT(ESALARY) 
    FROM EmployeeTable
    WHERE EJOINDATE BETWEEN date(?, '-1 month') AND date(?,'+1 day')
    """
    Tree5Cor = Tree5Conn.execute(
        query5, (D_Between_EntryFrom.get(), D_Between_EntryFrom.get())
    )
    fetchTree5 = Tree5Cor.fetchall()
    for dataTree5 in fetchTree5:
        Tree5.insert("", "end", values=(dataTree5))
        Count_labSalary.configure(text=f"{dataTree5[1]}", font=default_font_bold)
    Tree5Cor.close()
    Tree5Conn.close()

    # -------------------------------------
    # -------------------------------------
    Tree6.delete(*Tree6.get_children())
    Tree6Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    query6 = """
    SELECT
    SUM(EmployeeTable.ESALARY) AS SM0,
    SUM(LSTTable.STL_USAGE) AS SM1,
    SUM(FCostTable.FAMOUNT) AS SM2,
    SUM(LSTTable.STL_TTLPID) AS SM3,
    SUM(LaserTableCutDone.DONE_O_CUT_TTLPID) AS SM4,
    SUM(LaserTableEngraveDone.DONE_O_ENGR_TTLPID) AS SM5
    FROM LSTTable
    JOIN EmployeeTable ON EmployeeTable.EJOINDATE = LSTTable.STL_CURTIME
    JOIN FCostTable ON FCostTable.FDATE = LSTTable.STL_CURTIME
    JOIN LaserTableCutDone ON LaserTableCutDone.DONE_O_CUT_DATE = LSTTable.STL_CURTIME
    JOIN LaserTableEngraveDone ON LaserTableEngraveDone.DONE_O_ENGR_DATE = LSTTable.STL_CURTIME
    WHERE
    STL_CURTIME
    BETWEEN date(?, '-1 month') AND date(?,'+1 day')
    """
    Tree6Cor = Tree6Conn.execute(
        query6, (E_Between_EntryFrom.get(), E_Between_EntryFrom.get())
    )
    fetchTree6 = Tree6Cor.fetchall()
    for dataTree6 in fetchTree6:
        ProfitData0P = dataTree6[0]
        ProfitData1P = dataTree6[1]
        ProfitData2P = dataTree6[2]
        ProfitData3P = dataTree6[3]
        ProfitData4P = dataTree6[4]
        ProfitData5P = dataTree6[5]

        try:
            CalcProfitP = int(ProfitData3P+ProfitData4P+ProfitData5P) - (
                int(ProfitData0P) + int(ProfitData1P) + int(ProfitData2P)
            )
            Tree6.insert("", "end", values=(CalcProfitP))
        except:
            Tree6.insert("", "end", values="هیچ")
    Tree6Cor.close()
    Tree6Conn.close()

    # -------------------------------------
    # -------------------------------------
    MTree7_0.delete(*MTree7_0.get_children())
    MTree7_0Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    MTree7_0Cor = MTree7_0Conn.execute(
        """
        SELECT
        INOTE,
        IDATE,
        IAMOUNT,
        IINCTYPE,
        ITYPE,
        ITID
        FROM IncomeTable
        """
    )
    fetchMTree7_0 = MTree7_0Cor.fetchall()
    for dataMTree7_0 in fetchMTree7_0:
        MTree7_0.insert("", "end", values=(dataMTree7_0))
    MTree7_0Cor.close()
    MTree7_0Conn.close()

    # -------------------------------------
    # -------------------------------------
    Tree7.delete(*Tree7.get_children())
    Tree7Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    Tree7Cor = Tree7Conn.execute(
        """
        SELECT
        FNOTE,
        FDATE,
        FAMOUNT,
        FCOSTTYPE,
        FTYPE,
        FTID
        FROM FCostTable
        """
    )
    fetchTree7 = Tree7Cor.fetchall()
    for dataTree7 in fetchTree7:
        Tree7.insert("", "end", values=(dataTree7))
    Tree7Cor.close()
    Tree7Conn.close()


def FDeleteFunc():  # This is for deleting in cases. looking at multi selections and then deleting
    selected_item = Tree7.selection()
    selected_item2 = MTree7_0.selection()
    if selected_item:
        for selected_item in Tree7.selection():
            conn = sqlite3.connect("DataBaseDir/PressDb.db")
            cur = conn.cursor()
            messageDelete = messagebox.askyesno(
                "هشدار", "؟آیا میخواهید این داده را حذف کنید"
            )
            if messageDelete > 0:
                cur.execute(
                    "DELETE FROM FCostTable WHERE FTID=?",
                    (Tree7.set(selected_item, "#6"),),
                )
                conn.commit()
                Tree7.delete(selected_item)
                conn.close()

    elif selected_item2:
        for selected_item2 in MTree7_0.selection():
            conn2 = sqlite3.connect("DataBaseDir/PressDb.db")
            cur2 = conn2.cursor()
            messageDelete2 = messagebox.askyesno(
                "هشدار", "؟آیا میخواهید این داده را حذف کنید"
            )
            if messageDelete2 > 0:
                cur2.execute(
                    "DELETE FROM IncomeTable WHERE ITID=?",
                    (MTree7_0.set(selected_item2, "#6"),),
                )
                conn2.commit()
                MTree7_0.delete(selected_item2)
                conn2.close()

    else:
        messagebox.showerror("Space4", "! لطفاً ریکارد مورد نظر را انتخاب کنید")


Type_Values = [
    "غذا",
    "ابزاراولیه",
    "کرایه_شرکت",
    "بل_برق",
    "تکس",
    "دیگر مالیات",
    "هزینه تبلیغات",
    "لوازم داخلی",
]


def RadioFunc1():
    DateNow = datetime.date.today()
    Finance_MngEntry4.delete(0, END)
    Finance_MngEntry2.configure(state=NORMAL, border_width=2)
    Finance_MngEntry3.configure(state=NORMAL, border_width=2)
    Finance_MngEntry4.configure(state=NORMAL)
    Finance_MngEntry4.insert(0, DateNow)
    Finance_MngEntry5.configure(state=NORMAL, border_width=2)
    FCOSTTYPE.set("انتخاب نوع")
    Finance_MngEntry2.focus()


def RadioFuncInc1():
    Inc_Entry1.configure(state=NORMAL, border_width=2)
    Inc_Entry2.configure(state=NORMAL, border_width=2)
    Inc_Entry3.configure(state=NORMAL, border_width=2)
    Inc_Entry4.configure(state=NORMAL, border_width=2)
    Inc_Entry1.focus()


# =========== Main Frames Opened ===========
Tab3_Frame_InTop = ctk.CTkFrame(tab3_1)
Tab3_Frame_InTop.grid(row=0, column=0, padx=5, pady=10, sticky=NE)
Tab3_Frame_InBot = ctk.CTkFrame(tab3_1)
Tab3_Frame_InBot.grid(row=1, column=0, padx=5, pady=10, sticky=NE)

MainFrame_BOT_L_T3 = ctk.CTkFrame(Tab3_Frame_InTop)
MainFrame_BOT_L_T3.grid(row=1, column=0, padx=5, pady=2, sticky=NE)
MainFrame_CEN_L_T3 = ctk.CTkFrame(Tab3_Frame_InTop)
MainFrame_CEN_L_T3.grid(row=0, column=0, padx=5, pady=10, sticky=NE)
MainFrame_BTN_L_T3 = ctk.CTkFrame(MainFrame_CEN_L_T3, fg_color="#2B2B2B")
MainFrame_BTN_L_T3.place(x=5, y=5)
MainFrame_BTN_R_T3 = ctk.CTkFrame(MainFrame_CEN_L_T3, fg_color="#2B2B2B")
MainFrame_BTN_R_T3.place(x=270, y=5)

MainFrame_RIGHT_T3 = ctk.CTkFrame(Tab3_Frame_InTop)
MainFrame_RIGHT_T3.grid(row=0, column=1, padx=10, pady=10, sticky=NE)
MainButFrame1 = ctk.CTkFrame(Tab3_Frame_InTop)
MainButFrame1.grid(row=1, column=1, padx=10, pady=10, sticky=NE)

# =========== Main Frames Closed ===========
Count_labSalary = ctk.CTkLabel(
    master=MainFrame_BOT_L_T3,
    text="",
    text_color=BGYELLOW
)
Count_labSalary.place(x=400, y=0)

Finance_MngLabel0 = ctk.CTkLabel(
    MainFrame_RIGHT_T3,
    text="حالت مصرف",
    font=default_font_bold,
    text_color=("teal", "orange"),
    justify=RIGHT,
)
Finance_MngLabel0.grid(row=0, column=1, sticky=E, padx=10, pady=10)


Finance_MngLabel1 = ctk.CTkLabel(
    MainFrame_RIGHT_T3, text="نوع هزینه", font=default_font_bold, justify=RIGHT
)
Finance_MngLabel1.grid(row=1, column=1, sticky=E, padx=10, pady=5)

Finance_MngLabel2 = ctk.CTkLabel(
    MainFrame_RIGHT_T3,
    text="مقدار / افـ",
    font=default_font_bold,
    justify=RIGHT
)
Finance_MngLabel2.grid(row=2, column=1, sticky=E, padx=10, pady=5)

Finance_MngLabel3 = ctk.CTkLabel(
    MainFrame_RIGHT_T3, text="تاریخ", font=default_font_bold, justify=RIGHT
)
Finance_MngLabel3.grid(row=3, column=1, sticky=E, padx=10, pady=5)

Finance_MngLabel4 = ctk.CTkLabel(
    MainFrame_RIGHT_T3, text="نوت", font=default_font_bold, justify=RIGHT
)
Finance_MngLabel4.grid(row=4, column=1, sticky=E, padx=10, pady=5)


DAILY_VAL = "روزانه"
MONTHLY_VAL = "ماهانه"
YEARLY_VAL = "سالانه"

RadioTypeFrame = ctk.CTkFrame(MainFrame_RIGHT_T3, corner_radius=5)
RadioTypeFrame.grid(row=0, column=0, padx=10, sticky=E)
FinanceRadio1_1 = ctk.CTkRadioButton(
    RadioTypeFrame,
    variable=REGTYPE_VAR,
    font=default_font_bold1,
    text="روزانه",
    width=30,
    hover_color=BGYELLOW,
    fg_color=BGORANGE,
    command=RadioFunc1,
    value=DAILY_VAL,
)
FinanceRadio1_1.grid(row=0, column=0, sticky=E, padx=10)
FinanceRadio1_2 = ctk.CTkRadioButton(
    RadioTypeFrame,
    variable=REGTYPE_VAR,
    font=default_font_bold1,
    text="ماهانه",
    width=30,
    hover_color=BGYELLOW,
    fg_color=BGORANGE,
    command=RadioFunc1,
    value=MONTHLY_VAL,
)
FinanceRadio1_2.grid(row=0, column=1, sticky=E, padx=10)
FinanceRadio1_3 = ctk.CTkRadioButton(
    RadioTypeFrame,
    variable=REGTYPE_VAR,
    font=default_font_bold1,
    text="سالانه",
    width=30,
    hover_color=BGYELLOW,
    fg_color=BGORANGE,
    command=RadioFunc1,
    value=YEARLY_VAL,
)
FinanceRadio1_3.grid(row=0, column=2, sticky=E, padx=10)

Finance_MngEntry2 = ctk.CTkComboBox(
    MainFrame_RIGHT_T3,
    width=200,
    font=default_font_bold,
    justify=RIGHT,
    values=Type_Values,
    variable=FCOSTTYPE,
    state=DISABLED,
    border_width=False,
)
Finance_MngEntry2.grid(row=1, column=0, padx=10, sticky=E)

Finance_MngEntry3 = ctk.CTkEntry(
    MainFrame_RIGHT_T3,
    width=200,
    font=default_font_bold,
    justify=RIGHT,
    textvariable=FAMOUNT,
    state=DISABLED,
    border_width=False,
)
Finance_MngEntry3.grid(row=2, column=0, padx=10, sticky=E)
Finance_MngEntry4 = DateEntry(
    MainFrame_RIGHT_T3,
    width=15,
    font=("Nexa Heavy", 12),
    justify=LEFT,
    textvariable=FDATE,
    state=DISABLED,
    date_pattern="yyyy-mm-dd",
    background=CTKDARK,
    foreground=CTKLIGHT,
    borderwidth=0,
    relief=SOLID,
    style="Custom.DateEntry",
)
Finance_MngEntry4.grid(row=3, column=0, padx=10, sticky=E)
Finance_MngEntry5 = ctk.CTkEntry(
    MainFrame_RIGHT_T3,
    width=200,
    font=default_font_bold,
    justify=RIGHT,
    textvariable=FNOTE,
    state=DISABLED,
    border_width=False,
)
Finance_MngEntry5.grid(row=4, column=0, padx=10, sticky=E)


# ---------- Incomes -----------
# ---------- Incomes -----------


# ----------- Income Labels ----------------

Inc_MngLabel0 = ctk.CTkLabel(
    MainFrame_CEN_L_T3,
    text="حالت عاید",
    font=default_font_bold,
    text_color=("teal", "orange"),
    justify=RIGHT,
)
Inc_MngLabel0.grid(row=0, column=1, sticky=E, padx=10, pady=10)

Inc_MngLabel1 = ctk.CTkLabel(
    MainFrame_CEN_L_T3,
    text="نوع عاید",
    font=default_font_bold,
    justify=RIGHT
)
Inc_MngLabel1.grid(row=1, column=1, sticky=E, padx=10, pady=5)
Inc_MngLabel2 = ctk.CTkLabel(
    MainFrame_CEN_L_T3,
    text="مقدار / اف",
    font=default_font_bold,
    justify=RIGHT
)
Inc_MngLabel2.grid(row=2, column=1, sticky=E, padx=10, pady=5)
Inc_MngLabel3 = ctk.CTkLabel(
    MainFrame_CEN_L_T3, text="تاریخ", font=default_font_bold, justify=RIGHT
)
Inc_MngLabel3.grid(row=3, column=1, sticky=E, padx=10, pady=5)
Inc_MngLabel4 = ctk.CTkLabel(
    MainFrame_CEN_L_T3, text="نوت", font=default_font_bold, justify=RIGHT
)
Inc_MngLabel4.grid(row=4, column=1, sticky=E, padx=10, pady=5)

# ---------- Income Radios --------

RadioTypeFrameInc = ctk.CTkFrame(MainFrame_CEN_L_T3, corner_radius=5)
RadioTypeFrameInc.grid(row=0, column=0, padx=10, sticky=E)
FinanceRadioInc1_1 = ctk.CTkRadioButton(
    RadioTypeFrameInc,
    variable=INCTYPE_VAR,
    font=default_font_bold1,
    text="روزانه",
    width=30,
    hover_color=BGYELLOW,
    fg_color=BGORANGE,
    command=RadioFuncInc1,
    value=DAILY_VAL,
)
FinanceRadioInc1_1.grid(row=0, column=0, sticky=E, padx=10)
FinanceRadioInc1_2 = ctk.CTkRadioButton(
    RadioTypeFrameInc,
    variable=INCTYPE_VAR,
    font=default_font_bold1,
    text="ماهانه",
    width=30,
    hover_color=BGYELLOW,
    fg_color=BGORANGE,
    command=RadioFuncInc1,
    value=MONTHLY_VAL,
)
FinanceRadioInc1_2.grid(row=0, column=1, sticky=E, padx=10)
FinanceRadioInc1_3 = ctk.CTkRadioButton(
    RadioTypeFrameInc,
    variable=INCTYPE_VAR,
    font=default_font_bold1,
    text="سالانه",
    width=30,
    hover_color=BGYELLOW,
    fg_color=BGORANGE,
    command=RadioFuncInc1,
    value=YEARLY_VAL,
)
FinanceRadioInc1_3.grid(row=0, column=2, sticky=E, padx=10)


# -------- Income Entries --------------
Inc_Entry1 = ctk.CTkEntry(
    MainFrame_CEN_L_T3,
    width=200,
    font=default_font_bold,
    justify=RIGHT,
    textvariable=IINCTYPE,
    state=DISABLED,
    border_width=0,
)
Inc_Entry1.grid(row=1, column=0, padx=10, sticky=E)
Inc_Entry2 = ctk.CTkEntry(
    MainFrame_CEN_L_T3,
    width=200,
    font=default_font_bold,
    justify=RIGHT,
    textvariable=IAMOUNT,
    state=DISABLED,
    border_width=0,
)
Inc_Entry2.grid(row=2, column=0, padx=10, sticky=E)
Inc_Entry3 = ctk.CTkEntry(
    MainFrame_CEN_L_T3,
    width=200,
    font=default_font_bold,
    justify=RIGHT,
    textvariable=IDATE,
    state=DISABLED,
    border_width=0,
)
Inc_Entry3.grid(row=3, column=0, padx=10, sticky=E)
Inc_Entry4 = ctk.CTkEntry(
    MainFrame_CEN_L_T3,
    width=200,
    font=default_font_bold,
    justify=RIGHT,
    textvariable=INOTE,
    state=DISABLED,
    border_width=0,
)
Inc_Entry4.grid(row=4, column=0, padx=10, sticky=E)

# -------------------- Buttons Tab2 -------------------
FSaveBtn1 = ctk.CTkButton(
    MainButFrame1,
    image=SaveImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="ذخیره",
    width=40,
    font=default_font_bold2,
    command=FSubmit,
)
FSaveBtn1.grid(row=0, column=5, padx=5, pady=2)
FClearBtn1 = ctk.CTkButton(
    MainButFrame1,
    image=ClearImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="پاک کردن",
    width=40,
    font=default_font_bold2,
    command=FClearFunc,
)
FClearBtn1.grid(row=0, column=4, padx=5, pady=2)
FEditBtn1 = ctk.CTkButton(
    MainButFrame1,
    image=EditImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="ویرایش",
    width=40,
    font=default_font_bold2,
)
FEditBtn1.grid(row=0, column=3, padx=5, pady=2)
FBillGenBtn1 = ctk.CTkButton(
    MainButFrame1,
    image=PrintImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="صدور بل",
    width=40,
    font=default_font_bold2,
)
FBillGenBtn1.grid(row=0, column=2, padx=5, pady=2)
FRefreshBtn1 = ctk.CTkButton(
    MainButFrame1,
    image=RefreshImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="تجدید ",
    width=40,
    font=default_font_bold2,
    command=FRef,
)
FRefreshBtn1.grid(row=0, column=1, padx=5, pady=2)
FDeleteBtn1 = ctk.CTkButton(
    MainButFrame1,
    image=DeleteImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="حذف",
    width=40,
    font=default_font_bold2,
    command=FDeleteFunc,
)
FDeleteBtn1.grid(row=0, column=0, padx=5, pady=2)


# -------------------- Buttons Tab2 M -------------------
MFSaveBtn1 = ctk.CTkButton(
    MainFrame_BTN_L_T3,
    image=SaveImg,
    compound=RIGHT,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="ذخیره",
    width=60,
    font=default_font_bold1,
    command=Income_Submit,
)
MFSaveBtn1.grid(row=0, column=0, padx=5, pady=5)


# -------------------- Buttons Tab3 Frame In Bot -------------------


A_YM_Date = time.strftime("%Y-%m-%d")
A_Between_EntryFrom = ctk.CTkEntry(
    MainFrame_BOT_L_T3,
    width=100,
    height=20,
    font=default_font_bold1,
    justify=RIGHT
)
A_Between_EntryFrom.grid(row=0, column=0, sticky=E, padx=10, pady=5)
A_Between_EntryFrom.insert(0, A_YM_Date)


B_YM_Date = time.strftime("%Y-%m-%d")
B_Between_EntryFrom = ctk.CTkEntry(
    MainFrame_BOT_L_T3,
    width=100,
    height=20,
    font=default_font_bold1,
    justify=RIGHT
)
B_Between_EntryFrom.grid(row=0, column=1, sticky=E, padx=10, pady=5)
B_Between_EntryFrom.insert(0, B_YM_Date)


C_YM_Date = time.strftime("%Y-%m-%d")
C_Between_EntryFrom = ctk.CTkEntry(
    MainFrame_BOT_L_T3,
    width=100,
    height=20,
    font=default_font_bold1,
    justify=RIGHT
)
C_Between_EntryFrom.grid(row=0, column=2, sticky=E, padx=10, pady=5)
C_Between_EntryFrom.insert(0, C_YM_Date)


D_YM_Date = time.strftime("%Y-%m-%d")
D_Between_EntryFrom = ctk.CTkEntry(
    MainFrame_BOT_L_T3,
    width=90, height=20,
    font=default_font_bold1,
    justify=RIGHT
)
D_Between_EntryFrom.grid(row=0, column=3, sticky=E, padx=10, pady=5)
D_Between_EntryFrom.insert(0, D_YM_Date)


E_YM_Date = time.strftime("%Y-%m-%d")
E_Between_EntryFrom = ctk.CTkEntry(
    MainFrame_BOT_L_T3,
    width=100,
    height=20,
    font=default_font_bold1,
    justify=RIGHT
)
E_Between_EntryFrom.grid(row=0, column=4, sticky=E, padx=10, pady=5)
E_Between_EntryFrom.insert(0, E_YM_Date)
# -------------- TreeView Right Title Name --------------


Tree3Frame = ctk.CTkFrame(MainFrame_BOT_L_T3)
Tree3Frame.grid(row=1, column=0, padx=10, pady=10, sticky=W)
Tree3 = ttk.Treeview(Tree3Frame, columns=("L1"), selectmode="brows", height=1)
Tree3.heading("L1", text="مصارف ماهانه", anchor=E)
Tree3.column("#0", stretch=NO, minwidth=0, width=0)
Tree3.column("#1", stretch=NO, minwidth=0, width=100, anchor=E)
Tree3.grid()


Tree3.delete(*Tree3.get_children())
Tree3Conn = sqlite3.connect("DataBaseDir/PressDb.db")
query3 = """
SELECT
strftime('%Y-%m-%d', FCostTable.FDATE) AS Month,
SUM(FCostTable.FAMOUNT)AS SM0,
SUM(EmployeeTable.ESALARY)AS SM1
FROM
FCostTable
JOIN EmployeeTable ON EmployeeTable.EJOINDATE = FCostTable.FDATE
WHERE FDATE BETWEEN date(?, '-1 month') AND date(?,'+1 day')
AND FTYPE LIKE '%' || ? || '%'
"""
Tree3Cor = Tree3Conn.execute(
    query3, (A_Between_EntryFrom.get(), A_Between_EntryFrom.get(), "ماهانه")
)
fetchTree3 = Tree3Cor.fetchall()
for dataTree3 in fetchTree3:
    dt1 = dataTree3[1]
    dt2 = dataTree3[2]
    try:
        data1 = int(dt1 + dt2)
        Tree3.insert("", "end", values=data1)
    except:
        Tree3.insert("", "end", values="هیچ")
Tree3Cor.close()
Tree3Conn.close()


Tree4Frame = ctk.CTkFrame(MainFrame_BOT_L_T3)
Tree4Frame.grid(row=1, column=1, padx=10, pady=10, sticky=W)
Tree4 = ttk.Treeview(Tree4Frame, columns=("L1"), selectmode="none", height=1)
Tree4.heading("L1", text="مصارف روزانه", anchor=E)
Tree4.column("#0", stretch=NO, minwidth=0, width=0)
Tree4.column("#1", stretch=NO, minwidth=0, width=100, anchor=E)
Tree4.grid()


Tree4.delete(*Tree4.get_children())
Tree4Conn = sqlite3.connect("DataBaseDir/PressDb.db")
query4 = """
SELECT
    SUM(FAMOUNT) AS SM0
FROM
    FCostTable
WHERE
    FDATE BETWEEN date(?, '-1 month') AND date(?, '+1 day')
    AND FTYPE LIKE '%' || ? || '%'
"""

Tree4Cor = Tree4Conn.execute(
    query4, (B_Between_EntryFrom.get(), B_Between_EntryFrom.get(), "روزانه")
)
fetchTree4 = Tree4Cor.fetchall()
for dataTree4 in fetchTree4:
    try:
        CalcProfit = int(dataTree4[0])
        Tree4.insert("", "end", values=(CalcProfit,))
    except:
        Tree4.insert("", "end", values=("هیچ",))
Tree4Cor.close()
Tree4Conn.close()


Tree4_0Frame = ctk.CTkFrame(MainFrame_BOT_L_T3)
Tree4_0Frame.grid(row=1, column=2, padx=10, pady=10, sticky=W)
Tree4_0 = ttk.Treeview(
    Tree4_0Frame,
    columns=("L1"),
    selectmode="none",
    height=1
)
Tree4_0.heading("L1", text="مصارف سالانه", anchor=E)
Tree4_0.column("#0", stretch=NO, minwidth=0, width=0)
Tree4_0.column("#1", stretch=NO, minwidth=0, width=120, anchor=E)
Tree4_0.grid()


Tree4_0.delete(*Tree4_0.get_children())
Tree4_0Conn = sqlite3.connect("DataBaseDir/PressDb.db")
query4_0 = """
SELECT
    SUM(FAMOUNT) AS SM00
FROM
    FCostTable
WHERE
    FDATE BETWEEN date(?, '-12 month') AND date(?, '+1 day')
    AND FTYPE LIKE '%' || ? || '%'
"""
Tree4_0Cor = Tree4_0Conn.execute(
    query4_0, (C_Between_EntryFrom.get(), C_Between_EntryFrom.get(), "سالانه")
)
fetchTree4_0 = Tree4_0Cor.fetchall()
for dataTree4_0 in fetchTree4_0:
    Tree4_0.insert("", "end", values=(dataTree4_0))
Tree4_0Cor.close()
Tree4_0Conn.close()


Tree5Frame = ctk.CTkFrame(MainFrame_BOT_L_T3)
Tree5Frame.grid(row=1, column=3, padx=10, pady=10, sticky=W)
Tree5 = ttk.Treeview(Tree5Frame, columns=("L1"), selectmode="none", height=1)
Tree5.heading("L1", text="معاش کارمندان", anchor=E)
Tree5.column("#0", stretch=NO, minwidth=0, width=0)
Tree5.column("#1", stretch=NO, minwidth=0, width=120, anchor=E)
Tree5.grid()


Tree5.delete(*Tree5.get_children())
Tree5Conn = sqlite3.connect("DataBaseDir/PressDb.db")
query5 = """
SELECT
SUM(ESALARY),
COUNT(ESALARY)
FROM EmployeeTable
WHERE EJOINDATE BETWEEN date(?, '-1 month') AND date(?,'+1 day')
"""
Tree5Cor = Tree5Conn.execute(
    query5, (D_Between_EntryFrom.get(), D_Between_EntryFrom.get())
)
fetchTree5 = Tree5Cor.fetchall()
for dataTree5 in fetchTree5:
    Tree5.insert("", "end", values=(dataTree5))
    Count_labSalary.configure(text=f"{dataTree5[1]}", font=default_font_bold)
Tree5Cor.close()
Tree5Conn.close()


Tree6Frame = ctk.CTkFrame(MainFrame_BOT_L_T3)
Tree6Frame.grid(row=1, column=4, padx=10, pady=10, sticky=W)
Tree6 = ttk.Treeview(Tree6Frame, columns=("L1"), selectmode="none", height=1)
Tree6.heading("L1", text="مفاد یک ماه پروژه ها", anchor=E)
Tree6.column("#0", stretch=NO, minwidth=0, width=0)
Tree6.column("#1", stretch=NO, minwidth=0, width=120, anchor=E)
Tree6.grid()


Tree6.delete(*Tree6.get_children())
Tree6Conn = sqlite3.connect("DataBaseDir/PressDb.db")
query6 = """
SELECT
SUM(EmployeeTable.ESALARY) AS SM0,
SUM(LSTTable.STL_USAGE) AS SM1,
SUM(FCostTable.FAMOUNT) AS SM2,
SUM(LSTTable.STL_TTLPID) AS SM3,
SUM(LaserTableCutDone.DONE_O_CUT_TTLPID) AS SM4,
SUM(LaserTableEngraveDone.DONE_O_ENGR_TTLPID) AS SM5
FROM LSTTable
JOIN EmployeeTable ON EmployeeTable.EJOINDATE = LSTTable.STL_CURTIME
JOIN FCostTable ON FCostTable.FDATE = LSTTable.STL_CURTIME
JOIN LaserTableCutDone ON LaserTableCutDone.DONE_O_CUT_DATE = LSTTable.STL_CURTIME
JOIN LaserTableEngraveDone ON LaserTableEngraveDone.DONE_O_ENGR_DATE = LSTTable.STL_CURTIME
WHERE
STL_CURTIME
BETWEEN date(?, '-1 month') AND date(?,'+1 day')
"""
Tree6Cor = Tree6Conn.execute(
    query6, (E_Between_EntryFrom.get(), E_Between_EntryFrom.get())
)
fetchTree6 = Tree6Cor.fetchall()
for dataTree6 in fetchTree6:
    ProfitData0P = dataTree6[0]
    ProfitData1P = dataTree6[1]
    ProfitData2P = dataTree6[2]
    ProfitData3P = dataTree6[3]
    ProfitData4P = dataTree6[4]
    ProfitData5P = dataTree6[5]

    try:
        CalcProfitP = int(ProfitData3P+ProfitData4P+ProfitData5P) - (
            int(ProfitData0P) + int(ProfitData1P) + int(ProfitData2P)
        )
        Tree6.insert("", "end", values=(CalcProfitP))
    except:
        Tree6.insert("", "end", values="هیچ")
Tree6Cor.close()
Tree6Conn.close()


# -------------- TreeView Left Title Name --------------

"""
D_MngEntry7 = DateEntry(MainFrame_BOT_L_T3,textvariable=TREE7_SHOW_BY_DATE_FROM,font=("Arial",10,"bold"),justify=RIGHT,width=14)
D_MngEntry7.place(x=10,y=10)
"""


MTreeVTitle7_0 = ctk.CTkLabel(
    Tab3_Frame_InBot,
    text="عاید روزانه",
    font=default_font_bold,
    text_color=("teal", "orange"),
    justify=RIGHT,
)
MTreeVTitle7_0.grid(row=0, column=0, sticky=E, padx=10, pady=10)

MTree7_0Frame = ctk.CTkFrame(Tab3_Frame_InBot)
MTree7_0Frame.grid(row=1, column=0, padx=10, sticky=W)
MTree7_0 = ttk.Treeview(
    MTree7_0Frame,
    columns=("MLIn1", "MLIn2", "MLIn3", "MLIn4", "MLIn5", "MLIn6"),
    selectmode="browse",
    height=6,
)
MTree7_0.heading("MLIn1", text="نوت", anchor=E)
MTree7_0.heading("MLIn2", text="تاریخ", anchor=E)
MTree7_0.heading("MLIn3", text="مقدار پ اف", anchor=E)
MTree7_0.heading("MLIn4", text="نوع عاید", anchor=E)
MTree7_0.heading("MLIn5", text="حالت عاید", anchor=E)
MTree7_0.heading("MLIn6", text="ID", anchor=E)

MTree7_0.column("#0", stretch=NO, minwidth=0, width=0)
MTree7_0.column("#1", stretch=NO, minwidth=0, width=120, anchor=E)
MTree7_0.column("#2", stretch=NO, minwidth=0, width=80, anchor=E)
MTree7_0.column("#3", stretch=NO, minwidth=0, width=80, anchor=E)
MTree7_0.column("#4", stretch=NO, minwidth=0, width=80, anchor=E)
MTree7_0.column("#5", stretch=NO, minwidth=0, width=80, anchor=E)
MTree7_0.column("#6", stretch=NO, minwidth=0, width=50, anchor=E)
MTree7_0.grid(padx=0, pady=0)


MTree7_0.delete(*MTree7_0.get_children())
MTree7_0Conn = sqlite3.connect("DataBaseDir/PressDb.db")
MTree7_0Cor = MTree7_0Conn.execute(
    """
    SELECT
    INOTE,
    IDATE,
    IAMOUNT,
    IINCTYPE,
    ITYPE,
    ITID
    FROM IncomeTable"""
)
fetchMTree7_0 = MTree7_0Cor.fetchall()
for dataMTree7_0 in fetchMTree7_0:
    MTree7_0.insert("", "end", values=(dataMTree7_0))
MTree7_0Cor.close()
MTree7_0Conn.close()


# ================== apart from bottom  ======================

TreeVTitle7 = ctk.CTkLabel(
    Tab3_Frame_InBot,
    text="همه هزینه ها",
    font=default_font_bold,
    text_color=("teal", "orange"),
    justify=RIGHT,
)
TreeVTitle7.grid(row=0, column=2, sticky=E, padx=20, pady=10)


Tree7Frame = ctk.CTkFrame(Tab3_Frame_InBot)
Tree7Frame.grid(row=1, column=2, padx=5, sticky=W)
Tree7 = ttk.Treeview(
    Tree7Frame,
    columns=("L1", "L2", "L3", "L4", "L5", "L6"),
    selectmode="browse",
    height=6,
)
Tree7.heading("L1", text="نوت", anchor=E)
Tree7.heading("L2", text="تاریخ", anchor=E)
Tree7.heading("L3", text="مقدار / اف", anchor=E)
Tree7.heading("L4", text="نوع هزینه", anchor=E)
Tree7.heading("L5", text="نوع ثبت", anchor=E)
Tree7.heading("L6", text="ID", anchor=E)

Tree7.column("#0", stretch=NO, minwidth=0, width=0)
Tree7.column("#1", stretch=NO, minwidth=0, width=120, anchor=E)
Tree7.column("#2", stretch=NO, minwidth=0, width=80, anchor=E)
Tree7.column("#3", stretch=NO, minwidth=0, width=80, anchor=E)
Tree7.column("#4", stretch=NO, minwidth=0, width=80, anchor=E)
Tree7.column("#5", stretch=NO, minwidth=0, width=80, anchor=E)
Tree7.column("#6", stretch=NO, minwidth=0, width=50, anchor=E)
Tree7.grid(padx=0, pady=0)


Tree7.delete(*Tree7.get_children())
Tree7Conn = sqlite3.connect("DataBaseDir/PressDb.db")
Tree7Cor = Tree7Conn.execute(
    """
    SELECT
    FNOTE,
    FDATE,
    FAMOUNT,
    FCOSTTYPE,
    FTYPE,
    FTID
    FROM FCostTable
    """
)
fetchTree7 = Tree7Cor.fetchall()
for dataTree7 in fetchTree7:
    Tree7.insert("", "end", values=(dataTree7))
Tree7Cor.close()
Tree7Conn.close()


# ========================= Tab3_2 Financial ==========================
# ========================= Tab3_2 Financial ==========================
# ========================= Tab3_2 Financial ==========================
# ========================= Tab3_2 Financial ==========================
# ========================= Tab3_2 Financial ==========================
# ========================= Tab3_2 Financial ==========================
# ========================= Tab3_2 Financial ==========================

LDRLENDER = StringVar()
LDRBEHALF = StringVar()
LDRAMOUNT = StringVar()
LDRDATE = StringVar()
LDRNOTE = StringVar()

DBTDEBTOR = StringVar()
DBTBEHALF = StringVar()
DBTAMOUNT = StringVar()
DBDATE = StringVar()
DBTNOTE = StringVar()


# ========= Debtor Funcs ================
# ========= Debtor Funcs ================
# ========= Debtor Funcs ================


def DebSubmit():
    DebConn = sqlite3.connect("DataBaseDir/PressDb.db")
    DebCur = DebConn.cursor()
    if DebtorEntry1.get() == "" or DebtorEntry2.get() == "" or DebtorEntry3.get() == "":
        messagebox.showerror(
            "ببخشید", "الزامی است که ورودی ها قبل از ذخیره پر شود."
        )
    else:
        DebCur.execute(
            f"insert into DebtorTable (DBTDEBTOR,DBTBEHALF,DBTAMOUNT,DBDATE,\
            DBTNOTE) values ('{DBTDEBTOR.get()}','{DBTBEHALF.get()}',\
            '{DBTAMOUNT.get()}','{DBDATE.get()}','{DBTNOTE.get()}')"
        )
    DebConn.commit()
    DebConn.close()
    DebtorEntry1.delete(0, END)
    DebtorEntry2.delete(0, END)
    DebtorEntry3.delete(0, END)
    # DebtorEntry4.delete(0, END)
    DebtorEntry5.delete(0, END)
    DebtorEntry1.focus()
    DebRef()


def DebRef():
    TreeDeb.delete(*TreeDeb.get_children())
    TreeDebConn = sqlite3.connect("DataBaseDir/PressDb.db")
    TreeDebCor = TreeDebConn.execute(
        """
        SELECT
        DBTNOTE,
        DBDATE,
        DBTAMOUNT,
        DBTBEHALF,
        DBTDEBTOR,
        DBTID
        FROM DebtorTable
        """
    )
    fetchTreeDeb = TreeDebCor.fetchall()
    for dataTreeDeb in fetchTreeDeb:
        TreeDeb.insert("", "end", values=(dataTreeDeb))
    TreeDebCor.close()
    TreeDebConn.close()

    # -==========================================
    SumTreeDeb.delete(*SumTreeDeb.get_children())
    SumTreeDebConn = sqlite3.connect("DataBaseDir/PressDb.db")
    SumTreeDebCor = SumTreeDebConn.execute(
        """
        SELECT
        SUM(DBTAMOUNT) 
        FROM DebtorTable
        """
    )
    ftsl = SumTreeDebCor.fetchall()
    for dtsl in ftsl:
        SumTreeDeb.insert("", "end", values=(dtsl))
    SumTreeDebCor.close()
    SumTreeDebConn.close()


def DebClear():
    DebtorEntry1.delete(0, END)
    DebtorEntry2.delete(0, END)
    DebtorEntry3.delete(0, END)
    # DebtorEntry4.delete(0, END)
    DebtorEntry5.delete(0, END)
    DebtorEntry1.focus()


def DebDelete():
    DebSelected_item = TreeDeb.selection()
    if DebSelected_item:
        for DebSelected_item in TreeDeb.selection():
            conn = sqlite3.connect("DataBaseDir/PressDb.db")
            cur = conn.cursor()
            messageDelete = messagebox.askyesno(
                "هشدار", "؟آیا میخواهید این داده را حذف کنید"
            )
            if messageDelete > 0:
                cur.execute(
                    "DELETE FROM DebtorTable WHERE DBTID=?",
                    (TreeDeb.set(DebSelected_item, "#6"),),
                )
                conn.commit()
                TreeDeb.delete(DebSelected_item)
                conn.close()
                DebRef()
    else:
        messagebox.showwarning("Space4", "ریکارد انتخاب نشده")


# ========= Lender Funcs ================
# ========= Lender Funcs ================
# ========= Lender Funcs ================


def LenSubmit():
    LenConn = sqlite3.connect("DataBaseDir/PressDb.db")
    LenCur = LenConn.cursor()
    if LenderEntry1.get() == "" or LenderEntry2.get() == "" or LenderEntry3.get() == "":
        messagebox.showerror(
            "ببخشید", "الزامی است که ورودی ها قبل از ذخیره پر شود."
        )
    else:
        LenCur.execute(
            f"insert into LenderTable (LDRLENDER,LDRBEHALF,LDRAMOUNT,LDRDATE,\
            LDRNOTE) values ('{LDRLENDER.get()}','{LDRBEHALF.get()}',\
            '{LDRAMOUNT.get()}','{LDRDATE.get()}','{LDRNOTE.get()}')"
        )
    LenConn.commit()
    LenConn.close()
    LenderEntry1.delete(0, END)
    LenderEntry2.delete(0, END)
    LenderEntry3.delete(0, END)
    # LenderEntry4.delete(0, END)
    LenderEntry5.delete(0, END)
    LenderEntry1.focus()
    LenRef()


def LenRef():
    TreeLen.delete(*TreeLen.get_children())
    TreeLenConn = sqlite3.connect("DataBaseDir/PressDb.db")
    TreeLenCor = TreeLenConn.execute(
        """
        SELECT
        LDRNOTE,
        LDRDATE,
        LDRAMOUNT,
        LDRBEHALF,
        LDRLENDER,
        LDRID
        FROM LenderTable
        """
    )
    fetchTreeLen = TreeLenCor.fetchall()
    for dataTreeLen in fetchTreeLen:
        TreeLen.insert("", "end", values=(dataTreeLen))
    TreeLenCor.close()
    TreeLenConn.close()

    # =================================
    TreeSumLen.delete(*TreeSumLen.get_children())
    TreeSumLenConn = sqlite3.connect("DataBaseDir/PressDb.db")
    TreeSumLenCor = TreeSumLenConn.execute(
        """
        SELECT
        SUM(LDRAMOUNT) 
        FROM LenderTable
        """
    )
    ftsl = TreeSumLenCor.fetchall()
    for dtsl in ftsl:
        TreeSumLen.insert("", "end", values=(dtsl))
    TreeSumLenCor.close()
    TreeSumLenConn.close()


def LenClear():
    LenderEntry1.delete(0, END)
    LenderEntry2.delete(0, END)
    LenderEntry3.delete(0, END)
    # LenderEntry4.delete(0, END)
    LenderEntry5.delete(0, END)
    LenderEntry1.focus()


def LenDelete():
    LenSelected_item = TreeLen.selection()
    if LenSelected_item:
        for LenSelected_item in TreeLen.selection():
            conn = sqlite3.connect("DataBaseDir/PressDb.db")
            cur = conn.cursor()
            messageDelete = messagebox.askyesno(
                "هشدار", "؟آیا میخواهید این داده را حذف کنید"
            )
            if messageDelete > 0:
                cur.execute(
                    "DELETE FROM LenderTable WHERE LDRID=?",
                    (TreeLen.set(LenSelected_item, "#6"),),
                )
                conn.commit()
                TreeLen.delete(LenSelected_item)
                conn.close()
                LenRef()
    else:
        messagebox.showwarning("Space4", "ریکارد انتخاب نشده")


# ========== Frames Lender ===========


DebtorFrame_Top_R = ctk.CTkFrame(tab3_2)
DebtorFrame_Top_R.grid(row=0, column=3, padx=5, pady=5, sticky=NE)
DebtorFrame_CEN_R = ctk.CTkFrame(tab3_2)
DebtorFrame_CEN_R.grid(row=0, column=2, padx=5, pady=5, sticky=SE)
DebtorFrame_Bot_R = ctk.CTkFrame(tab3_2)
DebtorFrame_Bot_R.grid(
    row=1,
    column=1,
    padx=5,
    pady=5,
    sticky=NE,
    columnspan=4
)


LenderFrame_Top_L = ctk.CTkFrame(tab3_2)
LenderFrame_Top_L.grid(row=0, column=1, padx=5, pady=5, sticky=NE)
LenderFrame_CEN_L = ctk.CTkFrame(tab3_2)
LenderFrame_CEN_L.grid(row=0, column=0, padx=5, pady=5, sticky=SE)
LenderFrame_Bot_L = ctk.CTkFrame(tab3_2)
LenderFrame_Bot_L.grid(
    row=1,
    column=0,
    padx=5,
    pady=5,
    sticky=NE,
    columnspan=2
)


# ======= Debtor Labels ============

DebtorLbl0 = ctk.CTkLabel(
    master=DebtorFrame_Top_R, text="بدهکار", font=default_font_bold, text_color=BGORANGE
)
DebtorLbl0.grid(row=0, column=1, padx=5, pady=5, sticky=NE)

DebtorLbl1 = ctk.CTkLabel(
    master=DebtorFrame_Top_R,
    text="نام",
    font=default_font_bold,
)
DebtorLbl1.grid(row=1, column=1, padx=5, pady=5, sticky=NE)

DebtorLbl2 = ctk.CTkLabel(
    master=DebtorFrame_Top_R,
    text="بابت",
    font=default_font_bold,
)
DebtorLbl2.grid(row=2, column=1, padx=5, pady=5, sticky=NE)

DebtorLbl3 = ctk.CTkLabel(
    master=DebtorFrame_Top_R,
    text="مقدار",
    font=default_font_bold,
)
DebtorLbl3.grid(row=3, column=1, padx=5, pady=5, sticky=NE)

DebtorLbl4 = ctk.CTkLabel(
    master=DebtorFrame_Top_R,
    text="تاریخ",
    font=default_font_bold,
)
DebtorLbl4.grid(row=4, column=1, padx=5, pady=5, sticky=NE)

DebtorLbl5 = ctk.CTkLabel(
    master=DebtorFrame_Top_R,
    text="نوت",
    font=default_font_bold,
)
DebtorLbl5.grid(row=5, column=1, padx=5, pady=5, sticky=NE)


# ================ Entry Part ===============
DebtorEntry1 = ctk.CTkEntry(
    master=DebtorFrame_Top_R,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=DBTDEBTOR,
)
DebtorEntry1.grid(row=1, column=0, padx=5, pady=5, sticky=NE)

DebtorEntry2 = ctk.CTkEntry(
    master=DebtorFrame_Top_R,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=DBTBEHALF,
)
DebtorEntry2.grid(row=2, column=0, padx=5, pady=5, sticky=NE)

DebtorEntry3 = ctk.CTkEntry(
    master=DebtorFrame_Top_R,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=DBTAMOUNT,
)
DebtorEntry3.grid(row=3, column=0, padx=5, pady=5, sticky=NE)

DebtorEntry4 = DateEntry(
    master=DebtorFrame_Top_R,
    font=("Arial", 10, "bold"),
    justify=RIGHT,
    width=18,
    date_pattern="yyyy-mm-dd",
    textvariable=DBDATE,
)
DebtorEntry4.grid(row=4, column=0, padx=5, pady=5, sticky=NE)

DebtorEntry5 = ctk.CTkEntry(
    master=DebtorFrame_Top_R,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=DBTNOTE,
)
DebtorEntry5.grid(row=5, column=0, padx=5, pady=5, sticky=NE)


# ======== Debtor Buttons ===============

DebSaveBtn1 = ctk.CTkButton(
    DebtorFrame_CEN_R,
    image=SaveImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="ذخیره",
    width=40,
    font=default_font_bold1,
    command=DebSubmit,
)
DebSaveBtn1.grid(row=0, column=3, padx=7, pady=2)
DebClearBtn1 = ctk.CTkButton(
    DebtorFrame_CEN_R,
    image=ClearImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="پاک کردن",
    width=40,
    font=default_font_bold1,
    command=DebClear,
)
DebClearBtn1.grid(row=0, column=2, padx=7, pady=2)
DebRefreshBtn1 = ctk.CTkButton(
    DebtorFrame_CEN_R,
    image=RefreshImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="تجدید ",
    width=40,
    font=default_font_bold1,
    command=DebRef,
)
DebRefreshBtn1.grid(row=0, column=1, padx=7, pady=2)
DebDeleteBtn1 = ctk.CTkButton(
    DebtorFrame_CEN_R,
    image=DeleteImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="حذف",
    width=40,
    font=default_font_bold1,
    command=DebDelete,
)
DebDeleteBtn1.grid(row=0, column=0, padx=7, pady=2)


# ============= Debtor Treeview ============

TreeDebLbl = ctk.CTkLabel(
    master=DebtorFrame_Bot_R,
    text="لیست بدهکاران",
    font=default_font_bold,
    text_color=("teal", "orange"),
    justify=RIGHT,
)
TreeDebLbl.grid(row=0, column=0, padx=20, pady=10, sticky=NE)


TreeDebFrame = ctk.CTkFrame(DebtorFrame_Bot_R)
TreeDebFrame.grid(row=1, column=0, padx=5, sticky=NE)
TreeDeb = ttk.Treeview(
    TreeDebFrame,
    columns=("L1", "L2", "L3", "L4", "L5", "L6"),
    selectmode="browse",
    height=8,
)
TreeDeb.heading("L1", text="نوت", anchor=E)
TreeDeb.heading("L2", text="تاریخ", anchor=E)
TreeDeb.heading("L3", text="مقدار", anchor=E)
TreeDeb.heading("L4", text="بابت", anchor=E)
TreeDeb.heading("L5", text="نام", anchor=E)
TreeDeb.heading("L6", text="ID", anchor=E)

TreeDeb.column("#0", stretch=NO, minwidth=0, width=0)
TreeDeb.column("#1", stretch=NO, minwidth=0, width=100, anchor=E)
TreeDeb.column("#2", stretch=NO, minwidth=0, width=90, anchor=E)
TreeDeb.column("#3", stretch=NO, minwidth=0, width=80, anchor=E)
TreeDeb.column("#4", stretch=NO, minwidth=0, width=100, anchor=E)
TreeDeb.column("#5", stretch=NO, minwidth=0, width=100, anchor=E)
TreeDeb.column("#6", stretch=NO, minwidth=0, width=50, anchor=E)
TreeDeb.grid(padx=0, pady=0)


TreeDeb.delete(*TreeDeb.get_children())
TreeDebConn = sqlite3.connect("DataBaseDir/PressDb.db")
TreeDebCor = TreeDebConn.execute(
    """
    SELECT
    DBTNOTE,
    DBDATE,
    DBTAMOUNT,
    DBTBEHALF,
    DBTDEBTOR,
    DBTID
    FROM DebtorTable
    """
)
fetchTreeDeb = TreeDebCor.fetchall()
for dataTreeDeb in fetchTreeDeb:
    TreeDeb.insert("", "end", values=(dataTreeDeb))
TreeDebCor.close()
TreeDebConn.close()


# ======== Mini Sum Lender Tree =============
SumDebTree = ctk.CTkFrame(tab3_2)
SumDebTree.place(x=590, y=10)
SumTreeDeb = ttk.Treeview(SumDebTree, columns=("L1"), selectmode=None, height=1)
SumTreeDeb.heading("L1", text="باقیات از شرکت", anchor=E)
SumTreeDeb.column("#0", stretch=NO, minwidth=0, width=0)
SumTreeDeb.column("#1", stretch=NO, minwidth=0, width=120, anchor=E)
SumTreeDeb.grid()

SumTreeDeb.delete(*SumTreeDeb.get_children())
SumTreeDebConn = sqlite3.connect("DataBaseDir/PressDb.db")
SumTreeDebCor = SumTreeDebConn.execute(
    """
    SELECT
    SUM(DBTAMOUNT) 
    FROM DebtorTable
    """
)
ftsl = SumTreeDebCor.fetchall()
for dtsl in ftsl:
    SumTreeDeb.insert("", "end", values=(dtsl))
SumTreeDebCor.close()
SumTreeDebConn.close()


# ========= Lender Part ============
# ========= Lender Part ===========


# ======= Lender Labels ============

LenderLbl0 = ctk.CTkLabel(
    master=LenderFrame_Top_L, text="طلبکار", font=default_font_bold, text_color=BGORANGE
)
LenderLbl0.grid(row=0, column=1, padx=5, pady=5, sticky=NE)

LenderLbl1 = ctk.CTkLabel(
    master=LenderFrame_Top_L,
    text="نام",
    font=default_font_bold,
)
LenderLbl1.grid(row=1, column=1, padx=5, pady=5, sticky=NE)

LenderLbl2 = ctk.CTkLabel(
    master=LenderFrame_Top_L,
    text="بابت",
    font=default_font_bold,
)
LenderLbl2.grid(row=2, column=1, padx=5, pady=5, sticky=NE)

LenderLbl3 = ctk.CTkLabel(
    master=LenderFrame_Top_L,
    text="مقدار",
    font=default_font_bold,
)
LenderLbl3.grid(row=3, column=1, padx=5, pady=5, sticky=NE)

LenderLbl4 = ctk.CTkLabel(
    master=LenderFrame_Top_L,
    text="تاریخ",
    font=default_font_bold,
)
LenderLbl4.grid(row=4, column=1, padx=5, pady=5, sticky=NE)

LenderLbl5 = ctk.CTkLabel(
    master=LenderFrame_Top_L,
    text="نوت",
    font=default_font_bold,
)
LenderLbl5.grid(row=5, column=1, padx=5, pady=5, sticky=NE)

# ================ Entry Part ===============
LenderEntry1 = ctk.CTkEntry(
    master=LenderFrame_Top_L,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=LDRLENDER,
)
LenderEntry1.grid(row=1, column=0, padx=5, pady=5, sticky=NE)

LenderEntry2 = ctk.CTkEntry(
    master=LenderFrame_Top_L,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=LDRBEHALF,
)
LenderEntry2.grid(row=2, column=0, padx=5, pady=5, sticky=NE)

LenderEntry3 = ctk.CTkEntry(
    master=LenderFrame_Top_L,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=LDRAMOUNT,
)
LenderEntry3.grid(row=3, column=0, padx=5, pady=5, sticky=NE)

LenderEntry4 = DateEntry(
    master=LenderFrame_Top_L,
    font=("Arial", 10, "bold"),
    justify=RIGHT,
    width=18,
    date_pattern="yyyy-mm-dd",
    textvariable=LDRDATE,
)
LenderEntry4.grid(row=4, column=0, padx=5, pady=5, sticky=NE)

LenderEntry5 = ctk.CTkEntry(
    master=LenderFrame_Top_L,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=LDRNOTE,
)
LenderEntry5.grid(row=5, column=0, padx=5, pady=5, sticky=NE)


# ======== Lender Buttons ===============

LenSaveBtn1 = ctk.CTkButton(
    LenderFrame_CEN_L,
    image=SaveImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="ذخیره",
    width=40,
    font=default_font_bold1,
    command=LenSubmit,
)
LenSaveBtn1.grid(row=0, column=3, padx=7, pady=2)
LenClearBtn1 = ctk.CTkButton(
    LenderFrame_CEN_L,
    image=ClearImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="پاک کردن",
    width=40,
    font=default_font_bold1,
    command=LenClear,
)
LenClearBtn1.grid(row=0, column=2, padx=7, pady=2)
LenRefreshBtn1 = ctk.CTkButton(
    LenderFrame_CEN_L,
    image=RefreshImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="تجدید ",
    width=40,
    font=default_font_bold1,
    command=LenRef,
)
LenRefreshBtn1.grid(row=0, column=1, padx=7, pady=2)
LenDeleteBtn1 = ctk.CTkButton(
    LenderFrame_CEN_L,
    image=DeleteImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="حذف",
    width=40,
    font=default_font_bold1,
    command=LenDelete,
)
LenDeleteBtn1.grid(row=0, column=0, padx=7, pady=2)


# ============= Lender Treeview ============

TreeLenLbl = ctk.CTkLabel(
    master=LenderFrame_Bot_L,
    text="لیست طلب کاران",
    font=default_font_bold,
    text_color=("teal", "orange"),
    justify=RIGHT,
)
TreeLenLbl.grid(row=0, column=0, padx=20, pady=10, sticky=NE)


TreeLenFrame = ctk.CTkFrame(LenderFrame_Bot_L)
TreeLenFrame.grid(row=1, column=0, padx=5, sticky=NE)
TreeLen = ttk.Treeview(
    TreeLenFrame,
    columns=("L1", "L2", "L3", "L4", "L5", "L6"),
    selectmode="browse",
    height=8,
)
TreeLen.heading("L1", text="نوت", anchor=E)
TreeLen.heading("L2", text="تاریخ", anchor=E)
TreeLen.heading("L3", text="مقدار", anchor=E)
TreeLen.heading("L4", text="بابت", anchor=E)
TreeLen.heading("L5", text="نام", anchor=E)
TreeLen.heading("L6", text="ID", anchor=E)

TreeLen.column("#0", stretch=NO, minwidth=0, width=0)
TreeLen.column("#1", stretch=NO, minwidth=0, width=100, anchor=E)
TreeLen.column("#2", stretch=NO, minwidth=0, width=90, anchor=E)
TreeLen.column("#3", stretch=NO, minwidth=0, width=80, anchor=E)
TreeLen.column("#4", stretch=NO, minwidth=0, width=100, anchor=E)
TreeLen.column("#5", stretch=NO, minwidth=0, width=100, anchor=E)
TreeLen.column("#6", stretch=NO, minwidth=0, width=50, anchor=E)
TreeLen.grid(padx=0, pady=0)


TreeLen.delete(*TreeLen.get_children())
TreeLenConn = sqlite3.connect("DataBaseDir/PressDb.db")
TreeLenCor = TreeLenConn.execute(
    """
    SELECT
    LDRNOTE,
    LDRDATE,
    LDRAMOUNT,
    LDRBEHALF,
    LDRLENDER,
    LDRID
    FROM LenderTable
    """
)
fetchTreeLen = TreeLenCor.fetchall()
for dataTreeLen in fetchTreeLen:
    TreeLen.insert("", "end", values=(dataTreeLen))
TreeLenCor.close()
TreeLenConn.close()


# ======== Mini Sum Lender Tree =============
SumLenTree = ctk.CTkFrame(tab3_2)
SumLenTree.place(x=80, y=10)
TreeSumLen = ttk.Treeview(
    SumLenTree,
    columns=("L1"),
    selectmode=None,
    height=1
)
TreeSumLen.heading("L1", text="باقیات خود شرکت", anchor=E)
TreeSumLen.column("#0", stretch=NO, minwidth=0, width=0)
TreeSumLen.column("#1", stretch=NO, minwidth=0, width=120, anchor=E)
TreeSumLen.grid()

TreeSumLen.delete(*TreeSumLen.get_children())
TreeSumLenConn = sqlite3.connect("DataBaseDir/PressDb.db")
TreeSumLenCor = TreeSumLenConn.execute(
    """
    SELECT
    SUM(LDRAMOUNT) 
    FROM LenderTable
    """
)
ftsl = TreeSumLenCor.fetchall()
for dtsl in ftsl:
    TreeSumLen.insert("", "end", values=(dtsl))
TreeSumLenCor.close()
TreeSumLenConn.close()


# ========================= Tab3_3 Financial ==========================
# ========================= Tab3_3 Financial ==========================
# ========================= Tab3_3 Financial ==========================

Tab3_3Frame_InTop = ctk.CTkFrame(tab3_3)
Tab3_3Frame_InTop.grid(row=0, column=0, padx=5, pady=10, sticky=NE)
Tab3_3Frame_InBot = ctk.CTkFrame(tab3_3)
Tab3_3Frame_InBot.grid(row=1, column=0, padx=5, pady=10, sticky=NE)


# ========================= Tab4 Financial ==========================
# ========================= Tab4 Financial ==========================
# ========================= Tab4 Financial ==========================
# ========================= Tab4 Financial ==========================
# ========================= Tab4 Financial ==========================
# ========================= Tab4 Financial ==========================
# ========================= Tab4 Financial ==========================


GraphFrame_TOP_R = ctk.CTkFrame(tab4)
GraphFrame_TOP_R.grid(row=0, column=1, padx=10, pady=10, sticky=NE)
GraphFrame_TOP_L = ctk.CTkFrame(tab4)
GraphFrame_TOP_L.grid(row=0, column=0, padx=10, pady=10, sticky=NE)

GraphFrame_BOT_R = ctk.CTkFrame(tab4)
GraphFrame_BOT_R.grid(row=1, column=1, padx=10, pady=10, sticky=NE)
GraphFrame_BOT_L = ctk.CTkFrame(tab4)
GraphFrame_BOT_L.grid(row=1, column=0, padx=10, pady=10, sticky=NE)

# ---------- Main Frames in Tab4 End -------------


def fetch_income_data():
    G_conn = sqlite3.connect("DataBaseDir/PressDb.db")
    G_query = """
    SELECT
        strftime('%m', STL_DATE) AS G_date,
        SUM(STL_TTLPID)
    FROM LSTTable
    WHERE STL_TTLPID IS NOT NULL
    GROUP BY G_date
    """
    G_cur = G_conn.execute(G_query)
    G_fetch = G_cur.fetchall()
    income_per_month = {}
    income = [0] * 12
    for row in G_fetch:
        month = row[0]
        income_value = row[1]
        month_index = int(month) - 1
        income[month_index] = income_value
        income_per_month[month] = income_value
    G_cur.close()
    G_conn.close()
    return income_per_month, income


def fetch_expenses_data():
    Ex_conn = sqlite3.connect("DataBaseDir/PressDb.db")
    Ex_exQuery = """
    SELECT
        strftime('%m', FDATE) AS Ex_date,
        SUM(FAMOUNT) AS EXSUM
    FROM FCostTable
    GROUP BY Ex_date
    """
    Ex_cur = Ex_conn.execute(Ex_exQuery)
    Ex_fetch = Ex_cur.fetchall()
    expenses_per_month = {}
    expenses = [0] * 12  # Initialize expenses list with zeros for all months
    for row in Ex_fetch:
        month = row[0]
        expenses_value = row[1]
        month_index = int(month) - 1
        expenses[month_index] = expenses_value
        expenses_per_month[month] = expenses_value
    Ex_cur.close()
    Ex_conn.close()
    return expenses_per_month, expenses


def plot_income_and_expenses_graph():
    plot_profit_graph()
    LearnLabel.destroy()
    GraphBtn_TOP_R_IN.destroy()
    income_per_month, income = fetch_income_data()
    (
        expenses_per_month,
        expenses,
    ) = fetch_expenses_data()  # Replace with your expense data fetching function
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    fig = Figure(figsize=(7, 5), dpi=80, facecolor="#333333")
    plot = fig.add_subplot(111)
    plot.spines["bottom"].set_color("orange")
    plot.spines["top"].set_color("orange")
    plot.spines["left"].set_color("red")
    plot.spines["right"].set_color("orange")
    plot.xaxis.label.set_color("yellow")
    plot.yaxis.label.set_color("yellow")
    plot.tick_params(axis="x", colors="white")
    plot.tick_params(axis="y", colors="white")
    plot.title.set_color("white")
    plot.set_facecolor("#333333")
    # Plot income
    # plot.bar(months, income,color="lightgray")
    plot.plot(
        months,
        income,
        color="green",
        marker="^",
        markersize=8,
        markerfacecolor="lightgreen",
    )
    # Plot expenses
    plot.plot(
        months,
        expenses,
        color=BGRED,
        marker="v",
        markersize=8,
        markerfacecolor=BGORANGE,
    )
    plot.set_xlabel(
        "A long the year",
        fontdict={"weight": "bold", "fontfamily": "Tahoma"}
    )
    plot.set_ylabel(
        "Amount per / Af",
        fontdict={"weight": "bold", "fontfamily": "Tahoma"}
    )
    plot.set_title(
        "Income and Expenses Per Month",
        fontdict={"weight": "bold", "fontfamily": "Tahoma"}
    )
    plot.legend(labels=["Income", "Expense"])

    canvas = FigureCanvasTkAgg(fig, master=GraphFrame_TOP_R)
    canvas.draw()
    canvas.get_tk_widget().pack(anchor=W)


GraphBtn_TOP_R_IN = ctk.CTkButton(
    GraphFrame_TOP_R,
    fg_color="#2D2D2D",
    text="مشاهده گراف",
    font=default_font_bold,
    command=plot_income_and_expenses_graph,
)
GraphBtn_TOP_R_IN.pack()

LearnLabel = ctk.CTkLabel(
    GraphFrame_TOP_R,
    text="به یاد داشته باشید \n\
    تا زمانی که  داده ای ذخیره نکنید \n\
    اینجا چیزی نمایش داده نمیشود\n\
    پس لطفاً اطلاعات تان را \n\
    ذخیره کنید و بعد تلاش کنید",
    justify=RIGHT,
    font=default_font_bold2,
)
LearnLabel.pack(anchor="e", pady=50)


# ------------- Profit ----------------
def fetch_profit_data1():
    Pf_conn = sqlite3.connect("DataBaseDir/PressDb.db")
    Pf_cur = Pf_conn.cursor()
    Pf_exQuery = """
    SELECT
    strftime('%Y-%m', FCostTable.FDATE) AS Month,
    SUM(FCostTable.FAMOUNT) AS FSUM1,
    SUM(EmployeeTableDone.DONE_ESALARY) AS ESUM1,
    SUM(LSTTable.STL_TTLPID) AS LSUM1,
    SUM(LaserTableEngraveDone.DONE_O_ENGR_TTLPID) AS ENSUM1,
    SUM(LaserTableCutDone.DONE_O_CUT_TTLPID) AS CTSUM1
    FROM
    FCostTable
    JOIN EmployeeTableDone ON
    strftime('%Y-%m', EmployeeTableDone.DONE_EJOINDATE) =
    strftime('%Y-%m', FCostTable.FDATE)
    JOIN LSTTable ON
    strftime('%Y-%m', LSTTable.STL_CURTIME ) =
    strftime('%Y-%m', FCostTable.FDATE)
    JOIN LaserTableEngraveDone ON
    strftime('%Y-%m', LaserTableEngraveDone.DONE_O_ENGR_CURTIME ) =
    strftime('%Y-%m', FCostTable.FDATE)
    JOIN LaserTableCutDone ON
    strftime('%Y-%m', LaserTableCutDone.DONE_O_CUT_CURTIME ) =
    strftime('%Y-%m', FCostTable.FDATE)
    GROUP BY Month
    """
    Pf_cur.execute(Pf_exQuery)
    Pf_fetch = Pf_cur.fetchall()
    profit_per_month = {}
    profit = [0] * 12  # Initialize profit list with zeros for all months
    for row in Pf_fetch:
        month = row[0]
        SUM1 = row[1]
        SUM2 = row[2]
        SUM3 = row[3]
        SUM4 = row[4]
        SUM5 = row[5]
        try:
            profit_value = int(int(SUM3 + SUM4 + SUM5) - int(SUM1 + SUM2))
            print(profit_value)
            month_index = int(month) - 1
            profit[month_index] = profit_value
            profit_per_month[month] = profit_value
        except:
            messagebox.showerror("Space4", "عاید خالص در دسترس نیست")

    Pf_cur.close()
    Pf_conn.close()
    return profit_per_month, profit


def plot_profit_graph():
    profit_per_month, profit = fetch_profit_data1()
    months1 = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    fig1 = Figure(figsize=(6, 5), dpi=80, facecolor="#333333")
    plot1 = fig1.add_subplot(111)
    plot1.spines["bottom"].set_color("orange")
    plot1.spines["top"].set_color("orange")
    plot1.spines["left"].set_color("red")
    plot1.spines["right"].set_color("orange")
    plot1.xaxis.label.set_color("yellow")
    plot1.yaxis.label.set_color("yellow")
    plot1.tick_params(axis="x", colors="white")
    plot1.tick_params(axis="y", colors="white")
    plot1.title.set_color("white")
    plot1.set_facecolor("#333333")
    # Plot income
    # plot1.bar(months1, profit,color="lightgray")
    plot1.plot(
        months1,
        profit,
        color=BGBLUE,
        marker="s",
        markersize=8,
        markerfacecolor="lightblue",
    )
    plot1.set_xlabel("A long the year", fontdict={"weight": "bold"})
    plot1.set_ylabel("Amount per / Af", fontdict={"weight": "bold"})
    plot1.set_title("Profit Per Month", fontdict={"weight": "bold"})
    plot1.legend(labels=["Profit"])

    canvas1 = FigureCanvasTkAgg(fig1, master=GraphFrame_TOP_L)
    canvas1.draw()
    canvas1.get_tk_widget().pack(anchor=W)



# ========================= Tab5 Display All ==========================
# ========================= Tab5 Display All ==========================
# ========================= Tab5 Display All ==========================
# ========================= Tab5 Display All ==========================
# ========================= Tab5 Display All ==========================
# ========================= Tab5 Display All ==========================
# ========================= Tab5 Display All ==========================


# ========================= Tab6 Store ==========================
# ========================= Tab6 Store ==========================
# ========================= Tab6 Store ==========================
# ========================= Tab6 Store ==========================
# ========================= Tab6 Store ==========================
# ========================= Tab6 Store ==========================
# ========================= Tab6 Store ==========================
#========================= Tab1_1 ============================
#========================= Tab1_1 ============================
#========================= Tab1_1 ============================
#========================= Tab1_1 ============================
SRMODEL = StringVar()
SRTYPE = StringVar()
SRGROUP = StringVar()
SRPRICE = StringVar()
SRQTT = StringVar()
SRDATE = StringVar()
SRNOTE = StringVar()
SEARCHVAR0 = StringVar()
SEARCHVAR1 = StringVar()


def SRSubmit():
    SRConn1 = sqlite3.connect("DataBaseDir/PressDb.db")
    SRCur1 = SRConn1.cursor()
    if strEnty2.get() == "":
        messagebox.showwarning(
            "ببخشید", "الزامی است که ورودی ها قبل از ذخیره پر شود."
        )
    else:
        if SRPRICE.get() == "" or SRQTT.get() == "":
            SRCur1.execute(
                f"""
                insert into StorageTable(
                SRMODEL,
                SRTYPE,
                SRGROUP,
                SRPRICE,
                SRQTT,
                SRDATE,
                SRNOTE
                )
                values(
                '{SRMODEL.get()}',
                '{SRTYPE.get()}',
                '{SRGROUP.get()}',
                0,
                0,
                '{SRDATE.get()}',
                '{SRNOTE.get()}'
                )
                """
            )

        else:
            SRCur1.execute(
                f"""
                insert into StorageTable(
                SRMODEL,
                SRTYPE,
                SRGROUP,
                SRPRICE,
                SRQTT,
                SRDATE,
                SRNOTE
                )
                values(
                '{SRMODEL.get()}',
                '{SRTYPE.get()}',
                '{SRGROUP.get()}',
                '{SRPRICE.get()}',
                '{SRQTT.get()}',
                '{SRDATE.get()}',
                '{SRNOTE.get()}'
                )
                """
            )

    SRConn1.commit()
    SRConn1.close()
    strEnty2.delete(0, END)
    strEnty3.delete(0, END)
    strEnty4.delete(0, END)
    strEnty5.delete(0, END)
    strEnty7.delete(0, END)
    strEnty1.focus()
    SRRef()


def SRRef():
    ReRef()
    TreeStg.delete(*TreeStg.get_children())
    TreeStgConn = sqlite3.connect("DataBaseDir/PressDb.db")
    TreeStgCor = TreeStgConn.execute(
        """
        SELECT
        SRNOTE,
        SRDATE,
        SRQTT,
        SRPRICE,
        SRGROUP,
        SRTYPE,
        SRMODEL,
        SRID
        FROM StorageTable
        """
    )
    fetchTreeStg = TreeStgCor.fetchall()
    for indexSR in fetchTreeStg:
        TreeStg.insert("", "end", values=indexSR)
    TreeStgCor.close()
    TreeStgConn.close()

    # Sooooold ----------------------------------------
    TreeStgSold.delete(*TreeStgSold.get_children())
    TreeStgSoldConn = sqlite3.connect("DataBaseDir/PressDb.db")
    TreeStgSoldCor = TreeStgSoldConn.execute(
        """
        SELECT
        SOLDNOTE,
        SOLDDATE,
        SOLDQTT,
        SOLDPRICE,
        SOLDGROUP,
        SOLDTYPE,
        SOLDMODEL,
        SOLDID
        FROM StorageSoldTable
        """
    )
    fetchTreeStgSold = TreeStgSoldCor.fetchall()
    for indexSRSold in fetchTreeStgSold:
        TreeStgSold.insert("", "end", values=indexSRSold)
    TreeStgSoldCor.close()
    TreeStgSoldConn.close()


    #----------------------------------------
    TreeStgSum.delete(*TreeStgSum.get_children())
    TreeStgSumConn = sqlite3.connect("DataBaseDir/PressDb.db")
    queryStgSum1 = """
    SELECT
    SUM(SRPRICE * SRQTT) AS SMG0
    FROM StorageTable
    """
    TreeStgSumCor = TreeStgSumConn.execute(queryStgSum1)
    fetchTreeStgSum = TreeStgSumCor.fetchall()
    for dataTreeStgSum in fetchTreeStgSum:
        SMG0 = dataTreeStgSum[0]
        try:
            SMGS = SMG0
            TreeStgSum.insert("", "end", values=(SMGS))
        except:
            SMGS = "هیچ"
            TreeStgSum.insert("", "end", values=(SMGS))
    TreeStgSumCor.close()
    TreeStgSumConn.close()


    #----------------------------------------
    TreeStgSum2.delete(*TreeStgSum2.get_children())
    TreeStgSum2Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    queryStgSum2 = """
    SELECT
    SUM(SOLDREALPRICE * SOLDQTT)
    FROM StorageSoldTable
    """
    TreeStgSum2Cor = TreeStgSum2Conn.execute(queryStgSum2)
    fetchTreeStgSum2 = TreeStgSum2Cor.fetchall()
    for dataTreeStgSum2 in fetchTreeStgSum2:
        SMG1 = dataTreeStgSum2[0]
        try:
            SMGS2 = SMG1
            TreeStgSum2.insert("", "end", values=(SMGS2))
        except:
            SMGS2 = "هیچ"
            TreeStgSum2.insert("", "end", values=(SMGS2))
    TreeStgSum2Cor.close()
    TreeStgSum2Conn.close()


    #----------------------------------------
    TSS3.delete(*TSS3.get_children())
    TSS3Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    queryStgSum3 = """
    SELECT
    SUM(SOLDPRICE * SOLDQTT),
    SUM(SOLDREALPRICE * SOLDQTT)
    FROM StorageSoldTable
    """
    TSS3Cor = TSS3Conn.execute(queryStgSum3)
    fetchTSS3 = TSS3Cor.fetchall()
    for dataTSS3 in fetchTSS3:
        SMG3_0 = dataTSS3[0]
        SMG3_1 = dataTSS3[1]
        try:
            SMGS3 = int(SMG3_0) - int(SMG3_1)
            TSS3.insert("", "end", values=(SMGS3))
        except:
            SMGS3 = "هیچ"
            TSS3.insert("", "end", values=(SMGS3))
    TSS3Cor.close()
    TSS3Conn.close()


    #----------------------------------------
    TSS4.delete(*TSS4.get_children())
    TSS4Conn = sqlite3.connect("DataBaseDir/PressDb.db")
    queryStgSum4 = """
    SELECT
    SUM(SOLDPRICE * SOLDQTT) AS SMG4
    FROM StorageSoldTable
    """
    TSS4Cor = TSS4Conn.execute(queryStgSum4)
    fetchTSS4 = TSS4Cor.fetchall()
    for dataTSS4 in fetchTSS4:
        SMG4 = dataTSS4[0]
        try:
            SMGS4 = SMG4
            TSS4.insert("", "end", values=(SMGS4))
        except:
            SMGS4 = "هیچ"
            TSS4.insert("", "end", values=(SMGS4))
    TSS4Cor.close()
    TSS4Conn.close()


def SRClear():
    strEnty6.delete(0, END)
    strEnty1.set("انتخاب نوع مواد")
    strEnty2.delete(0, END)
    strEnty3.delete(0, END)
    strEnty4.delete(0, END)
    strEnty5.delete(0, END)
    strEnty6.insert(0, DateNow)
    strEnty7.delete(0, END)
    strEnty1.focus()


def StrDeletFunc():
    StrSelected_item = TreeStg.selection()
    if StrSelected_item:
        for StrSelected_item in TreeStg.selection():
            conn = sqlite3.connect("DataBaseDir/PressDb.db")
            cur = conn.cursor()
            messageDelete = messagebox.askyesno(
                "هشدار", "؟آیا میخواهید این داده را حذف کنید"
            )
            if messageDelete > 0:
                cur.execute(
                    "DELETE FROM StorageTable WHERE SRID=?",
                    (TreeStg.set(StrSelected_item, "#8"),),
                )
                conn.commit()
                TreeStg.delete(StrSelected_item)
                conn.close()
                SRRef()
    else:
        messagebox.showwarning("Space4", "ریکارد انتخاب نشده")


def TreeSoldDeleteFunc():
    SoldSelected_item = TreeStgSold.selection()
    if SoldSelected_item:
        for SoldSelected_item in TreeStgSold.selection():
            conn = sqlite3.connect("DataBaseDir/PressDb.db")
            cur = conn.cursor()
            messageDelete = messagebox.askyesno(
                "هشدار", "؟آیا میخواهید این داده را حذف کنید"
            )
            if messageDelete > 0:
                cur.execute(
                    "DELETE FROM StorageSoldTable WHERE SOLDID=?",
                    (TreeStgSold.set(SoldSelected_item, "#8"),),
                )
                conn.commit()
                TreeStgSold.delete(SoldSelected_item)
                conn.close()
                SRRef()
    else:
        messagebox.showwarning("Space4", "ریکارد انتخاب نشده")




def EditingFuncStr():
    try:
        conn = sqlite3.connect("DataBaseDir/PressDb.db")
        cur1 = conn.cursor()
        selected_item = TreeStg.selection()[0]
        for selected_item in TreeStg.selection():
            LrQueryEdit = """
            SELECT
            SRMODEL,
            SRTYPE,
            SRGROUP,
            SRPRICE,
            SRQTT,
            SRDATE,
            SRNOTE
            FROM StorageTable
            WHERE SRID=?
            """
            cur1.execute(
                LrQueryEdit,
                (TreeStg.set(selected_item, "#8"),),
            )
            fetch1 = cur1.fetchall()
            for Row in fetch1:
                data1 = Row[0]
                data2 = Row[1]
                data3 = Row[2]
                data4 = Row[3]
                data5 = Row[4]
                data6 = Row[5]
                data7 = Row[6]
                SRClear()
                strEnty6.delete(0, END)

                strEnty1.set(data1)
                strEnty2.insert(0, data2)
                strEnty3.insert(0, data3)
                strEnty4.insert(0, data4)
                strEnty5.insert(0, data5)
                strEnty6.insert(0, data6)
                strEnty7.insert(0, data7)

        cur1.close()
        conn.close()
        strEnty1.focus()
    except:
        messagebox.showerror("Space4", "عدم  شناسایی  ریکارد منتخب")


def SaveUpdateFuncStr():
    if strEnty2.get() == "":
        messagebox.showerror("Space4", "نوعیت نا مشخص")
    else:
        if strEnty2.get() != "":
            dt1 = strEnty1.get()
            dt2 = strEnty2.get()
            dt3 = strEnty3.get()
            dt4 = strEnty4.get()
            dt5 = strEnty5.get()
            dt6 = strEnty6.get()
            dt7 = strEnty7.get()
            for selected_item in TreeStg.selection():
                conn = sqlite3.connect("DataBaseDir/PressDb.db")
                cur = conn.cursor()
                UpdQueryL = """
                UPDATE StorageTable
                SET
                SRMODEL=?,
                SRTYPE=?,
                SRGROUP=?,
                SRPRICE=?,
                SRQTT=?,
                SRDATE=?,
                SRNOTE=?
                WHERE SRID=?
                """
                cur.execute(
                    UpdQueryL,
                    (
                        dt1,
                        dt2,
                        dt3,
                        dt4,
                        dt5,
                        dt6,
                        dt7,
                        TreeStg.set(selected_item, "#8"),
                    ),
                )

                SRClear()
                messagebox.showinfo("Space4 Software", "! آپدیت موفقانه انجام شد")
                conn.commit()
                conn.close()
                SRRef()
        else:
            messagebox.showinfo("اوووه", "!!!ریکارد ذخیره نشد")




# ============ Storage Frames =============

StoreEnt_FrameTop_right = ctk.CTkFrame(master=tab1_1)
StoreEnt_FrameTop_right.grid(row=0, column=1, padx=5, pady=10, sticky=NE)

StoreTreeFrameTop_left = ctk.CTkFrame(master=tab1_1)
StoreTreeFrameTop_left.grid(row=0, column=0, padx=5, pady=10, rowspan=3, sticky=NE)


StoreBtnFrameBot_left = ctk.CTkFrame(master=tab1_1)
StoreBtnFrameBot_left.grid(row=1, column=1, padx=5, pady=10, sticky=NE)

StoreSumTreeFrameBot_right = ctk.CTkFrame(master=tab1_1)
StoreSumTreeFrameBot_right.grid(row=2, column=1, padx=5, pady=10, sticky=NE)


# ============ Labels and entries ===============

strLabel0 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="درج اقلام",
    font=default_font_bold,
    text_color=BGLIGHTGREEN,
)
strLabel0.grid(row=0, column=1, padx=5, pady=5, sticky=NE)

strLabel1 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="نوع مواد",
    font=default_font_bold,
)
strLabel1.grid(row=1, column=1, padx=5, pady=5, sticky=NE)

strLabel2 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="نام مواد",
    font=default_font_bold,
)
strLabel2.grid(row=2, column=1, padx=5, pady=5, sticky=NE)

strLabel3 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="طبقه",
    font=default_font_bold,
)
strLabel3.grid(row=3, column=1, padx=5, pady=5, sticky=NE)

strLabel4 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="قیمت فی",
    font=default_font_bold,
)
strLabel4.grid(row=4, column=1, padx=5, pady=5, sticky=NE)

strLabel5 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="تعداد",
    font=default_font_bold,
)
strLabel5.grid(row=5, column=1, padx=5, pady=5, sticky=NE)

strLabel6 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="تاریخ",
    font=default_font_bold,
)
strLabel6.grid(row=6, column=1, padx=5, pady=5, sticky=NE)

strLabel7 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="نوت",
    font=default_font_bold,
)
strLabel7.grid(row=7, column=1, padx=5, pady=5, sticky=NE)

# ================ Entry Part ===============
TValues_1 = [
    "اکرلیک",
    "چلنیوم",
    "الکوبان",
    "PVC",
    "LED",
    "دیگر"
]
SRMODEL.set("انتخاب نوع مواد")
strEnty1 = ctk.CTkComboBox(
    master=StoreEnt_FrameTop_right,
    font=default_font_bold,
    width=200,
    values=TValues_1,
    justify=RIGHT,
    variable=SRMODEL,
)
strEnty1.grid(row=1, column=0, padx=5, pady=5, sticky=NE)

strEnty2 = ctk.CTkEntry(
    master=StoreEnt_FrameTop_right,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=SRTYPE,
)
strEnty2.grid(row=2, column=0, padx=5, pady=5, sticky=NE)

strEnty3 = ctk.CTkEntry(
    master=StoreEnt_FrameTop_right,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=SRGROUP,
)
strEnty3.grid(row=3, column=0, padx=5, pady=5, sticky=NE)

strEnty4 = ctk.CTkEntry(
    master=StoreEnt_FrameTop_right,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=SRPRICE,
)
strEnty4.grid(row=4, column=0, padx=5, pady=5, sticky=NE)

strEnty5 = ctk.CTkEntry(
    master=StoreEnt_FrameTop_right,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=SRQTT,
)
strEnty5.grid(row=5, column=0, padx=5, pady=5, sticky=NE)

strEnty6 = ctk.CTkEntry(
    master=StoreEnt_FrameTop_right,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=SRDATE
)
strEnty6.grid(row=6, column=0, padx=5, pady=5, sticky=NE)
strEnty6.insert(0, DateNow)

strEnty7 = ctk.CTkEntry(
    master=StoreEnt_FrameTop_right,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=SRNOTE,
)
strEnty7.grid(row=7, column=0, padx=5, pady=5, sticky=NE)

# -------------------- Buttons tab1 -------------------
# -------------------- Buttons tab1 -------------------
StrSaveBtn1 = ctk.CTkButton(
    StoreBtnFrameBot_left,
    image=SaveImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="ذخیره",
    width=40,
    font=default_font_bold2,
    command=SRSubmit,
)
StrSaveBtn1.grid(row=0, column=5, padx=2, pady=2)
StrUpdateBtn1 = ctk.CTkButton(
    StoreBtnFrameBot_left,
    image=UpdateImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="آپدیت",
    width=40,
    font=default_font_bold2,
    command=SaveUpdateFuncStr
)
StrUpdateBtn1.grid(row=0, column=4, padx=2, pady=2)
StrClearBtn1 = ctk.CTkButton(
    StoreBtnFrameBot_left,
    image=ClearImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="پاک کردن",
    width=40,
    font=default_font_bold2,
    command=SRClear,
)
StrClearBtn1.grid(row=0, column=3, padx=2, pady=2)
StrEditBtn1 = ctk.CTkButton(
    StoreBtnFrameBot_left,
    image=EditImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="ویرایش",
    width=40,
    font=default_font_bold2,
    command=EditingFuncStr
)
StrEditBtn1.grid(row=0, column=2, padx=2, pady=2)
StrRefreshBtn1 = ctk.CTkButton(
    StoreBtnFrameBot_left,
    image=RefreshImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="تجدید ",
    width=40,
    font=default_font_bold2,
    command=SRRef,
)
StrRefreshBtn1.grid(row=0, column=1, padx=2, pady=2)
StrDeleteBtn1 = ctk.CTkButton(
    StoreBtnFrameBot_left,
    image=DeleteImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color="#2B2B2B",
    text="حذف",
    width=40,
    font=default_font_bold2,
    command=StrDeletFunc,
)
StrDeleteBtn1.grid(row=0, column=0, padx=2, pady=2)


# ============ Mini Treeview for Summing ============


# ============= Tree Storage and Selling options ============
# ============= Tree Storage and Selling options ============


def sell_item():
    for selected_item in TreeSellDebt.selection():
        conn = sqlite3.connect("DataBaseDir/PressDb.db")
        cur = conn.cursor()
        SlQueryEdit = """
        SELECT
        SLNAME,
        SLFNAME,
        SLADDR,
        SLMTYPE,
        SLQTTY,
        SLPRICE,
        SLDAMOUNT,
        SLDATE,
        SLNOTE
        FROM SellingDebtTable
        WHERE SLID=?
        """
        cur.execute(
            SlQueryEdit,
            (TreeSellDebt.set(selected_item, "#10"),),
        )

        fetch = cur.fetchall()
        for data in fetch:
            data0 = data[0]
            data1 = data[1]
            data2 = data[2]
            data3 = data[3]
            data4 = data[4]
            data5 = data[5]
            data6 = data[6]
            data7 = data[7]
            data8 = data[8]


        bill_text = "Space4 auto billing system.\n\n\
        Name: {}\n\
        FrName: {}\n\
        Address: {}\n\
        Material Type: {}\n\
        Quantity: {}\n\
        Total Price: {}\n\
        Debt amount: {}\n\
        Date: {}\n\
        Note: {}\n\n\n\
        آیا میخواهید چاپ کنید".format(
            data0,
            data1,
            data2,
            data3,
            data4,
            data5,
            data6,
            data7,
            data8,
        )

        conn.close()
        askme1 = messagebox.askyesno("Space4 factor generator", bill_text)
        if askme1 > 0:
            messagebox.showinfo("Space4", "بل شما به سیستم چاپگر تحویل شد")


def BillingFunc():
    SellRoot = ctk.CTkToplevel(root)
    SellRoot.title("Space4 software")
    SellRoot.iconbitmap('Space4.ico')
    SellRoot.geometry("+300+220")
    SellRoot.resizable(0, 0)
    SellRoot.grab_set()

    SLNAME = StringVar()
    SLFNAME = StringVar()
    SLADDR = StringVar()
    SLMTYPE = StringVar()
    SLQTTY = StringVar()
    SLPRICE = StringVar()
    SLDAMOUNT = StringVar()
    SLDATE = StringVar()
    SLNOTE = StringVar()


    def SellSubmit():
        DateNow = datetime.date.today()
        if SellCheck3.get() > 0:
            if SellEnty2.get() == "":
                messagebox.showerror("Space4", "ورودی نمیتواند خالی باشد")
            else:
                for selected_item0 in TreeStg.selection():
                    conn0 = sqlite3.connect("DataBaseDir/PressDb.db")
                    cur0 = conn0.cursor()
                    cur01 = conn0.cursor()
                    conn1 = cur0.execute(
                        """
                        SELECT
                        SRMODEL,
                        SRTYPE,
                        SRGROUP,
                        SRPRICE,
                        SRQTT,
                        SRDATE,
                        SRNOTE
                        FROM StorageTable
                        WHERE SRID=?
                        """,
                        (TreeStg.set(selected_item0, "#8"),),
                    )
                    fetch = cur0.fetchall()
                    for data in fetch:
                        data0 = data[0]
                        data1 = data[1]
                        data2 = data[2]
                        data3 = data[3]
                        data4 = data[4]
                        data5 = data[5]
                        data6 = data[6]
                        dtget1 = SellEnty1.get()
                        dtget2 = SellEnty2.get()
                        dtget3 = SellEnty3.get()
                        dtget4 = SellEnty4.get()
                        dtget5 = SellEnty5.get()
                        dtget6 = SellEnty6.get()
                        dtget7 = halfPayEnt7.get()
                        dataSum12 = int(dtget1)*int(dtget2)
                        dataSum7 = int(dataSum12) - int(dtget7)
                        if int(data4) > 0:
                            cur0.execute(
                                f"""
                                insert into StorageSoldTable (
                                SOLDMODEL,
                                SOLDTYPE,
                                SOLDGROUP,
                                SOLDPRICE,
                                SOLDQTT,
                                SOLDDATE,
                                SOLDNOTE,
                                SOLDREALPRICE
                                )
                                values(
                                '{data0}',
                                '{data1}',
                                '{data2}',
                                '{dtget1}',
                                '{dtget2}',
                                '{DateNow}',
                                '{dtget6}',
                                '{data3}'
                                )
                                """
                            )
                            try:
                                dtget_123 = int(dtget1) * int(dtget2)
                                dt3_4 = int(data3) * int(data4)
                                bill_text1 = "Space4 auto billing system.\n\n\
                                Model: {}\n\
                                Material Type: {}\n\
                                Group: {}\n\
                                Price: {}\n\
                                Quantity: {}\n\
                                Date: {}\n\
                                Note: {}\n\
                                Name: {}\n\
                                Debt Amount: {}\
                                ".format(
                                    data0,
                                    data1,
                                    data2,
                                    dtget_123,
                                    dtget2,
                                    data5,
                                    dtget6,
                                    dtget3,
                                    dataSum7
                                )
                                SoldCounter = int(data4) - int(dtget2)
                                cur01.execute(
                                    "UPDATE StorageTable SET SRQTT=? WHERE SRID=?",
                                    (SoldCounter, TreeStg.set(selected_item0, "#8")),
                                )
                                messagebox.showinfo("Space4", bill_text1)
                            except:
                                messagebox.showerror(
                                    "Space4", "ذخیره اطلاعات \
                                    روش انجام نشد"
                                )
                        else:
                            messagebox.showwarning(
                                "Space4",
                                "مدیر عزیز\nهیچ مواد در گدام موجود نیست\n\
                                اگر مواد موجود دارید لطف نموده\n\
                                اول به لیست گدام اضافه کنید \n\
                                و بعداً اقدام به فروش آن کنید",
                            )
                        cur2 = conn0.cursor()
                        cur2.execute(
                            f"""
                            insert into SellingDebtTable (
                            SLNAME,
                            SLFNAME,
                            SLADDR,
                            SLMTYPE,
                            SLQTTY,
                            SLPRICE,
                            SLDAMOUNT,
                            SLDATE,
                            SLNOTE
                            )
                            values(
                            '{dtget3}',
                            '{dtget4}',
                            '{dtget5}',
                            '{data1}',
                            '{dtget2}',
                            '{dataSum12}',
                            '{dataSum7}',
                            '{DateNow}',
                            '{dtget6}'
                            )
                            """
                        )
                        conn0.commit()
                        conn1.close()
                        conn0.close()
                        SellRoot.destroy()
                        SRRef()

        elif SellCheck3.get() < 1:
            for selected_item in TreeStg.selection():
                conn = sqlite3.connect("DataBaseDir/PressDb.db")
                cur = conn.cursor()
                conn1 = cur.execute(
                    """
                    SELECT
                    SRMODEL,
                    SRTYPE,
                    SRGROUP,
                    SRPRICE,
                    SRQTT,
                    SRDATE,
                    SRNOTE
                    FROM StorageTable
                    WHERE SRID=?
                    """,
                    (TreeStg.set(selected_item, "#8"),),
                )
                fetch = cur.fetchall()
                for data in fetch:
                    data0 = data[0]
                    data1 = data[1]
                    data2 = data[2]
                    data3 = data[3]
                    data4 = data[4]
                    data5 = data[5]
                    data6 = data[6]
                    dtget1 = SellEnty1.get()
                    dtget2 = SellEnty2.get()
                    dtget3 = SellEnty5.get()
                    dtget6 = SellEnty6.get()
                    if int(data4) > 0:
                        cur.execute(
                            f"""
                            insert into StorageSoldTable (
                            SOLDMODEL,
                            SOLDTYPE,
                            SOLDGROUP,
                            SOLDPRICE,
                            SOLDQTT,
                            SOLDDATE,
                            SOLDNOTE,
                            SOLDREALPRICE
                            )
                            values(
                            '{data0}',
                            '{data1}',
                            '{data2}',
                            '{dtget1}',
                            '{dtget2}',
                            '{DateNow}',
                            '',
                            '{data3}'
                            )
                            """
                        )

                        try:
                            dtget_123 = int(dtget1) * int(dtget2)
                            dt3_4 = int(data3) * int(data4)
                            bill_text1 = "Space4 auto billing system.\n\n\
                            Model: {}\n\
                            Material Type: {}\n\
                            Group: {}\n\
                            Price: {}\n\
                            Quantity: {}\n\
                            Date: {}\n\
                            Note: {}\n".format(
                                data0,
                                data1,
                                data2,
                                dtget_123,
                                dtget2,
                                data5,
                                ""
                            )
                            SoldCounter = int(data4) - int(dtget2)
                            cur.execute(
                                "UPDATE StorageTable SET SRQTT=? WHERE SRID=?",
                                (SoldCounter, TreeStg.set(selected_item, "#8")),
                            )
                            messagebox.showinfo("Space4", bill_text1)
                        except:
                            messagebox.showerror(
                                "Space4", "ذخیره اطلاعات \
                                روش انجام نشد"
                            )
                    else:
                        messagebox.showwarning(
                            "Space4",
                            "مدیر عزیز\nهیچ مواد در گدام موجود نیست\n\
                            اگر مواد موجود دارید لطف نموده\n\
                            اول به لیست گدام اضافه کنید \n\
                            و بعداً اقدام به فروش آن کنید",
                        )
                    conn.commit()
                    conn1.close()
                    conn.close()
                    SellRoot.destroy()
                    SRRef()

    def CheckBoxDebFunc():
        if SellCheck3.get() > 0:
            # SellEnty1.configure(state=NORMAL, font=default_font_bold)
            # SellEnty2.configure(state=NORMAL, font=default_font_bold)
            SellEnty3.configure(
                state=NORMAL,
                font=default_font_bold,
                border_width=2
                )
            SellEnty4.configure(
                state=NORMAL,
                font=default_font_bold,
                border_width=2
                )
            SellEnty5.configure(
                state=NORMAL,
                font=default_font_bold,
                border_width=2
                )
            SellEnty6.configure(
                state=NORMAL,
                font=default_font_bold,
                border_width=2
                )
            halfPayEnt7.configure(
                state=NORMAL,
                font=default_font_bold,
                border_width=2
                )
            SellEnty3.focus()
        elif SellCheck3.get() < 1:
            # SellEnty1.configure(state=DISABLED, font=default_font_bold)
            # SellEnty2.configure(state=DISABLED, font=default_font_bold)
            SellEnty3.configure(
                state=DISABLED,
                font=default_font_bold,
                border_width=0
                )
            SellEnty4.configure(
                state=DISABLED,
                font=default_font_bold,
                border_width=0
                )
            SellEnty5.configure(
                state=DISABLED,
                font=default_font_bold,
                border_width=0
                )
            SellEnty6.configure(
                state=DISABLED,
                font=default_font_bold,
                border_width=0
                )
            halfPayEnt7.configure(
                state=DISABLED,
                font=default_font_bold,
                border_width=0
                )
            SellEnty1.focus()

    SellTitleLbl = ctk.CTkLabel(
        SellRoot,
        text="فروش مواد",
        justify=RIGHT,
        font=default_font_bold,
        text_color=BGLIGHTGREEN,
    )
    SellTitleLbl.grid(row=0, column=1, padx=5, pady=5, sticky=NE)

    SellLabel1 = ctk.CTkLabel(
        master=SellRoot,
        text="قیمت فی",
        font=default_font_bold,
    )
    SellLabel1.grid(row=1, column=1, padx=5, pady=5, sticky=NE)

    SellLabel2 = ctk.CTkLabel(
        master=SellRoot,
        text="تعداد",
        font=default_font_bold,
    )
    SellLabel2.grid(row=2, column=1, padx=5, pady=5, sticky=NE)
    SellCheck3 = ctk.CTkCheckBox(
        SellRoot,
        onvalue=1,
        offvalue=0,
        text="قرضه",
        font=default_font_bold,
        text_color=BGLIGHTGREEN,
        fg_color="#2B2B2B",
        hover_color=BGLIGHTGREEN,
        command=CheckBoxDebFunc
    )
    SellCheck3.grid(row=3, column=1, padx=5, pady=5, sticky=E)
    SellLabel4 = ctk.CTkLabel(
        master=SellRoot,
        text="نام مشتری",
        font=default_font_bold,
    )
    SellLabel4.grid(row=4, column=1, padx=5, pady=5, sticky=NE)
    SellLabel5 = ctk.CTkLabel(
        master=SellRoot,
        text="نام پدر",
        font=default_font_bold,
    )
    SellLabel5.grid(row=5, column=1, padx=5, pady=5, sticky=NE)
    SellLabel6 = ctk.CTkLabel(
        master=SellRoot,
        text="آدرس",
        font=default_font_bold,
    )
    SellLabel6.grid(row=6, column=1, padx=5, pady=5, sticky=NE)
    SellLabel7 = ctk.CTkLabel(
        master=SellRoot,
        text="نوت",
        font=default_font_bold,
    )
    SellLabel7.grid(row=7, column=1, padx=5, pady=5, sticky=NE)
    SellLabel8 = ctk.CTkLabel(
        master=SellRoot,
        text="مقدار نقده",
        font=default_font_bold,
    )
    SellLabel8.grid(row=8, column=1, padx=5, pady=5, sticky=NE)

    #--------- Entry ------------
    SellEnty1 = ctk.CTkEntry(
        master=SellRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
        placeholder_text="قیمت را وارد کنید",
    )
    SellEnty1.focus()
    SellEnty1.grid(row=1, column=0, padx=5, pady=5, sticky=NE)

    SellEnty2 = ctk.CTkEntry(
        master=SellRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
        placeholder_text="تعداد را وارد کنید",
    )
    SellEnty2.grid(row=2, column=0, padx=5, pady=5, sticky=NE)
    SellEnty3 = ctk.CTkEntry(
        master=SellRoot,
        state=DISABLED,
        border_width=0,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SellEnty3.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
    SellEnty4 = ctk.CTkEntry(
        master=SellRoot,
        state=DISABLED,
        border_width=0,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SellEnty4.grid(row=5, column=0, padx=5, pady=5, sticky=NE)
    SellEnty5 = ctk.CTkEntry(
        master=SellRoot,
        state=DISABLED,
        border_width=0,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SellEnty5.grid(row=6, column=0, padx=5, pady=5, sticky=NE)
    SellEnty6 = ctk.CTkEntry(
        master=SellRoot,
        state=DISABLED,
        border_width=0,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SellEnty6.grid(row=7, column=0, padx=5, pady=5, sticky=NE)
    halfPayEnt7 = ctk.CTkEntry(
        master=SellRoot,
        state=DISABLED,
        border_width=0,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
        placeholder_text="مقدار نقده را وارد کنید"
    )
    halfPayEnt7.grid(row=8, column=0, padx=5, pady=10, sticky=NE)

    SellSaveBtn = ctk.CTkButton(
        SellRoot,
        text="فروش",
        font=default_font_bold,
        fg_color="#2B2B2B",
        hover_color=BGLIGHTGREEN,
        command=SellSubmit
    )
    SellSaveBtn.grid(row=9, column=0, padx=5, pady=10, sticky=NE)

    SellRoot.mainloop()
    # ===================================================
    # ===================== Sell Root Ended =============
def ViewPriceFunc():
    for selected_item in TreeStg.selection():
        conn = sqlite3.connect("DataBaseDir/PressDb.db")
        cur = conn.cursor()
        conn1 = cur.execute(
            """
            SELECT
            SUM(SRPRICE*SRQTT) AS SUM0,
            SRTYPE,
            SRQTT
            FROM StorageTable
            WHERE SRID=?
            """,
            (TreeStg.set(selected_item, "#8"),),
        )
        fetch = cur.fetchall()
        for data in fetch:
            dataSum1 = data[0]
            dataSum2 = data[1]
            dataSum3 = data[2]
            try:
                messagebox.showinfo(
                    "Space4",
                    f"\tTotal: {dataSum1}\n\
                    Name: {dataSum2}\n\
                    Qtty: {dataSum3}"
                )
            except:
                messagebox.showerror("Space4 Error", "مواد شناسای نشد\n\
                    مشکل احتمالاً از طریقه وارد کردن داده  خود شما است")
        conn1.close()
        conn.close()






def SearchFunc1():
    if SEARCHVAR0.get() == "01":
        if searchEnt1.get() != "":
            TreeStg.delete(*TreeStg.get_children())
            Sconn = sqlite3.connect("DataBaseDir/PressDb.db")
            Scur = Sconn.execute(
                """
                SELECT
                SRNOTE,
                SRDATE,
                SRQTT,
                SRPRICE,
                SRGROUP,
                SRTYPE,
                SRMODEL,
                SRID
                FROM StorageTable
                WHERE SRMODEL LIKE?
                """,
                ("%" + str(searchEnt1.get()) + "%",),
            )
            Sfetch = Scur.fetchall()
            for Sdata in Sfetch:
                TreeStg.insert("", "end", values=(Sdata))
        else:
            messagebox.showinfo("Space4", "لطفاً نوع مواد را وارد کنید")

    elif SEARCHVAR0.get() == "02":
        if searchEnt1.get() != "":
            TreeStg.delete(*TreeStg.get_children())
            Sconn = sqlite3.connect("DataBaseDir/PressDb.db")
            Scur = Sconn.execute(
                """
                SELECT
                SRNOTE,
                SRDATE,
                SRQTT,
                SRPRICE,
                SRGROUP,
                SRTYPE,
                SRMODEL,
                SRID
                FROM StorageTable
                WHERE SRTYPE LIKE?
                """,
                ("%" + str(searchEnt1.get()) + "%",),
            )
            Sfetch = Scur.fetchall()
            for Sdata in Sfetch:
                TreeStg.insert("", "end", values=(Sdata))
        else:
            messagebox.showinfo("Space4", "لطفاً نوع مواد را وارد کنید")

    elif SEARCHVAR0.get() == "03":
        if searchEnt1.get() != "":
            TreeStg.delete(*TreeStg.get_children())
            Sconn = sqlite3.connect("DataBaseDir/PressDb.db")
            Scur = Sconn.execute(
                """
                SELECT
                SRNOTE,
                SRDATE,
                SRQTT,
                SRPRICE,
                SRGROUP,
                SRTYPE,
                SRMODEL,
                SRID
                FROM StorageTable
                WHERE SRGROUP LIKE?
                """,
                ("%" + str(searchEnt1.get()) + "%",),
            )
            Sfetch = Scur.fetchall()
            for Sdata in Sfetch:
                TreeStg.insert("", "end", values=(Sdata))
        else:
            messagebox.showinfo("Space4", "لطفاً نوع مواد را وارد کنید")
    else:
        messagebox.showerror("Space4", "لطفاً  یکی از گزینه های زیر را در سمت راست \n\
            .ورودی جستجو انتخاب کنید و دوباره جستجو کنید\n\
            نوع مواد\n\
            نام مواد\n\
            طبقه مواد")


#------ O Laser Radiobuttons -----------

ORadioTypeFrame = ctk.CTkFrame(
    StoreTreeFrameTop_left,
    corner_radius=5,
    fg_color=TKDARK
)
ORadioTypeFrame.place(x=5, y=5)
#Radio Main Frame
ORadio1_1 = ctk.CTkRadioButton(
    ORadioTypeFrame,
    variable=SEARCHVAR0,
    font=default_font_bold1,
    text="طبقه مواد",
    width=20,
    hover_color=BGLIGHTGREEN,
    fg_color="#2B2B2B",
    value="03",
)
ORadio1_1.grid(row=0, column=0, sticky=E, padx=5, pady=3)
ORadio1_2 = ctk.CTkRadioButton(
    ORadioTypeFrame,
    variable=SEARCHVAR0,
    font=default_font_bold1,
    text="نام مواد",
    width=20,
    hover_color=BGLIGHTGREEN,
    fg_color="#2B2B2B",
    value="02",
)
ORadio1_2.grid(row=0, column=1, sticky=E, padx=5, pady=3)
ORadio1_3 = ctk.CTkRadioButton(
    ORadioTypeFrame,
    variable=SEARCHVAR0,
    font=default_font_bold1,
    text="نوع مواد",
    width=20,
    hover_color=BGLIGHTGREEN,
    fg_color="#2B2B2B",
    value="01",
)
ORadio1_3.grid(row=0, column=2, sticky=E, padx=5,pady=3)

# -----------------------
searchFrm1 = ctk.CTkFrame(
    StoreTreeFrameTop_left,
    corner_radius=5,
    fg_color=TKDARK
    )
searchFrm1.place(x=340,y=5)

searchBtn1 = ctk.CTkButton(
    master=searchFrm1,
    text="جستجو",
    font=default_font_bold,
    width=70,
    fg_color="#2B2B2B",
    command=SearchFunc1
    )
searchBtn1.grid(row=0,column=0,sticky=NE,padx=10)

searchEnt1 = ctk.CTkEntry(
    master=searchFrm1,
    placeholder_text="جستجوی مواد",
    justify=RIGHT,
    font=default_font_bold,
    width=150
    )
searchEnt1.grid(row=0,column=1,sticky=NE,padx=2)



# =======================================================

TreeStorageLbl = ctk.CTkLabel(
    master=StoreTreeFrameTop_left,
    text="لیست مواد موجوده",
    font=default_font_bold,
    text_color=("teal", BGLIGHTGREEN),
    justify=RIGHT,
)
TreeStorageLbl.grid(row=0, column=0, padx=20, pady=5, sticky=NE)

TreeStrFrame = ctk.CTkFrame(StoreTreeFrameTop_left)
TreeStrFrame.grid(row=1, column=0, padx=5, sticky=NE)
TreeStg = ttk.Treeview(
    TreeStrFrame,
    columns=("L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8"),
    selectmode="extended",
    height=8,
    style='MyStyle.Treeview'
)
TreeStg.heading("L1", text="نوت", anchor=E)
TreeStg.heading("L2", text="تاریخ", anchor=E)
TreeStg.heading("L3", text="تعداد", anchor=E)
TreeStg.heading("L4", text="قیمت فی", anchor=E)
TreeStg.heading("L5", text="طبقه", anchor=E)
TreeStg.heading("L6", text="نام مواد", anchor=E)
TreeStg.heading("L7", text="نوع مواد", anchor=E)
TreeStg.heading("L8", text="ID", anchor=E)

TreeStg.column("#0", stretch=NO, minwidth=0, width=0)
TreeStg.column("#1", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStg.column("#2", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStg.column("#3", stretch=NO, minwidth=0, width=70, anchor=E)
TreeStg.column("#4", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStg.column("#5", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStg.column("#6", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStg.column("#7", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStg.column("#8", stretch=NO, minwidth=0, width=60, anchor=E)
TreeStg.grid(padx=0, pady=0)


TreeStg.delete(*TreeStg.get_children())
TreeStgConn = sqlite3.connect("DataBaseDir/PressDb.db")
TreeStgCor = TreeStgConn.execute(
    """
    SELECT
    SRNOTE,
    SRDATE,
    SRQTT,
    SRPRICE,
    SRGROUP,
    SRTYPE,
    SRMODEL,
    SRID
    FROM StorageTable
    """
)
fetchTreeStg = TreeStgCor.fetchall()
for indexSR in fetchTreeStg:
    TreeStg.insert("", "end", values=indexSR)
TreeStgCor.close()
TreeStgConn.close()


def SellPopup(event):
    try:
        selectedRow = TreeStg.selection()[0]
        SellMenu = Menu(
            TreeStg,
            tearoff=0,
            font=default_font_bold1,
            bg=CTKDARK,
            fg=CTKLIGHT,
            activebackground=BGLIGHTGREEN,
        )
        SellMenu.add_command(
            compound=LEFT,
            image=SellImg_1,
            label="فروش",
            command=BillingFunc
        )
        SellMenu.add_command(
            compound=LEFT,
            image=PriceImg1,
            label="مشاهده قیمت",
            command=ViewPriceFunc
        )
        SellMenu.add_command(
            compound=LEFT,
            image=DeleteImg_1,
            label="حذف",
            command=StrDeletFunc
        )
        SellMenu.add_command(
            compound=LEFT,
            image=RefreshImg_1,
            label="تجدید",
            command=SRRef
        )
        SellMenu.add_command(
            compound=LEFT,
            image=EditImg_1,
            label="ویرایش",
            command=EditingFuncStr
        )
        SellMenu.add_command(
            compound=LEFT,
            image=UpdateImg_1,
            label="ذخیره تغییرات",
            command=SaveUpdateFuncStr
            )
        try:
            SellMenu.tk_popup(event.x_root, event.y_root)
        finally:
            SellMenu.grab_release()
    except:
        messagebox.showinfo("اوووه", "! ریکارد را انتخاب کنید لطفاً")


TreeStg.bind("<Button-3>", SellPopup)


# ============== Sold Tree view =====================
# ============== Sold Tree view =====================

TreeStorageLblSold = ctk.CTkLabel(
    master=StoreTreeFrameTop_left,
    text="لیست مواد فروخته شده",
    font=default_font_bold,
    text_color=("teal", BGLIGHTGREEN),
    justify=RIGHT,
)
TreeStorageLblSold.grid(row=2, column=0, padx=20, pady=5, sticky=NE)


TreeStrFrameSold = ctk.CTkFrame(StoreTreeFrameTop_left)
TreeStrFrameSold.grid(row=3, column=0, padx=5, sticky=NE)
TreeStgSold = ttk.Treeview(
    TreeStrFrameSold,
    columns=("L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8"),
    selectmode="browse",
    height=8,
)
TreeStgSold.heading("L1", text="نوت", anchor=E)
TreeStgSold.heading("L2", text="تاریخ", anchor=E)
TreeStgSold.heading("L3", text="تعداد", anchor=E)
TreeStgSold.heading("L4", text="قیمت فی", anchor=E)
TreeStgSold.heading("L5", text="طبقه", anchor=E)
TreeStgSold.heading("L6", text="نام مواد", anchor=E)
TreeStgSold.heading("L7", text="نوع مواد", anchor=E)
TreeStgSold.heading("L8", text="ID", anchor=E)

TreeStgSold.column("#0", stretch=NO, minwidth=0, width=0)
TreeStgSold.column("#1", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStgSold.column("#2", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStgSold.column("#3", stretch=NO, minwidth=0, width=70, anchor=E)
TreeStgSold.column("#4", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStgSold.column("#5", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStgSold.column("#6", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStgSold.column("#7", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStgSold.column("#8", stretch=NO, minwidth=0, width=60, anchor=E)
TreeStgSold.grid(padx=0, pady=0)


TreeStgSold.delete(*TreeStgSold.get_children())
TreeStgSoldConn = sqlite3.connect("DataBaseDir/PressDb.db")
TreeStgSoldCor = TreeStgSoldConn.execute(
    """
    SELECT
    SOLDNOTE,
    SOLDDATE,
    SOLDQTT,
    SOLDPRICE,
    SOLDGROUP,
    SOLDTYPE,
    SOLDMODEL,
    SOLDID
    FROM StorageSoldTable
    """
)
fetchTreeStgSold = TreeStgSoldCor.fetchall()
for indexSRSold in fetchTreeStgSold:
    TreeStgSold.insert("", "end", values=indexSRSold)
TreeStgSoldCor.close()
TreeStgSoldConn.close()

#--------------------------------
def SellPopup1(event):
    try:
        selectedRow = TreeStgSold.selection()[0]
        SellMenu = Menu(
            TreeStgSold,
            tearoff=0,
            font=default_font_bold1,
            bg=CTKDARK,
            fg=CTKLIGHT,
            activebackground=BGLIGHTGREEN,
        )
        SellMenu.add_command(
            compound=LEFT,
            image=DeleteImg_1,
            label="حذف",
            command=TreeSoldDeleteFunc
        )
        try:
            SellMenu.tk_popup(event.x_root, event.y_root)
        finally:
            SellMenu.grab_release()
    except:
        messagebox.showinfo("اوووه", "! ریکارد را انتخاب کنید لطفاً")


TreeStgSold.bind("<Button-3>", SellPopup1)

#=----------- Popup end---------------
# ------- Costs ------------

TreeStgSumFrame1 = ctk.CTkFrame(StoreSumTreeFrameBot_right)
TreeStgSumFrame1.grid(row=0, column=1, padx=10, pady=10, sticky=W)
TreeStgSum = ttk.Treeview(
    TreeStgSumFrame1,
    columns=("S1"),
    selectmode="none",
    height=1
)
TreeStgSum.heading("S1", text="ارزش مواد موجود", anchor=E)
TreeStgSum.column("#0", stretch=NO, minwidth=0, width=0)
TreeStgSum.column("#1", stretch=NO, minwidth=0, width=120, anchor=E)
TreeStgSum.grid()


TreeStgSum.delete(*TreeStgSum.get_children())
TreeStgSumConn = sqlite3.connect("DataBaseDir/PressDb.db")
queryStgSum1 = """
SELECT
SUM(SRPRICE * SRQTT) AS SMG0
FROM StorageTable
"""
TreeStgSumCor = TreeStgSumConn.execute(queryStgSum1)
fetchTreeStgSum = TreeStgSumCor.fetchall()
for dataTreeStgSum in fetchTreeStgSum:
    SMG0 = dataTreeStgSum[0]
    try:
        SMGS = SMG0
        TreeStgSum.insert("", "end", values=(SMGS))
    except:
        SMGS = "هیچ"
        TreeStgSum.insert("", "end", values=(SMGS))
TreeStgSumCor.close()
TreeStgSumConn.close()


# ----------------------------------------------
TreeStgSumFrame2 = ctk.CTkFrame(StoreSumTreeFrameBot_right)
TreeStgSumFrame2.grid(row=0, column=0, padx=10, pady=10, sticky=W)
TreeStgSum2 = ttk.Treeview(
    TreeStgSumFrame2, columns=("S1"), selectmode="none", height=1
)
TreeStgSum2.heading("S1", text="قیمت خالص فروش", anchor=E)
TreeStgSum2.column("#0", stretch=NO, minwidth=0, width=0)
TreeStgSum2.column("#1", stretch=NO, minwidth=0, width=130, anchor=E)
TreeStgSum2.grid()


TreeStgSum2.delete(*TreeStgSum2.get_children())
TreeStgSum2Conn = sqlite3.connect("DataBaseDir/PressDb.db")
queryStgSum2 = """
SELECT
SUM(SOLDREALPRICE * SOLDQTT)
FROM StorageSoldTable
"""
TreeStgSum2Cor = TreeStgSum2Conn.execute(queryStgSum2)
fetchTreeStgSum2 = TreeStgSum2Cor.fetchall()
for dataTreeStgSum2 in fetchTreeStgSum2:
    SMG1 = dataTreeStgSum2[0]
    try:
        SMGS2 = SMG1
        TreeStgSum2.insert("", "end", values=(SMGS2))
    except:
        SMGS2 = "هیچ"
        TreeStgSum2.insert("", "end", values=(SMGS2))
TreeStgSum2Cor.close()
TreeStgSum2Conn.close()


# ==========================================
# ==========================================

TSSF3 = ctk.CTkFrame(StoreSumTreeFrameBot_right)
TSSF3.grid(row=1, column=1, padx=10, pady=10, sticky=W)
TSS3 = ttk.Treeview(TSSF3, columns=("S1"), selectmode="none", height=1)
TSS3.heading("S1", text="مفاد خالص", anchor=E)
TSS3.column("#0", stretch=NO, minwidth=0, width=0)
TSS3.column("#1", stretch=NO, minwidth=0, width=120, anchor=E)
TSS3.grid()


TSS3.delete(*TSS3.get_children())
TSS3Conn = sqlite3.connect("DataBaseDir/PressDb.db")
queryStgSum3 = """
SELECT
SUM(SOLDPRICE * SOLDQTT),
SUM(SOLDREALPRICE * SOLDQTT)
FROM StorageSoldTable
"""
TSS3Cor = TSS3Conn.execute(queryStgSum3)
fetchTSS3 = TSS3Cor.fetchall()
for dataTSS3 in fetchTSS3:
    SMG3_0 = dataTSS3[0]
    SMG3_1 = dataTSS3[1]
    try:
        SMGS3 = int(SMG3_0) - int(SMG3_1)
        TSS3.insert("", "end", values=(SMGS3))
    except:
        SMGS3 = "هیچ"
        TSS3.insert("", "end", values=(SMGS3))
TSS3Cor.close()
TSS3Conn.close()


# ----------------------------------------------
TSSF4 = ctk.CTkFrame(StoreSumTreeFrameBot_right)
TSSF4.grid(row=1, column=0, padx=10, pady=10, sticky=W)
TSS4 = ttk.Treeview(TSSF4, columns=("S1"), selectmode="none", height=1)
TSS4.heading("S1", text="مجموعه فروشات", anchor=E)
TSS4.column("#0", stretch=NO, minwidth=0, width=0)
TSS4.column("#1", stretch=NO, minwidth=0, width=130, anchor=E)
TSS4.grid()


TSS4.delete(*TSS4.get_children())
TSS4Conn = sqlite3.connect("DataBaseDir/PressDb.db")
queryStgSum4 = """
SELECT
SUM(SOLDPRICE * SOLDQTT) AS SMG4
FROM StorageSoldTable
"""
TSS4Cor = TSS4Conn.execute(queryStgSum4)
fetchTSS4 = TSS4Cor.fetchall()
for dataTSS4 in fetchTSS4:
    SMG4 = dataTSS4[0]
    try:
        SMGS4 = SMG4
        TSS4.insert("", "end", values=(SMGS4))
    except:
        SMGS4 = "هیچ"
        TSS4.insert("", "end", values=(SMGS4))
TSS4Cor.close()
TSS4Conn.close()

#========================= Tab1_2 ============================
#========================= Tab1_2 ============================
#========================= Tab1_2 ============================
#========================= Tab1_2 ============================

def TreeSellDebtDeleteFunc():
    SellS_item = TreeSellDebt.selection()
    if SellS_item:
        for SellS_item in TreeSellDebt.selection():
            conn = sqlite3.connect("DataBaseDir/PressDb.db")
            cur = conn.cursor()
            messageDelete = messagebox.askyesno(
                "هشدار", "؟آیا میخواهید این داده را حذف کنید"
            )
            if messageDelete > 0:
                cur.execute(
                    "DELETE FROM SellingDebtTable WHERE SLID=?",
                    (TreeSellDebt.set(SellS_item, "#10"),),
                )
                conn.commit()
                TreeSellDebt.delete(SellS_item)
                conn.close()
                ReRef()
    else:
        messagebox.showwarning("Space4", "ریکارد انتخاب نشده")


def SRepayFunc():
    if RepayEnt1.get() != "":
        dt1 = RepayEnt1.get()
        for SL_item1 in TreeSellDebt.selection():
            conn = sqlite3.connect("DataBaseDir/PressDb.db")
            cur = conn.cursor()
            conn1 = cur.execute(
                "SELECT SLDAMOUNT FROM SellingDebtTable WHERE SLID=?",
                (TreeSellDebt.set(SL_item1, "#10"),),
            )
            fetch = cur.fetchall()
            for data in fetch:
                data0 = data[0]
                addm = int(data0) - int(dt1)
                cur.execute(
                    "UPDATE SellingDebtTable SET SLDAMOUNT=? WHERE SLID=?",
                    (addm, TreeSellDebt.set(SL_item1, "#10")),
                )
                RepayEnt1.delete(0, END)
                messagebox.showinfo("Space4 Software", "!رسید موفقانه  درج گردید")
                conn.commit()
                conn1.close()
                conn.close()
                ReRef()
    else:
        messagebox.showinfo("اوووه", "رسید درج نگردید")

def ReRef():
    TreeSellDebt.delete(*TreeSellDebt.get_children())
    TreeSellDebtConn = sqlite3.connect("DataBaseDir/PressDb.db")
    TreeSellDebtCor = TreeSellDebtConn.execute(
        """
        SELECT
        SLNOTE,
        SLDATE,
        SLPRICE,
        SLDAMOUNT,
        SLQTTY,
        SLMTYPE,
        SLADDR,
        SLFNAME,
        SLNAME,
        SLID
        FROM SellingDebtTable
        """
    )
    fetchTreeSellDebt = TreeSellDebtCor.fetchall()
    for indexSellD in fetchTreeSellDebt:
        TreeSellDebt.insert("", "end", values=indexSellD)
    TreeSellDebtCor.close()
    TreeSellDebtConn.close()


def PersonSearchFunc():
    if searchEntSell1.get() != "":
        TreeSellDebt.delete(*TreeSellDebt.get_children())
        Sconn = sqlite3.connect("DataBaseDir/PressDb.db")
        Scur = Sconn.execute(
            """
            SELECT
            SLNOTE,
            SLDATE,
            SLPRICE,
            SLDAMOUNT,
            SLQTTY,
            SLMTYPE,
            SLADDR,
            SLFNAME,
            SLNAME,
            SLID
            FROM SellingDebtTable
            WHERE SLNAME LIKE?
            """,
            ("%" + str(searchEntSell1.get()) + "%",),
        )
        Sfetch = Scur.fetchall()
        for Sdata in Sfetch:
            TreeSellDebt.insert("", "end", values=(Sdata))
    else:
        messagebox.showinfo("Space4", "لطفاً نام شخص مرود نظر را وارد کنید")


def InsertNewDebtFunc():
    if NewDebtEnt1.get() != "":
        dt1 = NewDebtEnt1.get()
        for SL_item1 in TreeSellDebt.selection():
            conn = sqlite3.connect("DataBaseDir/PressDb.db")
            cur = conn.cursor()
            conn1 = cur.execute(
                "SELECT SLDAMOUNT FROM SellingDebtTable WHERE SLID=?",
                (TreeSellDebt.set(SL_item1, "#10"),),
            )
            fetch = cur.fetchall()
            for data in fetch:
                data0 = data[0]
                addm1 = int(data0) + int(dt1)
                cur.execute(
                    "UPDATE SellingDebtTable SET SLDAMOUNT=?, SLPRICE=? WHERE SLID=?",
                    (addm1,addm1, TreeSellDebt.set(SL_item1, "#10")),
                )
                NewDebtEnt1.delete(0, END)
                messagebox.showinfo("Space4 Software", "!رسید موفقانه  درج گردید")
                conn.commit()
                conn1.close()
                conn.close()
                ReRef()


# def EditDebtFunc():
#     try:
#         conn = sqlite3.connect("DataBaseDir/PressDb.db")
#         cur1 = conn.cursor()
#         selected_item = TreeStg.selection()[0]
#         for selected_item in TreeStg.selection():
#             DebQuery = """
#             SELECT
#             SLNAME,
#             SLFNAME,
#             SLADDR,
#             SLMTYPE,
#             SLQTTY,
#             SLPRICE,
#             SLDAMOUNT,
#             SLDATE,
#             SLNOTE
#             FROM SellingDebtTable
#             WHERE SLID=?
#             """
#             cur1.execute(
#                 DebQuery,
#                 (TreeStg.set(selected_item, "#10"),),
#             )
#             fetch1 = cur1.fetchall()
#             for Row in fetch1:
#                 data1 = Row[0]
#                 data2 = Row[1]
#                 data3 = Row[2]
#                 data4 = Row[3]
#                 data5 = Row[4]
#                 data6 = Row[5]
#                 data7 = Row[6]
#                 SRClear()
#                 strEnty6.delete(0, END)
#                 strEnty1.set(data1)
#                 strEnty2.insert(0, data2)
#                 strEnty3.insert(0, data3)
#                 strEnty4.insert(0, data4)
#                 strEnty5.insert(0, data5)
#                 strEnty6.insert(0, data6)
#                 strEnty7.insert(0, data7)
#         cur1.close()
#         conn.close()
#         strEnty1.focus()
#     except:
#         messagebox.showerror("Space4", "عدم  شناسایی  ریکارد منتخب")

#============== Main Tab mini Frame ===========
SellDebtFrame1 = ctk.CTkFrame(master=tab1_2)
SellDebtFrame1.grid(
    row=0,
    column=0,
    padx=5,
    pady=10,
    rowspan=3,
    sticky=NE
)


# -------- Search Debtors ---------------
# -------- Search Debtors ---------------
searchFrmSell = ctk.CTkFrame(
    SellDebtFrame1,
    corner_radius=5,
    fg_color=TKDARK
    )
searchFrmSell.place(x=5, y=2)

RefreshRepay1 = ctk.CTkButton(
    master=searchFrmSell,
    text="تجدید لیست",
    font=default_font_bold,
    width=70,
    fg_color="#2B2B2B",
    command=ReRef
    )
RefreshRepay1.grid(row=0, column=0, sticky=NE, padx=10, pady=5)
searchBtnSell1 = ctk.CTkButton(
    master=searchFrmSell,
    text="جستجو",
    font=default_font_bold,
    width=70,
    fg_color="#2B2B2B",
    command=PersonSearchFunc
    )
searchBtnSell1.grid(row=0, column=1, sticky=NE, padx=10, pady=5)

searchEntSell1 = ctk.CTkEntry(
    master=searchFrmSell,
    placeholder_text="جستجوی شخص",
    justify=RIGHT,
    font=default_font_bold,
    width=150
    )
searchEntSell1.grid(row=0,column=2,sticky=NE,padx=5, pady=5)

#---------------------
RepayBtn1 = ctk.CTkButton(
    master=searchFrmSell,
    text="رسید",
    font=default_font_bold,
    width=70,
    fg_color="#2B2B2B",
    command=SRepayFunc
    )
RepayBtn1.grid(row=0,column=3,sticky=NE,padx=10, pady=5)

RepayEnt1 = ctk.CTkEntry(
    master=searchFrmSell,
    placeholder_text="درج کردن رسید",
    justify=RIGHT,
    font=default_font_bold,
    width=150
    )
RepayEnt1.grid(row=0,column=4,sticky=NE,padx=5, pady=5)

NewDebtBtn1 = ctk.CTkButton(
    master=searchFrmSell,
    text="دفعه کردن",
    font=default_font_bold,
    width=70,
    fg_color="#2B2B2B",
    command=InsertNewDebtFunc
    )
NewDebtBtn1.grid(row=0,column=5,sticky=NE,padx=10, pady=5)
NewDebtEnt1 = ctk.CTkEntry(
    master=searchFrmSell,
    placeholder_text="درج قرض جدید",
    justify=RIGHT,
    font=default_font_bold,
    width=150
    )
NewDebtEnt1.grid(row=0,column=6,sticky=NE,padx=2, pady=5)



def TreeSellEditFunc():
    SellEditRoot = ctk.CTkToplevel(root)
    SellEditRoot.title("سیستم مدیریت فروشگاه")
    SellEditRoot.iconbitmap("Space4.ico")
    SellEditRoot.resizable(0, 0)
    SellEditRoot.grab_set()

    def SlClear():
        SlEditEnt8.delete(0, END)
        SlEditEnt1.delete(0, END)
        SlEditEnt2.delete(0, END)
        SlEditEnt3.delete(0, END)
        SlEditEnt4.delete(0, END)
        SlEditEnt5.delete(0, END)
        SlEditEnt6.delete(0, END)
        SlEditEnt7.delete(0, END)
        SlEditEnt8.insert(0, DateNow)
        SlEditEnt9.delete(0, END)
        SlEditEnt1.focus()

    def InsertAfterFunc():
        conn = sqlite3.connect("DataBaseDir/PressDb.db")
        cur1 = conn.cursor()
        selected_item = TreeSellDebt.selection()[0]
        for selected_item in TreeSellDebt.selection():
            SlQueryEdit = """
            SELECT
            SLNOTE,
            SLDATE,
            SLPRICE,
            SLDAMOUNT,
            SLQTTY,
            SLMTYPE,
            SLADDR,
            SLFNAME,
            SLNAME
            FROM SellingDebtTable
            WHERE SLID=?
            """
            cur1.execute(
                SlQueryEdit,
                (TreeSellDebt.set(selected_item, "#10"),),
            )
            fetch1 = cur1.fetchall()
            for Row in fetch1:
                data0 = Row[0]
                data1 = Row[1]
                data2 = Row[2]
                data3 = Row[3]
                data4 = Row[4]
                data5 = Row[5]
                data6 = Row[6]
                data7 = Row[7]
                data8 = Row[8]
                SlClear()
                SlEditEnt8.delete(0, END)
                SlEditEnt1.insert(0, data8)
                SlEditEnt2.insert(0, data7)
                SlEditEnt3.insert(0, data6)
                SlEditEnt4.insert(0, data5)
                SlEditEnt5.insert(0, data4)
                SlEditEnt6.insert(0, data3)
                SlEditEnt7.insert(0, data2)
                SlEditEnt8.insert(0, data1)
                SlEditEnt9.insert(0, data0)

        cur1.close()
        conn.close()
        SlEditEnt1.focus()


    def SaveUpdateFuncSl():
        if SlEditEnt1.get() == "":
            messagebox.showerror("Space4", "نوعیت نا مشخص")
        else:
            if SlEditEnt1.get() != "":
                dt1 = SlEditEnt1.get()
                dt2 = SlEditEnt2.get()
                dt3 = SlEditEnt3.get()
                dt4 = SlEditEnt4.get()
                dt5 = SlEditEnt5.get()
                dt6 = SlEditEnt6.get()
                dt7 = SlEditEnt7.get()
                dt8 = SlEditEnt8.get()
                dt9 = SlEditEnt9.get()
                for selected_item in TreeSellDebt.selection():
                    conn = sqlite3.connect("DataBaseDir/PressDb.db")
                    cur = conn.cursor()
                    UpdQueryL = """
                    UPDATE SellingDebtTable
                    SET
                    SLNAME=?,
                    SLFNAME=?,
                    SLADDR=?,
                    SLMTYPE=?,
                    SLQTTY=?,
                    SLPRICE=?,
                    SLDAMOUNT=?,
                    SLDATE=?,
                    SLNOTE=?
                    WHERE SLID=?
                    """
                    cur.execute(
                        UpdQueryL,
                        (
                            dt1,
                            dt2,
                            dt3,
                            dt4,
                            dt5,
                            dt6,
                            dt7,
                            dt8,
                            dt9,
                            TreeSellDebt.set(selected_item, "#10"),
                        ),
                    )

                    SlClear()
                    messagebox.showinfo("Space4 Software", "! آپدیت موفقانه انجام شد")
                    conn.commit()
                    conn.close()
                    ReRef()
                    SellEditRoot.destroy()
            else:
                messagebox.showinfo("اوووه", "!!!ریکارد ذخیره نشد")


    SlttlLabel1 = ctk.CTkLabel(
        SellEditRoot,
        text="ویرایش کردن",
        justify=RIGHT,
        font=default_font_bold,
        text_color=BGLIGHTGREEN,
    )
    SlttlLabel1.grid(row=0, column=1, padx=5, pady=5, sticky=NE)

    SlLabel1 = ctk.CTkLabel(
        master=SellEditRoot,
        text="نام",
        font=default_font_bold,
    )
    SlLabel1.grid(row=1, column=1, padx=5, pady=5, sticky=NE)

    SlLabel2 = ctk.CTkLabel(
        master=SellEditRoot,
        text="نام پدر",
        font=default_font_bold,
    )
    SlLabel2.grid(row=2, column=1, padx=5, pady=5, sticky=NE)
    SlLabel3 = ctk.CTkLabel(
        master=SellEditRoot,
        text="آدرس",
        font=default_font_bold,
    )
    SlLabel3.grid(row=3, column=1, padx=5, pady=5, sticky=NE)
    SlLabel4 = ctk.CTkLabel(
        master=SellEditRoot,
        text="مواد",
        font=default_font_bold,
    )
    SlLabel4.grid(row=4, column=1, padx=5, pady=5, sticky=NE)
    SlLabel5 = ctk.CTkLabel(
        master=SellEditRoot,
        text="تعداد",
        font=default_font_bold,
    )
    SlLabel5.grid(row=5, column=1, padx=5, pady=5, sticky=NE)
    SlLabel6 = ctk.CTkLabel(
        master=SellEditRoot,
        text="مقدار باقی",
        font=default_font_bold,
    )
    SlLabel6.grid(row=6, column=1, padx=5, pady=5, sticky=NE)
    SlLabel7 = ctk.CTkLabel(
        master=SellEditRoot,
        text="قرض اولیه",
        font=default_font_bold,
    )
    SlLabel7.grid(row=7, column=1, padx=5, pady=5, sticky=NE)
    SlLabel8 = ctk.CTkLabel(
        master=SellEditRoot,
        text="تاریخ",
        font=default_font_bold,
    )
    SlLabel8.grid(row=8, column=1, padx=5, pady=5, sticky=NE)
    SlLabel9 = ctk.CTkLabel(
        master=SellEditRoot,
        text="نوت",
        font=default_font_bold,
    )
    SlLabel9.grid(row=9, column=1, padx=5, pady=5, sticky=NE)

    #--------- Entry ------------
    SlEditEnt1 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt1.focus()
    SlEditEnt1.grid(row=1, column=0, padx=5, pady=5, sticky=NE)

    SlEditEnt2 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt2.grid(row=2, column=0, padx=5, pady=5, sticky=NE)
    SlEditEnt3 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt3.grid(row=3, column=0, padx=5, pady=5, sticky=NE)
    SlEditEnt4 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt4.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
    SlEditEnt5 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt5.grid(row=5, column=0, padx=5, pady=5, sticky=NE)
    SlEditEnt6 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt6.grid(row=6, column=0, padx=5, pady=5, sticky=NE)
    SlEditEnt7 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt7.grid(row=7, column=0, padx=5, pady=10, sticky=NE)
    SlEditEnt8 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt8.grid(row=8, column=0, padx=5, pady=10, sticky=NE)
    SlEditEnt9 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt9.grid(row=9, column=0, padx=5, pady=10, sticky=NE)
    SellSaveBtn = ctk.CTkButton(
        SellEditRoot,
        text="انجام",
        font=default_font_bold,
        fg_color="#2B2B2B",
        hover_color=BGLIGHTGREEN,
        command=SaveUpdateFuncSl
    )
    SellSaveBtn.grid(row=10, column=0, padx=5, pady=10, sticky=NE)
    SellEditRoot.after(500, InsertAfterFunc)
    SellEditRoot.mainloop()
# ============== Sell Debt Tree view =====================
# ============== Sell Debt Tree view =====================

SellDebtLabel1 = ctk.CTkLabel(
    master=SellDebtFrame1,
    text="لیست قرضداران",
    font=default_font_bold,
    text_color=("teal", BGLIGHTGREEN),
    justify=RIGHT,
)
SellDebtLabel1.grid(row=2, column=0, padx=20, pady=5, sticky=NE)


TreeSellDebtFrm = ctk.CTkFrame(SellDebtFrame1)
TreeSellDebtFrm.grid(row=3, column=0, padx=5, sticky=NE)
TreeSellDebt = ttk.Treeview(
    TreeSellDebtFrm,
    columns=(
        "L1",
        "L2",
        "L3",
        "L4",
        "L5",
        "L6",
        "L7",
        "L8",
        "L9",
        "L10"
        ),
    selectmode="browse",
    height=18,
)
TreeSellDebt.heading("L1", text="نوت", anchor=E)
TreeSellDebt.heading("L2", text="تاریخ", anchor=E)
TreeSellDebt.heading("L3", text="مقدار", anchor=E)
TreeSellDebt.heading("L4", text="باقی", anchor=E)
TreeSellDebt.heading("L5", text="تعداد", anchor=E)
TreeSellDebt.heading("L6", text="مواد", anchor=E)
TreeSellDebt.heading("L7", text="آدرس", anchor=E)
TreeSellDebt.heading("L8", text="نام پدر", anchor=E)
TreeSellDebt.heading("L9", text="نام مشتری", anchor=E)
TreeSellDebt.heading("L10", text="نمبر", anchor=E)


TreeSellDebt.column("#0", stretch=NO, minwidth=0, width=0)
TreeSellDebt.column("#1", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#2", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#3", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#4", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#5", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#6", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#7", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#8", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#9", stretch=NO, minwidth=0, width=120, anchor=E)
TreeSellDebt.column("#10", stretch=NO, minwidth=0, width=60, anchor=E)
TreeSellDebt.grid(padx=0, pady=0)


TreeSellDebt.delete(*TreeSellDebt.get_children())
TreeSellDebtConn = sqlite3.connect("DataBaseDir/PressDb.db")
TreeSellDebtCor = TreeSellDebtConn.execute(
    """
    SELECT
    SLNOTE,
    SLDATE,
    SLPRICE,
    SLDAMOUNT,
    SLQTTY,
    SLMTYPE,
    SLADDR,
    SLFNAME,
    SLNAME,
    SLID
    FROM SellingDebtTable
    """
)
fetchTreeSellDebt = TreeSellDebtCor.fetchall()
for indexSellD in fetchTreeSellDebt:
    TreeSellDebt.insert("", "end", values=indexSellD)
TreeSellDebtCor.close()
TreeSellDebtConn.close()

#--------------------------------
def SellDebtPop(event):
    try:
        selectedRow = TreeSellDebt.selection()[0]
        SellMenu = Menu(
            TreeSellDebt,
            tearoff=0,
            font=default_font_bold1,
            bg=CTKDARK,
            fg=CTKLIGHT,
            activebackground=BGLIGHTGREEN,
        )
        SellMenu.add_command(
            compound=LEFT,
            image=PrintImg_1,
            label="صدور بل",
            command=sell_item
        )
        SellMenu.add_command(
            compound=LEFT,
            image=DeleteImg_1,
            label="حذف",
            command=TreeSellDebtDeleteFunc
        )
        SellMenu.add_command(
            compound=LEFT,
            image=RefreshImg_1,
            label="تجدید",
            command=ReRef
        )
        SellMenu.add_command(
            compound=LEFT,
            image=EditImg_1,
            label="ویرایش",
            command=TreeSellEditFunc
        )
        try:
            SellMenu.tk_popup(event.x_root, event.y_root)
        finally:
            SellMenu.grab_release()
    except:
        messagebox.showinfo("اوووه", "! ریکارد را انتخاب کنید لطفاً")


TreeSellDebt.bind("<Button-3>", SellDebtPop)

#=----------- Popup end---------------






root.mainloop()