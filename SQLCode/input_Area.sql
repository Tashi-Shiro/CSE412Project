CREATE TABLE IF NOT EXISTS public."Area"
(
    "FIPS" integer NOT NULL,
    "Area_Name" character(50) COLLATE pg_catalog."default",
    CONSTRAINT "Area_pkey" PRIMARY KEY ("FIPS")
);

CREATE TABLE IF NOT EXISTS public."State"
(
	"State_FIPS" integer,
    "Postal_Abbr" character(10) NOT NULL,
	FOREIGN KEY ("State_FIPS") REFERENCES "Area"("FIPS")
	ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS public."County"
(
	"County_FIPS" integer,
	FOREIGN KEY ("County_FIPS") REFERENCES "Area"("FIPS")
	ON DELETE CASCADE
);

COPY "Area"
FROM 'C:\Users\simon\Desktop\data\FinalData\county_fips_Area.csv'
DELIMITER ','
CSV HEADER;

COPY "Area"
FROM 'C:\Users\simon\Desktop\data\FinalData\state_fips_Area.csv'
DELIMITER ','
CSV HEADER;

COPY "State"
FROM 'C:\Users\simon\Desktop\data\FinalData\state_fips_State.csv'
DELIMITER ','
CSV HEADER;

COPY "County"
FROM 'C:\Users\simon\Desktop\data\FinalData\county_fips_County.csv'
DELIMITER ','
CSV HEADER;