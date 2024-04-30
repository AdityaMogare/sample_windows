import threading
import time

class SuzukiKasamiMutex:
    def __init__(self, num_processes, process_id):
        self.num_processes = num_processes
        self.process_id = process_id
        self.requesting = False
        self.sequence_numbers = [0] * num_processes
        self.reply_received = [False] * num_processes
        self.in_critical_section = False
        self.num_replies_needed = num_processes - 1
        
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        
    def request_cs(self):
        self.requesting = True
        self.sequence_numbers[self.process_id] += 1
        self.reply_received = [False] * self.num_processes
        self.num_replies_needed = self.num_processes - 1
        self.broadcast("REQUEST", self.sequence_numbers[self.process_id])
        
        self.lock.acquire()
        while not self.all_replies_received():
            self.condition.wait()
        self.lock.release()
        
        self.in_critical_section = True
        print(f"Process {self.process_id} enters critical section.")
        
    def release_cs(self):
        self.in_critical_section = False
        self.requesting = False
        self.sequence_numbers[self.process_id] += 1
        self.broadcast("RELEASE", self.sequence_numbers[self.process_id])
        print(f"Process {self.process_id} exits critical section.")
        
    def receive_message(self, source_id, msg_type, timestamp):
        if msg_type == "REQUEST":
            self.sequence_numbers[source_id] = max(self.sequence_numbers[source_id], timestamp) + 1
            if not self.requesting or (self.requesting and (timestamp, source_id) < (self.sequence_numbers[self.process_id], self.process_id)):
                self.reply(source_id)
            elif (timestamp, source_id) == (self.sequence_numbers[self.process_id], self.process_id):
                if source_id < self.process_id:
                    self.reply(source_id)
                else:
                    self.defer(source_id)
            else:
                self.defer(source_id)
        elif msg_type == "RELEASE":
            self.reply_received[source_id] = False
            if self.all_replies_received():
                self.condition.notify()
                
    def reply(self, dest_id):
        self.reply_received[dest_id] = True
        self.send_message(dest_id, "REPLY", self.sequence_numbers[self.process_id])
        
    def defer(self, dest_id):
        self.send_message(dest_id, "DEFER", self.sequence_numbers[self.process_id])
        
    def all_replies_received(self):
        return all(self.reply_received)
    
    def broadcast(self, msg_type, timestamp):
        for i in range(self.num_processes):
            if i != self.process_id:
                self.send_message(i, msg_type, timestamp)
                
    def send_message(self, dest_id, msg_type, timestamp):
        # In a real distributed system, this would send a message to another process
        # In this simplified example, we'll just print the message
        print(f"Sending message from process {self.process_id} to process {dest_id}: {msg_type} ({timestamp})")

# Function to execute in each thread
def process_execution(mutex, process_id):
    while True:
        print("\nMenu:")
        print("1. Enter critical section")
        print("2. Exit critical section")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            mutex.request_cs()
        elif choice == "2":
            mutex.release_cs()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter again.")

# Example usage
def main():
    num_processes = 5
    processes = []

    # Creating processes
    for i in range(num_processes):
        mutex = SuzukiKasamiMutex(num_processes, i)
        process = threading.Thread(target=process_execution, args=(mutex, i))
        processes.append(process)

    # Starting processes
    for process in processes:
        process.start()

    # Joining threads
    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
