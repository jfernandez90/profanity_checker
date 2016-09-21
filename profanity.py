from Tkinter import *
import urllib 
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    #Gives user output signaling whether there is a curse word in the text or not
    if "true" in output:
        print("Wow, you kiss your mother with that mouth?")
    elif "false" in output:
        print("Yay, no curse words!")
class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Check for Profanity")
        self.label = Label (self.root, text= "Enter your file path")
        self.label.pack()

        #User inputs file path 
        self.entrytext = StringVar()
        Entry(self.root, textvariable=self.entrytext).pack()

        self.buttontext = StringVar()
        self.buttontext.set("Open")
        Button(self.root, textvariable=self.buttontext, command=self.read_text).pack()

        self.label = Label (self.root, text="")
        self.label.pack()

        self.root.mainloop()


    def read_text(self):
       input = self.entrytext.get()
       doc = open(input)
       contents = doc.read()
       #print(contents)
       doc.close
       check_profanity(contents)
 
    def button_click(self, e):
        pass

App()



