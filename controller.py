from prices import Prices
from card import Card

class Controller():
    '''
    Class to control the Metro system, manage cards, and handle commands.

    Attributes:
        __price_list (Prices): Object to manage pricing information.
        __summary (dict): Summary of collected charges, discounts, and passenger types.
        __possible_return_trip (dict): Records for possible return trips.
        __cards (list): List of Card objects.

    Methods:
        handle(line): Handle a command line.
        add_card(id, amount): Add a new Card object to the list.
        check_in(line): Handle a CHECK_IN command.
        print_summary(summary): Print the summary of collected data.
        print_content(key, value): Print specific content of the summary.
    '''
    def __init__(self, summary, possible_return_trip):
      self.__price_list = Prices()
      self.__summary = summary
      self.__possible_return_trip = possible_return_trip
      self.__cards = []

    def handle(self, line):
      if line[0] == 'BALANCE':
        self.add_card(line[1], int(line[2]))
      elif line[0] == 'CHECK_IN':
        line.pop(0)
        self.check_in(line)
      elif line[0] == 'PRINT_SUMMARY':
        self.print_summary(self.__summary)

    def add_card(self, id, amount):
      self.__cards.append(Card(id, amount))

    def check_in(self, line):
      self.__card = [x for x in self.__cards if x.get_id() == line[0]][0]  # Get the Card object

      # Is it a return trip?
      self.__return_trip = line[0] in self.__possible_return_trip.keys()

      if self.__return_trip:
        self.__possible_return_trip.pop(line[0])  # Remove record from list
      else:
        self.__possible_return_trip[line[0]] = line[2]  # Add record to list in case of return trip

      self.__trip_cost = (self.__price_list.get_price(line[1], self.__return_trip))
      self.__discount = (self.__price_list.get_discount(line[1], self.__return_trip))

      # Deduct value from card
      self.__recharge = self.__card.deduct_cost(self.__trip_cost)

      # Add charge and discount amounts and passenger type to summary
      self.__summary[line[2]]["CHARGES"] += self.__trip_cost + self.__recharge
      self.__summary[line[2]]["DISCOUNTS"] += self.__discount
      self.__summary[line[2]][line[1]] += 1  # Type of passenger

    def print_summary(self, summary):
      for self.__key, self.__value in summary.items():
        self.print_content(self.__key, self.__value)

    def print_content(self, key, value):
      print("TOTAL_COLLECTION  {0} {1:.0f} {2:.0f}".format(
        self.__key,
        self.__value["CHARGES"],
        self.__value["DISCOUNTS"]))

      # Delete extra key-value pairs so we can sort the types of passengers
      del self.__value["CHARGES"]
      del self.__value["DISCOUNTS"]

      print("PASSENGER_TYPE_SUMMARY")
      self.__sorted_list = [
        (i[0], i[1]) for i in self.__value.items()
        if i[1] > 0
      ]

      # Print types of passengers and number (only if number is above 0)
      [print("{0} {1}".format(i[0], i[1])) for i in self.__sorted_list if i[1] > 0]
