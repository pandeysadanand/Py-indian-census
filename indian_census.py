import csv


class IndiaCensus:

    @staticmethod
    def read_indian_census_csv_file():
        """
            Reading indian census csv file and displaying it
        :return: None
        """
        with open("indian_census_data.csv", newline='') as f:
            reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
            reader_enum = enumerate(reader)
            for count, values in enumerate(reader):
                if count < 50:
                    print(count, values)
            print("-----------------------------------------------------\n")

    @staticmethod
    def write_csv_file():
        """
            Writing to the indian census file
        :return: None
        """
        IndiaCensus.read_indian_census_csv_file()
        with open("indian_census_data.csv", "a", newline="") as f:
            write_object = csv.writer(f)
            number_of_record = int(input("Number of record want to add: "))  # read
            for i in range(number_of_record):
                state = input("Enter name of state: ")
                population = int(input("enter total population: "))
                area_in_sq_km = int(input("enter total area:"))
                density_per_km = int(input("Enter density: "))
                state_code = input("Enter state code: ")
                write_object.writerow([state, population, area_in_sq_km, density_per_km, state_code])
        print("Total {} record added successfully".format(number_of_record))
        print("-----------------------------------------\n")

    @staticmethod
    def update_record():
        """
            Updating indian census csv file
        :return: None
        """
        with open("indian_census_data.csv", "r") as file_reader:
            reader = csv.reader(file_reader)
            found = 0  # False
            modified_indian_census_list = []
            state = input("Enter state to update record: ")
            for row in reader:
                if row[0] == state:
                    row[1] = int(input("Enter updated population : "))
                    print(row)
                    found = 1
                modified_indian_census_list.append(row)
        if found == 0:
            print("Data not found")
            return

        with open("indian_census_data.csv", "w", newline='') as file_writer:
            writer = csv.writer(file_writer)
            writer.writerows(modified_indian_census_list)
            print("File updated successfully")
        print("----------------------------------------------\n")

    @staticmethod
    def delete_record():
        """
            Deleting record from indian census csv file
        :return: None
        """
        with open("indian_census_data.csv", "r") as file_reader:
            reader = csv.reader(file_reader)
            found = 0  # False
            modified_indian_census_list = []
            state = input("Enter state to delete record: ")
            print(type(state))
            # assert type(int(state)) != int

            for row in reader:
                if row[0] != state:
                    modified_indian_census_list.append(row)
                else:
                    found = 1
            if found == 0:
                print("Record not found")
                file_reader.close()
            else:
                with open("indian_census_data.csv", "w", newline='') as file_writer:
                    writer = csv.writer(file_writer)
                    writer.writerows(modified_indian_census_list)
                    file_writer.close()
                    print("Record deleted successfully")
        print("-----------------------------------------------\n")


if __name__ == '__main__':
    print("------------------------------------------------------------------------")
    print("\t\t!! Welcome to Indian census analyzer !!")
    print("------------------------------------------------------------------------")
    more_choice = True
    while more_choice:
        print("1.Read indian census\n"
              "2.Write to indian census\n"
              "3.Delete record from indian census\n"
              "4.Update record\n"
              "5.Close file...\n")
        try:

            choice = {1: IndiaCensus.read_indian_census_csv_file,
                      2: IndiaCensus.write_csv_file,
                      3: IndiaCensus.delete_record,
                      4: IndiaCensus.update_record}
            user_input = int(input("Select option: "))
            if user_input != 5:
                choice.get(user_input)()
            elif user_input == 5:
                more_choice = False
                print("File closing...")
        except Exception as e:
            print("Please select valid option", e)
