#fleet_manager

def init_database():
    names = [ 
        "Pike",
        "Jean-Luc Picard",
        "Spock",
        "Kirk",
        "William Riker"
    ]

    ranks = [
        "Admiral",
        "Captain",
        "Ambassador",
        "Captain",
        "Commander"
    ]

    divs = [
        "Command",
        "Command",
        "Sciences",
        "Command",
        "Command"
    ]

    ids = [
        "1000",
        "1001",
        "1002",
        "1003",
        "1004"
    ]
    
    return names, ranks, divs, ids

def display_menu():
    user = input("Enter your name: ")

    print("/nWelcome,", user)
    print("1. Add crew member")
    print("2. Remove crew member")
    print("3. Update ranks")
    print("4. Display roster")
    print("5. Exit")
    print("6. Search Crew")
    print("7. Filter by division")
    print("8. Payroll Calculator")
    print("9. Senior officer count")

    choice = input("Choose an option (1-5): ")
    if choice.isdigit():
        return int(choice)
    else:
        return 0

def add_member(names, ranks, divs, ids):
    new_id = input("ENter ID: ")

    if new_id in ids:
        print("ID exists already")
        return
    
    valid_ranks = [
        "Admiral",
        "Captain",
        "Commander",
        "Ambassador"
    ]

    new_rank = input("Enter rank: ")

    if new_rank not in valid_ranks:
        print("Rank not valid")
        return
    
    new_name = input("Enter name: ")
    new_div = input("Enter divsion: ")

    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    
    print("Crew member added")

def remove_member(names, ranks, divs, ids):
    remove_id = input("Enter ID to remove: ")

    if remove_id not in ids:
        print("ID not found")
        return
    
    index = ids.index(remove_id)

    names.pop(index)
    ranks.pop(index)
    divs.pop(index)
    ids.pop(index)

    print("Member removed")

def update_rank(names, ranks, divs, ids):
    target_id = input("Enter crew ID: ")

    if target_id not in ids:
        print("ID not found")
        return
        
    index = ids.index(target_id)
    new_rank = input("Enter new rank: ")

    ranks[index] = new_rank
    print("Rank updated")

def display_roster(names, ranks, divs, ids):
    print("/n  Crew Roster   ")
    print(f"{'Name':<20}{'ID':<25}{'Rank':>15}{'Division'}")

    for i in range(len(names)):
        print(f"{ids[i]:<25}{names[i]:<20}{ranks[i]:>15}{divs[i]}")


def search_crew(names, ranks, divs, ids):
    term = input("Enter search term: ").lower()
    found = False

    print("/n   Search Results    ")

    for i in range(len(names)):
        if (term in names[i].lower() or
            term in ranks[i].lower() or
            term in divs[i].lower() or
            term in ids[i].lower()):

            print(f"{ids[i]} | {names[i]} | {ranks[i]} | {divs[i]}")
            found = True
    if not found:
        print("No matches")

def filter_by_division(names, ranks, divs, ids):
    division = input("Enter division")

    print(f"/n   Division Results   ")
    found = False

    for i in range(len(names)):
        if divs[i].lower() == division:
            print(f"{ids[i]} | {names[i]} | {ranks[i]}")
            found = True
    if not found:
        print("No crew members in division")

def calculate_payroll(ranks):
    credits = {
        "Captain": 1000,
        "Admiral": 2000,
        "Commander": 500,
        "Ambassador": 200
    }

    total = 0
    for rank in ranks:
        total += credits.get(rank, 0)
    print(f"/nTotal fleet payroll: {total} credits")
    return total

def count_senior_officers(ranks):
    count = 0
    for rank in ranks:
        if rank == "Captain" or rank == "Commander":
            count += 1 
    return count

def main():
    names, ranks, divs, ids = init_database()

    while True:
        choice = display_menu()

        if choice == 1:
            add_member(names, ranks, divs, ids)
        elif choice == 2:
            remove_member(names, ranks, divs, ids)
        elif choice == 3:
            update_rank(names, ranks, divs, ids)
        elif choice == 4:
            display_roster(names, ranks, divs, ids)
        elif choice == 5:
            print("Exiting")
        elif choice == 6:
            search_crew(names, ranks, divs, ids)
        elif choice == 7:
            filter_by_division(names, ranks, divs, ids)
        elif choice == 8:
            calculate_payroll(names, ranks, divs, ids)
        elif choice == 9:
            count = count_senior_officers(ranks)
            print(f"Captains and commanders: {count}")
            break
        else:
            print("Choice not valid")
            break
main()






        




