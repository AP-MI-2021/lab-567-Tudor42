from Domain.inventory import creaza_inventoriu
from UserInterface.handler import handle_command, multiple_commands_handle


def loop():
    inventory = creaza_inventoriu()
    while True:
        command = input('$').split()
        if len(command) == 0:
            continue
        if '&' not in command:
            n, inventory = handle_command(command, inventory)
        else:
            n, inventory = multiple_commands_handle(command, inventory)
        if n == 4:
            break


def run():
    print("For commands list type help")
    print("Separator &")
    loop()


if __name__ == "__main__":
    run()
