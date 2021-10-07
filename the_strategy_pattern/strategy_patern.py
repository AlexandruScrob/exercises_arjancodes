import string
import random
from typing import List
from abc import ABC, abstractmethod


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


# TODO this can be replaced with a functional approach
class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, lst: List[SupportTicket]
                        ) -> List[SupportTicket]:
        pass


class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, lst: List[SupportTicket]
                        ) -> List[SupportTicket]:
        return lst.copy()


class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, lst: List[SupportTicket]
                        ) -> List[SupportTicket]:
        list_copy = lst.copy()
        list_copy.reverse()
        return list_copy


class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, lst: List[SupportTicket]
                        ) -> List[SupportTicket]:
        list_copy = lst.copy()
        random.shuffle(list_copy)
        return list_copy


class BlackHoleOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, lst: List[SupportTicket]
                        ) -> List[SupportTicket]:
        return []


class CustomerSupport:

    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        # create the ordered list
        ticket_list = processing_strategy.create_ordering(self.tickets)

        if len(ticket_list) == 0:
            print("there are no tickets to process. Well done!")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)

    @staticmethod
    def process_ticket(ticket: SupportTicket):
        print("======================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("======================")


# create the application
app = CustomerSupport()

# register a few tickets
app.create_ticket("John", "Computer no work")
app.create_ticket("Linus", "hey Vsauce Michael here")
app.create_ticket("Arjan", "VSCode doesn't fix my code")

# process the tickets
app.process_tickets(RandomOrderingStrategy())
