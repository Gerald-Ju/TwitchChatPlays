import time
from Modules.ConnectSocket import ConnectSocket

def main():
    while True:
        choice = input("\nRun program (y/n): ").lower()
        if choice == "y":
            ConnectSocket().connectToSocket()
            break
        elif choice == "n":
            print("\nClosed\n")
            time.sleep(2)
            break
        else:
            print("\nInvalid Input. Try Again.\n")

if __name__ == "__main__":
    main()
