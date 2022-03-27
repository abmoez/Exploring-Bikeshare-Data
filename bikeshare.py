# the used data sets is available on Kaggle here : https://www.kaggle.com/datasets/samratp/bikeshare-analysis 

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
   
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("Choose a city: Chicago, New York City or Washington \n").lower().strip()
    while(city not in ['chicago', 'new york city', 'washington']):
        city = input('Please enter a valid city: Chicago, New York City or Washington \n').lower().strip()
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("Choose a month: January, February, March, April, May, June or ALL \n").lower().strip()
    while(month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']):
        month = input('Please enter a valid month \n').lower().strip()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Choose a day: Monday, Tuesday, ... Sunday or All \n").lower().strip()
    while(day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']):
        day = input('Please enter a valid day \n').lower().strip()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    df=pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['startHour'] = df['Start Time'].dt.hour
    
    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month= months.index(month)+1
        df=df[df['month']==month]
    
    if day != "all":
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day= days.index(day)+1
        df=df[df['day_of_week']==day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    commonMonth = df['month'].mode()
    print(f"The most common month is {commonMonth[0]}")

    # TO DO: display the most common day of week
    commonDay = df['day_of_week'].mode()
    print(f"The most common day is {commonDay[0]}")

    # TO DO: display the most common start hour
    commonHour = df['startHour'].mode()
    print(f"The most common hour is {commonHour[0]}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonSS = df['Start Station'].mode()
    print(f"The most common Start Station is {commonSS[0]}")


    # TO DO: display most commonly used end station
    commonES = df['End Station'].mode()
    print(f"The most common Ene Station is {commonES[0]}")

    # TO DO: display most frequent combination of start station and end station trip
    df['StartEnd']=df['Start Station']+ "-" +df['End Station']
    df['StartEnd'].value_counts()
    commonSEcomp = df['StartEnd'].value_counts().index[0]
    commonSEcompN = df['StartEnd'].value_counts()[0]
    print(f"The most common Start & End Combination is {commonSEcomp}, {commonSEcompN} times ")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totTime_hours = round(df['Trip Duration'].sum()/(60*60), 2) 
    print(f"The total travel time in hours equals {totTime_hours}")
    # TO DO: display mean travel time
    meanTime = round(df['Trip Duration'].mean()/60, 2)
    print(f"The average time for a trip duration in minutes equals {meanTime}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("By User Type")
    uType1 = df['User Type'].value_counts().index[0]
    uType1Counts = df['User Type'].value_counts()[0]
    uType2 = df['User Type'].value_counts().index[1]
    uType2Counts = df['User Type'].value_counts()[1]
    print(f"{uType1} : {uType1Counts} counts")
    print(f"{uType2} : {uType2Counts} counts")

    # TO DO: Display counts of gender
    if city != "washington" :
        print("By Gender")
        uGender1 = df['Gender'].value_counts().index[0]
        uGender1Counts = df['Gender'].value_counts()[0]
        uGender2 = df['Gender'].value_counts().index[1]
        uGender2Counts = df['Gender'].value_counts()[1]
        print(f"{uGender1} : {uGender1Counts} counts")
        print(f"{uGender2} : {uGender2Counts} counts")

    # TO DO: Display earliest, most recent, and most common year of birth
        print("By Year of Birth")
        erlBirth=df['Birth Year'].sort_values().iloc[0]
        print(f"The earliest year of birth is {erlBirth}")  
        recentBirth=df['Birth Year'].sort_values(ascending=False).iloc[0]
        print(f"The most recent year pf birth is {recentBirth}")
        commonYear = df['Birth Year'].mode()
        print(f"The most common year of birth is {commonYear[0]}")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no \n').strip().lower()
    while view_data not in ['yes' , 'no'] :
        view_data = input('\nPlease enter yes or no \n').strip().lower()
        
    start_loc = 0
    while (view_data=="yes"):
        print(df.iloc[start_loc:start_loc+5 , : ])
        start_loc += 5
        view_data = input("Do you wish to continue? Type yes if you do: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
