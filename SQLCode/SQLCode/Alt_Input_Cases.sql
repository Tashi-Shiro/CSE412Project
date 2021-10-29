CREATE TABLE IF NOT EXISTS "Covid_Cases"
(
	"Date" character(30) NOT NULL,
	"Cases_FIPS" integer,
	"Total_Cases" integer,
    "Total_Death" integer,
	PRIMARY KEY  ("Cases_FIPS", "Date"),
 	FOREIGN KEY  ("Cases_FIPS") REFERENCES "Area"("FIPS") 
	ON DELETE CASCADE
);

COPY "Covid_Cases"
FROM 'C:\Users\simon\Desktop\data\FinalData\covid_Cases.csv'
DELIMITER ','
CSV HEADER
;
