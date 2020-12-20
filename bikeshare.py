import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington)
    cities = ['chicago', 'new york city', 'washington']
    city = 0
    while city not in cities:
        city = input('Which city are you looking to explore? Please, enter one of the 3 cities; Chicago, New York City, or Washington.\n')
        city = city.lower()

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = 0
    while month not in months:
        month = input('Do you wish to filter by month? If not, type "All".\n')
        month = month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = 0
    while day not in days:
        day = input('Do you wih to filter by day? If not, type "All". \n')            
        day = day.lower()


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
    filename = city + '.csv'
    df = pd.read_csv(filename)
    
    # create datetime column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # create month column
    df['Month'] = df['Start Time'].dt.month
    
    # create day column
    df['Day Of Week'] = df['Start Time'].dt.dayofweek
    
    # filter month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['Month'] == month]
        
    # filter day
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day != 'all':
        day = days.index(day)
        df = df[df['Day Of Week']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    # display the most common month
    print('most common month:', months[df['Month'].mode()[0]-1].title())

    # display the most common day of week
    print('most common day of week:', days[df['Day Of Week'].mode()[0]].title())
    
    # create hour column
    df['Hour'] = df['Start Time'].dt.hour
    
    # display the most common start hour
    print('most common hour:', df['Hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(most_common_start_station, 'is the most common start station.')

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(most_common_end_station, 'is the most common end station.')

    # display most frequent combination of start station and end station trip
    start_end_combination = df['Start Station'] + ' - ' + df['End Station']
    most_common_combination_stations = start_end_combination.mode()[0]
    print(most_common_combination_stations, 'is the most common trip.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: {} seconds'.format(total_travel_time))

    # display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean(), 2)
    print('Mean travel time: {} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


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
