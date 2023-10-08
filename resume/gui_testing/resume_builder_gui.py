import PySimpleGUI as sg
import pdfkit
from xhtml2pdf import pisa
from backend_code import style_string



# Define the layout of the window
layout = [
    [sg.Text("What is your name?"),sg.InputText(key="name")],
    [sg.Text("What is your job title/industry?"),sg.InputText(key="title")],
    # [sg.Text("What contact information do you want to include?"), sg.Listbox(values=['Email', 'Phone', 'Website', 'LinkedIn'], size=(20, 4), key='contact-info', select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE)],


    [sg.Button('OK')]
]

# Create the window
window = sg.Window('Welcome to the Resume Builder App!', layout)

# Event loop to process events and interact with the window
while True:
    event, values = window.read()
    
    # If the window is closed or the button is clicked
    if event == sg.WINDOW_CLOSED:
        break
    if event == "OK":
        name = values["name"]
        title = values["title"]
        date = "1023"


        print(contact_info)


        html_string = f"""


        <!DOCTYPE html>
        <html>
        <head>
        <style>{style_string}</style>
        <title>Home</title>
        <meta charset="UTF-8">
        </head>


        <!-- Page Container -->
        <div class="page-container">


        

        
            <!-- Left Column -->
            <div class="left-column">
            <div class="left-card">
                <div class="display-container">
                <div class="display-bottommiddle">
                </div>
                </div>
                <div class="container">
                <h1>{name}</h1>
                <h2>{title}</h2>
                <h3> Contact Information </h3>
                <p>Email: mfritscher555@yahoo.com</p>
                <p>Phone: 985-867-0661</p>
                <p>Website: mfritscher555.github.io</p>

                <h3 class="left-column-title">Technical Skills</h4>
        
                <h4 class="left-column-subtitle">Programming languages</h4>
                    <ul>
                        <li> Python</li>
                        <li>R</li>
                        <li>SQL - (T-SQL & MySQL)</li>
                    </ul>
                    <h4 class="left-column-subtitle">Data Visualization</h4>
                    <ul>
                        <li>Tableau</li>
                        <li>seaborn</li>
                        <li>matplotlib</li>
                        <li>ggplot</li>
                    </ul>

                    <h4 class="left-column-subtitle">Machine Learning</h4>
                    <ul>
                    <li>TensorFlow</li>
                    <li>XGBoost</li>
                    <li>scikit-learn</li>
                    </ul>

                    <h4 class="left-column-subtitle">Other Tools</h4>
                    <ul>
                    <li>pandas, numpy, scipy</li>
                    <li>Excel Solver/Analysis Toolpak</li>
                    <li>HTML5, CSS</li>
                    <li>regex</li>
                    <li>SAS, JMP</li>
                    <li>STATA</li>
                    <li>RapidMiner</li>
                    <li>Web Scraping - scrapy</li>
                    </ul>
                <h4 class="left-column-subtitle">Languages</h4>
                <ul>
                <li>Spanish - Professional Fluency ~C1 </li>
                <li>Japanese - Beginner ~A2</li>

                </div>
            </div><br>

            



            <!-- End Left Column -->
            </div>

            <!-- Right Column -->
            <div class="right-column">
            <div class="right-card">
                <div class="container">
                <div class="sub-container">
                <h2>EXPERIENCE</h2>
                <hr>
                    <h3>JOB TITLE 1</h3>
                    <br>
                    <h4>JOB 1 COMPANY NAME HERE</h4>
                    <li class="job-bullets">job1_bullet1</li>
                    <li class="job-bullets">job1_bullet2</li>
                    <li class="job-bullets">job1_bullet3</li>
                    <hr>
                    <h3>job2_title</h3>
                    <br>
                    <h4>job2_company</h4>
                    <li class="job-bullets">job2_bullet1</li>
                    <li class="job-bullets">job2_bullet2</li>
                    <li class="job-bullets">job2_bullet3</li>
                    <li class="job-bullets">job2_bullet4</li>
                    <hr>
                    <h2> EDUCATION</h2>
                    <hr>
                    
                    <p class="university-name">university_name</p> 
                    <p class="degree-name">degree1_name</p>
                    <br>

                    <p class="university-name">university_name</p> 
                    <p class="degree-name">degree2_name, <b>Summa Cum Laude</b></p>
                    Activities: LSU Tiger Marching Band (4 Years) - Trumpet
                    <br>

                    <p class="university-name">Universidad de Granada</p>
                    <p class="degree-name"> Centro de Lenguas Modernas, Granada, Spain</p>
                    <li>Spanish minor coursework completed during study abroad program in Granada, Spain.</li>



                    

                </div>
            </div>

            <!-- End Right Column -->
            </div>
            
        <!-- End Grid -->
        </div>
        
        <!-- End Page Container -->
        </div>
        </body>
        </html>


        """













        # # Convert HTML to PDF
        with open('./resume/resume_gui_test.html', 'w') as file:
            file.write(html_string)



        # Specify the path to wkhtmltopdf executable
        config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

        options = {"page-size":"Letter",
                "margin-top":"0in",
                    "margin-bottom":"0in",
                "margin-left":"0in",
                "margin-right":"0in",
                'encoding': "UTF-8",
                "print-media-type": True,
                'disable-smart-shrinking': True,
                }

        # Convert HTML to PDF
        pdfkit.from_file('./resume/resume_gui_test.html', f'./resume/{name}_resume_test_{date}.pdf', configuration=config,options=options)


        # with open('./resume/resume.html', "r") as source_file:
        #     source_html = source_file.read()

        # # Create a PDF file
        # with open("./resume/resume_output_test.pdf", "wb") as output_file:
        #     pisa.CreatePDF(source_html, output_file)


        break