from queue import *
from request import Request

request_queue = Queue()


def generate_request(name, description):
    request = Request(name, description)
    request_queue.put(request)


def process_request():
    if not request_queue.empty():
        completed_request = request_queue.get()
        print(f"Request with id {completed_request.id} and name {completed_request.name} was successfully completed!")
    else:
        print("The queue is empty!")


def main():
    print(
        "Welcome to Request bot. Enter add-request to generate request, process-request to process first request or "
        "exit to leave bot")
    while True:
        command = input("Enter a command: ")
        if command == "exit":
            print("Good bye!")
            break
        elif command == "add-request":
            request_name = input("Enter request name:")
            request_description = input("Enter request description: ")
            generate_request(request_name, request_description)
            print("Request was added successfully")
        elif command == "process-request":
            process_request()
        else:
            print("Invalid command.")


main()
