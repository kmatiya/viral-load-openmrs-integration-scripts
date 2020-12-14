import pandas as pd
import numpy as np
import requests
import json
import datetime

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from requests.auth import HTTPBasicAuth

vl_samples_df = pd.read_excel('./Zalewa.xlsx', header=0)
upper_neno_df = pd.read_excel('./patient_identifiers_emr.xlsx', header=0)
encounterUrl = "http://lisungwi.pih-emr.org:8100/openmrs/ws/rest/v1/encounter"
username = "openmrs"
pwd = "openmrs"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def format_patient_identifier(facility_code, patient_number):
    return facility_code + "-" + patient_number


def format_emr_patient_identifier(facility_code, patient_number):
    return facility_code + " " + patient_number


def remove_leading_zeroes(identifier):
    if identifier == 'Not Applicable':
        return identifier
    if len(identifier) == 1:
        return identifier
    first_letter = identifier[0]
    second_letter = identifier[1]
    third_letter = identifier[2]
    fourth_letter = identifier[3]
    try:
        if fourth_letter == '0' and third_letter == '0' and first_letter == '0' and second_letter == '0':
            identifier = identifier[4:]
            return identifier
        if third_letter == '0' and first_letter == '0' and second_letter == '0':
            identifier = identifier[3:]
            return identifier
        if first_letter == '0' and second_letter == '0':
            identifier = identifier[2:]
            return identifier
        if first_letter == '0':
            identifier = identifier[1:]
            return identifier
        return identifier
    except:
        return identifier


def extract_patient_identifier(unformatted_patient_id):
    try:
        if unformatted_patient_id == 'Not Applicable':
            return unformatted_patient_id
        facility_code = unformatted_patient_id[0:4]  # first four characters

        patient_identifier = remove_leading_zeroes(unformatted_patient_id[5:])
        if facility_code == '3704':
            return str(format_patient_identifier("3704", patient_identifier))
        if facility_code == '3701':
            return str(format_patient_identifier("3701", patient_identifier))
        if facility_code == '3714':
            return str(format_patient_identifier("3714", patient_identifier))
        if facility_code == '3702':
            return str(format_patient_identifier("3702", patient_identifier))
        if facility_code == '3703':
            return str(format_patient_identifier("3703", patient_identifier))
        if facility_code == '3705':
            return str(format_patient_identifier("3705", patient_identifier))
        if facility_code == '3706':
            return str(format_patient_identifier("3706", patient_identifier))
        if facility_code == '3707':
            return str(format_patient_identifier("3707", patient_identifier))
        if facility_code == '3708':
            return str(format_patient_identifier("3708", patient_identifier))
        if facility_code == '3709':
            return str(format_patient_identifier("3709", patient_identifier))
        if facility_code == '3710':
            return str(format_patient_identifier("3710", patient_identifier))
        if facility_code == '3712':
            return str(format_patient_identifier("3712", patient_identifier))
        if facility_code == '3711':
            return str(format_patient_identifier("3711", patient_identifier))
        if facility_code == '3713':
            return str(format_patient_identifier("3713", patient_identifier))

        return "Not Applicable"
    except:
        return "Not Applicable"


def generate_emr_patient_identifier(unformatted_patient_id):
    try:
        if unformatted_patient_id == 'Not Applicable':
            return unformatted_patient_id
        facility_code = unformatted_patient_id[0:4]  # first four characters

        patient_identifier = remove_leading_zeroes(unformatted_patient_id[5:])
        if facility_code == '3704':
            return str(format_emr_patient_identifier("LWAN", patient_identifier))
        if facility_code == '3701':
            return str(format_emr_patient_identifier("CFGA", patient_identifier))
        if facility_code == '3714':
            return str(format_emr_patient_identifier("DAM", patient_identifier))
        if facility_code == '3702':
            return str(format_emr_patient_identifier("LGWE", patient_identifier))
        if facility_code == '3703':
            return str(format_emr_patient_identifier("LSI", patient_identifier))
        if facility_code == '3705':
            return str(format_emr_patient_identifier("MGT", patient_identifier))
        if facility_code == '3706':
            return str(format_emr_patient_identifier("MTDN", patient_identifier))
        if facility_code == '3707':
            return str(format_emr_patient_identifier("MTE", patient_identifier))
        if facility_code == '3708':
            return str(format_emr_patient_identifier("MIHC", patient_identifier))
        if facility_code == '3709':
            return str(format_emr_patient_identifier("NNO", patient_identifier))
        if facility_code == '3710':
            return str(format_emr_patient_identifier("NOP", patient_identifier))
        if facility_code == '3712':
            return str(format_emr_patient_identifier("NKA", patient_identifier))
        if facility_code == '3711':
            return str(format_emr_patient_identifier("NSM", patient_identifier))
        if facility_code == '3713':
            return str(format_emr_patient_identifier("ZLA", patient_identifier))

        return "Not Applicable"
    except:
        return "Not Applicable"


