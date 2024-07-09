import time
import pandas as pd
import numpy as np
# documents changes

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input("Please enter the name of the city to analyze (chicago, new york city, washington): ").strip().lower()
        
        if city in cities:
            break
        else:
            print("You have entered an incorrect city name. Please try again.")
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Please enter the name of the month to filter by (all, january, february, ..., june): ").strip().lower()
        if month in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Please enter the name of the day of the week to filter by (all, monday, tuesday, ..., sunday): ").strip().lower()
        if day in days:
            break

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
    file_name = CITY_DATA[city]
    df = pd.read_csv(file_name)
    
    # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month_name().str.lower()
    df['Day of Week'] = df['Start Time'].dt.day_name().str.lower()
    
    # Filter by month if applicable
    if month != 'all':
        df = df[df['Month'] == month]
        
    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['Day of Week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['Month'].mode()[0]
    print(f"The most common month: {common_month.title()}")

    # Display the most common day of week
    common_day = df['Day of Week'].mode()[0]
    print(f"The most common day of week: {common_day.title()}")

    # Display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    common_start_hour = df['Start Hour'].mode()[0]
    print(f"The most common start hour: {common_start_hour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: {common_start_station}")

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station: {common_end_station}")

    # Display most frequent combination of start station and end station trip
    df['Start-End Combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Start-End Combination'].mode()[0]
    print(f"The most frequent combination of start station and end station trip: {common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f"Counts of user types:\n{user_types}\n")

    # Display counts of gender (only if 'Gender' column exists in the DataFrame)
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(f"Counts of gender:\n{gender_counts}\n")
    else:
        print("Gender information is not available for this dataset.\n")

    # Display earliest, most recent, and most common year of birth (only if 'Birth Year' column exists)
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print(f"Earliest birth year: {earliest_birth_year}")
        print(f"Most recent birth year: {most_recent_birth_year}")
        print(f"Most common birth year: {most_common_birth_year}\n")
    else:
        print("Birth year information is not available for this dataset.\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):
    """사용자 요청 시 한 번에 5줄의 원시 데이터를 표시합니다."""
    row_length = df.shape[0]
    row_start = 0
    
    while True:
        display = input('Would you like to see 5 more rows of raw data? Please enter yes or no.').strip().lower()
        if display != 'yes':
            break
        print(df.iloc[row_start:row_start + 5])
        row_start += 5
        if row_start >= row_length:
            print("더 이상 표시할 데이터가 없습니다.")
            break
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        # 사용자 요청 시 원시 데이터를 표시합니다.
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
