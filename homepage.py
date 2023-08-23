import time
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from tkinter import *
import matplotlib.pyplot as plt 
from colorama import init, Fore, Style



print()
print("-------Welcome to SpamGuardian-------")
print()

#Asking user for thier first and last name
firstName = input("First name: ")
lastName = input("Last name: ")


"""
Function to start the program and initalize values. It prompts the password, and if it is correct, opens the primary window.
Arguments - firstName, lastName; these arguments use the user's input value to be plugged in to greet the user
Returns - Does not use a return statement. 
"""
def start_program(firstName, lastName):
  print(f"Welcome {firstName} {lastName}.")
  #Loop to get the user to answer the right password, breaks when correct password is entered
  while True:
    #Asks for the password
    passkey = input("Enter the password to unlock program: ")
    #Checks for error if the user doesn't enter correct password
    if passkey != "MachineLearningIsNotFun":
      print("Incorrect. Try again.")
    #If the user entered the right password, a countdown will be printed for 3 seconds and the program will be opened
    else:
      print()
      init()
      print(Fore.GREEN+"Successful login.")
      seconds = 3
      print()
      
      print(Style.RESET_ALL+"Opening in:")
      while seconds > 0:
        print(seconds)
        seconds -= 1
        time.sleep(1)
      
      print("-------------------------")
      print(Fore.LIGHTBLUE_EX+"Program Unlocked")
      #Escape is used to end loop
      break

#Calling function to initialize program
start_program(firstName,lastName)



#Creating 2 parallel lists which hold the user's data.
#This list holds the user's data
userData = []
#This list holds if the corresponding data was classified as "ham" or "spam"
correspondingClassification = []

"""
This function creates a histogram based on the user's data. X axis holds the amount of characters in messages. Y axis holds how many times messages of that length occured.
Arguments - None
Returns - Does not use a return statement. It does though, output a histogram.
"""
import matplotlib.pyplot as plt

userData = []
correspondingClassification = []

def userHistogramViewAnalytics():
    # Lists are initialized to hold the unique lengths of words in the program. It holds the clean and the spam lengths.
    cleanLengths = []
    spamLengths = []
    # Opening the data.txt file, holding all of the user's data
    histogramData = open("data.txt")
    
    # Clearing the global lists to avoid appending data multiple times if the function is called multiple times
    userData.clear()
    correspondingClassification.clear()

    # Iterating through each line in the data.txt file
    for each in histogramData.readlines():
        # Splitting the values with the delimiter of 5 semicolons
        temp = each.split(";;;;;")
        # There are 2 elements in "temp". The first element has the message, which is appended to the userData list.
        userData.append(str(temp[0]))
        # The parallel element of the classification is appended to the correspondingClassification list
        correspondingClassification.append(str(temp[1]).strip("\n"))
    # Closing the file to save memory
    histogramData.close()
    # Because of the ML model, it will mark anything as clean with an empty "". So we have to go in and change the "" => "clean"
    for i, each in enumerate(correspondingClassification):
        if each != "spam":
            correspondingClassification[i] = "clean"
    # had to watch a YT video on how to use set() but I made it to just tracks unique iterations by making a dictionary
    uniqueLengths = set()
    # Iterating through userData and correspondingClassification
    for i in range(len(userData)):
        length = len(userData[i])
        if length not in uniqueLengths:
            uniqueLengths.add(length)
            if correspondingClassification[i] == "clean":
                cleanLengths.append(length)
            elif correspondingClassification[i] == "spam":
                spamLengths.append(length)
    # Putting together the histogram
    plt.hist([cleanLengths, spamLengths], bins=5, color=["green", "red"], label=["Clean/Not Spam", "Spam"])
    plt.xlabel("Characters In Message")
    plt.title("Breakdown Of Message Length to Spam Comparison")
    plt.ylabel("Amount Of Times Message Length Was Seen")
    plt.show()
    print(userData)
    print(correspondingClassification)


