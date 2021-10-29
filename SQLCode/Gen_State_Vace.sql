CREATE TABLE IF NOT EXISTS "Jurisdiction_Temp"
(
	"Date" character(50) NOT NULL,
	"week" integer,
	"Location" character(10) NOT NULL,
	"Distributed" integer,
    "Distributed_Janssen" integer,
	"Distributed_Moderna" integer,
	"Distributed_Pfizer" integer,
	"Administered" integer,
	"Administered_Janssen" integer,
	"Administered_Moderna" integer,
	"Administered_Pfizer" integer,
	"Administered_Dose1_Recip" integer,
	"Administered_Dose1_Recip_18Plus" integer,
	"Administered_Dose1_Recip_65Plus" integer,
	"Series_Complete_Yes" integer,
	"Series_Complete_18Plus" integer,
	"Series_Complete_65Plus" integer
);

COPY "Jurisdiction_Temp"
FROM 'C:\Users\simon\Desktop\CSE412Project\COVID-19_Vaccinations_in_the_United_States_Jurisdiction.csv'
DELIMITER ','
CSV HEADER
;

CREATE TABLE PUBLIC."Jurisdiction_Final" AS
SELECT *
FROM "Jurisdiction_Temp", "States"
WHERE "Jurisdiction_Temp"."Location" = "States"."Postal_Abbr"
;

DROP TABLE "Jurisdiction_Temp"
;




