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

    [sg.Text("Please enter in your most recent work experience information below")],
    [sg.Text("What was your job position/title?"), sg.InputText(key="job_title1")],
    [sg.Text("What was the company name?"), sg.InputText(key="company_name1")],
    [sg.Text("Please include job duties and responsibilities in up to four bullet points below:")],
    [sg.Text("What to include in first bullet point?"), sg.InputText(key="job1_bullet1")],
    [sg.Text("What to include in second bullet point?"), sg.InputText(key="job1_bullet2")],
    [sg.Text("What to include in third bullet point?"), sg.InputText(key="job1_bullet3")],
    [sg.Text("What to include in fourth bullet point?"), sg.InputText(key="job1_bullet4")],
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
        ## UNCOMMENT OUT FOR TESTING SO USER CAN INPUT THEIR OWN INFO
        # name = values["name"]
        # title = values["title"]
        # date = "1023"
        # phone_number = values["phone-number"]
        # email = values["email-address"]

        # experience1_job_title = values["job_title1"]
        # experience1_company_name = values["company_name1"]
        # experience1_bullets = values["job1_bullet1"] + "\n" + values["job1_bullet2"] + "\n" + values["job1_bullet3"] + "\n" + values["job1_bullet4"] + "\n"

        
        ## FOR NOW, SAVING MY INFO FOR TESTING PURPOSES

        
        date = "1023"

        name = "Matthew Fritscher"
        title = "Data Analytics Professional"
        email = "mfritscher555@yahoo.com"
        phone_number = "985-867-0661"

        university_name = "Louisiana State University"

        degree1_name = "M.S. Analytics - Information Systems & Decision Sciences"
        degree1_date = "May 2023"


        degree2_name = "B.S. Economics - International Trade & Finance"
        degree2_date = "Dec 2021"

        honors = "Summa Cum Laude"
        experience1_job_title = "Project Manager"
        experience1_company_name = "Louisiana State University - MS Analytics Consulting Project (First Guaranty Bank)"
        job1_timeframe = "Jan 2023 - May 2023"
        job1_bullet1 = "Led a Tableau project for First Guaranty Bank, transforming raw deposit data into dynamic visualizations and expanding analyses with additional financial metrics."
        job1_bullet2 = "Organized a team of six Analytics Graduate students to analyze deposit data, design visualizations, document findings, and present insights to senior bank executives."
        job1_bullet3 = "Implemented Scrum and GitHub for version control, ensuring efficient project management and seamless collaboration."
        job1_bullet4 = ""



        # reformat below if conditionals into a function so that all optional resume features can be run through this function

        # Optionally including website into resume. (improve LOGIC here for user not following instructions)


        def optional_resume_features(feature_type, radio_result, user_text):
            """Takes in user input to create html that will be used in the html_string

            Parameters: 
            feature_type: Is this the website, the linkedin, etc?
            radio_result: If true, the label will be created in resume. otherwise it not be included in html string
            user_text: the text that the user typed/pasted into the GUI

            Returns: An html string to be inserted into the `html_string` variable, which ultimately is used to create the html version of the resume.
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


        def experience(h3_content, h4_content, user_input_bullet1, user_input_bullet2, user_input_bullet3, user_input_bullet4):

            """Takes in the user input and returns the appropriate html to insert into the `html_string` variable.
            
            Parameters: 
            h3_content: Job Title
            h4_content: Company Name (and description)
            user_input: Is a list of the inputs recorded by the user (the bullet points under the experience). This list is then
            iterated through and the html is written as long as there is content for that bullet. Otherwise, no bullet is created
            to avoid having empty bullet points on the page.
            
            """
            
            bullet_list = [user_input_bullet1, user_input_bullet2, user_input_bullet3, user_input_bullet4]
            h3_content_string = f"\n<h3>{h3_content}</h3>\n<br>"
            h4_content_string = f"<h4>{h4_content}</h4>\n"
            # bullet_list = user_input_bullet.split('\n')
            bullet_point = ""
            for item in bullet_list:
                if len(str(item)) > 0:
                    bullet_point += f"""<li class="job-bullets">{item}</li>\n"""
                else:
                    last_bullet_point = ""
            result = h3_content_string + h4_content_string + bullet_point + last_bullet_point
            return result
        

        
        # Actual Code 
        # experience1_string = meat_and_potatoes(experience1_job_title, experience1_company_name, values["job1_bullet1"], values["job1_bullet2"], values["job1_bullet3"], values["job1_bullet4"])


        # Tester Code
        experience1_string = experience(experience1_job_title, experience1_company_name, job1_bullet1, job1_bullet2, job1_bullet3, job1_bullet4)




        def education(degree_name, university_name, optional_information):

            if len(str(optional_information)) > 0:

                result = f""" <p class="university-name">{university_name}</p> 
                            <p class="degree-name">{degree_name}</p>
                            <br>{optional_information}
                            """
            else:
                result = f""" <p class="university-name">{university_name}</p> 
                            <p class="degree-name">{degree_name}</p>
                            <br>
                            """

            
            return result


        education1_string = education(degree1_name, university_name, "")


                

        html_string = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>{style_string}</style>
        <title>{name}'s Resume</title>
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
                    {experience1_string}
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
                    {education1_string}
                    
                    <p class="university-name">university_name</p> 
                    <p class="degree-name">degree1_name</p>
                    <br>

                    <p class="university-name">university_name</p> 
                    <p class="degree-name">degree2_name</p>
                    <br>
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