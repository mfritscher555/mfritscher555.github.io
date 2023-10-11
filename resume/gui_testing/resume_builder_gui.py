import PySimpleGUI as sg
import pdfkit
from xhtml2pdf import pisa
from backend_code import style_string



## Features to include:
## If key fields are left blank, have a popup occur to alert the user. Do not kill the program, but instead allow the user to correct
## his mistakes and then be able to still press "GO!"



# Define the layout of the window
layout = [
    [sg.Text("Welcome to the Resume Builder App!\nNeed helping designing a resume? You have come to the right place!\nAnswer the form below, and we will generate a pretty resume for you!")],
    [sg.Text("This section gathers your personal information and creates a section so that hiring managers can easily contact you.")],
    [sg.Text("What is your name?"),sg.InputText(key="name")],
    [sg.Text("What is your job title/industry?"),sg.InputText(key="title")],
    [sg.Text("Type in your phone number here, so that hiring managers can contact you!"), sg.InputText(key='phone-number')],
    [sg.Text("Likewise, type in your email address here:"), sg.InputText(key='email-address')],    
    [sg.Text("Do you have a website? If so, check YES and provide the link. Otherwise, check NO")],
    [sg.Radio("YES", "WEBSITE_RADIO", key="has_website"), sg.Radio("NO", "WEBSITE_RADIO", default=True, key="no_website"), sg.InputText(key="website_input")],
    [sg.Text("Do you have a LinkedIn page? If so, check YES and provide the link. Otherwise, check NO")],
    [sg.Radio("YES", "LINKEDIN_RADIO", key="has_linkedin"), sg.Radio("NO", "LINKEDIN_RADIO", default=True, key="no_linkedin"), sg.InputText(key="linkedin_input")],
    [sg.Text("This next section will contain all of the skills that you want to list on your resume!")],
    [sg.Text("Do you want to include technical skills on your resume? Type in a skill and press enter. Repeat until you have entered all your desired skills."), sg.Multiline(key="technical_skills")],
    [sg.Button('GO!')],
    ]



# Create the window
window = sg.Window('Welcome to the Resume Builder App!', layout)

# Event loop to process events and interact with the window
while True:
    event, values = window.read()
    
    # If the window is closed or the button is clicked
    if event == sg.WINDOW_CLOSED:
        break
    if event == "GO!":
        name = values["name"]
        title = values["title"]
        date = "1023"
        phone_number = values["phone-number"]
        email = values["email-address"]


        # reformat below if conditionals into a function so that all optional resume features can be run through this function

        # Optionally including website into resume. (improve LOGIC here for user not following instructions)


        def optional_resume_features(feature_type, radio_result, user_text):
            """Takes in user input to create html that will be used in the html_string

            Parameters: 
            feature_type: Is this the website, the linkedin, etc?
            radio_result: If true, the label will be created in resume. otherwise it not be included in html string
            user_text: the text that the user typed/pasted into the GUI
            """
            if radio_result is True:
                if user_text is not None:
                    if feature_type in ["Website", "LinkedIn"]:
                        result = f"<p>{feature_type}: {user_text}</p>"
                    elif feature_type == "Technical Skills":
                        result_list = user_text.split('\n')
                        result1 = f"""<h4 class="left-column-subtitle">{feature_type}:</h4>"""
                        result2 = "<ul>"
                        result3 = "" # intialize to be empty
                        for item in result_list:
                            result3 += f"<li>{item}</li>"
                        result4 = "</ul>"
                        result = result1 + result2 + result3 + result4
                    return result
                
            else:
                feature_type = ""
                user_text = ""
                result = ""
                return result
            
            
        website_string = optional_resume_features("Website", values["has_website"], values["website_input"])
        linkedin_string = optional_resume_features("LinkedIn", values["has_linkedin"], values["linkedin_input"])
        technical_skills_string = optional_resume_features("Technical Skills", True, values["technical_skills"])


                

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
                <p>Email: {email}</p>
                <p>Phone: {phone_number}</p>
                {website_string}
                {linkedin_string}

                <h3 class="left-column-title">Skills</h3>
                {technical_skills_string}
        
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
        with open(f'./resume/gui_testing/{name}_resume_gui_test.html', 'w') as file:
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
        pdfkit.from_file(f'./resume/gui_testing/{name}_resume_gui_test.html', f'./resume/gui_testing/{name}_resume_test_{date}.pdf', configuration=config,options=options)


        # with open('./resume/resume.html', "r") as source_file:
        #     source_html = source_file.read()

        # # Create a PDF file
        # with open("./resume/resume_output_test.pdf", "wb") as output_file:
        #     pisa.CreatePDF(source_html, output_file)


        break