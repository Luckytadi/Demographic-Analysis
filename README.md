## Overview
The code reads demographic data from a CSV file and calculates statistics such as race distribution and average age of men.

It determines income percentages based on education level and identifies the country with the highest percentage of high earners and the most popular occupation for high earners in India.

Results are either printed to the console or returned as a dictionary, depending on the `print_data` flag.

## Files
- `adult.data.csv`: The source dataset used for the analysis.

## Preview
<pre>
Number of each race:
race
White                 27816
Black                  3124
Asian-Pac-Islander     1039
Amer-Indian-Eskimo      311
Other                   271
Name: count, dtype: int64
Average age of men: 39.43354749885268
Percentage with Bachelors degrees: 16.44605509658794%
Percentage with higher education that earn >50K: 12.005159546696968%
Percentage without higher education that earn >50K: 63.14916618039986%
Min work time: 1 hours/week
Percentage of rich among those who work fewest hours: 0.006142317496391388%
Country with highest percentage of rich: United-States
Highest percentage of rich people in country: 24.583476174151524%
Top occupations in India: Prof-specialty
{'race_count': race
White                 27816
Black                  3124
Asian-Pac-Islander     1039
Amer-Indian-Eskimo      311
Other                   271
Name: count, dtype: int64, 'average_age_men': 39.43354749885268, 'percentage_bachelors': 16.44605509658794, 'higher_education_rich': 12.005159546696968, 'lower_education_rich': 63.14916618039986, 'min_work_hours': 1, 'rich_percentage': 0.006142317496391388, 'highest_earning_country': 'United-States', 'highest_earning_country_percentage': 24.583476174151524, 'top_IN_occupation': 'Prof-specialty'}
</pre>

## How to Use
1. Clone this repository.
2. Open `demographic_data_analyzer with Jupyter Notebook.

## Data Sources
- The FreeCodeCamp provided the adult.data' data.
