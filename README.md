# CSE412 Covid 19 Project
Our project show information of COVID-19 in the USA.

# Setup & Installation

## Dependencies:
1. PostgreSQL (v13.5)
2. Python (v3.8)
3. Pycharm IDE
   - Psychopg2
   - pandas
   - plotly
4. Git Bash

To install any of python's packages, input `pip install packageName` in `Pycharm`'s terminal.

## Installation

### First: Clone the repository
Run this code or use anyway to clone the repository to local:

    $ git clone https://github.com/Tashi-Shiro/CSE412Project

### Second: Create a new database
Set up a new database with any name port, and password in local. Example:

    $ export PGPORT=5432    # set up port
    $ export PGHOST=/tmp    # set the directory for the socket files
    $ initdb $HOME/db412    # initialize databse
    $ pg_ctl -D $HOME/db412 -o '-k /tmp' start    # start the databse
    $ createdb $USER  # create a user for the databse

### Third: Inserting data
Before inserting data, update `setting.txt` in the project's main path. To do that,
open the `setting.txt` and change following information.

    dbname = <input databse name>
    username = <input user name>
    password = <your databse password>
    port= <your port ID>

After updated data, use the `Pycharm IDE` to run `datainsert.py`.

#### Important: because we have large datasets, it may take couple minutes to insert all data to database.

### Finally: Run Application
After inserting data, use the `Pycharm IDE` to run `GUI.py`.

# Sources Information:

    FIPS Code: https://github.com/kjhealy/fips-codes
  
    COVID19 Data: https://github.com/nytimes/covid-19-data
    
    Population: https://data.census.gov/cedsci/table?q=%20age%20%20%20%20%20%20%20%20%20%20%20&g=0100000US%240400000&tid=ACSDP1Y2019.DP05&moe=false&hidePreview=true
    
    County's Vaccinations: https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh
    
    State's Vaccinations: https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-Jurisdi/unsk-b7fc
  
    Download CSV from GitHub: https://downgit.github.io/#/home
