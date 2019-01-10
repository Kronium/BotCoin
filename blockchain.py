# Init our blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the correct blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

# Function accepts 2 arguments.
# One required one transaction_amount and one optional one
# optional one is optional because default value is => [1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to blockchain.

     Arguments:
         :transaction_amount: The amount that should be added.
         last_transaction: The last blockchain transaction (default [1]).
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_tranaction_value():
    """ Returns the input of the user (new transaction) as a float """
    # get the user input, transform it into string and store
    user_input = float(input('Your transaction amount please: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    # output the chain list to console
    for block in blockchain:
        print('Outputting Block')
        print(block)


while True:
    print('Please choose')
    print('1: Add new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_tranaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid please pick a choice from the list!')
    print('Choice registered!')

    # output blockchain list to console
    for block in blockchain:
        print('Outputting block')
        print(block)

print('Done thank you for using BotCoin!')
