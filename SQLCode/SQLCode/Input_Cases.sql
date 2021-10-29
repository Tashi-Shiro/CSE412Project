ALTER DATABASE "CSE412Project" SET datestyle TO "ISO, MDY";

CREATE TABLE IF NOT EXISTS "County_Cases"
(
	"Date" date NOT NULL,
	"Name" character(50) NOT NULL,
	"State" character(50) NOT NULL,
	"FIPS" integer,
	"Total_Cases" integer,
    "Total_Deaths" integer,
	PRIMARY KEY  ("FIPS", "Date")
);

COPY "County_Cases"
FROM 'C:\Users\simon\Desktop\CSE412Project\FinalData\Cases_Covid19_Counties.csv'
DELIMITER ','
CSV HEADER
WHERE "FIPS" IS NOT NULL
;

CREATE TABLE IF NOT EXISTS "State_Cases"
(
	"Date" date NOT NULL,
	"Name" character(50) NOT NULL,
	"FIPS" integer,
	"Total_Cases" integer,
    "Total_Deaths" integer,
	PRIMARY KEY  ("FIPS", "Date")
);

COPY "State_Cases"
FROM 'C:\Users\simon\Desktop\CSE412Project\FinalData\Cases_Covid19_States.csv'
DELIMITER ','
CSV HEADER
WHERE "FIPS" IS NOT NULL
;

CREATE TABLE PUBLIC."Cases_Temp" AS
SELECT "Date", "FIPS", "Total_Cases", "Total_Deaths"  
FROM "State_Cases"
UNION
SELECT "Date", "FIPS", "Total_Cases", "Total_Deaths"  
FROM "County_Cases"
;

CREATE TABLE PUBLIC."Covid_Cases" AS
SELECT "Date", "Cases_Temp"."FIPS", "Total_Cases", "Total_Deaths" 
FROM "Cases_Temp", "Areas"
WHERE "Cases_Temp"."FIPS" = "Areas"."FIPS"
;

DROP TABLE "County_Cases", "State_Cases", "Cases_Temp"
;

ALTER TABLE IF EXISTS public."Covid_Cases"
	ADD CONSTRAINT Covid_Case_Date_pkey PRIMARY KEY ("FIPS", "Date"),
	ADD FOREIGN KEY ("FIPS") REFERENCES "Areas"("FIPS")
	ON DELETE CASCADE
;
	


