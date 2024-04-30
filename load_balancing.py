def print_server_load(num_servers, num_processes):
    processes_per_server = num_processes // num_servers
    extra_processes = num_processes % num_servers

    i = 0

    # Loop for extra process i.e adding 1 to each server
    for i in range(extra_processes):
        print(f"Server {i + 1} has {processes_per_server + 1} processes")

    # Loop for remaining processes
    for i in range(extra_processes, num_servers):
        print(f"Server {i + 1} has {processes_per_server} processes")


def display_menu():
    print("1. Add Server")
    print("2. Remove Server")
    print("3. Add Processes")
    print("4. Remove Processes")
    print("5. Exit")


if __name__ == "__main__":
    num_servers = int(input("Enter no of servers: "))
    num_processes = int(input("Enter no of processes: "))

    while True:
        print_server_load(num_servers, num_processes)
        display_menu()
        choice = int(input("> "))
        temp = 0

        if choice == 1:
            print("Enter number of servers to be added: ")
            temp = int(input())
            num_servers += temp
        elif choice == 2:
            print("Enter number of servers to be removed: ")
            temp = int(input())
            num_servers -= temp
        elif choice == 3:
            print("Enter number of processes to be added: ")
            temp = int(input())
            num_processes += temp
        elif choice == 4:
            print("Enter number of processes to be removed: ")
            temp = int(input())
            num_processes -= temp
        elif choice == 5:
            break
