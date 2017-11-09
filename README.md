# Bindi

Project undertaken by [TechLauncher Professional Services Team](https://gitlab.cecs.anu.edu.au/u6087050/TechLauncher_Professional_Services_Team_2017).

This project's goal is to assist CECS student services by automating processing of their most frequent requests from students.

## Current Status

This is our newest project and was commenced in Aug 2017. Latest developments include:
* [Runnable UI Demo](https://gitlab.cecs.anu.edu.au/u6087050/Bindi)  connected to [CIMS API](https://gitlab.anu.edu.au/CIMS/django-cims)<sup>new!</sup>
* [Data-Model](https://drive.google.com/open?id=0B6Gi8SxOYcVcS3BGLWE0VXUweWc&authuser=0)<sup>new!</sup>
* [DSL Syntax definitions](https://drive.google.com/file/d/0B6Gi8SxOYcVcZFpQcmhjUWRyaWs/view)<sup>new!</sup>
* [Email Templates](https://drive.google.com/file/d/0B5WjPO1bT5lWalMzUlBLNElpLXc/view)<sup>new!</sup>
* [Student Validation Statement](https://gitlab.cecs.anu.edu.au/u6087050/Bindi/issues/18)
* [Problem Statement](https://gitlab.cecs.anu.edu.au/u6087050/Bindi/issues/17)
* [Expected Output Statement](https://gitlab.cecs.anu.edu.au/u6087050/Bindi/issues/16)
* [UX prototyping and validation](https://drive.google.com/drive/u/0/folders/0B5WjPO1bT5lWU0EtR0tnYUw0Qlkhttps://drive.google.com/drive/u/0/folders/0B5WjPO1bT5lWU0EtR0tnYUw0Qlk
  )
* [Detailed UX mockups](https://drive.google.com/file/d/0B6HnLcOVGBVPM1p4RzY5MFU3WXM/view?usp=sharing)
* [Requirements Specifications](https://docs.google.com/document/d/1OgiPKKXuQxGPbqgPvJBHi1qPd4xxDT24y5ZdrksM0I4/edit)
* [Project Context](https://docs.google.com/document/d/15-ZN6KQLDY3AECHjd7IGkOZYF_toA3wbyNNe_D1-w1k/edit)
* [Milestone Identification](https://docs.google.com/document/d/1OUI3Mvpm1Pk_m9U6coXjR60oIJiTWStOwZeiTafKU4A/edit)
* [Risk Assessment](https://docs.google.com/document/d/1VZXmNm6qpzCX0OCdQQnXlh9ju-BAZiEKvf297k-d0NA/edit)
* [Technical Considerations](https://drive.google.com/drive/folders/0B7pDhhYmgcOCS0RIY1RFWkxRTnM)

The decision making is recorded in the [Meeting Minutes](https://drive.google.com/drive/u/0/folders/0B5WjPO1bT5lWaVk3ZXR1Rzc0cTg), [Milestones](https://gitlab.cecs.anu.edu.au/u6087050/Bindi/milestones) and [Issues](https://gitlab.cecs.anu.edu.au/u6087050/Bindi/issues).

## Run Instructions

To run the project on a local machine, you must have Python and Django installed on your computer. To install Django:

You first need to install the `virtualenv` package -
```
pip install virtualenv
```
Then, `cd` into the project folder -
```
cd bindi_web_app/src
```
Create a new virtual environment in the project directory, and activate it -
```
virtualenv djangoEnv
source djangoEnv/bin/activate
```
Now, install Django in this virtual environment -
```
pip install django
```
You can verify the installation by typing `django-admin --version` to get the Django version installed.
Now, to run the project, just run the following command -
```
python manage.py runserver
```
to run the server on your machine. Now, go to the URL `http://127.0.0.1:8000/` to view the Bindi Homepage.
