from datetime import date as dt
import pandas as pd
import sys as sys

# My imports
import modules.file_helpers as fh
import modules.plot_helpers as ph
import modules.positivity as pt

def get_interval_df(df, weeksAgo = 2, prev = False):
    rowCount = df.shape[0] # - 1
    if (prev == False):
        return df[rowCount - (weeksAgo - 1)*14:rowCount - (weeksAgo - 2)*14]
    elif (prev):
        return df[rowCount - weeksAgo*14:rowCount - (weeksAgo - 1)*14]

def get_interval_mean(cases, date, weeksAgo = 2, region = 'MA', verbose = False):
    key = cases.columns[2]
    twoWksFrame = get_interval_df(cases)
    prevTwoWksFrame = get_interval_df(cases, 2, True)

    if (verbose):
        print(prevTwoWksFrame)
        print(twoWksFrame)

    ylabel = ph.get_ylabel(cases)
    prevPrev14Mean = prevTwoWksFrame[key].sum() / 14
    prev14Mean = twoWksFrame[key].sum() / 14
    today = dt.today().strftime('%Y-%m-%d')
    niceDate = dt.today().strftime('%d %B %Y')
    title = key + ' for ' + region + ' (2 wk averages starting ' + str(weeksAgo) + ' weeks ago)'
    prevTwoWkMean = str(int(round(prevPrev14Mean)))
    twoWkMean = str(int(round(prev14Mean)))
    delta = str(int(round(prev14Mean / prevPrev14Mean * 100 ))) + '%'
    print('\n' + title + '\n')
    print('\tPrev. 2 wk Mean:\t' + prevTwoWkMean)
    print('\t2 wk Mean:\t\t' + twoWkMean)
    print('\tDelta:\t\t\t' + delta)
    print('\n')
    if (region == 'MA' and cases.columns[2] != 'DeathsConfNew'):
        # tests = pd.read_csv('covid-data/data/' + file_name + '/Testing2.csv')
        tests = pd.read_excel(file_name + '.xlsx', 'Testing2 (Report Date)')
        tests2wks = get_interval_df(tests, 2)
        prevTests2wks = get_interval_df(tests, 2, True)
        avg_positivity = pt.positivity(twoWksFrame, tests2wks)
        prev_avg_positivity = pt.positivity(prevTwoWksFrame, prevTests2wks)
        original_stdout = sys.stdout
        with open('content/blog/' + date + '-' + region + '.md', 'w+') as outfile:
            sys.stdout = outfile
            print('Title: ' + niceDate + ' Covid-19 Two Week Rolling Average')
            print('Date: ' + today)
            print('Authors: Geoff St. Pierre')
            print('Category: covid-19')
            print('\n')
            print('<div class="covid-data-container">')
            print('  <div class="col-md-8">')
            print('    <img src="/images/' + date + '-' + region + '-' + ylabel + '-plot.png" width="100%">')
            print('  </div>')
            print('  <div class="col-md-4 covid-mean">')
            print('    <div>Prev. 2 Wk Mean: ' + prevTwoWkMean + '</div>')
            print('    <div>2 Wk Mean: ' + twoWkMean + '</div>')
            print('    <div>Delta: ' + delta + '</div>')
            print('    <div>Prev. 2 Wk Positivity Average: ' + str(prev_avg_positivity) + '%</div>')
            print('    <div>2 Wk Positivity Average: ' + str(avg_positivity) + '%</div>')
            print('  </div>')
            print('</div>')
            print('\n')
        sys.stdout = original_stdout
    else:
        original_stdout = sys.stdout
        with open('content/blog/' + date + '-MA.md', 'a+') as outfile:
            sys.stdout = outfile
            print('<div class="covid-data-container">')
            print('  <div class="col-md-8">')
            print('    <img src="/images/' + date + '-' + region + '-' + ylabel + '-plot.png" width="100%">')
            print('  </div>')
            print('  <div class="col-md-4 covid-mean">')
            print('    <div>Prev. 2 Wk Mean: ' + prevTwoWkMean + '</div>')
            print('    <div>2 Wk Mean: ' + twoWkMean + '</div>')
            print('    <div>Delta: ' + delta + '</div>')
            print('  </div>')
            print('</div>')
            print('\n')
            print('<div class="source-data">Source data: <a href="www.mass.gov/info-details/covid-19-response-reporting">Mass.gov</a></div>')
        sys.stdout = original_stdout

file_name = dt.today().strftime('%B-%d-%Y').lower()
# print(file_name)
# exit()

fh.get_file(file_name)
# fh.file_unzip(file_name + '.zip', 'covid-data/data/' + file_name)
# exit()

# cases = pd.read_csv('covid-data/data/' + file_name + '/Cases.csv')
cases = pd.read_excel(file_name + '.xlsx', 'Cases (Report Date)')
# hampdenCases = pd.read_csv('covid-data/data/' + file_name + '/County.csv')
hampdenCases = pd.read_excel(file_name + '.xlsx', 'County_Daily')
hampdenCases = hampdenCases[hampdenCases['County'] == 'Hampden']
# deaths = pd.read_csv('covid-data/data/' + file_name + '/DeathsReported.csv')
deaths = pd.read_excel(file_name + '.xlsx', 'DeathsReported (Report Date)')

ph.plot(cases.tail(14), file_name)
ph.plot(deaths.tail(14), file_name)
ph.plot(hampdenCases.tail(14), file_name, 'Hampden')
get_interval_mean(cases, file_name, 2, 'MA')
get_interval_mean(deaths, file_name, 2, 'MA')
get_interval_mean(hampdenCases, file_name, 2, 'Hampden')