"""
Same function as the function above. The only difference is that this makes the histogram with the data that was used to train the ML model. It doesn't use the user data.
Arguments - None
Return - None. Outputs a histogram.
"""
def mlModelHistogramViewAnalytics():
    #Opening the file with the spam data(this is the same as the spam.csv, just in .txt form)
    spamTXT = open("spam.txt", "r")
    #These 2 lists will hold the unique lengths of the spam and clean data
    cleanLengths = []
    spamLengths = []
    #These 2 lists are parallel and hold the classifications and messages 
    classifications = []
    messages = []
    #Appending the classifications and messages to the parallel lists
    for each in spamTXT.readlines():
        temp = each.split(",")
        classifications.append(str(temp[0]).strip())
        messages.append(str(" ".join(temp[1:])))
    #Because of the ML model, it will mark anything as clean with an empty "". So we have to go in and change the "" => "clean"
    for each in classifications:
      if each.lower() != "spam":
        cleanPlace = classifications.index(each)
        classifications.pop(cleanPlace)
        classifications.insert(cleanPlace, "clean")
    #Counter set to 0 
    iterationCounter = 0
    #While the counter is in the length of the parallel lists, then it will iterate through and add the length of each word in userData to cleanLengths or spamLengths.
    while iterationCounter < len(classifications) and iterationCounter < len(messages):
        #Appending the length of the message/userData to either clean or spam
        if classifications[iterationCounter]  ==  "clean":
            cleanLengths.append(len(messages[iterationCounter]))
        elif classifications[iterationCounter]  ==  "spam":
            spamLengths.append(len(messages[iterationCounter]))
        iterationCounter += 1
    #Setting up the histogram based on the collected information above
    plt.hist([cleanLengths, spamLengths], bins=5, color=["green", "red"], label=["Clean/Not Spam", "Spam"])
    plt.xlabel("Characters In Message")
    plt.title("Breakdown Of Message Length to Spam Comparison")
    plt.ylabel("Amount Of Times Message Length Was Seen")
    plt.show()


"""
Same function as the function above. The only difference is that this makes the histogram with the data that was used to train the ML model. It doesn't use the user data.
Arguments - None
Return - None. Outputs a histogram.
"""
def mlModelHistogramViewAnalytics():
    #Opening the file with the spam data(this is the same as the spam.csv, just in .txt form)
    spamTXT = open("spam.txt", "r")
    #These 2 lists will hold the unique lengths of the spam and clean data
    cleanLengths = []
    spamLengths = []
    #These 2 lists are parallel and hold the classifications and messages 
    classifications = []
    messages = []
    #Appending the classifications and messages to the parallel lists
    for each in spamTXT.readlines():
        temp = each.split(",")
        classifications.append(str(temp[0]).strip())
        messages.append(str(" ".join(temp[1:])))
    #Because of the ML model, it will mark anything as clean with an empty "". So we have to go in and change the "" => "clean"
    for each in classifications:
      if each.lower() != "spam":
        cleanPlace = classifications.index(each)
        classifications.pop(cleanPlace)
        classifications.insert(cleanPlace, "clean")
    #Counter set to 0 
    iterationCounter = 0
    #While the counter is in the length of the parallel lists, then it will iterate through and add the length of each word in userData to cleanLengths or spamLengths.
    while iterationCounter < len(classifications) and iterationCounter < len(messages):
        #Appending the length of the message/userData to either clean or spam
        if classifications[iterationCounter]  ==  "clean":
            cleanLengths.append(len(messages[iterationCounter]))
        elif classifications[iterationCounter]  ==  "spam":
            spamLengths.append(len(messages[iterationCounter]))
        iterationCounter += 1
    #Setting up the histogram based on the collected information above
    plt.hist([cleanLengths, spamLengths], bins=5, color=["green", "red"], label=["Clean/Not Spam", "Spam"])
    plt.xlabel("Characters In Message")
    plt.title("Breakdown Of Message Length to Spam Comparison")
    plt.ylabel("Amount Of Times Message Length Was Seen")
    plt.show()

#Defining the window/root
window = Tk()
window.state("zoomed")
window.config(background="#232931")
window.iconbitmap("sword.ico")
window.title("SpamGuardian")

