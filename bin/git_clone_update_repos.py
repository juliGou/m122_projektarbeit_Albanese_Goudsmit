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

directorys = os.listdir(baseDir)

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
        if (repoName in directorys):
            try:
                logging.info("Pulling repository")
                gitCommand = "cd " + repoDir + " && git pull"
            except:
                logging.error("error: cant pull repo")
        # Clone repo
        else:
            logging.info("Cloning repository")
            # The git config part was an error we got, so we just added it here. Now it works.
            gitCommand = "git clone " + str(repoLink) + " " + repoDir
        
        os.system(gitCommand)