[![Build Status](https://github.com/thejaminator/typesafe_parmap/actions/workflows/dev.yml/badge.svg)](https://github.com/thejaminator/be_engineer_interview/actions/workflows/dev.yml)

# Introduction

This is an assignment for LeadIQ's Senior Software Engineer position.
We estimate that it will take you 2 hours to complete. There isn't a timer that will stop you, but we simply are putting this intended time frame out there to be reasonable to our candidates.
After the assignment is completed, we will schedule a one-hour interview to discuss your solution.

In place of this assignment, you can also submit a link to a public GitHub repository that contains a project you've worked on and are proud of.
Please contact us if you choose this option.

We will evaluate your submission based on the following criteria:
- How you structure your code and how you solve problems. Pay attention to readability, maintainability, and making it testable.
We do not believe in leetcode-style questions as they do not reflect real-world problems, and the time constraint often adds unnecessary stress.
- API design. We use graphql, and you will need to be able to design a graphql schema that is easy to use and maintain in the future.
- Intermediate knowledge of typesafety is required. Our repo is typechecked, and you will need to be able to guide more junior engineers to write code in a typesafe way.

# Assignment

The task is to review the code in this repository and suggest changes to it.
The intention is to emulate a real-world scenario where you are asked to review code written by a junior engineer.

## An introduction to scribe
LeadIQ has a tool called scribe. It is a tool that helps sales people write emails to their prospects.

The flow of a sales person on scribe is as follows:
1. The user keys in a person's (lead) email. The frontend then displays the lead's information from the backend's response.
![lead_information.png](docs%2Fimages%2Flead_information.png)
2. The frontend displays information (insights) available regarding the lead. 
In this exercise, we have two insights: `company_description` and `news`.
Currently, the company_description insight will only show one single result  
![company_description_insight.png](docs%2Fimages%2Fcompany_description_insight.png)
The news insight will show multiple results. The user has the option to select categories to filter the results. 
![news_insight.png](docs%2Fimages%2Fnews_insight.png)
4. The user then clicks "Get Message" to generate a message using the one or more selected insights.
![generated_message.png](docs%2Fimages%2Fgenerated_message.png)

## Requirements of the "Get Message" button
As part of our machine learning pipeline, we need to store all the lead information, insights that the user has in view.
E.g. even if the user does not select the `company_description` insight, we still need to store the information of the `company_description` insight served to the user.


## Getting started
To start, clone this repository
Create a virtual environment on python 3.8 / 3.9 and install the requirements.

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the flask server. The server will be running on port 5001.
```
python main.py
```

Send your first query. We recommend using your favorite graphql client, but here is a curl example.
```
curl --request POST \
  --url http://localhost:5001/graphql \
  --header 'Content-Type: application/json' \
  --data '{"query":"query{\n\tleadInformation(email: \"elon@tesla.com\"){\n\t\tfullName\n\t\tlinkedinUrl\n\t\temail\n\t\ttitle\n\t\tlocation\n\t}\n}"}'
```

View graphql schema
```
curl --request POST \
  --url http://localhost:5001/graphql \
  --header 'Content-Type: application/json' \
  --data '{"query":"{\n  __schema {\n    types {\n      name\n      kind\n      fields {\n        name\n        type {\n          name\n          kind\n        }\n      }\n    }\n  }\n}"}'
```

Run pytest tests
```
pytest tests
```

Run mypy typechecking
```
dmypy run
```


## The code
We outline the main files in the codebase below.
- main.py: The flask server that serves the graphql endpoint.
- api/graphql/strawberry_schema.py: The graphql schema. We use [strawberry](https://strawberry.rocks/docs/integrations/pydantic), a python graphql library.
- api/graphql/strawberry_types.py: The graphql types. These are converted from [pydantic](https://pydantic-docs.helpmanual.io) data models.

### The graphql schema
The Junior Engineer has written his initial draft of the graphql schema.

These are the functions corresponding to the user's workflow that the Junior Engineer has written: 
1. The user keys in the lead's email. The frontend then displays the lead's information from the backend's response.
`lead_information`
2. The frontend displays the insights available.
`news` and `company_description`
3. The user then selects one or more insights that the user wants to write about. The user then clicks "Get Message" to generate a message using the selected insights.
`generate_message`

Your task is to review his code and suggest changes to it.

For the purposes of this exercise, assume that we have already chosen our stack of graphql, strawberry, flask and pydantic.
You do not need to suggest changes to the stack. Although if you do have ideas for improvements, we would love to hear them.

There is **no need** to implement an actual database connnection. You can just use a python dictionary to store the data if needed.

Guiding questions
1. Evaluate his API design. Keep in mind that
- we are a machine learning focused company. we will need to save the lead information and insights that the user has in view.
- the existing insights may take in more parameters in the future.
- we will need to add more insights in the future.
- the responsibility of the frontend and backend has to be clear.
2. Code out your suggested changes. If you have issues running the tests, please contact us.
If you find yourself spending more than 2 hours on this, you can just submit your suggested changes and we will discuss it in the interview.
3. Suggest ways to track / monitor / validate that we are saving the lead information and insights that the user has in view.
4. A test has been added in tests/test_get_lead_information.py. What are the pros and cons of the test? How can you improve the test?
5. What are some ways to speed up query response times? 
6. What kind of database(s) would you use to store the data? Why?


## Submission
Please make a fork of this repository.
Make a merge request to your own fork. You can write comments in your merge request to explain your changes.
If you do need to, you may also make simple slides to explain your changes.

Then, make your repository private and add the following users as collaborators:
@thejaminator

The reason we ask you to make your repository private is so that other candidates cannot see your solution.