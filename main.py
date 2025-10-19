from tkinter import *

# tkinter object instance
root = Tk()

# title, geometry, resizability
root.title("Time Zone Converter")
root.geometry("300x220+100+100")
root.resizable(False, False)

# conv func
def conv():
    try:
        fr = fromentry.get()
        to = toentry.get()
        result = float(convtimeHEntry.get())*60 + float(convtimeMEntry.get())*1

        fr = float(fr)
        to = float(to)

        # Wrong Value
        if not (-12 <= fr <= 12): raise ValueError()
        if not (-12 <= to <= 12): raise ValueError()
        if not (0 <= result <= 1440): raise ValueError()
        
        result = 60*(to - fr) + result
        result = int(result)
        hh = result//60
        mm = result%60

        result_label.config(text="Converted Time: "+str(hh)+" : "+str(mm))

        
    except ValueError:
        # 입력값이 숫자가 아닐 경우 오류 처리
        result_label.config(text="Put proper NUMBERS!")
    except Exception as e:
        result_label.config(text=f"unexpected: {e}")

f1 = Frame(root)
f2 = Frame(root)

# Label : title
title = Label(f1, text="Time Zone Converter", font=("Consolas", 15, "bold"))

title.pack()

# Label y Entry : conv time
convtimeLabel = Label(f1, text="Put convertin' time.(hour; min)", font=("Consolas", 12))
convtimeLabel.pack()
convtimeHEntry = Entry(f1, width=10)
convtimeHEntry.pack(side='left')
colonLabel = Label(f1, text=':', font=('Consolas', 14))
colonLabel.pack(side='left')
convtimeMEntry = Entry(f1, width=10)
convtimeMEntry.pack(side='left')

# button
#nowbutton = Button(root, text="NOW", 

# f1 frame
f1.pack()

# Label y Entry : from
fromlabel = Label(f2, text='From: GMT+')
fromlabel.pack(anchor='w', pady=3)
fromentry = Entry(f2, width=20)
fromentry.pack(anchor='w', padx=10)


# Label y Entry : to
tolabel = Label(f2, text='To: GMT+')
tolabel.pack(anchor='w', pady=3)
toentry = Entry(f2, width=20)
toentry.pack(anchor='w', padx=10)

convbutton = Button(f2, text="CONVERT", command=conv)
convbutton.pack(fill='x')

# f2 frame
f2.pack(fill='x')

result_label = Label(root, text="Converted Time: ??:??")
result_label.pack()

root.mainloop()
