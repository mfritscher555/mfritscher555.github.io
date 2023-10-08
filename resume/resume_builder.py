
import pdfkit
from xhtml2pdf import pisa


# Resume Builder - All of these fields can be edited!

date = "1023"

name = "Matthew Fritscher"
title = "Data Analytics Professional"

university_name = "Louisiana State University"

degree1_name = "M.S. Analytics - Information Systems & Decision Sciences"
degree1_date = "May 2023"


degree2_name = "B.S. Economics - International Trade & Finance"
degree2_date = "Dec 2021"

honors = "Summa Cum Laude"
job1_title = "Project Manager"
job1_company = "Louisiana State University - MS Analytics Consulting Project (First Guaranty Bank)"
job1_timeframe = "Jan 2023 - May 2023"
job1_bullet1 = "Led a Tableau project for First Guaranty Bank, transforming raw deposit data into dynamic visualizations and expanding analyses with additional financial metrics."
job1_bullet2 = "Organized a team of six Analytics Graduate students to analyze deposit data, design visualizations, document findings, and present insights to senior bank executives."
job1_bullet3 = "Implemented Scrum and GitHub for version control, ensuring efficient project management and seamless collaboration."
# job1_bullet4 = ""

job2_title = "Analytics Graduate Assistant"
job2_company = "Louisiana State University - Center for Analytics & Research for Transportation Safety (CARTS)"
job2_timeframe = "July 2022 - May 2023"
job2_bullet1 = "Collaborated with the analytics team to develop Python desktop applications for a Data Integration project, improving functionality and data accuracy by integrating data from various sources."
job2_bullet2 = "Created a statewide Excel-based crash percentage calculator, simplifying data input and aligning the tool with DOTD standards for seamless integration with current data tracking processes."
job2_bullet3 = "Refactored a Tableau application for HSIP to comply with MMUC5 convention, implementing dynamic calculations for an enhanced user experience and eliminating manual data updating."
job2_bullet4 = "Streamlined web applications on the CARTS website by providing comprehensive documentation for Python scripts, enabling efficient troubleshooting and streamlined maintenance."

programming_langauges = ""
data_viz = ""
data_etc = ""
other = ""


## Icons (HTML code in these strings)

briefcase_image_str = "-"
email_image_str = "-"
phone_image_str = "-"
website_image_str = "-"
job_str = "--"

style_string = """
/* Establishing a common font here */

/*
* {  margin: 0;
  padding: 0;
}


@page {
  size: letter;
}
*/

html,
body,
h1,
h2,
h3,
h4,
h5,
h6,
p {
  font-family: "Garamond";
  color: black;

}

.page-container {

  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  margin: 0 auto; /* Center the content */
  margin-top: 0.3rem;
  background-color: #fff; /* Set a white background */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Add a subtle shadow */
}

h1 {
  font-size: 3rem;
  font-weight: normal;
  margin: 0px;
}

h2 {
  font-size: 1.625rem;
  margin: 0.5rem;
  }

h3 {
  font-size: 1.2rem;
  margin: 0.3rem;
}

h4 {
  font-size: 1.05rem;
  margin: 0.3rem;
}

br {
  display: block; /* makes it have a width */
  content: ""; /* clears default height */
  margin-top: 20px; /* change this to whatever height you want it */
}

ul {
  list-style-type: circle;
  margin: 0.7rem;
}

li {
  margin: 0.3rem;
}

.left-column {
  -webkit-box-flex: 1;
      -ms-flex: 1;
          flex: 1;
  padding-left: 5px;
  padding-right:10px;
}

.right-column {
  -webkit-box-flex: 3;
      -ms-flex: 3;
          flex: 3;
  padding-right: 5px;
}

h5{
  text-align:right;
}

.job-bullets{
  margin-bottom: 5px;
}

p.university-name{
  font-size: 1.2rem;
  font-weight:bold;
  margin-bottom:0;
  margin-top: 0;
}

p.degree-name{
  font-size: 1.2rem;
  margin-top:0;
  margin-bottom: 0;
}

p {
  font-size: 1rem;
}


"""

## HTML string will update dynamically with the above fields

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
            <h3>{job1_title}</h3>
            <br>
            <h4>{job1_company}</h4>
            <li class="job-bullets">{job1_bullet1}</li>
            <li class="job-bullets">{job1_bullet2}</li>
            <li class="job-bullets">{job1_bullet3}</li>
            <hr>
            <h3>{job2_title}</h3>
             <br>
            <h4>{job2_company}</h4>
            <li class="job-bullets">{job2_bullet1}</li>
            <li class="job-bullets">{job2_bullet2}</li>
            <li class="job-bullets">{job2_bullet3}</li>
            <li class="job-bullets">{job2_bullet4}</li>
            <hr>
            <h2> EDUCATION</h2>
            <hr>
            
            <p class="university-name">{university_name}</p> 
            <p class="degree-name">{degree1_name}</p>
            <br>

            <p class="university-name">{university_name}</p> 
            <p class="degree-name">{degree2_name}, <b>Summa Cum Laude</b></p>
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









# Convert Markdown to HTML
# html_content = markdown2.markdown(markdown_content)

# Create a temporary HTML file with the styled Markdown content
# final_html_content = f"<style>{style_string}</style>{markdown_content}"




# # Convert HTML to PDF
with open('./resume/resume.html', 'w') as file:
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
pdfkit.from_file('./resume/resume.html', f'./resume/Matthew_Fritscher_{date}.pdf', configuration=config,options=options)


# with open('./resume/resume.html', "r") as source_file:
#     source_html = source_file.read()

# # Create a PDF file
# with open("./resume/resume_output_test.pdf", "wb") as output_file:
#     pisa.CreatePDF(source_html, output_file)