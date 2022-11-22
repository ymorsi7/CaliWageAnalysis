

#california vs USA (area name; outputs of montly employment and wages

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/ymorsi/Desktop/Quarterly_Census_of_Employment_and_Wages__QCEW_.csv')




AvgMontlyEmployment = df.groupby("Area Type")["Average Monthly Employment"].apply(list)

caliAME = np.mean(AvgMontlyEmployment[0])
countyAME = np.mean(AvgMontlyEmployment[1])
usaAME = np.mean(AvgMontlyEmployment[2])

monthlyEmpList = [caliAME, countyAME, usaAME]
monthlyEmpTitles = ["California", "County", "USA"]

fig = plt.figure(figsize = (10, 5))
plt.bar(monthlyEmpTitles, monthlyEmpList, color ='navy', width = 0.4)

plt.xlabel("Area Type")
plt.ylabel("Avg Monthly Employment")
plt.title("Avg Monthly Employment v. Area Type")
plt.show()

AvgWeeklyWages = df.groupby("Area Type")["Average Weekly Wages"].apply(list)


caliAWW = np.mean(AvgWeeklyWages[0])
countyAWW = np.mean(AvgWeeklyWages[1])
usaAWW = np.mean(AvgWeeklyWages[2])

weeklyWagesList = [caliAWW, countyAWW, usaAWW]
weeklyWagesTitles = ["California", "County", "USA"]

fig = plt.figure(figsize = (10, 5))
plt.bar(weeklyWagesTitles, weeklyWagesList, color ='maroon', width = 0.4)






areaNameMonthly = df.groupby("Area Name")["Average Monthly Employment"].apply(list)

caliEmp = areaNameMonthly[5]
laEmp = areaNameMonthly[19]
sdEmp = areaNameMonthly[37]
sfEmp = areaNameMonthly[38]
usaEmp = areaNameMonthly[56]



areaNameWeekly = df.groupby("Area Name")["Average Weekly Wages"].apply(list)


caliWages = areaNameWeekly[5]
laEmpWages = areaNameWeekly[19]
sdEmpWages = areaNameWeekly[37]
sfEmpWages = areaNameWeekly[38]
usaEmpWages = areaNameWeekly[56]












plt.xlabel("Area Type")
plt.ylabel("Avg Weekly Wages")
plt.title("Avg Weekly Wages v. Area Type")
plt.show()

countyOwnership = df[(df["Area Type"]=="County")& (df["Quarter"]=="Annual") & (df["Industry Name"]!="Total, All Industries")][["Industry Name", "Ownership"]].groupby(['Ownership']).count()
plt.pie(countyOwnership["Industry Name"],labels = countyOwnership.index,autopct="%.2f%%")
plt.title('County Ownership Comparison')




usOwnership = df[(df["Area Type"]=="United States")& (df["Quarter"]=="Annual") & (df["Industry Name"]!="Total, All Industries")][["Industry Name", "Ownership"]].groupby(['Ownership']).count()
plt.pie(usOwnership["Industry Name"],labels=usOwnership.index,autopct="%.2f%%")
plt.title('United States Ownership Comparison')




caOwnership = df[(df["Area Type"]=="California - Statewide")& (df["Quarter"]=="Annual") & (df["Industry Name"]!="Total, All Industries")][["Industry Name", "Ownership"]].groupby(['Ownership']).count()
plt.pie(caOwnership["Industry Name"],labels=caOwnership.index,autopct="%.2f%%")
plt.title('California Ownership Comparison')

































