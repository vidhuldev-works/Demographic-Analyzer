import pandas as pd

from demographic_data_analyzer import *

def main():
    
    print(f'No.of people who represented in each race : \n {race_count()} \n')

    print(f'Average age of men : {round(avg_men_age(), 1)}')

    print(f'Percentage of people who have Bachelors Degree : {round(bachelor_percent(), 1)} %')

    print(f'Percentage of people who have Advanced Education and Earning morethan 50k: {round(adv_edu_morethan_50k_percent(), 1)} %')

    print(f"Percentage of people who doesn't have Advanced Education but Earning morethan 50k: {round(non_adv_edu_morethan_50k_percent(), 1)} %")

    print(f'The minimum number of hours a person works per week is : {min_worktime()} ')

    print(f'Percentage of people who earns morethan 50K with minimum worktime per week : {round(min_worktime_morethan50_percent(), 1)} %')

    highest_percentage_country, highest_percentage = country_percent()
    print(f'The country with highest percentage of earning morethan 50K is {highest_percentage_country} with {round(highest_percentage, 1)} %')

    most_popular_occupation, most_popular_occupation_count = india_occupation()
    print(f"The most popular occupation for those earning morethan 50K in India is {most_popular_occupation} with {most_popular_occupation_count} people.")

if __name__ == "__main__":
    main()

