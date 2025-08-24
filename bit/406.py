# You are given an array of people, people, which are the attributes of some people in 
# a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith 
# person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

# Reconstruct and return the queue that is represented by the input array people. 
# The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is 
# the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

def reconstructQueue(people):
    


    return

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
print(reconstructQueue(people))

people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
# Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
print(reconstructQueue(people))