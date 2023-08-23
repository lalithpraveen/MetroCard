class Card:
    """
    Represents a MetroCard that passengers use for travel.

    Attributes:
        __id (str): Identifier of the MetroCard.
        __amount (int): Current balance in the MetroCard.
        __recharge_cost (float): Recharge cost incurred due to insufficient balance.
        __recharge_rate (float): Rate at which recharge cost is calculated.

    Methods:
        get_id(): Get the card's ID.
        get_amount(): Get the current balance of the card.
        deduct_cost(cost): Deduct travel cost from the card and calculate recharge cost.
        __reset_amount(): Reset the card's balance and calculate recharge cost.
    """
    def __init__(self, id, amount):
      self.__id = id
      self.__amount = amount
      self.__recharge_cost = 0
      self.__recharge_rate = 0.02


    def get_id(self):
      return self.__id


    def get_amount(self):
      return self.__amount


    def deduct_cost(self, cost):
      self.__amount -= cost

      if self.get_amount() < 0:
        self.__recharge_cost = self.__reset_amount()

      return self.__recharge_cost


    def __reset_amount(self):
      self.__recharge_cost = (-self.__amount * self.__recharge_rate)
      self.__amount = 0

      return self.__recharge_cost