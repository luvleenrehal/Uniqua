
from tkinter import *

root = Tk()
root.configure(background="lightblue")

high_70s = ['75', '76', '77', '78', '79']
low_80s = ['80', '81', '82', '83', '84', '85']
high_80s = ['85', '86', '87', '88', '89']
low_90s = ['90', '91', '92', '93', '94']
high_90s = ['95', '96', '97', '98', '99', '100']

greetings = ['hi', 'hello', "Hello", "Hi", "Hey", "hey"]
a = "Arts/Media, Social Sciences"

def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
    if e.get() in greetings:
        txt.insert(END, "\n" + "Bot -> Hello! I am Uniqua. I'm here to "
                               "help and guide you on which university and "
                               "program you should apply to. To get started, "
                               "enter 2 fields/programs you are interested in. "
                               "Choose from these given options: Arts/Media, "
                               "Computer Science, Healthcare, Social Sciences, "
                               "Business, Engineering")

    # get programs
    elif e.get() == "Arts/Media, Social Sciences":
        txt.insert(END, "\n" + "Bot -> Wonderful! The universities that align "
                               "with your interests are: York, Ryerson, UofT, "
                               "McMaster")
        txt.insert(END, "\n" + "Bot -> Now I just need your most current "
                               "grade 12 average to help you further.")
    elif e.get() == "Computer Science, Business":
        txt.insert(END, "\n" + "Bot -> Wonderful! The universities that align "
                               "with your interests are: UofT, Waterloo, "
                               "York, Laurier, Ryerson")
        txt.insert(END, "\n" + "Bot -> Now I just need your most current "
                               "grade 12 average to help you further.")
    elif e.get() == "Healthcare, Business":
        txt.insert(END, "\n" + "Bot -> Wonderful! The universities that align "
                               "with your interests are: McMaster, York, "
                               "Ryerson, Western")
        txt.insert(END, "\n" + "Bot -> Now I just need your most current "
                               "grade 12 average to help you further.")
    elif e.get() == "Arts/Media, Engineering":
        txt.insert(END, "\n" + "Bot -> Wonderful! The universities that align "
                               "with your interests are: York, Ryerson"
                               "Waterloo, Queens")
        txt.insert(END, "\n" + "Bot -> Now I just need your most current "
                               "grade 12 average to help you further.")

    # get averages
    elif e.get() in high_70s:
        txt.insert(END, "\n" + "Bot -> Based on your average and interests, I "
                               "have determined the best suited program for you is at York")
    elif e.get() in low_80s:
        txt.insert(END, "\n" + "Bot -> Based on your average and interests, I "
                               "have determined the best suited program for you is at Laurier!")
    elif e.get() in high_80s:
        txt.insert(END, "\n" + "Bot -> Based on your average and interests, I "
                               "have determined the best suited program for you is at Waterloo!")

    elif e.get() in low_90s:
        txt.insert(END, "\n" + "Bot -> Based on your average and interests, I "
                               "have determined the best suited program for you is at UofT!")
    elif e.get() in high_90s:
        txt.insert(END, "\n" + "Bot -> Based on your average and interests, I "
                               "have determined the best suited program for you is at McMaster!")


    else:
        txt.insert(END, "\n" + "Bot -> Sorry I do not understand. Please try "
                               "typing again.")
    e.delete(0, END)

# GUI (i combined my gui code to make it look cleaner)
root.geometry("1000x500")
root.title("Virtual Assistant")

txt = Text(root)
#scrollbar = Scrollbar(txt)
txt.grid(row=0, column=0, columnspan=2)

e = Entry(root, width=80)
#send = Button(root, text="SEND", command=send).grid(row=1, column=1)
button = Button(root, bg="Red", fg= "blue", text = "Ask Assistant",
                font = ("Times New Roman", 18), command=send).grid(row=2, column=2)
e.grid(row=1, column=0)
root.title("Chatbot")
root.mainloop()