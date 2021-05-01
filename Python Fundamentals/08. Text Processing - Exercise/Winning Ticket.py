symbols = ["#", "^", "@", "$"]


def is_ticket_a_jackpot(ticket):
    for symbol in symbols:
        if symbol in ticket:
            if ticket.count(symbol) == 20:
                print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
                return True
    return False


def is_winning_ticket(ticket):
    avg = int(len(ticket) / 2)
    left_side = ticket[:avg] # [:10]
    right_side = ticket[avg:] # [10:]
    for symbol in symbols:
        if symbol * 6 in left_side and symbol * 6 in right_side:
            symbol_count_left = left_side.count(symbol)
            symbol_count_right = right_side.count(symbol)
            result = min(symbol_count_left, symbol_count_right)
            print(f'ticket "{ticket}" - {result}{symbol}')
            return True
    return False


tickets = [el.strip() for el in input().split(", ")]

for ticket in tickets:
    if not len(ticket) == 20:
        print("invalid ticket")
        continue
    if is_ticket_a_jackpot(ticket):
        continue
    if is_winning_ticket(ticket):
        continue

    print(f'ticket "{ticket}" - no match')
