# Introduction

This is an assignment for LeadIQ's Senior Software Engineer position.
We estimate that it will take you 2 hours to complete.

In place of this assignment, you can also submit a link to a public GitHub repository that contains a project you've worked on and are proud of.
Please contact us if you choose this option.

We will evaluate your submission based on the following criteria:
- How you structure your code and how you solve problems. Pay attention to readability, maintainability, and making it testable.
We do not believe in leetcode-style questions as they do not reflect real-world problems, and the time constraint often adds unnecessary stress. 
- Intermediate knowledge of typesafety is required. Our repo is typechecked, and you will need to be able guide more junior engineers to write code in a typesafe way.
- API design. We use graphql, and you will need to be able to design a graphql schema that is easy to use and maintain in the future.

# Assignment

The task is to review the code in this repository and suggest changes to it.
The intention is to emulate a real-world scenario where you are asked to review code written by a junior engineer.

## An introduction to scribe
LeadIQ has a tool called scribe. It is a tool that helps sales people write emails to their prospects.

The flow of a sales person on scribe is as follows:
1. The user keys in the lead's email. The frontend then displays the lead's information from the backend's response.
![lead_information.png](docs%2Fimages%2Flead_information.png)
2. The user then selects the insight that the user wants to write about. The frontend displays the insights available. 
In this exercise, we have two insights: `company_description` and `news`.
4. The user then clicks "Get Message" to generate a message using the selected insights.


## Requirements of "Get Message"
As part of our machine learning pipeline, we need to store all the lead information, insights that the user has in view.
E.g. even if the user does not select the `company_description` insight, we still need to store the information of the `company_description` insight served to the user.


## The code
To start, clone this repository
Create a virtual environment on python 3.9 and install the requirements.

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the flask server
```
python main.py
```

Run pytest tests
```
pytest
```

Run mypy typechecking
```
dmypy run
```

