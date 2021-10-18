import pandas as pd

city_df=pd.read_csv('cities.csv')

#Data Cleanup
#As there are two columns with area with 2 units(square miles and km square), looking at data values in sq mi column has less nulls so we will be using that columns
#Checking if for any null in sq mi we have data in km square, if so then converting and populating missing column from another column.
city_df.loc[city_df['area_total_sq_mi'].isnull() & city_df['area_total_km2'].notnull(),['area_total_sq_mi']]=city_df['area_total_km2']/2.59

city_df.loc[city_df['area_water_sq_mi'].isnull() & city_df['area_water_km2'].notnull(),['area_water_sq_mi']]=city_df['area_water_km2']/2.59

# a. The largest and smallest cities in terms of total area using Area_total_sq_mi column
sm_city=city_df.loc[city_df['area_total_sq_mi']==city_df['area_total_sq_mi'].min(),['city','area_total_sq_mi']]
print("\nSmallest City:",sm_city.iloc[0,0],",Area_total_sq_mi:",sm_city.iloc[0,1])

lr_city=city_df.loc[city_df['area_total_sq_mi']==city_df['area_total_sq_mi'].max(),['city','area_total_sq_mi']]
print("Largest City:",lr_city.iloc[0,0],",Area_total_sq_mi:",lr_city.iloc[0,1])


# b.The top 10 cities in terms of elevation.
#USing column elevation_ft and sorting dataframe in descending order on this column
sort_by_elevationft = city_df.sort_values('elevation_ft',ascending=False)
print("\nTop 10 cities in terms of elevation:")
#printing top 10 rows from sorted dataframe above
print(sort_by_elevationft[['city','elevation_ft']].head(10).to_string(index=False))


#c.Average land area, water area and total area in sq mi

print("\nAverage land area in sqmi:",round(city_df[['area_land_sq_mi']].mean()[0],2))

print("\nAverage water area in sqmi:",round(city_df[['area_water_sq_mi']].mean()[0],2))

print("\nAverage total area in sqmi:",round(city_df[['area_total_sq_mi']].mean()[0],2))

#d.Cities between latitude of 36 and 38 and longitude of -120 and -116
print("\nCities between latitude of 36 and 38 and longitude of -120 and -116:\n")
print(city_df.loc[(city_df['longd'] >=-120) & (city_df['longd'] <=-116) & (city_df['latd']>=36) & (city_df['latd']<=38),['city','latd','longd']].to_string(index=False))

#e.Cities with total population within interquartile range

desc=city_df['population_total'].describe()
print("\n25th percentile of total population:",desc[4])
print("75th percentile of total population:",desc[6])
pd.set_option("display.max_rows", None, "display.max_columns", None)

#Within IQR means , within 25th and 75th percentile
print("\nCities with total population within interquartile range:\n")
print(city_df.loc[(city_df['population_total'] >= desc[4]) & (city_df['population_total'] <= desc[6]) ,['city','population_total']].to_string(index=False))