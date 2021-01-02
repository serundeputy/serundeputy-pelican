Title: { python, pelican, serundeputy.io }
Date: 2021-01-02
Authors: Geoff St. Pierre
Category: python

## Intro

Over the last year I've re-ignited my passion for math and science and to that end I've started guiding some of my software development energy towards numbers, data, and predictions. Enter python and pandas.

## Covid-19

During the 2020 covid-19 pandemic many of us have spent a good deal of time looking at, listening to, and trying to make sense of numbers comming at us at high speed. So, I wanted a place where I could ingest, process, and make sense of all this data comming at me.  For me that meant/means taking those daily numbers and computing averages that I could compare on the regular and see if on average which things (cases, positivity rate, deaths) are trending up or down. Not on a sample size one, day to day, but on average so I took a 2 week rolling average to accomodate for testing, reporting, and other fluctuations.

## State of the Data

At this point I began looking at the data reported by [Mass.gov](https://mass.gov). That data was aggregated and delivered in PDF format. It provided lot's of useful information, but it was 

1. in PDF which I had to download/read/delete from my phone on the regular to prevent it from clogging up my disk space
2. hard to compare the day to day and week to week data as one would have to toggle to and fro from PDF to PDF depending on what day(s) they were interested

I wanted:

1. Data not in PDF format; just on the web info I could get on the daily
2. Comparison data of 2 week averages to see trends; instead of day to day (sample size one) ups and downs

Fortunately, Mass.gov provides the [raw data](https://www.mass.gov/info-details/covid-19-response-reporting#covid-19-weekly-public-health-report-) day to day as well as the PDF report!

## Python and Pandas

I learned python and pulled in the raw data from Mass.gov and processed it with pandas. You can see that code on [github/serundeputy/serundeputy-pelican](https://github.com/serundeputy/serundeputy-pelican/blob/main/covid-data/covid-data.py). It breaks the data into two week chunks for MA cases, MA deaths, and Hampden County cases and computes rolling averages, % increase/decrease, and a graphical line plot of the data. You can see an examples of that on the [covid-19](https://serundeputy.io/category/covid-19.html) section of this site.

## Conclusion

Now I've got one stop shopping to compare 2 wk averages over time. Making it very easy to pick out the up and down trends.