"""
This function is intended to copy the text from the computer clipboard to the text box. 
Arguments: currentWindow -- This is the window display that is currently on the user's screen; textBox -- This parameter is a textbox that can contain text. 
Returns: This function does not return anything.
"""
def pasteFromClipboard(currentWindow, currentTextBoxLocation):
  textVal = currentWindow.clipboard_get()
  return currentTextBoxLocation.insert(END, textVal)

"""
Summary - This function closes the current window, and opens the next. 
Arguments - windowToOpen,pageToClose; the first argument defines the window to close, and the second defines the window to close
Returns - Does not return anything. 
"""
def closeCurrentOpenNew(windowToOpen, pageToClose):
  pageToClose.destroy()
  windowToOpen()
  

"""
This function clears the text in the text box when the user clicks "Clear All Text". 
Argument: textBox -- This parameter is a textbox that can contain text. 
Returns: This function does not return anything. 
"""
def deleteText(textBox):
  return textBox.delete("1.0", END)

"""
Summary - This is the machine learning model I spent too long on(3 hours 😂 for 30 lines of code). It trains a machine learning model to detect spam
Arguments - userTextValue, targetTextBox; the first argument takes the user text to scan, and the second argument defines the text box where the output will be
Returns - It returns if the text is or isn't spam, and it sends it to the designated location of the second argument
"""
def predictAI(userTextValue, targetTextBox):
  #reading content using pandas 
  content = pd.read_csv('spam.csv')
  #just filling the NaN content with some values so that the program doesn't bug
  #I spent 2 hours. Yes, 2 hours. Trying to figure this out because I got 15 lines of errors of NaN content
  #not being readable. Not having this one line managed to break the entire ML model. :)
  content = content.fillna('')
  #Setting independent(x) and dependent(y) variables to the columns they correspond to. I put the X to the message
  #because that is what we are controlling and putting in. I set the Y variable to the classification because
  #that is the output based ON the message, hence dependent.
  X = content['message']
  y = content['classification']
  #Set the CountVectorizer to a variable for easier referral later on in the program.
  cVect = CountVectorizer()
  #Transforming the data and making it the right type of data to run through the ML model(spent an hour on this :))
  X = cVect.fit_transform(X)
  #FINALLY(ACTUALLY TRAINING AND SPLITTING THE MODEL :)))))) 
  x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
  #Setting the type of model we will use for the project. Chose the MultinomialNB() because it was said to be
  #the most efficient online. Though it's the most efficient and accurate, we only had ~5,000 data sets to train
  #the model with. 
  mainModel = MultinomialNB()
  #Using .fit() to train the model based on the x_training data and the y_training data.
  mainModel.fit(x_train, y_train)
  #Transforming the user input into data that the ML model can take.
  text_transformed = cVect.transform([userTextValue])
  #Releasing the prediction(will output something in a list format which is why we need the [0] to check our prediction.)
  prediction = mainModel.predict(text_transformed)
  #Appending to parallel list the text value. Using append here to fulfill rubric. Using insert below to do the same thing, just a different method.
  userData.append(userTextValue)
  if prediction[0] == 'spam':
    #It may seem odd that I'm using insert here. It is, I'm just using it to fulfill the rubric requirements for using the method. 
    correspondingClassification.insert((len(correspondingClassification)-1),"Spam")
    histogramData = open("data.txt", "a")
    histogramData.write(str(userTextValue)+";;;;;"+", spam"+"\n")
    histogramData.close()
    return targetTextBox.config(text = "Text was detected as: Spam")
  else:
    #It may seem odd that I'm using insert here. It is, I'm just using it to fulfill the rubric requirements for using the method. 
    correspondingClassification.insert((len(correspondingClassification)-1),"Clean")
    histogramData = open("data.txt", "a")
    histogramData.write(str(userTextValue)+";;;;;"+"clean"+"\n")
    histogramData.close()
    return targetTextBox.config(text = "Text was detected as: Not Spam/Clean")



