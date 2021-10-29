CREATE TABLE IF NOT EXISTS "Population_Temp"
(
	"FIPS" integer NOT NULL,
	"Total" integer,
	"Male" integer,
	"Female" integer,
    "18_Years_Plus" integer,
	"65_Years_Plus" integer,
	"One_Race" integer,
	"Two_Plus_Races" integer,
	PRIMARY KEY  ("FIPS")
);

COPY "Population_Temp"
FROM 'C:\Users\simon\Desktop\CSE412Project\FinalData\Population_States.csv'
DELIMITER ','
CSV HEADER
WHERE "FIPS" IS NOT NULL
;

COPY "Population_Temp"
FROM 'C:\Users\simon\Desktop\CSE412Project\FinalData\Population_Counties.csv'
DELIMITER ','
CSV HEADER
WHERE "FIPS" IS NOT NULL
;

CREATE TABLE PUBLIC."Population" AS
SELECT "Population_Temp"."FIPS", "Total", "Male", "Female", "18_Years_Plus",
	"65_Years_Plus", "One_Race", "Two_Plus_Races"
FROM "Population_Temp", "Areas"
WHERE "Population_Temp"."FIPS" = "Areas"."FIPS"
;

ALTER TABLE IF EXISTS public."Population"
	ADD PRIMARY KEY ("FIPS"),
	ADD FOREIGN KEY ("FIPS") REFERENCES "Areas"("FIPS")
	ON DELETE CASCADE
;

DROP TABLE "Population_Temp"
;

