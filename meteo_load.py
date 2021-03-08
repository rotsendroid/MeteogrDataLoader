#!/usr/bin/python3

import argparse
import datetime

from utils.scrap import Scraping
from utils.parse import ParseMeteo

#

def define_args_parsing():
    """
    Access args values:
    cmdargs.a => area name
    cmdargs.i => start year
    cmdargs.f => stop year
    cmdargs.d => display area names
    :return: cmdargs (type: class argparse.Namespace)
    """
    DEFAULT_START_YEAR = datetime.datetime.now().year - 1
    DEFAULT_STOP_YEAR = datetime.datetime.now().year

    parser = argparse.ArgumentParser(usage="meteo_load.py [-a <area-name> -i <start-year> -f <stop-year>]\n\n" \
                                           "Display the list of available area names: meteo_load.py -d\n\n" \
                                           "For help type: meteo_load.py -h",
                                     description=("MeteogrDataLoader downloads locally the meteorological data of " \
                                      "http://meteosearch.meteo.gr/ and then exports them in .csv format.\n" \
                                      "The exported meteorological properties include:\n" \
                                      "1) Average Temperature\n2) Minimum Temperature\n3) Maximum Temperature\n" \
                                      "4) Rain Height\n\n" \
                                                  ".csv columns format: <date>;<t_avg>;<t_min>;<t_max>"),
                                     formatter_class=argparse.RawTextHelpFormatter)

    # add the arguments
    parser.add_argument('-a',
                        type=str,
                        help="Area name, e.g. -a agiaparaskevi",
                        required=False)
    parser.add_argument('-i', type=int,
                        help="Start/Initial year, e.g. -i 2018. Default value: the previous year",
                        required=False,
                        default=DEFAULT_START_YEAR)
    parser.add_argument('-f', type=int,
                        help="Stop/Final year, e.g. -f 2019. Default value: the current year",
                        required=False,
                        default=DEFAULT_STOP_YEAR)
    parser.add_argument('-d',
                        help="Display the available area names",
                        required=False,
                        action="store_true")

    # cmdargs: a dictionary/hash
    cmdargs = parser.parse_args()

    return cmdargs



def display_area_names():
    with open("stations/stations.csv", "r") as f:
        while True:
            ln = f.readline().strip('\n')
            if not ln:
                break
            print(ln)


if __name__ == '__main__':
    cmdargs = define_args_parsing()

    # execute when user wants to display the available area names
    if cmdargs.d:
        display_area_names()

    # define args
    area_name = cmdargs.a
    start_year = cmdargs.i
    stop_year = cmdargs.f

    # initialize scraping
    scr = Scraping(area_name, start_year, stop_year)

    # download locally the data
    scr.download()

    # initialize parsing
    pars = ParseMeteo(area_name, start_year, stop_year)
    pars.parse_meteo()






