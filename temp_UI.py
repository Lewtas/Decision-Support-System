import temp
import tkinter as tk
import kourse_w

root = tk.Tk()
canvas1 = tk.Canvas(root, width=1080, height=720, bg='lightsteelblue2', relief='raised')
canvas1.pack()

frame = tk.Frame(root, bg='lightsteelblue2')
frame.place(relwidth=1, relheight=1)
entry_mas = []
label_mas = []
GlRange = kourse_w.Global_range()
p_y = 0
label_err1 = tk.Label(frame, text='Plese input number, from 3 to 7', bg='lightsteelblue2')
label_err2 = tk.Label(frame, text='Plese input numver, not sumbol for quantity_alter', bg='lightsteelblue2')
label_err3 = tk.Label(frame, text='Plese input numver, not sumbol for quantity_ranger', bg='lightsteelblue2')
label_set_a = tk.Label(frame, text='', bg='lightsteelblue2')


def input_quantity_alter():

    global GlRange, label_err1, label_err2, label_err3, entry_mas, label_set_a, label_mas, p_y
    label_set_a.config(text='\n')
    if(len(entry_mas) > 0):
        for i in range(len(entry_mas)):
            entry_mas[i].destroy()
            label_mas[i].config(text='\n')
    quantity_alter = entry1.get()
    quantity_ranger = entry2.get()
    GlRange.quantity_alter = 0
    GlRange.quantity_ranger = 0
    if(len(quantity_alter) == 1):
        if(quantity_alter.isnumeric()):
            if(int(quantity_alter) <= 7 and int(quantity_alter) >= 3):
                quantity_alter = int(quantity_alter)
                GlRange.quantity_alter = quantity_alter
                label_err1.config(text='')
                label_err2.config(text='')

            else:
                label_err1.config(text=' Введіть число, від 3 до 7 для к-ті альтернатив', font='30')
                label_err2.config(text='')
                label_err1.place(x=200, y=10)
        else:
            label_err2.config(text=' Введіть число, не символ для к-ті альтернатив', font='30')
            label_err1.config(text='')
            label_err2.place(x=200, y=10)

    if(len(quantity_ranger) == 1):
        if(quantity_ranger.isnumeric()):
            quantity_ranger = int(quantity_ranger)
            GlRange.quantity_ranger = quantity_ranger
            label_err3.config(text='')

        else:
            label_err3.config(text=' Введіть число, не символ для к-ті ранжувань', font='30')
            label_err3.place(x=200, y=50)

    if(GlRange.quantity_alter > 0 and GlRange.quantity_ranger > 0):

        entry_mas = []
        label_mas = []
        p_x = 200
        p_y = 10
        for i in range(GlRange.quantity_ranger):
            label_mas.append(tk.Label(frame, text=' Ранжування '+str(i+1), bg='lightsteelblue2', font='30'))
            label_mas[i].place(x=p_x, y=p_y)
            entry_mas.append(tk.Entry(frame, bg='lightsteelblue3', fg='black', font='30'))
            entry_mas[i].place(x=p_x+150, y=p_y, relwidth=0.075)
            p_y += 40
        button2.place(x=p_x, y=p_y+10)
        button2['state'] = "active"
        GlRange.setKitAlter()

        str1 = ''

        for i in range(quantity_alter):
            str1 += str(i)+' ' + GlRange.kit_alter[i]+'\n'
        label_set_a.config(text=' Кодові значення та їх сенс\n'+str1, font='30')
        label_set_a.place(x=10, y=p_y+40)
        label_err1.config(text=' Введіть послідовність цифр, які представленні нижче\nв прядкі спадання якості освіти\nв навчальному закладі', font='30')
        label_err1.place(x=430, y=10)

    return quantity_alter


def input_ranger():
    mas_range = []

    global label_err1, label_set_a
    GlRange.destroy_ranger()
    for i in range(len(entry_mas)):
        q = True
        GlRange.allowed_alter = [i for i in range(GlRange.quantity_alter)]
        mas_range.append(entry_mas[i].get())

        if(mas_range[i].isdigit() == False):
            label_err1.config(
                text=' Ви ввели символ, будь-ласка\nвводьте тільки послідовність\nцифер, що представлені нижче та не быльше одного разу', font='30')
            label_err1.place(x=430, y=10)
            return
        elif(len(mas_range[i]) <= GlRange.quantity_alter):
            q = True
            for j in mas_range[i]:
                if(int(j) not in GlRange.allowed_alter):
                    q = False

                    label_err1.config(
                        text=' Ви ввели недопустиму цифру, будь-ласка\nвводьте тільки цифери, що представлені нижче\nта не быльше одного разу', font='30')
                    label_err1.place(x=430, y=10)
                    break
                else:
                    GlRange.allowed_alter.remove(int(j))

            if(q):

                GlRange.create_ranger(mas_range[i])
        else:
            label_err1.config(
                text=' Ви ввели занадто багато значень, будь-ласка\nвводьте тільки цифери, що представлені нижче\nта не быльше одного разу', font='30')
            label_err1.place(x=440, y=10)

    if(len(GlRange.kit_ranger) == GlRange.quantity_ranger):

        label_err1.config(text='')
        GlRange.final_range_cond = GlRange.toGlobalRangerCondorse()
        GlRange.final_range_bord = GlRange.toGlobalRangerBord()
        GlRange.toUnif()

        GlRange.final_range_cond = GlRange.toGlobalRangerCondorse()
        GlRange.final_range_bord = GlRange.toGlobalRangerBord()

        str1 = ' Фінальне ранжування за методом Борда\n'
        j = 1
        for i in GlRange.final_range_bord:
            str1 += str(j)+' ' + GlRange.kit_alter[i]+'\n'
            j += 1
        j = 1
        str1 += '\n Фінальне ранжування за методом Кондорсе\n'
        for i in GlRange.final_range_cond:
            str1 += str(j)+' ' + GlRange.kit_alter[i]+'\n'
            j += 1
        label_set_a.config(text=str1, font='30')
        label_set_a.place(x=10, y=p_y+50)
        temp.toAll(GlRange.kit_ranger, GlRange.final_range_cond, GlRange.final_range_bord)
        button2['state'] = "disabled"


label1 = tk.Label(frame, text='К-ть альтернатив ', bg='lightsteelblue2', font='20')
label1.place(x=10, y=10)

entry1 = tk.Entry(frame, bg='lightsteelblue3', fg='black', font='30')
entry1.place(x=10, y=40, relwidth=0.05)


label2 = tk.Label(frame, text='К-ть ранжувань ', bg='lightsteelblue2', font='20')
label2.place(x=10, y=70)

entry2 = tk.Entry(frame, bg='lightsteelblue3', fg='black', font='30')
entry2.place(x=10, y=100, relwidth=0.05)

button2 = tk.Button(frame, text='Розрахувати', command=input_ranger,  bg='lightsteelblue1', fg='black', font=('helvetica', 12, 'bold'))

button1 = tk.Button(frame, text='Ввести данні', command=input_quantity_alter,  bg='lightsteelblue1', fg='black', font=('helvetica', 12, 'bold'))
button1.place(x=10, y=140)


root.mainloop()
