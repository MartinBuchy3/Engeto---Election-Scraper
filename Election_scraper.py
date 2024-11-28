"""
election_scraper.py: třetí projekt do Engeto Online Python Akademie
author: Martin Buchal
email: buchalM@seznam.cz
discord: buchy#6031
"""

import sys
import csv
import requests
from bs4 import BeautifulSoup


def check_args():
    # checks if we got both URL and filename
    if len(sys.argv) != 3:
        print("Error: Need URL and output file!")
        sys.exit()

    url = sys.argv[1]
    file = sys.argv[2]

    # make sure we're creating a csv file
    if not file.endswith(".csv"):
        print("Error: Must be CSV file!")
        sys.exit()

    return url, file


def get_data_from_url(url):
    # downloads the webpage
    try:
        r = requests.get(url)
        return BeautifulSoup(r.text, 'html.parser')
    except:
        print("Couldn't download the webpage")
        sys.exit()


def get_municipalities(soup):
    # will store all municipalities here
    mun_list = []

    rows = soup.find_all('tr')

    for r in rows:
        td = r.find_all('td')
        if len(td) > 2:  # only rows with data
            try:
                code = td[0].text.strip()
                name = td[1].text.strip()
                # need to add the base url part
                link = f"https://volby.cz/pls/ps2017nss/{td[0].a['href']}" if td[0].a else None

                if link:
                    mun_list.append({
                        'code': code,
                        'name': name,
                        'url': link
                    })
            except:
                continue

    return mun_list


def get_results(soup):
    # get basic info
    reg = soup.find('td', {'headers': 'sa2'}).text.strip()
    env = soup.find('td', {'headers': 'sa3'}).text.strip()
    valid = soup.find('td', {'headers': 'sa6'}).text.strip()

    votes = []

    # votes are in two tables for some reason
    votes1 = soup.find_all('td', {'headers': 't1sa2 t1sb3'})
    votes2 = soup.find_all('td', {'headers': 't2sa2 t2sb3'})

    # add all votes to one list
    for v in votes1:
        votes.append(v.text.strip())
    for v in votes2:
        votes.append(v.text.strip())

    return reg, env, valid, votes


def get_parties(soup):
    # list for party names
    party_list = []

    # parties are also in two tables...
    p1 = soup.find_all('td', {'headers': 't1sa1 t1sb2'})
    p2 = soup.find_all('td', {'headers': 't2sa1 t2sb2'})

    for p in p1:
        party_list.append(p.text.strip())
    for p in p2:
        party_list.append(p.text.strip())

    return party_list


def main():
    url, output_file = check_args()
    print("Downloading from:", url)

    # first get the main page
    soup = get_data_from_url(url)
    municipalities = get_municipalities(soup)

    # check if we found anything
    if len(municipalities) == 0:
        print("No municipalities found!")
        sys.exit()

    print("Found", len(municipalities), "municipalities")

    # need to get party names first
    first_mun = get_data_from_url(municipalities[0]['url'])
    parties = get_parties(first_mun)

    # prepare csv header
    header = ['Code', 'Name', 'Registered', 'Envelopes', 'Valid'] + parties

    # now get data for each municipality
    results = []
    for i in range(len(municipalities)):
        m = municipalities[i]
        print(f"Processing {i + 1}/{len(municipalities)}: {m['name']}")

        # get and process municipality page
        soup_mun = get_data_from_url(m['url'])
        reg, env, valid, votes = get_results(soup_mun)

        # add all info to one row
        row = [m['code'], m['name'], reg, env, valid] + votes
        results.append(row)

    # save everything to csv
    print("Saving to:", output_file)
    f = open(output_file, 'w', newline='', encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(results)
    f.close()

    print("Done!")


if __name__ == "__main__":
    main()