import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def boolin(a,b):
    if a in b:
        return True

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city = input('\nWould you like to see data for Chicago,New York city or Washington?\n').lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            break
        print('\nWrong Typedata:Try with (chicago, new york city, washington)')
    while True:
        options = input('\nwould you like to filter the data by month,day,both,or not at all?Type \'none\' for no time filter\n')
        month_list = ['january', 'february', 'march', 'april', 'may', 'june']
        day_list = ['all','monday','tuesday','Wednesday ','thursday','friday','saturday','sunday']
        if options == 'both':
            while True:
                month = input('\nWhich month? January, February, March, April, May, or June?\n').lower()
                day = input('\nAnd witch day? (all, monday, tuesday, ... sunday)\n').lower()
                if boolin(month,month_list) and boolin(day,day_list):
                    break
                print ('\n Wrong Typedata:Try month data with {} and Day data with {}'.format(month_list,day_list))
            break
        if options == 'month' :
    # TO DO: get user input for month (all, january, february, ... , june)
            while True:
                month = input('\nWhich month? January, February, March, April, May, or June?\n').lower()
                if boolin(month,month_list):
                    break
                print ('\n Wrong Typedata:Try month data with {}'.format(month_list))
            break
        elif options == 'day' :
            while True:
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
                day = input('\nAnd witch day? (all, monday, tuesday, ... sunday)\n').lower()
                if boolin(day,day_list):
                    break
                print ('\n Wrong Typedata:Try day data with {}'.format(day_list))
            break
        elif options == 'none':
            month = 'all'
            day = 'all'
            break
        print ('\nWrong Typedata:Try with (month,day,both or none)')
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #TO DO: load city_data files
    df = pd.read_csv(CITY_DATA[city])
    #TO DO:LOAD CITY_DATA BY mouth
    #make start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #get mouth and week from start time with new column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    #filter
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print ('\nThe most common month is {}'.format(common_month))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print ('\nThe most comon day of week is {}'.format(common_day))
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print ('\nThe most common start hour is',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_ss = df['Start Station'].mode()[0]
    print('\nThe most commonly used start station is :',most_ss)
    # TO DO: display most commonly used end station
    most_es = df['End Station'].mode()[0]
    print('\nThe most commonly uesd end station is :',most_es)
    # TO DO: display most frequent combination of start station and end station trip
    df['Se Station'] = df['Start Station'] +' to ' + df['End Station']
    most_ses = df['Se Station'].mode()[0]
    print ('\nThe most frequent combination of start station and end station trip is ',most_ses)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('The mean travel time is',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nThe counts of user types is : \n',df['User Type'].value_counts())
    try:

    # TO DO: Display counts of gender
        print('\nThe counts of gender is \n: ',df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        print ('\nThe earliest year of birth is %d'% df['Birth Year'].min())
        print ('\nThe most recent year of birth is %d'% df['Birth Year'].max())
        print ('\nThe most comon year of birth is %d'% df['Birth Year'].mode()[0])
    except:
        print ('\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
