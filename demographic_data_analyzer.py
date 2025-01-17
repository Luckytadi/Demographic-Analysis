import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # Number of each race
    race_count = df["race"].value_counts()

    # Average age of men
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # Percentage with Bachelors degrees
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    # Percentage with higher education that earn >50K
    higher_education_rich = ((df['education-num'] >= 13) & (df['salary'] == '>50K')).mean() * 100

    # Percentage without higher education that earn >50K
    lower_education_rich = ((df['education-num'] < 13) & (df['salary'] == '<=50K')).mean() * 100

    # Min work time
    min_work_hours = df['hours-per-week'].min()

    # Percentage of the people who work the minimum number of hours per week and have a salary of >50K
    rich_percentage = ((df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')).mean() * 100

    # Country with highest percentage of people that earn >50K
    highest_earning_country = df[df['salary'] == '>50K']['native-country'].value_counts().idxmax()
    highest_earning_country_percentage = (df[(df['salary'] == '>50K') & (df['native-country'] == highest_earning_country)].shape[0] / df[df['native-country'] == highest_earning_country].shape[0]) * 100

    # Identify the most popular occupation for those who earn >50K in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Print the results if print_data is True
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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
