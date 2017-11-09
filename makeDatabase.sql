----------------------------------------------
-- After Installing PostgreSQL in your system
----------------------------------------------
-- sudo su - postgres 
-- createdb DB_BINDI 
-- psql DB_BINDI
-- \i <path_to_makeDatabase.sql>
----------------------------------------
--  DELETE the existing tables (if any)
----------------------------------------
DROP TABLE IF EXISTS TAB_PROGRAMS CASCADE;
DROP TABLE IF EXISTS TAB_COURSES CASCADE;
DROP TABLE IF EXISTS TAB_COLLEGES CASCADE;
DROP TABLE IF EXISTS TAB_SPEC_MAJOR CASCADE;
DROP TABLE IF EXISTS TAB_COURSE_OFFERING CASCADE;
DROP TABLE IF EXISTS TAB_COURSE_SPEC_MAJOR CASCADE;
------------------------------------
-- CREATE new tables (if none exist)
------------------------------------
CREATE TABLE IF NOT EXISTS TAB_COLLEGES (
	COLLEGE_ID SERIAL PRIMARY KEY,
	COLLEGE_NAME varchar(500) NOT NULL,
	COLLEGE_SHORT varchar(10) NOT NULL,
	UNIQUE (COLLEGE_NAME)
	);

CREATE TABLE IF NOT EXISTS TAB_PROGRAMS (
	PROG_CODE varchar(10) NOT NULL,
	PROG_TITLE varchar(100) NOT NULL,
	PROG_LENGTH numeric(2,1),
	PROG_CAREER int,
	PROG_DELIVERY int,
	PROG_MIN_UNITS int NOT NULL,
	PROG_CONVENOR varchar(100) NOT NULL,
	PROG_CONVENOR_EMAIL varchar(100) NOT NULL,
	PRIMARY KEY (PROG_CODE),
	UNIQUE (PROG_CODE, PROG_TITLE)
	); 

CREATE TABLE IF NOT EXISTS TAB_SPEC_MAJOR (
	SPEC_PROG_CODE varchar(10) NOT NULL references TAB_PROGRAMS(PROG_CODE),
	SPEC_MAJOR_ID SERIAL PRIMARY KEY,
	SPEC_MAJOR_TYPE int NOT NULL,
	SPEC_MAJOR_TITLE varchar(200) NOT NULL,
	SPEC_MIN_UNITS int NOT NULL
	);

CREATE TABLE IF NOT EXISTS TAB_COURSES (
	COURSE_CODE varchar(8) NOT NULL PRIMARY KEY,
	COURSE_TITLE varchar(100) NOT NULL,
	COURSE_LENGTH int NOT NULL,
	COURSE_UNITS int NOT NULL,
	COURSE_COLLEGE int NOT NULL references TAB_COLLEGES(COLLEGE_ID),
	COURSE_MAJOR_FOR int  references TAB_SPEC_MAJOR(SPEC_MAJOR_ID),
	COURSE_CONVENOR varchar(100) NOT NULL,
	COURSE_CONVENOR_EMAIL varchar(100) NOT NULL,
	UNIQUE (COURSE_CODE, COURSE_TITLE)
	); 

CREATE TABLE IF NOT EXISTS TAB_COURSE_OFFERING (
	COF_ID SERIAL PRIMARY KEY,
	COURSE_CODE varchar(8) NOT NULL references TAB_COURSES(COURSE_CODE),
	COURSE_OFFERED_IN date NOT NULL,
	UNIQUE (COURSE_CODE, COURSE_OFFERED_IN) 
	);
	
CREATE TABLE IF NOT EXISTS TAB_COURSE_SPEC_MAJOR (
	CSM_ID SERIAL PRIMARY KEY,
	CSM_COURSE_CODE varchar(8) NOT NULL references TAB_COURSES(COURSE_CODE),
	CSM_SPEC_MAJOR_ID int NOT NULL references TAB_SPEC_MAJOR(SPEC_MAJOR_ID),
	UNIQUE (CSM_COURSE_CODE, CSM_SPEC_MAJOR_ID) 
	);	