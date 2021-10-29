CREATE TABLE IF NOT EXISTS "Vaccine_TMP"
(
	"Date" character(30) NOT NULL,
	"Vaccine_FIPS" integer,
	"Week" int,
	"Full_Foses_Pct" float,
	"Full_Foses_Number" integer,
	"Full_Foses_age_12_Number" integer,
	"Full_Foses_age_12_Pct" float,
	"Full_Foses_age_18_Number" integer,
	"Full_Foses_age_18_Pct" float,
	"Full_Foses_age_65_Number" integer,
	"Full_Foses_age_65_Pct" float,
	"Half_Foses_Number" integer,
	"Half_Foses_Pct" float,
	"Half_Foses_age_12_Number" integer,
	"Half_Foses_age_12_Pct" float,
	"Half_Foses_age_18_Number" integer,
	"Half_Foses_age_18_Pct" float,
	"Half_Foses_age_65_Number" integer,
	"Half_Foses_age_65_Pct" float
	
);


COPY "Vaccine_TMP"
FROM 'C:\Users\simon\Desktop\data\COVID-19_Vaccinations_in_the_United_States_County.csv'
DELIMITER ','
CSV HEADER
WHERE "Vaccine_FIPS" IS NOT NULL
;

CREATE TABLE IF NOT EXISTS "Vaccine_TMP_NO_Duplicated" AS
SELECT DISTINCT*
FROM "Vaccine_TMP";


CREATE TABLE IF NOT EXISTS "Vaccine_Comb" AS
	SELECT "Date", "Vaccine_FIPS", "Week", concat_ws(',', "Full_Foses_Pct", "Full_Foses_Number",
														"Full_Foses_age_12_Number" ,
														"Full_Foses_age_12_Pct" ,
														"Full_Foses_age_18_Number" ,
														"Full_Foses_age_18_Pct" ,
														"Full_Foses_age_65_Number" ,
														"Full_Foses_age_65_Pct" 
													) as "Full_Age_Dist", 
											concat_ws(',', "Half_Foses_Pct", "Half_Foses_Number",
														"Half_Foses_age_12_Number" ,
														"Half_Foses_age_12_Pct" ,
														"Half_Foses_age_18_Number" ,
														"Half_Foses_age_18_Pct" ,
														"Half_Foses_age_65_Number" ,
														"Half_Foses_age_65_Pct" 
													) as "Half_Age_Dist" 
													FROM "Vaccine_TMP_NO_Duplicated";

CREATE TABLE IF NOT EXISTS "Vaccine_Final" AS
	SELECT "Date", "Vaccine_FIPS", "Week", "Full_Age_Dist", "Half_Age_Dist"
	FROM "Vaccine_Comb", "Area"
	WHERE "Vaccine_Comb"."Vaccine_FIPS" = "Area"."FIPS";
												
												







