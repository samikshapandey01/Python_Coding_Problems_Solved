import urllib.request
import json

#API only gives data for a particular location and one day. To get monthly data need to call API in a loop by passing day of the month 
final_dict={}
print("created,\t\t      applicable_date,   the_temp")
for i in range(1,30):
    temp_list=[] #temperature list to store temperatures for each day
    response = urllib.request.urlopen(f"https://www.metaweather.com/api/location/2487956/2020/02/{i}")
    data = response.read()
    json_dict = json.loads(data.decode("utf-8"))
    
    for entry in json_dict:
        if entry['created'].split('T')[0]==entry['applicable_date']:
            date=entry['applicable_date']
            temp_list.append(entry['the_temp'])
            print(f"{entry['created']},{entry['applicable_date']}:{entry['the_temp']}")
    min_temp, max_temp =min(temp_list), max(temp_list)
    
    average_temp=sum(temp_list)/len(temp_list)
    temp=[max_temp,min_temp,average_temp]
    final_dict[date]= temp #adding  value for that date as list of max,min and average temperature 

#writing the dictionary to json file
with open("temp_stats.json", "w") as json_file:
    json.dump(final_dict, json_file,indent=4)
