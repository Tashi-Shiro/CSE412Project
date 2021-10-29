ALTER DATABASE "CSE412Project" SET datestyle TO "ISO, MDY";

CREATE TABLE IF NOT EXISTS "State_Vaccine_Dist"
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
	PRIMARY KEY ("FIPS", "Date")
);

COPY "State_Vaccine_Dist"
FROM 'C:\Users\simon\Desktop\CSE412Project\FinalData\Vaccine_Dist.csv'
DELIMITER ','
CSV HEADER
WHERE "FIPS" IS NOT NULL
	AND "Date" IS NOT NULL
;