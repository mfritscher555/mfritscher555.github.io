

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
  overflow-wrap: break-word;

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
  overflow-wrap: break-word;
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