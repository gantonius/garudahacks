#%%
from datetime import datetime as dt
import time
import pandas as pd

def toYearFraction(date):
    def sinceEpoch(date): # returns seconds since epoch
        return time.mktime(date.timetuple())
    s = sinceEpoch

    year = date.year
    startOfThisYear = dt(year=year, month=1, day=1)
    startOfNextYear = dt(year=year+1, month=1, day=1)

    yearElapsed = s(date) - s(startOfThisYear)
    yearDuration = s(startOfNextYear) - s(startOfThisYear)
    fraction = yearElapsed/yearDuration

    return date.year + fraction

#%%
def calculateOneDayFraction():
    return toYearFraction(dt(2020, 8, 15)) - toYearFraction(dt(2020, 8, 14))
#%%
def convertDayToFraction(day):
    max = 162
    difference = max - day
    return toYearFraction(dt(2020, 8, 15)) - (difference * calculateOneDayFraction())
#%%
def main():
    # print(convertDayToFraction(162))
    # print(toYearFraction(dt(2020, 8, 15)))
    df = pd.read_csv("eight_provinces_plotly.csv")
    df['DayStandard'] = df['Day'].apply(convertDayToFraction)
    df.to_csv('converted.csv')
# %%
if __name__ == "__main__":
    main()
# %%
