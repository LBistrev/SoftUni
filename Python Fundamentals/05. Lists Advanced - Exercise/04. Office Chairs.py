number_of_rooms = int(input())
free_chairs = 0
enough = True
for room in range(1, number_of_rooms+1):
    chairs, taken_places = input().split()
    taken_places = int(taken_places)
    diff = abs(taken_places - len(chairs))
    if len(chairs) >= taken_places:
        free_chairs += diff
    else:
        enough = False
        print(f"{diff} more chairs needed in room {room}")

if enough:
    print(f"Game On, {free_chairs} free chairs left")
