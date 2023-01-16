# Developing a Desktop Application 

Using the framework PySimpleGUI, I created a desktop application for my Graduate Assistantship position. For the backend, which I had already written, I refactored the scripts such that they could be called as functions within the PySimpleGUI framework. 

PySimpleGUI does exactly what its name implies - it provides a way to create a user interface in a simple manner. The goal of my program was to accept two files as inputs, do back-end calculations (which is beyond the scope of this blog) and return a folder with the outputs. In the case of this app, two Excel files are to be accepted as inputs, and 5 Excel files are returned as outputs. 

In basic Python programming, the `input()` function is used to accept user inputs. Similarly, using the `PySimpleGUI` package, you can accept inputs in a much more user-friendly manner. Below is the code for the front-end of the app.

The second function in this script creates the prompts for the first window. This window accepts inputs that connect to a user's local DB. However, this is an optional step. Once either the "Enter" button or "I don't have a local DB" buttons are pressed, the first function is then run. This function then accepts the inputs for the functions in the back-end; once the "Enter" button is pressed, the program runs and terminates once finished. The output files are put into a folder, and if the user inputted local DB information, the tables are created there as well.




```py
## DESKTOP APPLICATION VERSION

if __name__ == "__main__":

    # ---------------imports---------------
    import numpy as np
    import pandas as pd
    import PySimpleGUI as sg
    import pyodbc
    from functions import func1, func2, func3


    ## ---------------------------------- SECOND WINDOW --------------------------------------------------------------
    ## Once the user has input local DB information (or skipped that step), they will be brought to this window, which contains
    ## the main functionality of the app

    
    def mainFunction():

        layout = [
                    [sg.Text("Welcome to my Sample App ")],
                    [sg.Text("Input first input file here:"), sg.Input(key="-Input1-"), sg.FileBrowse()],
                    [sg.Text("Input seconf input file here:"), sg.Input(key="-Input2-"), sg.FileBrowse()],
                    [sg.Exit(), sg.Button("Generate Output")], 
        ]

        window = sg.Window("Desktop Application", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Exit"):
                window.close()
                break
            elif event == "Generate Output":
                fullFileName1 = values["-Input1-"]
                trimmedFileName1 = fullFileName1[-14:].split('/')[-1].split('.')[0]

                fullFileName2 = values["-Input2-"]
                trimmedFileName2 = fullFileName2[-14:].split('/')[-1].split('.')[0]

                # Assuming inputs have same year and quarter...
                quarters = [str.upper(fullFileName1.split('_', 1)[1])]
                loweryear = int(quarters[0].split('_', 1)[1]) - 3
                upperyear = loweryear + 4

                # date
                conditions = [
                    quarters[0].__contains__('Q1'),
                    quarters[0].__contains__('Q2'),
                    quarters[0].__contains__('Q3'),
                    quarters[0].__contains__('Q4')
                ]

                choices = ['-04-01', '-07-01', '-10-01', '-01-01']
                date = np.select(conditions, choices)
                inputfile1 = pd.read_excel(values["-Input1-"])
                inputfile2 = pd.read_excel(values["-Input2-"])

                try:

                    func1(inputfile=inputfile1, quarters=quarters, loweryear=loweryear, upperyear=upperyear, date=date, conn_16=conn_str_16)
                    func2(inputfile=inputfile2, quarters=quarters, loweryear=loweryear, upperyear=upperyear, date=date, conn_16=conn_str_16)
                    func3(inputfile1=inputfile1, inputfile2=inputfile2,quarters=quarters, conn_16=conn_str_16)

                    # clsoes the window once the program is done
                    window.close()
                    break

                except Exception as e:
                    sg.popup(e)
                    continue
                break


            window.close()



#### --------------------------------- Connecting to the user's local db -------------------------------------------

    def firstWindow():

        layout = [
            [sg.Text("Input your local db server name here:"), sg.Input(key="-SERVER-")],
            [sg.Text("Input your Database name here:"), sg.Input(key="-DB-")],
            [sg.Text("Input your local db USERNAME here:"), sg.Input(key="-UID-")],
            [sg.Text("Input your local db PASSWORD here: NOT SECURE"), sg.InputText("",key="-password-", password_char='*')],
            [sg.Button("Enter"), sg.Button("I don't have a local DB")],
            [sg.Exit()] ]

        window = sg.Window("Connection to Local DB", layout)

        while True:
            try:
                event, values = window.read()
                if event in (sg.WINDOW_CLOSED, "Exit"):
                    window.close()
                    break
                elif event == "Enter":
                    server = values["-SERVER-"]
                    database = values["-DB-"]
                    username = values["-UID-"]
                    password = values["-password-"]
                    global conn_str_16 # so it can be accessed in the mainFunction
                    conn_str_16 = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
                    # cursor_16 = conn_str_16.cursor()
                    mainFunction()
                elif event == "I don't have a local DB":
                    conn_str_16 = None
                    mainFunction()
                else:
                    break
                window.close()
            except Exception as e:
                sg.popup(e)
                continue
            break
        window.close()


    firstWindow()
```