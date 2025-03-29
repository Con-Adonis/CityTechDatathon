import requests
import json
import matplotlib

# Fetching data from the API
response = requests.get("https://data.cityofnewyork.us/resource/jz4z-kudi.json?$query=SELECT%0A%20%20%60ticket_number%60%2C%0A%20%20%60violation_date%60%2C%0A%20%20%60violation_time%60%2C%0A%20%20%60issuing_agency%60%2C%0A%20%20%60respondent_first_name%60%2C%0A%20%20%60respondent_last_name%60%2C%0A%20%20%60balance_due%60%2C%0A%20%20%60violation_location_borough%60%2C%0A%20%20%60violation_location_block_no%60%2C%0A%20%20%60violation_location_lot_no%60%2C%0A%20%20%60violation_location_house%60%2C%0A%20%20%60violation_location_street_name%60%2C%0A%20%20%60violation_location_floor%60%2C%0A%20%20%60violation_location_city%60%2C%0A%20%20%60violation_location_zip_code%60%2C%0A%20%20%60violation_location_state_name%60%2C%0A%20%20%60respondent_address_borough%60%2C%0A%20%20%60respondent_address_house%60%2C%0A%20%20%60respondent_address_street_name%60%2C%0A%20%20%60respondent_address_city%60%2C%0A%20%20%60respondent_address_zip_code%60%2C%0A%20%20%60respondent_address_state_name%60%2C%0A%20%20%60hearing_status%60%2C%0A%20%20%60hearing_result%60%2C%0A%20%20%60scheduled_hearing_location%60%2C%0A%20%20%60hearing_date%60%2C%0A%20%20%60hearing_time%60%2C%0A%20%20%60decision_location_borough%60%2C%0A%20%20%60decision_date%60%2C%0A%20%20%60total_violation_amount%60%2C%0A%20%20%60violation_details%60%2C%0A%20%20%60date_judgment_docketed%60%2C%0A%20%20%60respondent_address_or_facility_number_for_fdny_and_dob_tickets%60%2C%0A%20%20%60penalty_imposed%60%2C%0A%20%20%60paid_amount%60%2C%0A%20%20%60additional_penalties_or_late_fees%60%2C%0A%20%20%60compliance_status%60%2C%0A%20%20%60violation_description%60%2C%0A%20%20%60charge_1_code%60%2C%0A%20%20%60charge_1_code_section%60%2C%0A%20%20%60charge_1_code_description%60%2C%0A%20%20%60charge_1_infraction_amount%60%2C%0A%20%20%60charge_2_code%60%2C%0A%20%20%60charge_2_code_section%60%2C%0A%20%20%60charge_2_code_description%60%2C%0A%20%20%60charge_2_infraction_amount%60%2C%0A%20%20%60charge_3_code%60%2C%0A%20%20%60charge_3_code_section%60%2C%0A%20%20%60charge_3_code_description%60%2C%0A%20%20%60charge_3_infraction_amount%60%2C%0A%20%20%60charge_4_code%60%2C%0A%20%20%60charge_4_code_section%60%2C%0A%20%20%60charge_4_code_description%60%2C%0A%20%20%60charge_4_infraction_amount%60%2C%0A%20%20%60charge_5_code%60%2C%0A%20%20%60charge_5_code_section%60%2C%0A%20%20%60charge_5_code_description%60%2C%0A%20%20%60charge_5_infraction_amount%60%2C%0A%20%20%60charge_6_code%60%2C%0A%20%20%60charge_6_code_section%60%2C%0A%20%20%60charge_6_code_description%60%2C%0A%20%20%60charge_6_infraction_amount%60%2C%0A%20%20%60charge_7_code%60%2C%0A%20%20%60charge_7_code_section%60%2C%0A%20%20%60charge_7_code_description%60%2C%0A%20%20%60charge_7_infraction_amount%60%2C%0A%20%20%60charge_8_code%60%2C%0A%20%20%60charge_8_code_section%60%2C%0A%20%20%60charge_8_code_description%60%2C%0A%20%20%60charge_8_infraction_amount%60%2C%0A%20%20%60charge_9_code%60%2C%0A%20%20%60charge_9_code_section%60%2C%0A%20%20%60charge_9_code_description%60%2C%0A%20%20%60charge_9_infraction_amount%60%2C%0A%20%20%60charge_10_code%60%2C%0A%20%20%60charge_10_code_section%60%2C%0A%20%20%60charge_10_code_description%60%2C%0A%20%20%60charge_10_infraction_amount%60%0AWHERE%0A%20%20caseless_ne(%60violation_location_borough%60%2C%20%22NOT%20NYC%22)%0A%20%20AND%20caseless_ne(%60charge_1_code%60%2C%20%22N%22)%0AORDER%20BY%20%60violation_date%60%20DESC%20NULL%20FIRST")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Try to parse the JSON data
    try:
        data = response.json()
        print("Data fetched successfully!")
    except ValueError:
        print("Error: Unable to parse JSON data.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

fullText = (json.dumps(data)).split("}, {")

#Dictionaries of burrows
MannDict = {}
BrookDict = {}
BrxDict = {}
QnsDict = {}
SIDict = {}

for case in fullText:
    #splits full text into individual cases x, only counts if cases have both city and charge code
    lineSplitted = case.split('", "')
    tempList = []
    if 'violation_location_borough' in case and 'charge_1_code' in case:
        print('\nNew Case\n')
    else:
        continue

    ##splits cases into individual lines based on if it has the corret start
    for line in lineSplitted:
        if 'violation_location_borough' in line or 'charge_1_code"' in line:
            tempList.append(line[-4:])
            print(line, '\n')
    
    print(tempList)

    if tempList[0] == 'KLYN':
        print('Brooklyn')
        if tempList[1] in BrookDict:
            BrookDict[tempList[1]] += 1
        else:
            BrookDict[tempList[1]] = 1
        
    #if tempList[0] == 'RONX':
        #if tempList[1] in BrxDict:
            #BrxDict.tempList[1] += 1

    #if tempList[0] == 'EENS':
       # if tempList[1] in BrxDict:
            #BrxDict.tempList[1] += 1

    ##if tempList[0] == 'TTAN':
        #if tempList[1] in MannDict:
            # MannDict.tempList[1] += 1
            
    print(MannDict)