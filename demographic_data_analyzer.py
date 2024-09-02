import numpy as np

import pandas as pd

df=pd.read_csv("adult.data")

df.columns=['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship',
'race','sex','capital-gain','capital-loss','hours-per-week','native-country','salary']

total_num = len(df)

'''print(df.columns)

print(df.head())'''


#function to find race_count_value and print it as pandas series
def race_count():
    
    race_count_result = df['race'].value_counts()
    return race_count_result


#function to find average age of men
def avg_men_age():
    
    avg_age_of_men = df[df['sex'] == ' Male']['age'].mean()
    return avg_age_of_men


#function to find percentage of people who have bachelors degree
def bachelor_percent():

    count_bachelor = df[df['education'] == ' Bachelors']['education'].count()

    percentage_of_bachelor = (count_bachelor / total_num) * 100

    return percentage_of_bachelor


#function to find people who have advanced education and earn morethan 50k
def adv_edu_morethan_50k_percent():

    adv_education = df[df['education'].isin([' Bachelors' , ' Masters', ' Doctorate'])]

    earning_morethan_50k = adv_education[adv_education['salary'] == ' >50K' ]

    count_morethan_50 = earning_morethan_50k['education'].count()

    percentage_of_adv_education = (count_morethan_50 / total_num) * 100

    return percentage_of_adv_education


#function to find people who earn morethan 50 without advanced education
def non_adv_edu_morethan_50k_percent():

    not_adv_education = df[~df['education'].isin([' Bachelors' , ' Masters', ' Doctorate'])]

    non_adv_edu_earn_morethan_50k = not_adv_education[not_adv_education['salary'] == ' >50K' ]

    count_morethan_50 = non_adv_edu_earn_morethan_50k['education'].count()

    percentage_of_non_adv_education = (count_morethan_50 / total_num) * 100

    return percentage_of_non_adv_education


#function to find minimum worktime per week
def min_worktime():

    min_worktime_per_week = df['hours-per-week'].min()

    return min_worktime_per_week


#function to find people who have min worktime but earn morethan 50k
def min_worktime_morethan50_percent():
    
    min_worktime_per_week = df['hours-per-week'].min()

    min_time_df = df[df['hours-per-week'] == min_worktime_per_week]

    earn_morethan50_with_min_work = min_time_df[min_time_df['salary'] == ' >50K']

    count_50_with_min = earn_morethan50_with_min_work['hours-per-week'].count()

    percentage_of_min_with_50k = (count_50_with_min / total_num) * 100

    return percentage_of_min_with_50k


#function to find the country and percentage of people earn morethan 50k
def country_percent():
    
    salary_morethan_50k = df[df['salary'] == ' >50K']

    grp = df.groupby(['native-country'])
    total_people = grp.size()
    earn_morethan_50k = salary_morethan_50k.groupby('native-country').size()

    percent_each_country = (earn_morethan_50k / total_people) * 100

    highest_percentage_country = percent_each_country.idxmax()
    highest_percentage = percent_each_country.max()
    
    return highest_percentage_country, highest_percentage



#function to find occupation which most people do who earn morethan 50k in india
def india_occupation():
    
    india_df = df[df['native-country'] == ' India']

    ind_sal_50k = india_df[india_df['salary'] == ' >50K']

    occ_grp_50kind = ind_sal_50k.groupby(['occupation'])

    occ_count = occ_grp_50kind.size()

    most_popular_occupation = occ_count.idxmax()
    most_popular_occupation_count = occ_count.max()

    return most_popular_occupation, most_popular_occupation_count