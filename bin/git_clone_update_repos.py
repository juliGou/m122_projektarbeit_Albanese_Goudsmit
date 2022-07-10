import argparse
import os
import csv
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(asctime)s:%(message)s')

PARSER = argparse.ArgumentParser(description='get params baseDir and inputFile')
PARSER.add_argument('-b','--baseDir', dest='baseDir', help='directories where the repos will be cloned ore pulled')
PARSER.add_argument('-i','--inputFile', dest='inputFile', help='input file with the git repos')

inputFile = PARSER.parse_args().inputFile
baseDir = PARSER.parse_args().baseDir

if (inputFile.split('.')[-1] != 'csv' or not os.path.exists(baseDir)):
    logging.error('wrong filename')
    logging.error('exit')
    sys.exit()

if not baseDir.endswith('/'):
    baseDir += '/'

directories = os.listdir(baseDir)

with open(inputFile, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
        if len(row) != 2:
            logging.error('wrong filestructure')
            break
        repoLink = row[0]
        repoName = row[1]
        repoDir = baseDir + str(repoName)
        # Pull repo
        if (repoName in directories):
            try:
                logging.info("Pulling repository")
                os.system("cd " + repoDir + " && git pull")
            except:
                logging.error("error: cant pull repo")
        # Clone repo
        else:
            try:
                logging.info("Cloning repository")
                os.system("git clone " + str(repoLink) + " " + repoDir)
            except:
                logging.error("error: cant clone repo")

for dir in directories:
    with open(inputFile) as f:
        if dir not in f.read().split(' ')[1]:
            try:
                logging.info('remove ' + dir)
                os.system("rm -rf " + baseDir + str(dir))
            except:
                logging.error('cant remove ' + dir)