# Election Scraper

Third project for Engeto Python Academy.

### Author

	•	Name: Martin Buchal
	•	Email: buchalM@seznam.cz
	•	Discord: buchy#6031

## Project Overview

This project is designed to extract and process data from the 2017 Czech parliamentary elections for specific regions. The main source of data is the official election page: volby.cz.

Users can input a region URL to download its election data and save the results to a CSV file for further analysis.

## Installation

To ensure compatibility, use the requirements.txt file to install the necessary libraries. It’s recommended to work in a virtual environment for better project isolation.

### Steps to Install:

	1.	Create and activate a virtual environment.
	2.	Install dependencies with:

    pip install -r requirements.txt

## How to Run

The script election_scraper.py can be executed from the command line. It requires two mandatory arguments:
	•	A URL for the region’s election data.
	•	A file name for the CSV output.

### Syntax:

python election_scraper.py "URL" "output_file.csv"

## Example Usage

### Input Example:

	1.	URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4204
	2.	Output File: results_louny.csv

### Command:

python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4204" "results_louny.csv"

### Progress Display:
DOWNLOADING DATA FROM URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4204
SAVING DATA TO FILE: results_louny.csv
TERMINATING election_scraper.py, ALL DATA ARE SAVED.

### Sample Output:
Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,...
541346,Blatno,439,269,267,24,0,0,26,0,14,18,2,1,4,1,39,0,1,109,0,0,1,27
541401,Blšany,802,405,404,20,0,0,29,0,23,19,1,0,2,1,58,1,1,205,0,1,0,43