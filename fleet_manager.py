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
        "C 386-249 SP",
        "SP 937-215",
        "S 179-276 SP"
        "SC 937-0176 CEC"
        "S 496-828 SP"
    ]
    
    return names, ranks, divs, ids

def display_menu():
    user = input("Enter your name: ")

    print("Welcome," + user)
    print("1. Add crew member")
    print("2. Remove crew member")
    print("3. View crew list")
    print("4. Exit")

    choice = input("Select option (1-4): ")
    return choice

def add_crew_member(names, ranks, divs, ids):
    new_id = input("Enter unique id: ")
    if new_id in ids:
        print("ID already exists.")
        return
    
    valid_ranks = [
        "Admiral",
        "Captain",
        "Commander",
        "Ambassador",
    ]

    new_rank = input("Enter rank: ")

    if new_rank not in valid_ranks:
        print("Invalid rank.")
        return
    
    new_name = input("Enter name: ")
    new_div = input("Enter division: ")

    names.append(new_name)
    divs.append(new_div)
    ids.append(new_id)
    ranks.append(new_rank)

    print("Crew member added.")

    def remove_crew_memeber(names, ranks, divs, ids):
        remove_id = input("Enter id to remove: ")

        if remove_id not in ids:
            print("ID not found. ")
            return
        
        index = ids.index(remove_id)

        names.pop(index)
        divs.pop(index)
        ids.pop(index)
        ranks.pop(index)

        print(" Crew member has been removed.")


    

