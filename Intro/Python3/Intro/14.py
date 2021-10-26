# # # # # # # # Through the Fog

# # Circle of Numbers
# Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

def circleOfNumbers(n, firstNumber):
    if firstNumber < n/2:
        return n/2+firstNumber
    elif firstNumber > n/2:
        return n/2+firstNumber-n
    else:
        return 0


def circleOfNumbers(n, firstNumber):
    return (firstNumber + n/2) % n

# # Deposit Profit


def depositProfit(deposit, rate, threshold):
    amount = deposit
    years = 0
    while amount < threshold:
        amount = (rate/100+1)*amount
        years += 1
    return years


def depositProfit(deposit, rate, threshold):
    return math.ceil(math.log(threshold/deposit, 1+rate/100))
