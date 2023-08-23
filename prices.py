class Prices:
    '''
    To manage pricing information for different passenger types.

    Attributes:
        __price_list (dict): Price information for different passenger types.

    Methods:
        get_price(type, return_trip): Get travel price for a passenger type.
        get_discount(type, return_trip): Get discount amount for a passenger type.
    '''
    def __init__(self):
      self.__price_list = {"ADULT": 200, "SENIOR_CITIZEN": 100, "KID": 50}

    def get_price(self, type, return_trip=False):
      if return_trip:
        return (self.__price_list[type] / 2)

      return self.__price_list[type]

    def get_discount(self, type, return_trip=False):
      if return_trip:
        return (self.__price_list[type] / 2)

      return 0
