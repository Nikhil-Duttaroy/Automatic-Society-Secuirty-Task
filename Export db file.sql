--
-- File generated with SQLiteStudio v3.3.0 on Fri Mar 12 10:00:25 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Irregular
CREATE TABLE Irregular (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Name STRING NOT NULL, Phn TEXT, Visit TEXT, Purpose STRING, EntryTime DATETIME, Temperature DOUBLE);
INSERT INTO Irregular (ID, Name, Phn, Visit, Purpose, EntryTime, Temperature) VALUES (1, 'test', '123433', 'Visit', 'meet', '2021-03-04 17:25:26', 101.0);
INSERT INTO Irregular (ID, Name, Phn, Visit, Purpose, EntryTime, Temperature) VALUES (2, 'Test', '99672522152', 'Home', 'Heelo', '2021-03-04 17:26:38', 96.0);
INSERT INTO Irregular (ID, Name, Phn, Visit, Purpose, EntryTime, Temperature) VALUES (3, 'Himani', '9967252236', 'Home', 'Vissit', '2021-03-04 17:27:24', 98.0);

-- Table: Users
CREATE TABLE Users (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Name STRING NOT NULL, Flat STRING, Time TEXT DEFAULT NULL, Type STRING, "Temp" DOUBLE);
INSERT INTO Users (ID, Name, Flat, Time, Type, "Temp") VALUES (2, 'Nikhil', 'A-101', '2021-03-06 22:37:59', 'Resident', 98.0);
INSERT INTO Users (ID, Name, Flat, Time, Type, "Temp") VALUES (3, 'Vaishnavi', 'sdfsdf', '2021-03-06 11:58:43', 'Resident', 102.0);
INSERT INTO Users (ID, Name, Flat, Time, Type, "Temp") VALUES (4, 'Ishika', 'D-101', NULL, 'Resident', 96.0);
INSERT INTO Users (ID, Name, Flat, Time, Type, "Temp") VALUES (5, 'Himani', 'B-101', NULL, 'Resident', 99.0);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
