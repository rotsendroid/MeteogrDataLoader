import re
from utils.scrap import Scraping

class ParseMeteo:
    """
    Parse the .txt files and export them in .csv format
    """

    MONTHS = Scraping.MONTHS
    DATA_DIR = Scraping.DATA_DIR

    def __init__(self, area, start_y, stop_y):
        self.txt_file_lines = []
        self.area = area
        self.start_year = start_y
        self.stop_year = stop_y
        self.years_range = range(start_y, stop_y + 1)
        self.month = 0


    def parse_meteo(self, mode='r'):
        """
        mode values:
        'r' read the file (default),
        'p' read and print the file lines
        """
        for i in self.years_range:
            for j in ParseMeteo.MONTHS:
                try:
                    with open('{}/{}/{}_{}.txt'.format(ParseMeteo.DATA_DIR, self.area, i, j), 'rb') as f:
                        self.year = i
                        self.month = int(j)
                        if mode == 'p':
                            self.__line_preprocessing(f)
                            self.__print_lines()
                        else:
                            self.__line_preprocessing(f)
                except FileNotFoundError as e:
                    continue

    def __print_lines(self):
        """
        helper method
        print the parsed lines
        :return:
        """
        for i,l in enumerate(self.txt_file_lines):
            print("{}:\t\t{}".format(i, l))


    def __line_preprocessing(self, txt_file):
        while True:
            raw_line = txt_file.readline()
            if not raw_line:
                break
            try:
                line = re.sub(r'[\n^\r]+', '', raw_line.decode('utf-8'))
                self.__read_lines(line)
            except UnicodeDecodeError as e:
                continue


    def __read_lines(self, l):
        # matches the daily records
        values_record_pattern = re.compile(r'\s*(\d+)\s+(\-*\d+\.\d+)\s+(\-*\d+\.\d+)\s+(\d+\:\d+\w*)\s+(\-*\d+\.\d+)\s+(\d+\:\d+\w*)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\:\d+\w*)\s+')
        match = re.search(values_record_pattern, l)
        if match:
            ln = self.__format_record(match)
            with open('csv/meteogr_{}_{}_{}.csv'.format(self.area,self.years_range[0],
                                                       self.years_range[len(self.years_range)-1]), 'a') as fl:
                fl.write(ln)


    def __format_record(self, match):
        date = "{}/{}/{}".format(match.group(1), self.month, self.year)
        # format description
        # record_formatted = "Date: {}, T_AVG: {}, T_MIN: {}, T_MAX: {}, RAIN: {}\n".format(date,
        #                                                                       match.group(2),
        #                                                                       match.group(4),
        #                                                                       match.group(3),
        #                                                                       match.group(9))

        record_formatted = "{};{};{};{};{}\n".format(date,
                                                     match.group(2),
                                                     match.group(5),
                                                     match.group(3),
                                                     match.group(9))

        return record_formatted




if __name__ == '__main__':
    p = ParseMeteoTxt()
    p.read_meteogr_txt()