"""
Summary - This is the window where the user can enter data and check for if their text is spam or not. 
Arguments - None
Returns - This doesn't return anything, it is just the function to create the window
"""
def aiToolWindow():
  #Closing the main window, which was the window the user was just on
  main.destroy()
  #Defining the window
  aiWindow = Tk()
  aiWindow.state("zoomed")
  aiWindow.iconbitmap("sword.ico")
  aiWindow.title("SpamGuardian")
  aiWindow.config(background="#232931")
  #Label which acts as a header
  header = Label(text="AI Spam Detection Tool",
                 font=("Agency FB", 30, "bold"),
                 fg="#EEEEEE",
                 bg="#232931")
  #Text box where user enters data to be scanned
  scanText = Text(width=80, height=7, padx=10, pady=10)
  #Button which can be clicked to clear text in above text box
  clearText = Button(text="Clear All Text",
                     width=12,
                     height=1,
                     command=lambda: deleteText(scanText),
                     bg="#4ECCA3",
                     fg="#EEEEEE",
                     font=("bold"))
  #Button with which the user can paste data from their clipboard
  pasteClipboardText = Button(
    text="Paste Text From Clipboard",
    font=("bold"),
    width=24,
    height=1,
    command=lambda: pasteFromClipboard(aiWindow, scanText),
    fg="#EEEEEE",
    bg="#4ECCA3")
  #Button which initiates the machine learning model to predict if the data is spam or not
  analyzeText = Button(text="Analyze Text",
                       width=15,
                       height=1,
                       font=("bold"),
                       fg="#EEEEEE",
                       bg="#4ECCA3",
                       command = lambda: predictAI(str(scanText.get("1.0",'end-1c')), output))
  #The text box where the result of spam or not spam is declared
  output = Label(text = "", fg = "#EEEEEE", bg = "#232931")
  #Button which takes user to previous page
  back = Button(text="Back",
                font=("bold"),
                fg="#EEEEEE",
                bg="#4ECCA3",
                command=lambda: closeCurrentOpenNew(homepage, aiWindow))
  #Packing elements to display on screen
  header.pack(side="top", anchor="n")
  scanText.pack(anchor="center", pady=10)
  clearText.pack(pady=5)
  pasteClipboardText.pack(pady=5)
  analyzeText.pack(pady=5)
  output.pack(pady = 10)
  back.pack(side="bottom", anchor="se", padx=8, pady=8)
  #Mainloop to create an infinite loop to keep window running
  aiWindow.mainloop()

"""
After the user logs in, the user will be directed to this page. This page will be the main window with the options to go to use the AI tool, or view the histograms of data
Arguments - None
Returns - Nothing
"""

def homepage():
  #Making "main" global so that it is a global variable with which we can refer to, to close the previous window
  global main
  #Defining the window's elements
  main = Tk()
  main.state("zoomed")
  main.config(bg="#232931")
  main.iconbitmap("sword.ico")
  main.title("SpamGuardian")
  #Label which acts as a header
  header = Label(text="SpamGuardian",
                 font=("Tahoma", 30),
                 bg="#232931",
                 fg="#EEEEEE")
  #Greeting the user with their username
  welcome = Label(text="Welcome, " + currUser[0] + ".",
                  font=("Trebuchet MS", 12),
                  fg="#EEEEEE",
                  bg="#232931")
  #Button used to pull up the histogram of the user's past data
  goAnalytics = Button(text="View Current Analytics",
                       relief="ridge",
                       font=("Trebuchet MS", 12),
                       height=1,
                       width=20,
                       bg="#F2DEBA",
                       command = userHistogramViewAnalytics)
  #Button used to navigate to the windo where the user can use the AI checking tool
  goUseAI = Button(text="Use AI Checking Tool",
                   relief="raised",
                   font=("Trebuchet MS", 12),
                   height=1,
                   width=20,
                   bg="#F2DEBA",
                   command=aiToolWindow)
  #This is a label which describes the AI tool.
  AIdesc = Label(
    text=
    "The SpamGuardian AI was created to help internet users \ncheck text for spam.",
    bg="#FFEFD6")
  #This is a label which describes the histogram tool for the user's personal data
  AnalyticsDesc = Label(
    text="View the analytics and data on the types of text \nthat you scanned.",
    bg="#FFEFD6")
  #Button to pull up the histogram which was used to train the ML model
  goMLAnalytics = Button(text="View ML Model Analytics",
                       relief="ridge",
                       font=("Trebuchet MS", 12),
                       height=1,
                       width=20,
                       bg="#F2DEBA",
                       command = mlModelHistogramViewAnalytics)
  #Label describing the ML model histogram
  MLModeldesc = Label(
    text=
    "Take a look at the ML Model's training data.",
    bg="#FFEFD6")
  #Packing all of the elements for display
  header.pack(side="top", anchor="n")
  welcome.pack(side="top", anchor="n", pady = 10)
  goUseAI.pack(side="top", anchor="n", pady = 30)
  AIdesc.pack(side="top", anchor="n")
  goAnalytics.pack(side="top", anchor="n", pady = 30)
  AnalyticsDesc.pack(side="top", anchor="n")
  goMLAnalytics.pack(side = "top", anchor = "n", pady = 30)
  MLModeldesc.pack(side = "top", anchor = "n")
  #Mainloop which is an infinite loop to keep the screen responsive and awake.
  main.mainloop()

