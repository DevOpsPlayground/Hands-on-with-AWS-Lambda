from random import randint

def lambda_handler(event, context):
    # TODO implement
    myNumber = randint(0,100)
    print myNumber
    return myNumber
