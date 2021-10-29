CREATE TABLE IF NOT EXISTS public."Areas"
(
    "FIPS" integer NOT NULL,
    "Area_Name" character(50),
    CONSTRAINT "Areas_pkey" PRIMARY KEY ("FIPS")
);

CREATE TABLE IF NOT EXISTS public."States"
(
	"FIPS" integer,
    "Postal_Abbr" character(10) NOT NULL,
	PRIMARY KEY  ("FIPS"),
	FOREIGN KEY ("FIPS") REFERENCES "Areas"("FIPS")
	ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS public."Counties"
(
	"FIPS" integer,
	PRIMARY KEY  ("FIPS"),
	FOREIGN KEY ("FIPS") REFERENCES "Areas"("FIPS")
	ON DELETE CASCADE
);


COPY "Areas"
FROM 'C:\Users\simon\Desktop\CSE412Project\FinalData\Areas_Fips_Counties.csv'
DELIMITER ','
CSV HEADER;

COPY "Areas"
FROM 'C:\Users\simon\Desktop\CSE412Project\FinalData\Areas_Fips_States.csv'
DELIMITER ','
CSV HEADER;

COPY "States"
FROM 'C:\Users\simon\Desktop\CSE412Project\FinalData\States_Fips_States.csv'
DELIMITER ','
CSV HEADER;

COPY "Counties"
FROM 'C:\Users\simon\Desktop\CSE412Project\FinalData\Counties_Fips_Counties.csv'
DELIMITER ','
CSV HEADER;