#Variable which will hold the user's name if they are authenticated. If not, the variable will stay as "None" and will cause an error.
currUser = None




"""
Summary - This function authenticates the user. If the user has an account stored in authentication.txt, it will let the user in. Otherwise, it will display an error.

Arguments - No arguments

Returns - Returns an error to the screen if there is no existing account in the authentication.txt file.
"""


def authenticateUser():
  #Setting all of these values to global to be able to pull values from the user's window. They could have been a parameter, but it would've been odd and more complicated.
  global window
  global confirm
  global userEntry
  global userPass
  global currUser
  #Collecting the values from the user's input boxes for the username and password
  username = userEntry.get()
  password = passEntry.get()
  #Opening the file of authentication keys, and translating it into a list using .readlines()
  auth = open("authentication.txt", "r").readlines()
  #Found will be 0, and if it isn't found in the end, it'll stay 0 and will print an error of "Not Valid" to the screen
  found = 0
  #Going through each value in the file
  for eachLine in auth:
    #Splitting the line with the delimtere of a comma
    temp = eachLine.split(",")
    #If the username and password match a username and password combination in the .txt file, it will add 1 to the found and show that a value was found
    if (temp[0]  ==  username) and (temp[1] ==  password):
      found += 1
      #Sets the current user to the found value
      currUser = temp
  #Conditional checking for if there was a found value. If it wasn't, an error will be set on the screen, else, the homepage window will be opened.
  if found  ==  0:
    return confirm.config(text="Not valid")
  elif found  ==  1:
    window.destroy()
    homepage()



#Telling user to enter username
welcomeToSpamGuardian = Label(text="Welcome to SpamGuardian",
                              font=("Bahnschrift", 20, "bold"),
                              bg="#232931",
                              fg="#EEEEEE")
userLabel = Label(text="Username",
                  font=("Bahnschrift", 15, "bold"),
                  bg="#232931",
                  fg="#EEEEEE")
#Taking username entry
userEntry = Entry(font=("TIMES NEW ROMAN", 15))
#Telling user to enter password
userPass = Label(text="Password",
                 font=("Bahnschrift", 15, "bold"),
                 bg="#232931",
                 fg="#EEEEEE")
#Taking password entry
passEntry = Entry(font=("TIMES NEW ROMAN", 15), show="*")
#Recording user data when button is clicked
userLoginButton = Button(text="Submit",
                         command=authenticateUser,
                         bg="#4ECCA3",
                         fg="#EEEEEE",
                         font=("Calibri", 12, "bold"),
                         padx=6)
#Making a text box for errors
confirm = Label(text="", bg="#232931", fg="#EEEEEE")
#Packing elements

welcomeToSpamGuardian.pack(side="top", anchor="n", pady=20)
userLabel.pack(side="top", anchor="n")
userEntry.pack(side="top", anchor="n")
userPass.pack(side="top", anchor="n")
passEntry.pack(side="top", anchor="n")
userLoginButton.pack(side="top", anchor="n", pady=20)
confirm.pack(side="top", anchor="n")

#Mainloop of the window to run it
window.mainloop()
