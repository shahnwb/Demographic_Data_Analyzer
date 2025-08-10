import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    male = df.loc[(df.sex == 'Male')]
    average_age_men = male['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelor = df.loc[(df.education == 'Bachelors')]
    percentage = (bachelor['education'].count() / df['education'].count()) * 100
    percentage = percentage.round(1)
    percentage_bachelors = percentage

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    advance = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters')| (df['education'] == 'Doctorate')]
    higher_education = advance

    non_advance = df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]
    lower_education = non_advance

    # percentage with salary >50K
    salary = higher_education.loc[(higher_education['salary'] == '>50K')]
    higher = (salary['salary'].count()/higher_education['salary'].count())*100
    higher_education_rich = higher.round(1)

    salary2 = lower_education.loc[(lower_education['salary'] == '>50K')]
    lower = (salary2['salary'].count()/lower_education['salary'].count())*100
    lower_education_rich = lower.round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours = df.loc[(df['hours-per-week'] == 1)]
    salary3 = min_hours.loc[min_hours['salary'] == '>50K']
    salary3 = salary3['salary'].count() / min_hours['salary'].count() * 100
    
    num_min_workers = min_hours.count()
    rich_percentage = salary3.round(1)

    # What country has the highest percentage of people that earn >50K?
    high_salary = df.loc[df['salary'] == '>50K']

    highest_earning_country = high_salary['native-country'].value_counts().idxmax()
    earn = high_salary['native-country'].value_counts().max() / high_salary['native-country'].count() * 100
    highest_earning_country_percentage = earn.round(1)


    # Identify the most popular occupation for those who earn >50K in India.
    india = df.loc[df['native-country'] == 'India']
    salary4 = india.loc[india['salary'] == '>50K']
    top_IN_occupation = salary4['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
