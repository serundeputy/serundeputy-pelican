from datetime import date as dt
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
import pandas as pd

def get_ylabel(df):
    ylabel = 'Cases'
    if (df.columns[2] == 'DeathsConfNew'):
        ylabel = 'Deaths'

    return ylabel

def plot(data, date, region = 'MA'):
    key = data.columns[2]
    ylabel = 'Cases'
    if (key == 'DeathsConfNew'):
        ylabel = 'Deaths'
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
    title = region + ' Two Week Rolling Cases Reported\nEnding ' + str(endDate)
    if (region == 'Hampden'):
        title = region + ' County Two Week Rolling Cases Reported\nEnding ' + str(endDate)
    elif (ylabel == 'Deaths'):
        title = region + ' Two Week Rolling Deaths Reported\nEnding ' + str(endDate)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_ylim(data[key].min() - 100, data[key].max() + 1000)
    for i, j in zip(xData, data[key]):
        ax.annotate(str(int(round(j))),xy=(i,j), xytext = (-14, 22), textcoords = 'offset points')
    fig.tight_layout()
    fig.autofmt_xdate()
    plt.savefig('content/images/' + date + '-' + region + '-' + ylabel + '-plot.png')

