import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def show_Ownership(data):
    """
    draw the ownership relation picture
    :param data:
    :return:
    """
    county_data = data[(data["Area Type"] == "County") & (data["Quarter"] == "Annual") & (
            data["Industry Name"] != "Total, All Industries")]
    State_data = data[(data["Area Type"] == "California - Statewide") & (data["Quarter"] == "Annual") & (
            data["Industry Name"] == "Total, All Industries")]
    US_data = data[(data["Area Type"] == "United States") & (data["Quarter"] == "Annual") & (
            data["Industry Name"] == "Total, All Industries")]
    State_data2 = data[(data["Area Type"] == "California - Statewide") & (data["Quarter"] == "Annual") & (
            data["Industry Name"] != "Total, All Industries")]
    State_data2_ownership_count = State_data2[["Industry Name", "Ownership"]].groupby(['Ownership']).count()

    # Plot the picture of Proportion of different Ownership in California and US
    plt.pie(State_data2_ownership_count["Industry Name"], labels=State_data2_ownership_count.index, autopct="%.2f%%",
            explode=[0.1, 0.1, 0.1, 0])
    plt.title('Proportion of different Ownership in California')
    US_data2 = data[(data["Area Type"] == "United States") & (data["Quarter"] == "Annual") & (
            data["Industry Name"] != "Total, All Industries")]
    US_data2_ownership_count = US_data2[["Industry Name", "Ownership"]].groupby(['Ownership']).count()
    plt.pie(US_data2_ownership_count["Industry Name"], labels=US_data2_ownership_count.index, autopct="%.2f%%",
            explode=[0.1, 0.1, 0.1, 0])
    plt.title('Proportion of different Ownership in the United States')

    # Average number of employment of each company with different ownership in California from 2004 to 2021
    county_ownership_employment_data = county_data[["Year", "Ownership", "Average Monthly Employment"]]
    county_ownership_employment_average = county_ownership_employment_data.groupby(['Ownership', 'Year']).mean()
    for Ownership in ['Federal Government', 'Local Government', 'Private', 'State Government']:
        item = county_ownership_employment_average.loc[Ownership, :]
        plt.plot(item, label=Ownership)
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.ylabel('number of employment')
    plt.xlabel('year')
    plt.title("Average number of employment of each company with different ownership in California from 2004 to 2021")
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.show()

    # Average number of employment in different ownership in California for whole state from 2004 to 2021
    State_ownership_employment_data = State_data[["Year", "Ownership", "Average Monthly Employment"]]
    State_ownership_employment_average = State_ownership_employment_data.groupby(['Ownership', 'Year']).mean()
    State_ownership_employment_total = State_ownership_employment_average.loc["Total Covered", :]
    State_ownership_employment_average = State_ownership_employment_average.drop(level='Ownership', index=["Total Covered"])
    for Ownership in ['Federal Government', 'Local Government', 'Private', 'State Government']:
        item = State_ownership_employment_average.loc[Ownership, :]
        plt.plot(item, label=Ownership)
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.ylabel('number of employment')
    plt.xlabel('year')
    plt.title("Average number of employment in different ownership in California for whole state from 2004 to 2021",
              x=1, y=1)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.show()

    # Average number of employment in different ownership in California for whole state from 2004 to 2021
    State_ownership_employment_average = State_ownership_employment_average.drop(level='Ownership', index=["Private"])
    for Ownership in ['Federal Government', 'Local Government', 'State Government']:
        item = State_ownership_employment_average.loc[Ownership, :]
        plt.plot(item, label=Ownership)
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.ylabel('number of employment')
    plt.xlabel('year')
    plt.title("Average number of employment in different ownership in California for whole state from 2004 to 2021",
              x=1, y=1)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.show()

    # Average number of employment in different ownership in US from 2004 to 2021
    US_ownership_employment_data = US_data[["Year", "Ownership", "Average Monthly Employment"]]
    US_ownership_employment_average = US_ownership_employment_data.groupby(['Ownership', 'Year']).mean()
    US_ownership_employment_total = US_ownership_employment_average.loc["Total Covered", :]
    US_ownership_employment_average = US_ownership_employment_average.drop(level='Ownership', index=["Total Covered"])
    for Ownership in ['Federal Government', 'Local Government', 'Private', 'State Government']:
        item = US_ownership_employment_average.loc[Ownership, :]
        plt.plot(item, label=Ownership)
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.ylabel('number of employment')
    plt.xlabel('year')
    plt.title("Average number of employment in different ownership in US from 2004 to 2021", x=1, y=1)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.show()

    # Average number of employment in different ownership in US from 2004 to 2021
    US_ownership_employment_average = US_ownership_employment_average.drop(level='Ownership', index=["Private"])
    for Ownership in ['Federal Government', 'Local Government', 'State Government']:
        item = US_ownership_employment_average.loc[Ownership, :]
        plt.plot(item, label=Ownership)
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.ylabel('number of employment')
    plt.xlabel('year')
    plt.title("Average number of employment in different ownership in US from 2004 to 2021", x=1, y=1)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.show()

    # California's share of employment of the United States
    State_ownership_employment_total.mean() / US_ownership_employment_total.mean()
    x = [int(State_ownership_employment_total.mean()),
         int(US_ownership_employment_total.mean() - State_ownership_employment_total.mean())]
    plt.pie(x, labels=["California", "Other states"], autopct="%.2f%%", explode=[0.1, 0])
    plt.title('California\'s share of employment of the United States')

    # The percentage of California's employment of the United States from 2004 to 2021
    plt.plot(State_ownership_employment_total / US_ownership_employment_total.mean())
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.title('The percentage of California\'s employment of the United States from 2004 to 2021')
    plt.ylabel('ratio')
    plt.xlabel('year')
    plt.show()

    # Average wages of each company with different ownership in California from 2004 to 2021
    State_ownership_Wages_data = State_data[["Year", "Ownership", "Average Weekly Wages"]]
    State_ownership_Wages_average = State_ownership_Wages_data.groupby(['Year', 'Ownership']).mean()
    US_ownership_Wages_data = US_data[["Year", "Ownership", "Average Weekly Wages"]]
    US_ownership_Wages_average = US_ownership_Wages_data.groupby(['Year', 'Ownership']).mean()
    State_ownership_Wages_average = State_ownership_Wages_average.swaplevel(i=1, j=0).sort_index()
    US_ownership_Wages_average = US_ownership_Wages_average.swaplevel(i=1, j=0).sort_index()
    State_ownership_Wages_total = State_ownership_Wages_average.loc["Total Covered", :]
    US_ownership_Wages_total = US_ownership_Wages_average.loc["Total Covered", :]
    for Ownership in ['Federal Government', 'Local Government', 'Private', 'State Government']:
        item = State_ownership_Wages_average.loc[Ownership, :]
        plt.plot(item, label=Ownership)
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.ylabel('Average Weekly Wages')
    plt.xlabel('year')
    plt.title("Average wages of each company with different ownership in California from 2004 to 2021")
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.show()

    # Average wages of each company with different ownership in the United States from 2004 to 2021
    for Ownership in ['Federal Government', 'Local Government', 'Private', 'State Government']:
        item = US_ownership_Wages_average.loc[Ownership, :]
        plt.plot(item, label=Ownership)
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.ylabel('Average Weekly Wages')
    plt.xlabel('year')
    plt.title("Average wages of each company with different ownership in the United States from 2004 to 2021")
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.show()

    # Comparison of average week wages between California and the United States from 2004 to 2001
    plt.plot(State_ownership_Wages_total, label='California Wages')
    plt.plot(US_ownership_Wages_total, label='US Wages')
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.title('Comparison of average week wages between California and the United States from 2004 to 2001')
    plt.ylabel('Average Weekly Wages')
    plt.xlabel('year')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv("Quarterly_Census_of_Employment_and_Wages__QCEW_.csv")
    show_Ownership(data)