def validate_facility_and_identifier(facility, identifier):
    try:
        facility_str = str(facility)
        identifier = str(identifier)
        if identifier == 'Not Applicable':
            return False
        if facility_str.lower().startswith("dambe") and identifier.startswith("DAM"):
            return True
        if facility_str.lower().startswith("nsambe") and identifier.startswith("NSM"):
            return True
        if facility_str.lower().startswith("neno parish") and identifier.startswith("NOP"):
            return True
        if facility_str.lower().startswith("nkula") and identifier.startswith("NKA"):
            return True
        if facility_str.lower().startswith("zalewa") and identifier.startswith("ZLA"):
            return True
        if facility_str.lower().startswith("chifunga") and identifier.startswith("CFGA"):
            return True
        if facility_str.lower().startswith("lisungwi") and identifier.startswith("LSI"):
            return True
        if facility_str.lower().startswith("matope") and identifier.startswith("MTE"):
            return True
        if facility_str.lower().startswith("midzemba") and identifier.startswith("MIHC"):
            return True
        if facility_str.lower().startswith("ligowe") and identifier.startswith("LGWE"):
            return True
        if facility_str.lower().startswith("luwani") and identifier.startswith("LWAN"):
            return True
        if facility_str.lower().startswith("magareta") and identifier.startswith("MGT"):
            return True
        if facility_str.lower().startswith("matandani") and identifier.startswith("MTDN"):
            return True
        if facility_str.lower().startswith("neno district") and identifier.startswith("NNO"):
            return True
        return False
    except:
        return False


def validate_payload(date_received, facility, identifier, result):
    facility_identifier_result = validate_facility_and_identifier(facility, identifier)
    if not facility_identifier_result:
        return False
    return True


def get_encounter_location_uuid(location):
    location_str = str(location)
    if location_str.lower().startswith("dambe"):
        return '976dcd06-c40e-4e2e-a0de-35a54c7a52ef'
    if location_str.lower().startswith("nsambe"):
        return '0d416830-5ab4-11e0-870c-9f6107fee88e'
    if location_str.lower().startswith("neno parish"):
        return '0d41505c-5ab4-11e0-870c-9f6107fee88e'
    if location_str.lower().startswith("nkula"):
        return '0d4169b6-5ab4-11e0-870c-9f6107fee88e'
    if location_str.lower().startswith("zalewa"):
        return '0d417fd2-5ab4-11e0-870c-9f6107fee88e'
    if location_str.lower().startswith("chifunga"):
        return '0d4166a0-5ab4-11e0-870c-9f6107fee88e'
    if location_str.lower().startswith("lisungwi"):
        return '0d416376-5ab4-11e0-870c-9f6107fee88e'
    if location_str.lower().startswith("matope"):
        return '0d416b3c-5ab4-11e0-870c-9f6107fee88e'
    if location_str.lower().startswith("midzemba"):
        return '0d4182e8-5ab4-11e0-870c-9f6107fee88e'
    if location_str.lower().startswith("ligowe"):
        return '0d417e38-5ab4-11e0-870c-9f6107fee88e'
    if location_str.lower().startswith("luwani"):
        return '0d416506-5ab4-11e0-870c-9f6107fee88e'
    if location_str.lower().startswith("magareta"):
        return '0d414eae-5ab4-11e0-870c-9f6107fee88e'
    if location_str.lower().startswith("matandani"):
        return '0d415200-5ab4-11e0-870c-9f6107fee88e'
    if location_str.lower().startswith("neno district"):
        return '0d414ce2-5ab4-11e0-870c-9f6107fee88e'
    return False


