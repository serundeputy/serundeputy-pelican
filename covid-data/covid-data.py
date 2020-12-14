import json as json
import numpy as np
import pandas as pd
import requests as req
import zipfile
import os as os
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import date as dt
import sys as sys

# Mass.gov URL format example:
# https://www.mass.gov/doc/covid-19-raw-data-december-11-2020/download
base_url = 'https://www.mass.gov/doc/covid-19-raw-data-'

# Download the data
def get_file(date):
    # do the things
    r = req.get(base_url + date + '/download')
    with open(date + '.zip', 'wb') as outfile:
        outfile.write(r.content)

def file_unzip(path_of_zip, directory_to_extract_to):
    os.mkdir(directory_to_extract_to)
    with zipfile.ZipFile(path_of_zip, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

# Download several/all data
def get_mult_files(start_date, end_date):
    # do the things
    pass

def copy_file(date, file_name):
    os.system('mkdir -p content/images/' + date)
    os.system('cp covid-data/data/' + date + '/' + file_name + ' content/images/' + date + file_name)

def get_interval_mean(cases, date, weeksAgo = 2, region = 'MA', verbose = False):
    rowCount = cases.shape[0] - 1
    key = cases.columns[2]
    twoWksFrame = cases[rowCount - (weeksAgo - 1)*14:rowCount - (weeksAgo - 2)*14]
    prevTwoWksFrame = cases[rowCount - weeksAgo*14:rowCount - (weeksAgo - 1)*14]
    if (verbose):
        print(prevTwoWksFrame)
        print(twoWksFrame)

    prevPrev14Mean = prevTwoWksFrame[key].sum() / 14
    prev14Mean = twoWksFrame[key].sum() / 14
    title = key + ' for ' + region + ' (2 wk averages starting ' + str(weeksAgo) + ' weeks ago)'
    prevTwoWkMean = str(int(round(prevPrev14Mean)))
    twoWkMean = str(int(round(prev14Mean)))
    delta = str(int(round(prev14Mean / prevPrev14Mean * 100 ))) + '%'
    print('\n' + title + '\n')
    print('\tPrev. 2 wk Mean:\t' + prevTwoWkMean)
    print('\t2 wk Mean:\t\t' + twoWkMean)
    print('\tDelta:\t\t\t' + delta)
    print('\n')
    original_stdout = sys.stdout
    with open('content/blog/' + date + '-' + region + '.md', 'w+') as outfile:
        sys.stdout = outfile
        print('Title: ' + date + ' Covid-19 Two Week Rolling Average')
        today = dt.today().strftime('%Y-%m-%d')
        print('Date: ' + today)
        print('Category: blog')
        print('\n')
        print('<div class="covid-data-container">')
        print('  <div class="col-md-8">')
        print('    <img src="/images/' + date + '-' + region + '-plot.png" width="100%">')
        print('  </div>')
        print('  <div class="col-md-4 covid-mean">')
        print('    <div>Prev. 2 Wk Mean: ' + prevTwoWkMean + '</div>')
        print('    <div>2 Wk Mean: ' + twoWkMean + '</div>')
        print('    <div>Delta: ' + delta + '</div>')
        print('  </div>')
        print('</div>')
        print('\n')
        sys.stdout = original_stdout

def plot(data, date, region = 'MA'):
    key = data.columns[2]
    xData = pd.to_datetime(data.Date).dt.strftime('%d %b')
    lastRow = data.tail(1)
    if (region == 'MA'):
        endDate = lastRow['Date'][lastRow['Date'].index.stop - 1]
    else:
        endDate = lastRow['Date'][lastRow['Date'].index[0]]

    paramDict = {
        'marker': '.'
    }
    fig, ax = plt.subplots()
    ax.plot(xData, data[key], **paramDict)
    ax.set_title(region + ' Two Week Rolling Cases Reported\nEnding ' + str(endDate))
    ax.set_ylabel('Cases')
    ax.set_ylim(data[key].min() - 100, data[key].max() + 1000)
    for i, j in zip(xData, data[key]):
        ax.annotate(str(int(round(j))),xy=(i,j), xytext = (-14, 22), textcoords = 'offset points')
    fig.tight_layout()
    fig.autofmt_xdate()
    plt.savefig('content/images/' + date + '-' + region + '-plot.png')

def write_28_day_rolling_component():
   pass


# get_file('december-11-2020')
# file_unzip('december-11-2020.zip', 'covid-data/data/december-11-2020')

# get_file('december-12-2020')
# file_unzip('december-12-2020.zip', 'covid-data/data/december-12-2020')
# get_file('december-13-2020')
# file_unzip('december-13-2020.zip', 'covid-data/data/december-13-2020')
# exit()

# cases11 = pd.read_csv('covid-data/data/december-11-2020/Cases.csv')
# countyCases11 = pd.read_csv('covid-data/data/december-11-2020/County.csv')
# countyCases12 = pd.read_csv('covid-data/data/december-12-2020/County.csv')
# hampdenCases11 = countyCases11[countyCases12['County'] == 'Hampden']
# deaths = pd.read_csv('covid-data/data/december-11-2020/DeathsReported.csv')

cases13 = pd.read_csv('covid-data/data/december-13-2020/Cases.csv')
get_interval_mean(cases13, 'december-13-2020', 2, 'MA')
plot(cases13.tail(14), 'december-13-2020')


# get_interval_mean(deaths, 3)
# get_interval_mean(deaths, 2)

#plot(cases12.tail(14), 'december-12-2020')
#plot(hampdenCases11.tail(14), 'december-11-2020', 'Hampden')
