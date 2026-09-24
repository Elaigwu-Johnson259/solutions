#Q3 Part A
#Before running the code, predict all three output lines. Explain what copy() copies here and which object is still shared. [7 marks]
#Q3 Part C
#Write assertions showing that the original tags remain unchanged and the returned tags contain the new tag. Then append another tag to the returned list and assert that the original still has only its initial tag. [6 marks]
#Q3 Part B
#Repair add_tag so its returned dictionary and tags list are independent of the original. Do not change the public function signature. [7 marks]

'''


Challenging  |  13 minutes  |  25 marks
You receive a list of strings representing whole-unit amounts. Return a dictionary with total and rejected. Use Python int(raw) conversion: surrounding whitespace is accepted. A converted amount of zero or more is valid. Negative amounts and strings that cannot be converted must each increase rejected by one. An empty list returns both values as zero. Do not change the input.
def summarise_amounts(raw_values):
    total = 0
    for raw in raw_values:
        try:
            total += int(raw)
        except:
            pass
    return {"total": total, "rejected": 0}
Required example: ["10", " 5 ", "bad", "-3", "0", ""] must return {"total": 15, "rejected": 3}. Inputs are always strings; no other type validation is required.
Q4 Part C
Write four executable assertions covering the required mixed example, empty input, all rejected input, and a valid zero. State why checking only total could miss a bug. [8 marks]
Q4 Part A
Identify three defects or risks in the supplied function. Explain why a bare except can hide an unrelated failure. [6 marks]




Question 5 Make stock reservation reliable
Hardest  |  16 minutes  |  30 marks
stock maps item names to available quantities. order is a list of (item, quantity) pairs. Stock values are non-negative integers; order quantities are integers, not booleans. Keys are strings. These shapes and types are guaranteed.
def reserve_stock(stock, order):
    remaining = stock.copy()
    for item, quantity in order:
        if quantity > stock[item]:
            raise ValueError("Insufficient stock")
        remaining[item] = stock[item] - quantity
    return remaining
Required behaviour
Return a new dictionary containing every stock key with its remaining quantity. Never modify stock or order, including when a request fails.
An item may occur more than once in order. Its combined requested quantity must be reserved. Never allow a negative remaining quantity.
Raise ValueError for an unknown item, a quantity of zero or less, or insufficient stock. Error message wording is your choice. An empty order returns an equal but separate dictionary.
You may use try/except with an assertion that fails if ValueError is not raised. Tests must call the function and check a result or failure, not just print it.
Q5 Part C
Write four tests: successful repeated items, repeated items exceeding stock, an unknown item, and zero quantity. In the overselling test, make at least one earlier line valid, then assert the original stock is unchanged after the exception. Explain why editing a local copy protects the caller when a later line fails. [10 marks]
Q5 Part A
With stock = {"pen": 5}, trace order = [("pen", 3), ("pen", 3)]. Explain why the supplied code incorrectly succeeds, and identify the other validation gaps. [6 marks]



'''


def ticket_total(price, quantity):
    total = price * quantity
    print(total)
amount = ticket_total("7", 3)
print(amount)



def passing_scores(scores):
    passed = []
    for index in range(len(scores)):
        if scores[index] >= 50:
            passed.append(scores[index])
    return passed
print(passing_scores([49, 50, 80, 65]))
#assert passing_scores([85]) == 1
#assert passing_scores([50, 20]) == 1
#assert passing_scores([]) == 0


def add_tag(profile, tag):
    updated = profile.copy()
    updated["tags"].append(tag)
    return updated
original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")
print(original["tags"])
print(changed is original)
print(changed["tags"] is original["tags"])