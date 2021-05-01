deck_as_string = input().split(" ")
number_of_shuffles = int(input())
left_half = []
right_half = []
current_deck = []
sum_all = ""
for shuffles in range(number_of_shuffles):
    current_deck = []
    half = int(len(deck_as_string) / 2)
    left_half = deck_as_string[0:half]
    right_half = deck_as_string[half::]
    for card in range(len(left_half)):
        current_deck.append(left_half[card])
        current_deck.append(right_half[card])
    deck_as_string = current_deck
print(deck_as_string)
