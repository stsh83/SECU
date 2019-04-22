# Code written by Sergio Serrano.
# www.sergioserranohernandez.net

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import decimal
import sys
import math

#Global variables
decimal.getcontext().prec=12
operativeSystem=sys.platform


class SIH(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # A small window popup to send diverse messages from the main app.
        def popupWindow(windowTitle, articleTitle, msg):
            popup = tk.Toplevel()

            popup.wm_title(windowTitle)
            titleLabel = tk.Label(popup, text=articleTitle, fg="black", font='Verdana 14 bold')
            titleLabel.place(anchor='center', y=25, x=480)
            msgLabel = tk.Label(popup, text=msg, anchor='sw', justify='center',  fg="black", font='Verdana 14')
            msgLabel.place(y=130, x=220)
            B1 = ttk.Button(popup, text='Return', command=popup.destroy, width=10)
            if operativeSystem == 'linux':
                B1.place(y=370, x=805)
            elif operativeSystem == 'win32':
                B1.place(y=370, x=812)
            elif operativeSystem == 'darwin':
                B1.place(y=370, x=800)
            popup.geometry('924x428')
            popup.resizable(0, 0)
            popup.focus_set()
            popup.grab_set()
            popup.wait_window()

        if operativeSystem!='darwin':
            tk.Tk.iconbitmap(self,default='favicon.ico')

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Menu Bar.
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        helpmenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Exit', command=lambda: self.destroy())
        helpmenu.add_command(label='About',  command=lambda: popupWindow('About SECU','Spanish Empire - Early Modern Era - Conversion Utilities','Research and programming by Sergio Serrano\n\nSpecial thanks to:\nAntonio Ibarra\n\n More information at: \nwww.sergioserranohernandez.net\n'))
        menubar.add_cascade(label='File', menu=filemenu)
        menubar.add_cascade(label='Help', menu=helpmenu)
        tk.Tk.config(self, menu=menubar)

        self.frames = {}
        for F in (MainPage, CurrencyOne, CurrencyTwo, PesosADecimal, DecimalAPesos):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame('MainPage')
        self.title('Spanish Empire Conversion Utilities - Early Modern Era')
        self.geometry('1280x720')
        self.resizable(0, 0)
        self.pack_propagate(0)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        headerFrame = tk.Frame(self)
        headerFrame.grid(row=0, column=0, padx=290, pady=30)
        logo = tk.PhotoImage(file='Logo.gif')
        titleLabel = tk.Label(headerFrame, image=logo, text='   Spanish Empire Conversion Utilities\n\nEarly Modern Era',
              compound='left', fg="black", font='Verdana 14 bold')
        titleLabel.PhotoImage = logo
        titleLabel.grid(row=0, column=0, ipadx=10, ipady=2)

        # Currency Conversion Widgets
        mainFrame = tk.Frame(self)
        mainFrame.grid(row=1, column=0, padx=30, pady=30)
        moneyFrame = tk.LabelFrame(mainFrame, text='Currency.')
        moneyFrame.grid(row=0, column=0, padx=10, pady=10)
        moneyXVII = ttk.Button(moneyFrame, text='XVIth & XVIIth Centuries', command=lambda: controller.show_frame('CurrencyOne'), width=43)
        moneyXVII.grid(row=1, column=0, padx=8, pady=4)
        moneyXVIII = ttk.Button(moneyFrame, text='XVIIIth & XIXth Centuries', command=lambda: controller.show_frame('CurrencyTwo'), width=43)
        moneyXVIII.grid(row=2, column=0, padx=8, pady=4)
        # Decimal Conversion Widgets
        decimalFrame = tk.LabelFrame(mainFrame, text='Decimal.')
        decimalFrame.grid(row=1, column=0, padx=10, pady=10)
        toDecimal = ttk.Button(decimalFrame, text='From Pesos de a 8 to Decimal', command=lambda: controller.show_frame('PesosADecimal'), width=43)
        toDecimal.grid(row=0, column=0, padx=8, pady=4)
        fromDecimal = ttk.Button(decimalFrame, text='From Decimal to Pesos de a 8', command=lambda: controller.show_frame('DecimalAPesos'), width=43)
        fromDecimal.grid(row=1, column=0, padx=8, pady=4)
        # Weights and Measurements Conversion Widgets
        measurementFrame = tk.LabelFrame(mainFrame, text='Weight and Measurement.')
        measurementFrame.grid(row=2, column=0, padx=10, pady=10)
        weight = ttk.Button(measurementFrame, text='Spanish Silver Mark', width=43)
        weight.grid(row=0, column=0, padx=8, pady=4)
        weight = ttk.Button(measurementFrame, text='Weight', width=43)
        weight.grid(row=1, column=0, padx=8, pady=4)


class CurrencyOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # The currency names that will be used by the list are stored here
        listacombo = ['Pesos de a ocho', 'Pesos de oro ensayado',
                 'Castellanos de oro', 'Ducados', 'Maravedíes',
                 'Reales', 'Pesos de a nueve', 'Pesos de buen oro',
                 'Pesos de oro de 20 quilates', 'Pesos de oro ensayado [12.5]',
                 'Ducados de vellon', 'Escudos', 'Tostones',
                 'Pesos de plata corriente', 'Pesos de oro de 13 quilates']
        # These are the values in Maravedíes for each currency; this is the factor that will be used to operate
        # the conversion.
        M = {0: 272, 1: 450, 2: 576, 3: 375, 4: 1, 5: 34, 6: 306,
             7: 556, 8: 484, 9: 425, 10: 150, 11: 340, 12: 136, 13: 312, 14: 315}
        finalConversion = StringVar()

        def conversionOp(*args):
            while True:
                try:
                    num = decimal.Decimal(entryFrom.get())
                except:
                    messagebox.showwarning('Error', 'A number is required in the From field')
                    break
                else:
                    numFrom = decimal.Decimal(entryFrom.get())
                    fromCaseD = fromlistbox.curselection()
                    fromCase = int(fromCaseD[0])
                    fromCurrency = listacombo[fromCase]
                    factorFrom = M[fromCase]
                    valueinMaravedis = int(numFrom * factorFrom)
                    toCaseD = tolistbox.curselection()
                    toCase = int(toCaseD[0])
                    toCurrency = listacombo[toCase]
                    Divisor = M[toCase]
                    convertedValue = str(decimal.Decimal(valueinMaravedis/Divisor))
                    SIH.clipboard_clear(self)
                    SIH.clipboard_append(self, convertedValue[0:14])
                    finalConversion.set("%s %s = %s %s" % (numFrom, fromCurrency, convertedValue[0:14], toCurrency))
                    break

        # Title
        frameTitle = tk.Frame(self)
        frameTitle.grid(row=0, column=0, padx=300, pady=25)
        logo = tk.PhotoImage(file='Centen.png')
        titleLabel = tk.Label(frameTitle, image=logo,
                              text='   XVIth and XVIIth Centuries',
                              compound='left', fg="black", font='Verdana 14 bold')
        titleLabel.PhotoImage = logo
        titleLabel.grid(row=0, column=0, ipadx=10, ipady=2)

        frameConversion = tk.Frame(self)
        frameConversion.grid(row=1, column=0, padx=0, pady=0)
        valueLabel = tk.Label(frameConversion, text='Value:', fg='black', font='Verdana 12')
        valueLabel.grid(row=0, column=0, padx=6, pady=8)
        entryFrom = ttk.Entry(frameConversion)
        entryFrom.grid(row=1, column=0, padx=6, pady=6)
        origcurrencyLabel = tk.Label(frameConversion, text="Original Currency:", fg="black", font='Verdana 12')
        origcurrencyLabel.grid(row=0, column=1)
        origcurrencyLabel = tk.Label(frameConversion, text="New Currency:", fg="black", font='Verdana 12')
        origcurrencyLabel.grid(row=0, column=4)

        scrollbar = Scrollbar(frameConversion, orient=VERTICAL)
        fromlistbox = tk.Listbox(frameConversion, yscrollcommand=scrollbar.set, width=40, font='Verdana 11', selectmode=BROWSE, exportselection=0)
        for item in listacombo:
            fromlistbox.insert(END, item)
        for i in range(0, len(listacombo), 2):
            fromlistbox.itemconfigure(i, background='#f0f0ff')

        fromlistbox.selection_set(0)
        scrollbar.config(command=fromlistbox.yview)
        fromlistbox.grid(row=1, column=1, rowspan=16, sticky=(N,S,E,W))
        scrollbar.grid(row=1, column=2, rowspan=16, sticky=(N,S,E,W))

        middleLegend = tk.Label(frameConversion, text='Convert To:', anchor='center', font='Verdana 12')
        middleLegend.grid(row=1, column=3, padx=6, pady=8)

        scrollbar2 = Scrollbar(frameConversion, orient=VERTICAL)
        tolistbox = tk.Listbox(frameConversion, width=40, yscrollcommand=scrollbar2.set, font='Verdana 11', selectmode=BROWSE, exportselection=0)
        for item in listacombo:
            tolistbox.insert(END, item)
        for i in range(1, len(listacombo), 2):
            tolistbox.itemconfigure(i, background='#f0f0ff')
        tolistbox.selection_set(1)
        scrollbar2.config(command=tolistbox.yview)
        tolistbox.grid(row=1, column=4, rowspan=16,  sticky=(N,S,E,W))
        scrollbar2.grid(row=1, column=5, rowspan=16, sticky=(N,S,E,W))

        fromlistbox.bind('<<ListboxSelect>>', conversionOp)
        tolistbox.bind('<<ListboxSelect>>', conversionOp)
        entryFrom.bind('<Return>', conversionOp)
        entryFrom.bind('<Double-1>', conversionOp)

        frameResults = tk.Frame(self)
        frameResults.grid(row=2, column=0, padx=0, pady=0)
        entryTo = tk.Label(frameResults, fg="red", font='Verdana 12 bold', textvariable=finalConversion, anchor='center')
        entryTo.grid(row=0, column=0, padx=20, pady=6)
        moneyXVIII=ttk.Button(frameResults, text='Return to main page', command=lambda: controller.show_frame('MainPage'), width=80)
        moneyXVIII.grid(row=1, column=0, padx=8, pady=4)


class CurrencyTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # The currency names that will be used by the list are stored here
        listacombo = ['Reales Corrientes', 'Pesos Corrientes',
                 'Rupias Sica', 'Reales Fuertes', 'Pesos Fuertes',
                 'Reales de Vellón', 'Reales Nuevos']
        # These are the values in Reales de Vellón for each currency; this is the factor that will be used to operate
        # the conversion.
        M = {0: 1.875, 1: 15, 2: 9.43396226415, 3: 2.5, 4: 20, 5: 1, 6: 2}
        finalConversion = StringVar()

        def conversionOp(*args):
            while True:
                try:
                    num = decimal.Decimal(entryFrom.get())
                except:
                    messagebox.showwarning('Error', 'A number is required in the From field')
                    break
                else:
                    numFrom = decimal.Decimal(entryFrom.get())
                    fromCaseD = fromlistbox.curselection()
                    fromCase = int(fromCaseD[0])
                    fromCurrency = listacombo[fromCase]
                    factorFrom = decimal.Decimal(M[fromCase])
                    valueinMaravedis = decimal.Decimal(numFrom * factorFrom)
                    toCaseD = tolistbox.curselection()
                    toCase = int(toCaseD[0])
                    toCurrency = listacombo[toCase]
                    Divisor = decimal.Decimal(M[toCase])
                    convertedValue = str(decimal.Decimal(valueinMaravedis / Divisor))
                    SIH.clipboard_clear(self)
                    SIH.clipboard_append(self, convertedValue[0:14])
                    finalConversion.set("%s %s = %s %s" % (numFrom, fromCurrency, convertedValue[0:14], toCurrency))
                    break

        # Title
        frameTitle = tk.Frame(self)
        frameTitle.grid(row=0, column=0, padx=300, pady=25)
        logo = tk.PhotoImage(file='RealDeA8.png')
        titleLabel = tk.Label(frameTitle, image=logo,
                              text='   XVIIIth & XIXth Centuries',
                              compound='left', fg="black", font='Verdana 14 bold')
        titleLabel.PhotoImage = logo
        titleLabel.grid(row=0, column=0, ipadx=10, ipady=2)

        frameConversion = tk.Frame(self)
        frameConversion.grid(row=1, column=0, padx=0, pady=0)
        valueLabel = tk.Label(frameConversion, text='Value:', fg='black', font='Verdana 12')
        valueLabel.grid(row=0, column=0, padx=8, pady=6)
        entryFrom = ttk.Entry(frameConversion)
        entryFrom.grid(row=1, column=0, padx=6, pady=6)
        origcurrencyLabel = tk.Label(frameConversion, text="Original Currency:", fg="black", font='Verdana 12')
        origcurrencyLabel.grid(row=0, column=1, padx=8, pady=6)
        origcurrencyLabel = tk.Label(frameConversion, text="New Currency:", fg="black", font='Verdana 12')
        origcurrencyLabel.grid(row=0, column=4, padx=8, pady=6)

        fromlistbox = tk.Listbox(frameConversion, width=40, font='Verdana 11',
                                 selectmode=BROWSE, exportselection=0)
        for item in listacombo:
            fromlistbox.insert(END, item)
        for i in range(0, len(listacombo), 2):
            fromlistbox.itemconfigure(i, background='#f0f0ff')

        fromlistbox.selection_set(1)
        fromlistbox.grid(row=1, column=1, rowspan=16, sticky=(N,S,E,W))

        middleLegend = ttk.Label(frameConversion, text='Convert To:', anchor='center', font='Verdana 12')
        middleLegend.grid(row=1, column=3, padx=8, pady=6)

        tolistbox = tk.Listbox(frameConversion, width=40, font='Verdana 11',
                               selectmode=BROWSE, exportselection=0)
        for item in listacombo:
            tolistbox.insert(END, item)
        for i in range(1, len(listacombo), 2):
            tolistbox.itemconfigure(i, background='#f0f0ff')
        tolistbox.selection_set(4)
        tolistbox.grid(row=1, column=4, rowspan=16, sticky=(N,S,E,W))

        fromlistbox.bind('<<ListboxSelect>>', conversionOp)
        tolistbox.bind('<<ListboxSelect>>', conversionOp)
        entryFrom.bind('<Return>', conversionOp)
        entryFrom.bind('<Double-1>', conversionOp)

        frameResults = tk.Frame(self)
        frameResults.grid(row=2, column=0, padx=0, pady=0)
        entryTo = tk.Label(frameResults, fg="red", font='Verdana 12 bold', textvariable=finalConversion, anchor='center')
        entryTo.grid(row=0, column=0, padx=20, pady=6)
        moneyXVIII = ttk.Button(frameResults, text='Return to main page',
                                command=lambda: controller.show_frame('MainPage'), width=80)
        moneyXVIII.grid(row=1, column=0, padx=8, pady=4)


class PesosADecimal(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        logo = tk.PhotoImage(file='ColumnariaVect.png')
        titleLabel = tk.Label(self, image=logo, text='    Conversion from Pesos de a 8\nto decimal system',
                               compound='left', fg="black", font='Verdana 14 bold')
        titleLabel.PhotoImage = logo
        titleLabel.grid(row=0, column=0, pady=10, padx=300)

        def Operation():
            Tot.delete(0, END)
            D = {}
            Pta = 1
            # Tests the field Pesos to determine if it is (int) and then it continues
            while True:
                try:
                    num = int(PE.get())
                except:
                    messagebox.showwarning('Error', 'A number is required in the Pesos field')
                    PE.delete(0, END)
                    break
                else:
                    D['pesos'] = int(PE.get())
                    Pta = 2
                    break
            if Pta == 2:
                D['tomines'] = TE.get()
                while True:
                    if not D['tomines'].isdigit():
                        messagebox.showwarning('Error', 'A number is required in the Tomines field')
                        TE.delete(0, END)
                        break
                    else:
                        D['tomines'] = int(D['tomines'])
                        if D['tomines'] > 7:
                            messagebox.showwarning('Error', 'The Tomines value must be equal or less than 7')
                            TE.delete(0, END)
                            break
                        else:
                            Pta = 3
                            break
            if Pta == 3:
                D['granos'] = GE.get()
                while True:
                    if not D['granos'].isdigit():
                        messagebox.showwarning('Error', 'A number is required in the Granos field')
                        GE.delete(0, END)
                        break
                    else:
                        D['granos'] = int(D['granos'])
                        if D['granos'] > 11:
                            messagebox.showwarning('Error', 'The Granos value must be equal or less than 11')
                            GE.delete(0, END)
                            break
                        else:
                            D['counter'] = 1
                            break
            try:
                num = int(D['counter'])
            except:
                Tot.delete(0, END)
            else:
                D['total'] = (decimal.Decimal(D['pesos'])) + (
                        (decimal.Decimal(D['tomines']) / 8) + (decimal.Decimal(D['granos']) / 96))
                Tot.insert(10, D['total'])
                D['counter'] = 0

        def Clean():
            PE.delete(0, END)
            TE.delete(0, END)
            GE.delete(0, END)
            Tot.delete(0, END)

        pesosFrame = tk.LabelFrame(self, text='Please type the desired conversion')
        pesosFrame.grid(row=1, column=0, padx=6, pady=6)
        pesosLabel = tk.Label(pesosFrame, text='Pesos')
        pesosLabel.grid(row=0, column=0, padx=4, pady=4)
        tominesLabel = tk.Label(pesosFrame, text='Tomines')
        tominesLabel.grid(row=1, column=0, padx=4, pady=4)
        granosLabel = tk.Label(pesosFrame, text='Granos')
        granosLabel.grid(row=2, column=0, padx=4, pady=4)
        totalLabel = tk.Label(pesosFrame, text='Total')
        totalLabel.grid(row=3, column=0, padx=4, pady=4)
        PE = ttk.Entry(pesosFrame)
        PE.grid(row=0, column=1, padx=4, pady=4)
        TE = ttk.Entry(pesosFrame)
        TE.grid(row=1, column=1, padx=4, pady=4)
        GE = ttk.Entry(pesosFrame)
        GE.grid(row=2, column=1, padx=4, pady=4)
        Tot = ttk.Entry(pesosFrame)
        Tot.grid(row=3, column=1, padx=4, pady=4)
        cleanButton = ttk.Button(pesosFrame, text='Clean', command=Clean)
        cleanButton.grid(row=4, column=1, padx=4, pady=4)
        calculateButton = ttk.Button(pesosFrame, text='Calculate', command=Operation)
        calculateButton.grid(row=4, column=0, padx=4, pady=4)
        B1 = ttk.Button(self, text='Return', width=43, command=lambda: controller.show_frame('MainPage'))
        B1.grid(row=2, column=0, pady=10, padx=10)


class DecimalAPesos(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        logo = tk.PhotoImage(file='MoVta.png')
        titleLabel = tk.Label(self, image=logo, text='    Conversion from decimal values\nto pesos de a 8',
                               compound='left', fg="black", font='Verdana 14 bold')
        titleLabel.PhotoImage = logo
        titleLabel.grid(row=0, column=0, pady=10, padx=330)

        def turnon(*args):
            calculateButton['state'] = 'normal'

        def Operation():
            PE.delete(0, END)
            TE.delete(0, END)
            GE.delete(0, END)
            D = {}
            while True:
                try:
                    num = decimal.Decimal(DEC.get())
                except:
                    messagebox.showwarning('Error', 'A number is required in the Decimal field')
                    DEC.delete(0, END)
                    break
                else:
                    PE['state'] = 'normal'
                    pesosLabel['state'] = 'normal'
                    TE['state'] = 'normal'
                    tominesLabel['state'] = 'normal'
                    GE['state'] = 'normal'
                    granosLabel['state'] = 'normal'
                    D['num'] = num
                    D['pesos'] = math.trunc(D['num'])
                    D['subtraction1'] = ((D['num'] - D['pesos']) * 8)
                    D['tomines'] = math.trunc(D['subtraction1'])
                    D['subtraction2'] = D['subtraction1'] - D['tomines']
                    D['granos'] = math.trunc(D['subtraction2'] * 12)
                    PE.insert(10, D['pesos'])
                    TE.insert(1, D['tomines'])
                    GE.insert(2, D['granos'])
                    cleanButton['state'] = 'normal'
                    break

        def Clean():
            DEC.delete(0, END)
            PE.delete(0, END)
            TE.delete(0, END)
            GE.delete(0, END)
            PE['state'] = 'disabled'
            pesosLabel['state'] = 'disabled'
            TE['state'] = 'disabled'
            tominesLabel['state'] = 'disabled'
            GE['state'] = 'disabled'
            granosLabel['state'] = 'disabled'
            cleanButton['state'] = 'disabled'
            DEC.focus()

        pesosFrame = tk.LabelFrame(self, text='Please type the desired value in decimal')
        pesosFrame.grid(row=1, column=0, padx=6, pady=6)
        decimalLabel = tk.Label(pesosFrame, text='Decimal')
        decimalLabel.grid(row=0, column=0, padx=4, pady=4)
        pesosLabel = tk.Label(pesosFrame, text='Pesos', state=DISABLED)
        pesosLabel.grid(row=1, column=0, padx=4, pady=4)
        tominesLabel = tk.Label(pesosFrame, text='Tomines', state=DISABLED)
        tominesLabel.grid(row=2, column=0, padx=4, pady=4)
        granosLabel = tk.Label(pesosFrame, text='Granos', state=DISABLED)
        granosLabel.grid(row=3, column=0, padx=4, pady=4)
        DEC = ttk.Entry(pesosFrame)
        DEC.grid(row=0, column=1, padx=4, pady=4)
        DEC.bind('<FocusIn>', turnon)
        PE = ttk.Entry(pesosFrame, state=DISABLED)
        PE.grid(row=1, column=1, padx=4, pady=4)
        TE = ttk.Entry(pesosFrame, state=DISABLED)
        TE.grid(row=2, column=1, padx=4, pady=4)
        GE = ttk.Entry(pesosFrame, state=DISABLED)
        GE.grid(row=3, column=1, padx=4, pady=4)
        cleanButton = ttk.Button(pesosFrame, text='Clean', state=DISABLED, command=Clean)
        cleanButton.grid(row=4, column=1, pady=10, padx=10)
        calculateButton = ttk.Button(pesosFrame, text='Calculate', state=DISABLED, command=Operation)
        calculateButton.grid(row=4, column=0, pady=10, padx=10)
        B1 = ttk.Button(self, text='Return', width=43, command=lambda: controller.show_frame('MainPage'))
        B1.grid(row=2, column=0, pady=10, padx=10)


if __name__ == '__main__':
    app = SIH()
    app.mainloop()
