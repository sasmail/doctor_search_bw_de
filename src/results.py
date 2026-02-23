# TODO: write unit tests

def get_rows(parse_result):
    rows_from_results = parse_result.find_all('li', class_='resultrow')
    print(f"Found {len(rows_from_results)} doctors, with following names:")
    for row in rows_from_results:
        doc_in_row = row.find('dd', class_='name')
        doc_name = doc_in_row.find('dt').get_text(separator=' ', strip=True)
        print(doc_name)
    return rows_from_results

def build_doc_dict(rows_from_results):
    doctors_info = []
    for doctor in rows_from_results:
        info_per_doctor = {}


        # TODO: refactor as addresses, telephone and mail structures differ from doctor to doctor --> check if it works
        # name + address
        doc_primary_details_result = list(doctor.find('p', class_="anschrift-arzt").stripped_strings)
        doc_name = doc_primary_details_result[0] if len(doc_primary_details_result) > 0 else ''
        doc_street = doc_primary_details_result[1] if len(doc_primary_details_result) > 1 else ''
        doc_postal = doc_primary_details_result[2] if len(doc_primary_details_result) > 2 else ''
        doc_city_district = doc_primary_details_result[3] if len(doc_primary_details_result) > 3 else ''
        doc_town = doc_primary_details_result[4] if len(doc_primary_details_result) > 4 else ''

        # telephone
        contact_text = doctor.find('dd', class_='adresse').find_next('dl').find_next('dd').get_text()
        contact_fields = {"Telefon:": "", "Telefax:": "", "Mobil:": ""}

        for line in contact_text.split('\n'):
            for key in contact_fields:
                if key in line:
                    contact_fields[key] = line.split(key)[1].strip()

        doc_telephone = contact_fields["Telefon:"]
        doc_telefax = contact_fields["Telefax:"]
        doc_mobile = contact_fields["Mobil:"]


        # mail
        doc_mail_result = doctor.find('a', class_='obfuscatedEmail')
        doc_mail = doc_mail_result.get_text() if doc_mail_result is not None else ''


        # filling dict
        info_per_doctor['name'] = doc_name
        info_per_doctor['street'] = doc_street
        info_per_doctor['postal'] = doc_postal
        info_per_doctor['city'] = doc_city_district
        info_per_doctor['town'] = doc_town
        info_per_doctor['telephone'] = doc_telephone
        info_per_doctor['telefax'] = doc_telefax
        info_per_doctor['mobile'] = doc_mobile
        info_per_doctor['mail'] = doc_mail

        doctors_info.append(info_per_doctor)

    return doctors_info