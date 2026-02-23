import csv
import os
from openpyxl import Workbook

def write_to_csv(all_doctors, user_path):
    # TODO: implement
    keys = all_doctors[0].keys()

    file_path = os.path.join(user_path, 'all_doctors.csv')

    with open(file_path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_doctors)

    return output_file, file_path

def write_to_xlsx(all_doctors, user_path):
    # 1. preparing workbook
    wb = Workbook()
    ws = wb.active
    ws.title = 'All Doctors'
    file_path = os.path.join(user_path, 'all_doctors.xlsx')

    # 2. generating headers
    keys = all_doctors[0].keys()
    ws.append(list(keys))

    for doctor in all_doctors:
        ws.append(list(doctor.values()))

    wb.save(file_path)

def export_data(all_doctors, user_path):
    write_to_csv(all_doctors, user_path)

    write_to_xlsx(all_doctors, user_path)