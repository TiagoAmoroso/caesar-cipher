from tkinter import *
from tkinter import ttk
import os

THIS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class GUIobject():
    def __init__(self):
        self.root = Tk()
        self.root.title("Caesar Cipher")
        self.root.geometry('500x500')
        icon = PhotoImage(file = THIS_DIRECTORY + '/Images/CaesarIcon.png') #SKSlogo.png
        self.root.iconphoto(False, icon)
        self.cipherText = ''

    def menu(self):
        frame = ttk.Frame(self.root, padding="5 5 5 5")
        frame.grid(column=0, row=0, sticky=(N, W, E, S))

        #Configure the row/col of our frame and root window to be resizable and fill all available space
        frame.grid_rowconfigure(0, weight=0) #Other than the rows
        frame.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        #Labels
        title = Label(frame, text = 'Caesar Cipher')
        title.grid(columnspan = 2)
        title.config(font=("Courier", 44))

        placeHolder = Label(frame)
        placeHolder.grid(column = 0, row = 1)
        placeHolder1 = Label(frame)
        placeHolder1.grid(column = 0, row = 4)
        placeHolder1 = Label(frame)
        placeHolder1.grid(column = 0, row = 6)

        messageLabel = Label(frame, text = 'Message: ')
        messageLabel.grid(column = 0, row = 2, sticky = W)
        shiftLabel = Label(frame, text = 'Shift: ')
        shiftLabel.grid(column = 0, row = 3, sticky = W)


        #Entries
        messageEntry = Entry(frame)
        messageEntry.grid(column = 1, row = 2, sticky = W)
        shiftEntry = Entry(frame)
        shiftEntry.grid(column = 1, row = 3, sticky = W)

        #Buttons
        useButton = Button(frame, text = 'Encrypt', fg = 'red', command = lambda : self.encrypt(message = messageEntry.get(), shift = shiftEntry.get()))
        useButton.grid(column = 0, row = 5, sticky = W)

        #Scrollbar and Displays
        '''
        scrollbar = Scrollbar(frame, orient = 'horizontal')
        scrollbar.grid(column = 0, row = 8)
        '''
        EncryptionDisplay = Text(frame, height = 5, borderwidth = 0) # xscrollcommand = scrollbar.set  <--  For setting scrollbar
        EncryptionDisplay.grid(column = 0, row = 7, columnspan = 2, sticky = W)
        EncryptionDisplay.insert(1.0, 'Encrypted message: ' + self.cipherText)
        EncryptionDisplay.configure(state="disabled")



    def encrypt(self, message, shift):
        shift = int(shift)
        self.cipherText = caesarShift(message, shift)
        self.menu()
        

        print('Your encrypted message: ' + self.cipherText)

        decryptedText = caesarShift(self.cipherText, -shift)

        print('Your unencrypted message: ' + decryptedText)

        


def caesarShift(message, shiftSize):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    message = list(message)
    cipherText = ''

    #Iterating through each character in message
    for character in range(len(message)):
        upper = False

        try:
            #Checking that the character being checked is in the alphabet
            if message[character].lower() in alphabet:

                #Finding out the position of the character in the alphabet
                position = alphabet.index(message[character].lower()) 
                #Checking if the character being checked is upper case
                if message[character] == message[character].upper():
                    upper = True  

                #Setting the position of the shifted character 
                newPosition = position + shiftSize

                #Ensuring that the position of the shifted character is within the range of the alphabet
                while newPosition > len(alphabet) - 1:
                    newPosition -= len(alphabet)
                while newPosition < 0:
                    newPosition += len(alphabet)
                #Adding the shifted character to the cipherText
                if upper:
                    cipherText += alphabet[newPosition].upper()
                else:
                    cipherText += alphabet[newPosition]
            #Checking if the character being checked is a space
            elif message[character] == ' ':
                cipherText += ' '

            else:
                print('Character not recognised - Not within the English alphabet')
                
        except Exception as error:
            print(error)
            print('Character not recognised - Not within the English alphabet')

    return cipherText


GUI = GUIobject()
GUI.menu()
GUI.root.mainloop()


'''
shift = 2

message = input('Punctuation and numbers are removed from your message\nEnter your message: ')

cipherText = caesarShift(message, shift)

print('Your encrypted message: ' + cipherText)

decryptedText = caesarShift(cipherText, -shift)

print('Your unencrypted message: ' + decryptedText)
'''
