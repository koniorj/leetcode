# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival
#  airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". 
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical
# order when read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

from collections import defaultdict, deque
def findItinerary(tickets):
    flights = defaultdict(list)

    for s, t in tickets:
        flights[s].append(t)
    
    for key in flights:
        flights[key].sort(reverse=True)

    if not flights.get("JFK"):
        return []

    itinerary = []
    stack = deque(["JFK"])
    while stack:
        u = stack[-1]

        if flights[u]:
            stack.append(flights[u].pop())
        else:
            itinerary.append(stack.pop())

    return itinerary[::-1]

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]] # ["JFK","MUC","LHR","SFO","SJC"]
print(findItinerary(tickets))
