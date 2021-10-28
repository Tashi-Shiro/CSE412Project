CREATE TABLE IF NOT EXISTS "County_Cases"
(
	"Date" character(30) NOT NULL,
	"Name" character(50) NOT NULL,
	"State" character(50) NOT NULL,
	"Cases_FIPS" integer,
	"Total_Cases" integer,
    "Total_Death" integer,
	PRIMARY KEY  ("Cases_FIPS", "Date")
);

COPY "County_Cases"
FROM 'C:\Users\simon\Desktop\data\us-counties.csv'
DELIMITER ','
CSV HEADER
WHERE "Cases_FIPS" IS NOT NULL
;

CREATE TABLE IF NOT EXISTS "State_Cases"
(
	"Date" character(30) NOT NULL,
	"Name" character(50) NOT NULL,
	"Cases_FIPS" integer,
	"Total_Cases" integer,
    "Total_Death" integer,
	PRIMARY KEY  ("Cases_FIPS", "Date")
);

COPY "State_Cases"
FROM 'C:\Users\simon\Desktop\data\us-states.csv'
DELIMITER ','
CSV HEADER
WHERE "Cases_FIPS" IS NOT NULL
;

CREATE TABLE PUBLIC."Cases_Temp" AS
SELECT "Date", "Cases_FIPS", "Total_Cases", "Total_Death"  
FROM "State_Cases"
UNION
SELECT "Date", "Cases_FIPS", "Total_Cases", "Total_Death"  
FROM "County_Cases"
;

CREATE TABLE PUBLIC."Covid_Case" AS
SELECT "Date", "Cases_FIPS", "Total_Cases", "Total_Death" 
FROM "Cases_Temp", "Area"
WHERE "Cases_Temp"."Cases_FIPS" = "Area"."FIPS"
;

DROP TABLE "County_Cases", "State_Cases", "Cases_Temp"
;

ALTER TABLE IF EXISTS public."Covid_Case"
	ADD CONSTRAINT Covid_Case_Date_pkey PRIMARY KEY ("Cases_FIPS", "Date"),
	ADD FOREIGN KEY ("Cases_FIPS") REFERENCES "Area"("FIPS")
	ON DELETE CASCADE
;
	


