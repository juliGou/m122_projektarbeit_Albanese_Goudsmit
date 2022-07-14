import logging
import argparse
import os
import csv
import subprocess
import sys
from configparser import ConfigParser

#Read config.ini file
config_object = ConfigParser()
config_object.read("../etc/config.conf")
LOG_DIR = config_object.get("config", "LOG_DIR")


logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(asctime)s:%(message)s')

PARSER = argparse.ArgumentParser(description='get params baseDir and inputFile')
PARSER.add_argument('-b','--baseDir', dest='baseDir', help='directories where the repos will be cloned ore pulled')
PARSER.add_argument('-f','--filename', dest='filename', help='input file with the git repos')

filename = PARSER.parse_args().filename
baseDir = PARSER.parse_args().baseDir

if not os.path.exists(baseDir):
    logging.error(baseDir + ' directory does not exist')
    logging.error('exit')
    sys.exit()

# Checks if output dir exists, if not creates it
file = LOG_DIR + filename
if not os.path.exists(file):
    logging.info('create directory: ' + file)
    os.makedirs(file)

if not baseDir.endswith('/'):
    baseDir += '/'

directories = os.listdir(baseDir)
header = ['Zielverzeichnis', 'Datum', 'Commit-Hash', 'Author']

with open(filename, 'w', newline='\n') as csvfile:
    CSV_WRITER = csv.writer(csvfile, delimiter=',')
    CSV_WRITER.writerow(header)
    for dir in directories:
        try:
            logging.info('write log details to file')
            gitCommand = "cd " + baseDir + str(dir) + "&& git log --date=format:%Y%m%" + "d --pretty=format:" + str(dir) + ",%" + "cd,%H,%" + "cn"
            gitOut = subprocess.check_output(gitCommand, shell=True, text=True, universal_newlines=True)

            splitedRows = gitOut.split("\n")
            for row in splitedRows:
                CSV_WRITER.writerow(row)
        except:
            logging.error('cant write log infos to file')