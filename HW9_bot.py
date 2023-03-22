contacts = {}

def hello():
    print("""Hello, I'm a bot. I will help you use the program.
        - For add contact to directory input <<< add 'name" 'number'>>> use a space without a comma
        - For find contact in directory input <<< find 'name'  >>> use a space without a comma
        - For show all contacts in directory input <<< show >>> 
        - For update contact in directory input <<< update 'name" 'new number'  >>> use a space without a comma
        - To exit the program input <<<exit>>> or <<<bye>>>""")

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Added {name} with phone number {phone}")

def find_contact(name):
    if name in contacts:
        print(f"The phone number for {name} is {contacts[name]}")
    else:
        print(f"{name} not found in contacts")

def update_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        print(f"Updated {name}'s phone number to {phone}")
    else:
        print(f"{name} not found in contacts")

def show_all_contacts():
    print("All contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def parse_command(command):
    parts = command.split()
    if parts[0] == "hello":
        hello()
    
    elif parts[0] == "add":
        add_contact(parts[1], parts[2])
    elif parts[0] == "find":
        find_contact(parts[1])
    elif parts[0] == "update":
        update_contact(parts[1], parts[2])
    elif parts[0] == "show":
        show_all_contacts()

def main():
    while True:
        command = input("Enter command:>>>>>>> ")
        if command == "exit":
            print ("The program is finish")
            break
        elif command == "bye":
            print ("The program is finish")
            break
        else:
            parse_command(command)
        

if __name__ == '__main__':
    main()
