"""author: Luvleen Rehal, Meghna Ghosh"""
from tkinter import *

root = Tk()
root.configure(background="seagreen")

high_70s = ['75', '76', '77', '78', '79']
low_80s = ['80', '81', '82', '83', '84', '85']
high_80s = ['85', '86', '87', '88', '89']
low_90s = ['90', '91', '92', '93', '94']
high_90s = ['95', '96', '97', '98', '99', '100']

greetings = ['hi', 'hello', "Hello", "Hi", "Hey", "hey"]


def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
    if e.get() in greetings:
        txt.insert(END, "\n" + "UniQua -> Hello! I am UniQua. I'm here to "
                               "help and guide you on which university and "
                               "program you should apply to. To get started, "
                               "enter 2 programs you are interested in. "
                               "Choose from these given options: Arts/Media, "
                               "Computer Science, Healthcare, Social Sciences, "
                               "Business, Engineering")

    # get programs

    #first option
    elif e.get() == "Arts/Media, Social Sciences":
        txt.insert(END, "\n" + "UniQua -> Wonderful! The universities that align "
                               "with your interests are: York, Ryerson, UofT, "
                               "McMaster")
        txt.insert(END, "\n" + "UniQua -> Now I just need your most current "
                               "grade 12 average to help you further.")
    # for arts
    elif e.get() in high_70s:
        txt.insert(END, "\n" + "UniQua -> Based on your average and interests, I "
                               "have determined the best suited program for you!:"
                               "Arts/Media at York University")
    # for social Science
    elif e.get() in low_80s:
        txt.insert(END, "\n" + "UniQua -> Based on your average and interests, I "
                               "have determined the best suited program for you!:"
                               "Social Sciences at Ryerson University")

    # second option
    elif e.get() == "Computer Science, Business":
        txt.insert(END, "\n" + "UniQua -> Wonderful! The universities that align "
                               "with your interests are: UofT, Waterloo, "
                               "York, Laurier, Ryerson")
        txt.insert(END, "\n" + "UniQua -> Now I just need your most current "
                               "grade 12 average to help you further.")
    # for business
    elif e.get() in low_80s:
        txt.insert(END, "\n" + "UniQua -> Based on your average and interests, I "
                               "have determined the best suited program for you!:"
                               "Business at Ryerson")
    # for computer science
    elif e.get() in low_90s:
        txt.insert(END, "\n" + "UniQua -> Based on your average and interests, I "
                               "have determined the best suited program for you!:"
                               "Computer Science at Waterloo")


    # third option
    elif e.get() == "Healthcare, Business":
        txt.insert(END, "\n" + "UniQua -> Wonderful! The universities that align "
                               "with your interests are: McMaster, York, "
                               "Ryerson, Western")
        txt.insert(END, "\n" + "UniQua -> Now I just need your most current "
                               "grade 12 average to help you further.")
    # for healthcare
    elif e.get() in low_90s:
        txt.insert(END, "\n" + "UniQua -> Based on your average and interests, I "
                               "have determined the best suited program for you!:"
                               "Health sciences at McMaster University")
    # for Business
    elif e.get() in high_80s:
        txt.insert(END, "\n" + "UniQua -> Based on your average and interests, I "
                               "have determined the best suited program for you!:"
                               "Business at York University")

    # fourth option
    elif e.get() == "Arts/Media, Engineering":
        txt.insert(END, "\n" + "UniQua -> Wonderful! The universities that align "
                               "with your interests are: York, Ryerson"
                               "Waterloo, Queens")
        txt.insert(END, "\n" + "UniQua -> Now I just need your most current "
                               "grade 12 average to help you further.")
    # for engineering
    elif e.get() in high_90s:
        txt.insert(END, "\n" + "UniQua -> Based on your average and interests, I "
                               "have determined the best suited program for you!:"
                               "Engineering at Waterloo")
    # for Arts
    elif e.get() in low_80s:
        txt.insert(END, "\n" + "UniQua -> Based on your average and interests, I "
                               "have determined the best suited program for you!:"
                               "Design/Media at Ryerson")
    # if bot cannot understand
    else:
        txt.insert(END, "\n" + "UniQua -> Sorry I do not understand. Please try "
                               "typing again.")
    e.delete(0, END)


# GUI
root.geometry("1000x500")
root.title("Virtual Assistant")

txt = Text(root)
txt.grid(row=0, column=0, columnspan=1)

e = Entry(root, width=90)
button = Button(root, bg="Orange", fg= "White", text = "Ask UniQua",
                font = ("Trebuchet Ms", 25), command=send).grid(row=2, column=2)

e.grid(row=1, column=0)
root.title("UniQua: Your Virtual Assistant")
root.mainloop()
