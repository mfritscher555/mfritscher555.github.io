
# Developing a Simple Web Application in Python

~ 9 December 2022 ~

The other day, I began learning the Flask framework in Python, which is used to develop web applications. This allowed me to practice using html and css, use Python in a way that I hadn't used it before, and learn the basics of software development. By no means do I think that I aspire to be a software developer, but it is a topic that has interested me for the past few months, and I decided to give it a crack.

The inspiration for the application sprouted from when I was trying to learn more about Object-Oriented programming. I began learning about classes in Python and how they can be used. In a practice file, I created different classes of shapes -- I gave each shapes unique attributes. For example, I created simple formulas that would calculate a circle's area and circumference, given its radius.

```py
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(radius):
        value = pi * self.radius ** 2
        return value

    def circumference(radius):
        value = 2 * pi * self.radius
        return value


```

I then created a web application that would accept a radius as an input, and would output the area and circumference as outputs. Though these calculations are simple, the focus on the project was learning *how* to implement this function in a way that is user-friendly. Here is a link to the tool in its current state: 

<https://hello-app-370916.uc.r.appspot.com/>


I then had to refactor my code such that the functions could be called within the Flask framework. 
The code can be found on my GitHub page [here](https://github.com/mfritscher555/webapp)



## Learning Curves

Learning the sytnax relevant to Flask was somewhat difficult, given that it is a brand-new package to me. It was an extremely rewarding feeling to finally enter an input into the box and generate an output.




