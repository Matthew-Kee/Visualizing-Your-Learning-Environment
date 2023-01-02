# What will your learning environment really feel like?
This is a web app that enables current and incoming University of Waterloo students to visualize the environmental conditions in their classrooms and study spaces, then compare them to industry standards for minimum/maximum allowable temperature, humidity, light, and sunlight. 

This was one of three design options that were prototyped by our team to educate students and empower them to advocate for better learning conditions and improved quality of life on campus. 

## How Does It Work?
The web app displays 4 interactive plots with data that we collected over the course of one week in 3 environments: an engineering classroom, a university library, and an engineering study lounge. Each plot is then overlayed with the acceptable ranges defined by ASHRAE, the American Society of Heating, Refrigerating and Air-Conditioning Engineers. 

Data was collected using a portable device that we designed and built, run by an Arduino, with code written in C. 

The app was deployed to Heroku using Docker. 

## Conclusion
**Our visualizer clearly demonstrated that classrooms exceed the acceptable standards for both temperature and humidity, while study spaces failed to meet minimum light requirements. User interviews with students confirmed that these conditions affected their ability to learn on campus. This project was presented to TAs, professors, and university administrators in an effort to demand better learning environments for our students.**

## Credits
This app was written in Python using Dash and Pandas and created by Malak Ali and Matthew Kee, designed by Joy He, with contributions from Ada Hong and Martha Matsui. 
