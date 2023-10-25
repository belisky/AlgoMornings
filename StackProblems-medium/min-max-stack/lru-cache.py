# A transaction is possibly invalid if:

# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
# You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

# Return a list of transactions that are possibly invalid. You may return the answer in any order.

 
# Example 1:

# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
# Example 2:

# Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# Output: ["alice,50,1200,mtv"]
# Example 3:

# Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# Output: ["bob,50,1200,mtv"]
from collections import defaultdict

def invalid(transactions=["alice,20,800,mtv","alice,50,1200,mtv"]):
    invalids=[]
    transactions_map=defaultdict(list)  
    for t in transactions:
        name,time,amount,city=t.split(',')
        transactions_map[name].append( city )
    for t in transactions:
        name,time,amount,city=t.split(',')
        amount=int(amount)
        if amount>1000:
            invalids.append(t)
        for loc in transactions_map[name]:
            if city!=loc:
                invalids.append(t)
                break
    return invalids
    

print(invalid())


