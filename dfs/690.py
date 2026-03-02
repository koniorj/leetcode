# You have a data structure of employee information, including the employee's unique ID, importance value, 
# and direct subordinates' IDs.

# You are given an array of employees employees where:

# employees[i].id is the ID of the ith employee.
# employees[i].importance is the importance value of the ith employee.
# employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.
# Given an integer id that represents an employee's ID, return the total importance value of this
# employee and all their direct and indirect subordinates.

class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
        self.visited = False

def getImportance(employees, id):    
    map = {e.id: e for e in employees} 

    def dfs(eid):
        u = map[eid]
        total = u.importance
        for sub_id in u.subordinates:
            total += dfs(sub_id)
        return total
            
    return dfs(id)

employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]]
id = 1
print(employees, id)