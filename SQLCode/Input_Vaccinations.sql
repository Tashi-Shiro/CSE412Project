ALTER DATABASE "CSE412Project" SET datestyle TO "ISO, MDY";

CREATE TABLE IF NOT EXISTS "Vaccinations_Temp"
(
	"Date" date NOT NULL,
	"FIPS" integer NOT NULL,
	"Week" integer,
	"Complete" integer,
	"Complete_18Plus" integer,
	"Complete_65Plus" integer,
	"Dose1_Recip" integer,
	"Dose1_18Plus" integer,
	"Dose1_65Plus" integer
);

COPY "Vaccinations_Temp"
FROM 'C:\Users\simon\Desktop\CSE412Project\FinalData\Vaccination_Stats.csv'
DELIMITER ','
CSV HEADER
WHERE "FIPS" IS NOT NULL
;

COPY "Vaccinations_Temp"
FROM 'C:\Users\simon\Desktop\CSE412Project\FinalData\Vaccination_Counties.csv'
DELIMITER ','
CSV HEADER
WHERE "FIPS" IS NOT NULL
;

CREATE TABLE IF NOT EXISTS "Vaccinations_Final" AS
SELECT DISTINCT*
FROM "Vaccinations_Temp";
;

CREATE TABLE PUBLIC."Vaccinations" AS
SELECT "Date", "Vaccinations_Final"."FIPS", "Week", "Complete", "Complete_18Plus", "Complete_65Plus",
	   "Dose1_Recip", "Dose1_18Plus", "Dose1_65Plus"
FROM "Vaccinations_Final", "Areas"
WHERE "Vaccinations_Final"."FIPS" = "Areas"."FIPS"
;

DROP TABLE "Vaccinations_Temp", "Vaccinations_Final"
;

ALTER TABLE IF EXISTS public."Vaccinations"
	ADD CONSTRAINT Vaccinations_Date_pkey PRIMARY KEY ("FIPS", "Date"),
	ADD FOREIGN KEY ("FIPS") REFERENCES "Areas"("FIPS")
	ON DELETE CASCADE
;












