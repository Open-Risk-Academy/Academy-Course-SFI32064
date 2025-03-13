# Academy-Course-SFI32064

This repository contains supporting material for the [Open Risk Academy course](https://www.openriskacademy.com/course/view.php?id=64): "An introduction to Environmentally Extended Input-Output Economic Models using Python (the pymrio package)".
![US-IO](US-IO.png)

## Course Overview

This course is a DeepDive type course with nine course segments, exploring _economic Input-Output models_ using Python and the **Pymrio library**. 

The course is at a _core technical_ level. It requires working familiarity with Python, basic knowledge of linear algebra (vectors, matrices) and elements of economic systems. 

Step by step we explore how one can define and perform useful operations in Environmentally Extended Input-Output Analysis. This course is the first installment of a series dedicated to EEIO models. The focus here is on thorough familiarization with the Python environment (and the pymrio package in particular) and understanding the general structure and abilities of such a toolkit. 

## Specific Benefits

* We get exposed to the concept and structure of **Input-Output Models**
* We create a variety of stylized IO models in Python
* We perform basic IO related workflows as those are facilitated by the Pymrio package
* Discuss open and closed IO models
* Discuss hybrid IO models
* Work with a small but realistic IO table
* Illustrate the tasks of importing and slicing of production EEIO data

More in-depth discussion of economic and mathematical aspects of EEIO models is given in the seminal Miller-Blair Book, which is the main recommended reading for this course. The material we cover in this course is contained mostly in Chapter 2 of that book (Foundations of Input–Output Analysis).

## Related Courses

The Open Risk Academy includes several other courses that introduce different aspects of Input-Output Frameworks.

* [Working with large matrices using Command Line Tools](https://www.openriskacademy.com/course/view.php?id=76)
* [Input-Output Model Interactivities](https://www.openriskacademy.com/course/view.php?id=73)
* [Crash Course on Input-Output Model Mathematics](https://www.openriskacademy.com/course/view.php?id=70)
* [Input-Output Models as Graph Networks](https://www.openriskacademy.com/course/view.php?id=51)


The Open Risk Manual [category EEIO](https://www.openriskmanual.org/wiki/Category:EEIO) documents a large number of related concepts. 

## Computational Setup

This flow is assuming a Linux desktop but should work with small modifications on macOS / Windows

* Clone the course directory from GitHub
* -> git clone https://github.com/Open-Risk-Academy/Academy-Course-SFI32064.git
* Enter the project directory and create a virtual environment and install the required packages. Besides Pymrio we need pandas, numpy and matplotlib
* -> uv pip install -r requirements.txt
* Run scripts as usual
* -> python3 step1.py

## Get Further Help

* Within the [Open Risk Academy](https://www.openriskacademy.com/)
* You can also discuss the course at the [Open Risk Commons](https://www.openriskcommons.org/t/academy-course-introduction-to-input-output-models-using-python/96)


