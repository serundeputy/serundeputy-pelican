Title: First Python Data Project
Date: 2021-01-22
Category: python

## tl;dr

* Download data/files with python
* Load and manipulate data with pandas
* Create graphs with matplotlib
* Source code: [serundeputy/serundeputy-pelican](https://github.com/serundeputy/serundeputy-pelican/tree/main/covid-data)

## Intro

As I was studying python and data science like many others I did a bunch of tutorials, videos, courses, and kaggles. I wanted to tackle a less guided project to apply my skills. I was following and interested in the spread of covid-19 and the oceans of data that accompany it seeemed like a good place to do some data manipulation.

I decided to focus on my local area and Massachusetts data. I looked for data on [Mass.gov](https://mass.gov) and to see if the provided an API. No API, but they had raw data, so I was in luck!

I also wanted to get information about covid cases, testing postivity rates, and deaths in 2 week rolling averages, rather than observing single day spikes or drop offs, the 2 week averages smooth out some of the rough edges and anomalies.

## Fetching the Data

To get the data I've used the python [`requests`](https://requests.readthedocs.io/en/master/) library. Load up the library with an `import` statement:

```py
import requests as req
```

Then I've written a small file helper function called [`get_file`](https://github.com/serundeputy/serundeputy-pelican/blob/main/covid-data/modules/file_helpers.py#L11) to, well, get the file:

```py
base_url = 'https://www.mass.gov/doc/covid-19-raw-data-'

# Download the data
def get_file(date):
    r = req.get(base_url + date + '/download')
    with open(date + '.xlsx', 'wb') as outfile:
        outfile.write(r.content)
```

After running/calling the `get_file` function it drops the data file into the current working directory.

## Processing the Data

The raw data is delivered from Mass.gov as an `xlsx` spreadseet with tabs. To open and process the data I use the [`pandas`](https://pandas.pydata.org/docs/) library. First load in the `pandas` lib:

```py
import pandas as pd
```

Pandas is an excellent library for loading and processing data and is the industry standard. It comes with functions to load `csv`, `xlsx`, and `sql` data built in! So, loading the data is made easy by leveraging the [`read_excel`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html?highlight=read_excel#pandas.read_excel) function.

In my program that is done in the main worker file for the `covid-data` project called `covid-data.py`:

```py
cases = pd.read_excel(file_name + '.xlsx', 'Cases (Report Date)', engine='openpyxl')
```

This stores the data in a `cases` pandas data frame from the `xlsx` file `Cases (Report Date)` tab. Similarly we pluck off the `hampdenCases` by reading in the `County_Daily` tab and pattern matching on the `County` column for `Hampden`:

```py
hampdenCases = pd.read_excel(file_name + '.xlsx', 'County_Daily', engine='openpyxl')
hampdenCases = hampdenCases[hampdenCases['County'] == 'Hampden']
```

Then use the same pattern to get the `deaths` (RIP) data from another tab of the spreadsheet.

Now that we have the data we can pass it around to some more data processing functions and plot functions.

## Plotting the Data

Use [`matplotlib`](https://matplotlib.org/contents.html) library to make some plots of the datasets. I've broken [`plot_helpers`](https://github.com/serundeputy/serundeputy-pelican/blob/main/covid-data/modules/plot_helpers.py) out into its own separate library. First things first import `matplotlib`:

```py
import matplotlib.pyplot as plt
```

From there I've defined a `plot` function that takes in a dataframe, date, and region and executes the `matplotlib` magic to make graphs. Here is a sample output chart:

<div style="text-align: center;">
  <img
    src="/images/january-05-2021-MA-Cases-plot.png"
    alt="Example MatPlotLib Chart">
    <br>
</div>

And the `plot` function that creates it:

```py
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
    ax.set_ylim(data[key].min() - 0.3*data[key].min(), data[key].max() + 0.3*data[key].max())
    for i, j in zip(xData, data[key]):
        ax.annotate(str(int(round(j))),xy=(i,j), xytext = (-14, 22), textcoords = 'offset points')
    fig.tight_layout()
    fig.autofmt_xdate()
    plt.savefig('content/images/' + date + '-' + region + '-' + ylabel + '-plot.png')
```


## Calculating the Means and Deltas

Then to calculate the 2 Wk Means we need to chunk the data sets into the latest 2 Wk chunks and the previous 2 Wks for comparision. To get the 2 week intervals I've written the `get_interval_df` helper function:

```py
def get_interval_df(df, weeksAgo = 2, prev = False):
    rowCount = df.shape[0] # - 1
    if (prev == False):
        return df[rowCount - (weeksAgo - 1)*14:rowCount - (weeksAgo - 2)*14]
    elif (prev):
        return df[rowCount - weeksAgo*14:rowCount - (weeksAgo - 1)*14]
```

And finally calulating the means of the data sets with `get_interval_mean`:

```py
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
        tests = pd.read_excel(file_name + '.xlsx', 'Testing2 (Report Date)', engine='openpyxl')
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
            if (region == "Hampden"):
                city_town_df = pd.read_excel('january-16-2021' + '.xlsx', 'Weekly_City_Town', engine = 'openpyxl')
                city_town_print.city_town(city_town_df)
        sys.stdout = original_stdout
```

This code calculates the means, percent positivity rate, and writes out the blog post for the day reporting data and analysis for that day.

You can see the rolling averages on the [covid-19](/category/covid-19.html) page of this blog.

## Conclusion

This was a fun and carthartic learning project for me. I hope you can gleen some use and insights from it as well. Here is the full source code for the project [serundeputy/serundeputy-pelican](https://github.com/serundeputy/serundeputy-pelican/tree/main/covid-data).

Follow me on twitter [@serundeputy](https://twitter.com/serundeputy).