def get_reason_for_testing_uuid(reason):
    reason_str = str(reason)
    if reason_str.lower().startswith("routine"):
        return 'e0821812-955d-11e7-abc4-cec278b6b50a'
    if reason_str.lower().startswith("target"):
        return 'e0821df8-955d-11e7-abc4-cec278b6b50a'
    if reason_str.lower().startswith("confirm"):
        return '65590f06-977f-11e1-8993-905e29aff6c1'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # DataFrame for target_patients.xls
    print(vl_samples_df.head(20))
    vl_samples_df['identifier'] = vl_samples_df['ART Clinic No'].apply(generate_emr_patient_identifier)
    vl_samples_df['ART Clinic No'] = vl_samples_df['ART Clinic No'].apply(extract_patient_identifier)
    final_df = pd.merge(vl_samples_df, upper_neno_df, on='identifier', how='inner')

    viral_load_par = {
        'patient': 'c4eeeae6-2695-102d-b4c2-001d929acb54',
        'fromdate': '2019-05-29',
        'todate': '2019-05-29',
        'encounterType': '9959A261-2122-4AE1-A89D-1CA444B712EA'
    }
    encounter_result = requests.get(encounterUrl, params=viral_load_par,
                                    auth=HTTPBasicAuth(username=username, password=pwd))
    # final_df["Collection Date"] = pd.to_datetime(final_df["Collection Date"])
    final_df["Collection Date"] = final_df["Collection Date"].dt.date
    my_sum = 0
    for index, row in final_df.iterrows():
        # Check if payload is valid
        payload_valid = validate_payload(row['Collection Date'], row['Facility Name'], row['identifier'], row['Result'])
        start_date = row['Collection Date']
        end_date = row['Collection Date'] + datetime.timedelta(days=1)
        if payload_valid:
            encounter_par = {
                'patient': row['uuid'],
                'fromdate': start_date,
                'todate': end_date,
                'encounterType': '664b8650-977f-11e1-8993-905e29aff6c1'
            }
            encounter_result = requests.get(encounterUrl, params=encounter_par,
                                            auth=HTTPBasicAuth(username=username, password=pwd))

            viral_load_par = {
                'patient': row['uuid'],
                'fromdate': start_date,
                'todate': end_date,
                'encounterType': '9959A261-2122-4AE1-A89D-1CA444B712EA'
            }
            viral_load_encounter_result = requests.get(encounterUrl, params=viral_load_par,
                                                       auth=HTTPBasicAuth(username=username, password=pwd))

            data = json.loads(encounter_result.text)
            data1 = json.loads(viral_load_encounter_result.text)
            len_of_data = len(data['results'])
            len_of_data_1 = len(data1['results'])
            if (len_of_data == 1 or len_of_data == 0) and len_of_data_1 == 0:
                patient_uuid = row['uuid']
                encounter_date = row["Collection Date"]
                encounter_location = get_encounter_location_uuid(row['Facility Name'])
                reason_for_testing = get_reason_for_testing_uuid(row['Reason for Test'])
                result = row['Result']
                print(result)
                if int(row['Result']) == 1:
                    ldl_encounter = {
                        "patient": patient_uuid,
                        "encounterType": "9959A261-2122-4AE1-A89D-1CA444B712EA",
                        "encounterDatetime": str(encounter_date),
                        "location": encounter_location,
                        "obs": [
                            {
                                "concept": "83931c6d-0e5a-4302-b8ce-a31175b6475e",
                                "groupMembers": [
                                    {
                                        "concept": "f792f2f9-9c24-4d6e-98fd-caffa8f2383f",
                                        "comment": "vl-form^vl-test-set^vl-bled",
                                        "value": "655e2f90-977f-11e1-8993-905e29aff6c1"
                                    },
                                    {
                                        "concept": "164126AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
                                        "comment": "vl-form^vl-test-set^vl-reason-for-testing",
                                        "value": reason_for_testing
                                    },
                                    {
                                        "concept": "6fc0ab50-9492-11e7-abc4-cec278b6b50a",
                                        "comment": "vl-form^vl-test-set^vl-lab-location",
                                        "value": "e0820552-955d-11e7-abc4-cec278b6b50a"
                                    },
                                    {
                                        "concept": "e97b36a2-16f5-11e6-b6ba-3e1d05defe78",
                                        "comment": "vl-form^vl-test-set^vl-numeric",
                                        "value": '655e2f90-977f-11e1-8993-905e29aff6c1'
                                    }
                                ]
                            }
                        ]
                    }
                    new_ldl_encounter = requests.post(encounterUrl, json=ldl_encounter,
                                                      auth=HTTPBasicAuth(username=username, password=pwd))
                    print("LDL encounters\n")
                    print(new_ldl_encounter.text)
                    final_df['LDL Encounter Result'] = new_ldl_encounter.text

                if int(row['Result']) == 839 or int(row['Result']) == 40:
                    less_than_limit_encounter = {
                        "patient": patient_uuid,
                        "encounterType": "9959A261-2122-4AE1-A89D-1CA444B712EA",
                        "encounterDatetime": str(encounter_date),
                        "location": encounter_location,
                        "obs": [
                            {
                                "concept": "83931c6d-0e5a-4302-b8ce-a31175b6475e",
                                "groupMembers": [
                                    {
                                        "concept": "f792f2f9-9c24-4d6e-98fd-caffa8f2383f",
                                        "comment": "vl-form^vl-test-set^vl-bled",
                                        "value": "655e2f90-977f-11e1-8993-905e29aff6c1"
                                    },
                                    {
                                        "concept": "164126AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
                                        "comment": "vl-form^vl-test-set^vl-reason-for-testing",
                                        "value": reason_for_testing
                                    },
                                    {
                                        "concept": "6fc0ab50-9492-11e7-abc4-cec278b6b50a",
                                        "comment": "vl-form^vl-test-set^vl-lab-location",
                                        "value": "e0820552-955d-11e7-abc4-cec278b6b50a"
                                    },
                                    {
                                        "concept": '69e87644-5562-11e9-8647-d663bd873d93',
                                        "comment": "vl-form^vl-test-set^vl-numeric",
                                        "value": int(row['Result'])
                                    }
                                ]
                            }
                        ]
                    }
                    new_less_than_limit_encounter = requests.post(encounterUrl, json=less_than_limit_encounter,
                                                                  auth=HTTPBasicAuth(username=username, password=pwd))

                    print(new_less_than_limit_encounter.text)
                    final_df['less than Limit Encounters Result'] = new_less_than_limit_encounter.text

                if int(row['Result']) != 839 and int(row['Result']) != 40 and int(row['Result']) != 1:
                    high_viral_load_encounter = {
                        "patient": patient_uuid,
                        "encounterType": "9959A261-2122-4AE1-A89D-1CA444B712EA",
                        "encounterDatetime": str(encounter_date),
                        "location": encounter_location,
                        "obs": [
                            {
                                "concept": "83931c6d-0e5a-4302-b8ce-a31175b6475e",
                                "groupMembers": [
                                    {
                                        "concept": "f792f2f9-9c24-4d6e-98fd-caffa8f2383f",
                                        "comment": "vl-form^vl-test-set^vl-bled",
                                        "value": "655e2f90-977f-11e1-8993-905e29aff6c1"
                                    },
                                    {
                                        "concept": "164126AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
                                        "comment": "vl-form^vl-test-set^vl-reason-for-testing",
                                        "value": reason_for_testing
                                    },
                                    {
                                        "concept": "6fc0ab50-9492-11e7-abc4-cec278b6b50a",
                                        "comment": "vl-form^vl-test-set^vl-lab-location",
                                        "value": "e0820552-955d-11e7-abc4-cec278b6b50a"
                                    },
                                    {
                                        "concept": '654a7694-977f-11e1-8993-905e29aff6c1',
                                        "comment": "vl-form^vl-test-set^vl-numeric",
                                        "value": int(row['Result'])
                                    }
                                ]
                            }
                        ]
                    }
                    new_high_viral_load_encounter = requests.post(encounterUrl, json=high_viral_load_encounter,
                                                                  auth=HTTPBasicAuth(username=username,
                                                                                     password=pwd))

                    print(new_high_viral_load_encounter.text)
                    final_df['High Viral Load Encounter Result'] = new_high_viral_load_encounter.text
    final_df.to_csv("viral encounter result.csv", index=False)
    # vl_samples_df.to_csv("upper_neno_updated.csv", index=False)
    print("Viral load excel file generated successfully")
    # print(upper_neno_df.head(5))
    # print(vl_samples_df.head(1000))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
