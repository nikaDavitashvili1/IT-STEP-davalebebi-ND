import csv

# davaleba 1

headers1 = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
new_List1 = []
def gather_survivors_in_list():
    with open('titanic.csv') as csvfile:
        titanic_dict_reader = csv.DictReader(csvfile, delimiter=',')
        for row in titanic_dict_reader:
            if row['Survived'] == '1':
                new_List1.append(row)
            else:
                continue

def make_survivors_file():
    with open('survived.csv', 'w', newline='') as survivorsFile:
        writer = csv.DictWriter(survivorsFile, fieldnames=headers1)
        writer.writeheader()
        writer.writerows(new_List1)

gather_survivors_in_list()
make_survivors_file()

# davaleba 2

def sort_organizations_by_employees():
    try:
        with open('organizations-100.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)
            sorted_data = sorted(data,
                                 key=lambda x: int(x['Number of employees']),
                                 reverse=True)

            with open('sorted_csv.csv', 'w', newline='', encoding='utf-8') as sorted_file:
                fieldnames = data[0].keys()
                csv_writer = csv.DictWriter(sorted_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(sorted_data)

    except FileNotFoundError:
        print("Error: organizations-100.csv file not found!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


sort_organizations_by_employees()

# davaleba 3

def create_ssl_companies_csv():
    try:
        with open('organizations-100.csv', 'r') as file:
            csv_reader = csv.DictReader(file)

            ssl_companies = []
            for row in csv_reader:
                if row['Website'].lower().startswith('https'):
                    ssl_company = {
                        'Organization Id': row['Organization Id'],
                        'Name': row['Name'],
                        'Website': row['Website'],
                        'Industry': row['Industry'],
                        'Number of employees': row['Number of employees']
                    }
                    ssl_companies.append(ssl_company)

            with open('ssl_companies.csv', 'w', newline='') as secured_file:
                fieldnames = ['Organization Id', 'Name', 'Website', 'Industry', 'Number of employees']
                csv_writer = csv.DictWriter(secured_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(ssl_companies)

    except FileNotFoundError:
        print("Error: organizations-100.csv file not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


create_ssl_companies_csv()