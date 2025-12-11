This is my first attempt to create some sort of survey tool where people can click on some sort of front-end UI to fill out a form that sends the information to a database.


The way I see it, there are three parts to this

1. Front-End
2. Some sort of Backend API
3. Back End Database


# set up environment

As always, let's make sure we have python setup and configured before we do anthing else: 

## you will need python 3.10 - use pyenv perhaps to be able to install various pythons

## virtual environment
```
$ python3 --version
$ python3.10 -m venv .venv-3.10
$ source .venv-3.10/bin/activate
(venv) $
```

## install requirements
`pip install -r requirements.txt`




# Middle API Connection #

I am going to start with the middle part of this for now as it is the most familiar to me. Hopefully getting some traction going will motivate me to to push through and finish this project.

We are going to have to build an API from the ground up here. There are, fortunately, existing python packages that allow for this.

1. Chatgpt says that the best framework to use is fastapi.

0.124.0 is the newest version so I will put that into the requirements.txt file.

2. Now that we have our framework, we still need some sort of server to actually run our project. GPT says that uvicorn is the best bet here. Uvicorn is an Asynchronous Server Gateway Interface (ASGI). Essentially this is a tool for running python applications.

PYPL says that 0.38.0 is the newest uvicorn version so I will throw that in to requirements.txt as well.

3. Next we need a method to actually connect to some sort of SQL server. I have used pymySQL in the past, so I will be going with that here. I am still undecided if I am going to be using a local SQL server or some sort of cloud option, but this will allow for both. I will probably start local and build out into GCP or AWS.

PYPL says that 2.0.44 is the newest version so we are throwing that in requirements.txt as well.

4. Finally, we need an odbc driver to put this all together. The driver is used to actually execute sql commands using PYMYSQL.

PYPL says that 5.3.0 is the newest version so into requirements.txt we go.


# Backend SQL Database #


# 12/8/2025: # 
Since I am using MacOS, there is no local SQL application. I downloaded my sql and am just running it via terminal commands for now. I am going to updated this. I tried using MySQLWorkbench as UI option but it keeps crashing hence terminal commands. I am 100% switching to a cloud option once I get this more flushed out.

To access my local mysql setup, I run the following command in my local terminal:

```
/usr/local/mysql/bin/mysql -u dustinh -p
```

From here, I am able to run standard SQL commands such as 
```
create database survey_database;
```

For now, in my local setup, I created a database called survey_database. I don't think I need to create a table for now because sqlalchemy will do that for me.

# PY Files #

Now it's time to create our first .py file. 

[database file](database.py): this file is a function that will connect to our database.
[models file](models.py): this file defines the table structure that we are are going to be using.
[operations file](crud.py): this file actually performs the operations that we are going to be using (inset, query etc).
[main script](main.py): This defines the api endpoints and puts all of the above pieces together.


To run this locally use:
```
uvicorn main:app --reload
```

you should get the following output back:

```
INFO:     Started server process [15193]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:53976 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:53976 - "GET /openapi.json HTTP/1.1" 200 OK
```
# UI #

After running the code succesfully above, FASTAPI creates a local UI for you. You can go to http://127.0.0.1:8000/docs#/ you your local machine to see your created API. Pretty cool!

Now we have a completed local tool. Now we want both the data base and the UI to become cloud based.


# Cloud Based Database #

So for switching our database, I am going to use Google Cloud Platform due to my familiarity with the platform.

Furthermore, GCP allows for a tier tree. First you need to create a new email to connect the account to. I created the email: surveydatabasetool@gmail.com. 

Now we can use this email to create a free GCP account.

We will also need to the the following packages: google-cloud-sqlconnector and cryptography. I will add them to requirnments.txt

We will need to make a new file for our clouddatabase, you can find that here: [cloud database](clouddatabase.py).

NOTE: I made a .env file and .gitignore to hide my GCP credentials.

1. In the GCP API, you go to Cloud SQL API and click "Enable".

2. Once that is done, then you go to "Cloud SQL", and create an instance. NOTE: You will have to set up a billing acount first.

3. Enable the API, and choose your SQL version. Then create your instance.

4. Next, you have to create a database. I called mine "cloud_survey_database"

5. Next, you create the user. Add the UN and PW to the .env file.

6. We have have to make the connetion. Go to your Cloud SQL instance → Connections

Under Public IP, add your current IP to the allowed networks list

You can find your IP by searching “what is my IP” in Google

7. You can run the [test_connection](test_connection.py) file and create a  test table using [create_tables](create_tables.py) files


Now run

```
uvicorn main:app --reload
```

and execute the post REQUEST 

and the same payload should appear in the cloud database now! 

# Cloud Based Job #

Now that we have figured out how to push our data into a Google Cloud SQL database, it is time to take the next step and host the server in the cloud as well. Wanting to use the same tech stack, I am going to attempt this using a Google Cloud Run job. It should be essentially a script that is stored in GCP and schedueld when I would like as well.

1. In order to do this, we are going to need to create a docker file. A dockerfile is a mini enviornment that basically tells GCP the specific packages and requirnments that are required to perform the task we are doing. 










