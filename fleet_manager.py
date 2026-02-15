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
    

