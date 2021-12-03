import pandas as pd
import psycopg2

hostname = "localhost"

with open('setting.txt') as setting:
    lines = setting.readlines()

dbname = lines[0].replace(" ", "").replace("\n", "").split('=')[1]
username = lines[1].replace(" ", "").replace("\n", "").split('=')[1]
pwd = lines[2].replace(" ", "").replace("\n", "").split('=')[1]
port_id = lines[3].replace(" ", "").replace("\n", "").split('=')[1]

try:
    # reading files as csv file
    AreaData = pd.read_csv('./data/Area.csv')
    StateData = pd.read_csv('./data/State.csv')
    CountyData = pd.read_csv('./data/County.csv')
    CovidData = pd.read_csv('./data/Covid_Cases.csv')
    PopData = pd.read_csv('./data/population.csv')
    StateVaccData = pd.read_csv('./data/State_Vacc_Dist.csv')
    VaccData = pd.read_csv('./data/Vaccinations.csv')

    # store datasets as dataframe
    dfArea = pd.DataFrame(AreaData)
    dfState = pd.DataFrame(StateData)
    dfCounty = pd.DataFrame(CountyData)
    dfCovid = pd.DataFrame(CovidData)
    dfPop = pd.DataFrame(PopData)
    dfStateVacc = pd.DataFrame(StateVaccData)
    dfVacc = pd.DataFrame(VaccData)

    # connect to local database
    con = psycopg2.connect(
        host=hostname,
        database=dbname,
        user=username,
        password=pwd,
        port=port_id)

    # create a database cursor
    cur = con.cursor()

    print("Create Area, State, County... tables")

    # CREATE table command in a list
    commands = (
        ''' CREATE TABLE IF NOT EXISTS "Area"
            (
                "FIPS" integer NOT NULL,
                "Area_Name" character(50),
                PRIMARY KEY ("FIPS")
            )
        '''
        ,
        ''' CREATE TABLE IF NOT EXISTS "State"
            (
                "FIPS" integer,
                "Postal_Abbr" character(10) NOT NULL,
                PRIMARY KEY ("FIPS"),
                FOREIGN KEY ("FIPS") REFERENCES "Area"("FIPS")
                ON DELETE CASCADE
            )
        '''
        ,
        ''' CREATE TABLE IF NOT EXISTS "County"
            (
                "FIPS" integer,
                PRIMARY KEY  ("FIPS"),
                FOREIGN KEY ("FIPS") REFERENCES "Area"("FIPS")
                ON DELETE CASCADE
            )
        '''
        ,
        ''' CREATE TABLE IF NOT EXISTS "Covid_Cases"
            (
                "Date" date NOT NULL,
                "FIPS" integer,
                "Total_Cases" integer,
                "Total_Deaths" integer,
                PRIMARY KEY  ("FIPS", "Date"),
                FOREIGN KEY ("FIPS") REFERENCES "Area"("FIPS")
                ON DELETE CASCADE
            )
        '''
        ,
        ''' CREATE TABLE IF NOT EXISTS "Population"
            (
                "FIPS" integer NOT NULL,
                "Total" integer,
                "Male" integer,
                "Female" integer,
                "Eighteen_Years_Plus" integer,
                "SixFive_Years_Plus" integer,
                "One_Race" integer,
                "Two_Plus_Races" integer,
                PRIMARY KEY ("FIPS"),
                FOREIGN KEY ("FIPS") REFERENCES "Area" ("FIPS")
            )
        '''
        ,
        ''' CREATE TABLE IF NOT EXISTS "Vaccinations"
            (
                "Date" date NOT NULL,
	            "FIPS" integer NOT NULL,
	            "Week" integer,
	            "Complete" character(50),
	            "Complete_18Plus" character(50),
	            "Complete_65Plus" character(50),
	            "Dose1_Recip" character(50),
	            "Dose1_18Plus" character(50),
	            "Dose1_65Plus" character(50),
	            PRIMARY KEY ("FIPS", "Date"),
	            FOREIGN KEY ("FIPS") REFERENCES "Area"("FIPS")
	            ON DELETE CASCADE
            )
        '''
        ,
        ''' CREATE TABLE IF NOT EXISTS "State_Vacc_Dist"
            (
                "Date" date NOT NULL,
	            "FIPS" integer NOT NULL,
	            "Week" integer,
	            "Dist_Total" integer,
	            "Dist_Janssen" integer,
	            "Dist_Moderna" integer,
	            "Dist_Pfizer" integer,
                "Given_Total" integer,
                "Given_Janssen" integer,
                "Given_Moderna" integer,
                "Given_Pfizer" integer,
                PRIMARY KEY ("FIPS", "Date"),
	            FOREIGN KEY ("FIPS") REFERENCES "Area"("FIPS")
	            ON DELETE CASCADE
            )
        '''
    )

    # execute all command in the list
    for command in commands:
        cur.execute(command)


    # insert data to each table
    print("inserting Area data")
    for row in dfArea.itertuples():
        cur.execute('''
                    INSERT INTO "Area" ("FIPS", "Area_Name")
                    VALUES (%s,%s)
                    ''',
                    (row.FIPS, row.Area_Name)
                    )

    print("inserting State data")
    for row in dfState.itertuples():
        cur.execute('''
                    INSERT INTO "State" ("FIPS", "Postal_Abbr")
                    VALUES (%s,%s)
                    ''',
                    (row.FIPS, row.Postal_Abbr)
                    )

    print("inserting County data")
    for row in dfCounty.itertuples():
        cur.execute('''
                    INSERT INTO "County" ("FIPS")
                    VALUES (%s)
                    ''',
                    (row.FIPS,)
                    )

    print("inserting Covid data")
    for row in dfCovid.itertuples():
        cur.execute('''
                    INSERT INTO "Covid_Cases" ("Date", "FIPS", "Total_Cases", "Total_Deaths")
                    VALUES (%s, %s, %s, %s)
                    ''',
                    (row.Date, row.FIPS, row.Total_Cases, row.Total_Deaths)
                    )

    print("inserting Population data")
    for row in dfPop.itertuples():
        cur.execute('''
                    INSERT INTO "Population" ("FIPS", "Total", "Male", "Female", "Eighteen_Years_Plus", 
                                                "SixFive_Years_Plus", "One_Race", "Two_Plus_Races")
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ''',
                    (row.FIPS, row.Total, row.Male, row.Female, row.Eighteen_Years_Plus, row.SixFive_Years_Plus,
                     row.One_Race, row.Two_Plus_Races)
                    )

    print("inserting Vaccination data")
    for row in dfVacc.itertuples():
        cur.execute('''
                    INSERT INTO "Vaccinations" ("Date", "FIPS", "Week", "Complete", "Complete_18Plus",
                                                "Complete_65Plus", "Dose1_Recip", "Dose1_18Plus", "Dose1_65Plus")
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ''',
                    (row.Date, row.FIPS, row.Week, row.Complete, row.Complete_18Plus, row.Complete_65Plus,
                     row.Dose1_Recip, row.Dose1_18Plus, row.Dose1_65Plus)
                    )

    # change data type from character back to numeric
    print("changing data type back as bigint")
    cur.execute('''
                    ALTER TABLE "Vaccinations"
                    ALTER COLUMN "Complete" TYPE numeric USING ("Complete"::numeric),
                    ALTER COLUMN "Complete_18Plus" TYPE numeric USING ("Complete_18Plus"::numeric),
                    ALTER COLUMN "Complete_65Plus" TYPE numeric USING ("Complete_65Plus"::numeric),
                    ALTER COLUMN "Dose1_Recip" TYPE numeric USING ("Dose1_Recip"::numeric),
                    ALTER COLUMN "Dose1_18Plus" TYPE numeric USING ("Dose1_18Plus"::numeric),
                    ALTER COLUMN "Dose1_65Plus" TYPE numeric USING ("Dose1_65Plus"::numeric)
                ''')


    print("inserting State_Vacc_Dist data")
    for row in dfStateVacc.itertuples():
        cur.execute('''
                    INSERT INTO "State_Vacc_Dist" ("Date", "FIPS", "Week", "Dist_Total", "Dist_Janssen", "Dist_Moderna", 
                                                "Dist_Pfizer", "Given_Total", "Given_Janssen","Given_Moderna", 
                                                "Given_Pfizer")
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ''',
                    (row.Date, row.FIPS, row.Week, row.Dist_Total, row.Dist_Janssen, row.Dist_Moderna,
                     row.Dist_Pfizer, row.Given_Total, row.Given_Janssen, row.Given_Moderna, row.Given_Pfizer)
                    )


    con.commit()


except (Exception, psycopg2.Error) as error:
    print("Failed", error)

finally:
    if(con):
      cur.close()
      con.close()
      print("Have finished, PostgreSQL connection is closed.")
