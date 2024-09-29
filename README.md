# Docker-PostgreSQL

![LOGO](assets/images/Logo01.png)

This repository contains a docker-compose file for running PostgreSQL on your localhost.
With this project a python script is shipped that installs the popular Northind Database
for demo/learning purposes.

## TABLE OF CONTENTS
<ol>
<li><a href="#tested-with">Tested With</a></li>
<li><a href="#setup">Setup</a></li>
<li><a href="#python">Python</a></li>
<li><a href="#database">Database</a></li>
<li><a href="#stop">Stop</a></li>
<li><a href="#contributing">Contributing</a></li>
</ol>

## TESTED WITH
The project was tested with the following software components...

Name           | Reference    
-------------- | --------------- 
Windows        | >= 11
Python         | >= 3.11.3
Docker Desktop | >= 4.12.0
WSL            | >= 2
Ubuntu         | >= 20.04.6 LTS (Focal Fossa)
docker         | 20.10.17
docker-compose | v2.10.2

## SETUP
1. Open a WSL Terminal Window

2. Clone the Docker-PostgreSQL repo

        $ cd ~
        $ git clone https://github.com/schneidermatic/Docker-PostgreSQL.git

3. Switch into the 'Docker-PostgreSQL/wsl2' folder

        $ cd ~/Docker-PostgreSQL/wsl2

4. Start the container as daemon process
   
        $ docker-compose up -d

5. Sign into the pgAdmin4 web console

        http://localhost:5050

        Email Address / Username: pgadmin@pgadmin.com
        Password: changeme

## PYTHON
1. Install Python Libraries

        $ cd ~/Docker-PostgreSQL/scripts
        $ python -m venv venv
        $ . ./venv/bin/activate
        $ pip install -r ./requirements.txt

## DATABASE
1. Run the dbtool.py script that installs the Northwind Database.

        $ ./dbtool.py

        Downloaded ../data/northwind_ddl.sql from https://raw.githubusercontent.com/yugabyte/yugabyte-db/refs/heads/master/sample/northwind_ddl.sql
        Downloaded ../data/northwind_data.sql from https://raw.githubusercontent.com/yugabyte/yugabyte-db/refs/heads/master/sample/northwind_data.sql
        Executing SQL commands from ../data/northwind_ddl.sql
        Executing SQL commands from ../data/northwind_data.sql

## STOP
1. Stop and remove all docker images
   
        $ docker-compose down --rmi all

## CONTRIBUTING
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request