## Project Overview:

TriSquare is a finance application designed to provide users with comprehensive insights into stock data obtained from an API. The application's core functionality includes displaying stock details, visualizing sector-wise market capitalization, and analyzing fund movement between sectors.

## Installation:

1. Install git https://git-scm.com/downloads
2. Install Postgresql set username: Postgres, Password: Kenra123
3. Create Database named pulse.
4. Clone the repository to your local machine using `git clone https://github.com/kenrasoftorg/trisquare.git'
5. Open the cloned folder trisquare/src/pulse/scripts/pulseschema.sql
6. Run the table creation queries in postgresql under query tool or SQL editor and make sure tables were created
7. Open a terminal in vscode or cmd
8. Navigate to project directory trisquare
9. Type pip install -r requirements.txt
10. The above command installs all the requirements and denpendencies to run the project if faced errors for few packages continue to next step
11. run trisquare/src/main.py
12. If paced module not found or package not found error - use pip install {packagename} example: pip install numpy and rerun main
13. You will get the data in your database
14. Creating connection in DBeaver - set username: postgres, Password: Kenra123, Database: pulse, Hostname: 127.0.0.1, port: 5432

## Run Docker:

# Windows:

1. Install docker desktop
2. Open C:\Program Files\PostgreSQL\15\data\pg_hba.conf
3. Add this at end of file
   host all all 0.0.0.0/0 md5
4. Open cmd and navigate to cd "C:\Program Files\PostgreSQL\15\bin"
5. pg_ctl reload -D "C:\Program Files\PostgreSQL\15\data\"
6. create images and run:
   cd "D:\trisquare"
   Run these:
   docker build -f Dockerfile.pulse -t pulse .
   docker run -d --name my_pulse pulse

   docker build -f Dockerfile.pangea -t pangea .
   docker run -p 5000:5000 --name my_pangea pangea

   docker build -f Dockerfile.wave -t wave .
   docker run -p 3000:3000 --name my_wave wave

# Mac:

1. Install docker desktop
2. Open /usr/local/pgsql/data/
3. Open file pg_hba.conf
4. Add this line on last row
   host all all 0.0.0.0/0 md5
5. In terminal run this command: pg_ctl -D /usr/local/pgsql/data/ reload #match the path accordingly
6. create images and run:
   cd "D:\trisquare"
   Run these:
   docker build -f Dockerfile.pulse -t pulse .
   docker run -d --name my_pulse pulse

   docker build -f Dockerfile.pangea -t pangea .
   docker run -p 5000:5000 --name my_pangea pangea

   docker build -f Dockerfile.wave -t wave .
   docker run -p 3000:3000 --name my_wave wave
