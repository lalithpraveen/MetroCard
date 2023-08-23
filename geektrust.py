import sys
from file_reader import File_reader






def main():
  input_file = sys.argv[1]  # sys.argv[1] should give the absolute path to the input file
  input_file = open(input_file, 'r')
  summary = {"CENTRAL": {"CHARGES": 0, "DISCOUNTS": 0, "ADULT": 0, "KID": 0, "SENIOR_CITIZEN": 0},
             "AIRPORT": {"CHARGES": 0, "DISCOUNTS": 0, "ADULT": 0, "KID": 0, "SENIOR_CITIZEN": 0}}
  possible_return_trip = {}

  file = File_reader(input_file, summary, possible_return_trip)
  file.readfile()


if __name__ == "__main__":
    main()