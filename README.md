                                                                   City Bike
This is a small project processing data of bike rides and making up statistics on data shared by Capital Bikeshare https://ride.capitalbikeshare.com/system-data - metro DC's bikeshare service, with 5,000 bikes and 600+ stations across 7 jurisdictions: Washington, DC.; Arlington, VA; Alexandria, VA; Montgomery, MD; Prince George's County, MD; Fairfax County, VA; and the City of Falls Church, VA for quick trips around town.

HOW IT WORKS?
-------------------------------
1. The console applicaton gets some csv file with bike trips statistics for a quarter, year or month,
2. then it parsers and processes it,
3. afterwords 3 output csv files with folowing information below are generated. 

![App_Scheme drawio](https://user-images.githubusercontent.com/63054459/162261138-1cdafb3b-7811-455c-9df5-09880d876e48.png)


WHAT OUTPUT DATA I WILL GET?
-------------------------------
You are to get:

*general-stats.csv* file with general statistics for a particular period:
- total trips amount
- duration of the longest ride
- total of unprocessed data in input file

*usage-stats.csv* provides you with some information about the total rides amount by month of the original data file.

*bike-stats.csv* contains information about the number of trips and the time of use of each bike by decrease, based on the original data file.

WHICH INPUT FILES REQUIRED?
------------------------------
Feel free to download data shared by capital bikeshare https://ride.capitalbikeshare.com/system-data. Each quarter, they publish downloadable files of Capital Bikeshare trip data. The data includes:
- Duration – Duration of trip
- Start Date – Includes start date and time
- End Date – Includes end date and time
- Start Station – Includes starting station name and number
- End Station – Includes ending station name and number
- Bike Number – Includes ID number of bike used for the trip
- Member Type – Indicates whether user was a "registered" member (Annual Member, 30-Day Member or Day Key Member) or a "casual" rider (Single Trip, 24-Hour Pass, 3-Day Pass or 5-Day Pass)

*This data is provided according to the Capital Bikeshare Data License Agreement.*

HOW TO LAUNCH THE APP?
--------------------------------
You chould clone the project and launch it from main.py file.

HISTORY OF THE APP
--------------------------------
I built this app as my firststyding project in data engineering for my internship at iTechArt Group.

                           You are very welcome to use it or share your recomendations and comments for me on this project;)
GRATITUDES
--------------------------------
Hat tip to anyone whose code was used and analysed before building the app. And great THANK YOU to my patient mentor and friends!
