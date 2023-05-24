from db import *
def confirmation():
    response = input("Run? (y/n/)")
    if response.lower() =="y":
        return True
    elif response.lower() == "n":
        return False
    else:
        print("bozo")

def main():
    confirm = confirmation()
    if confirm:
        reset_database()
        populate_crashes()
        populate_all_coordinates()


if __name__ == "__main__":
    main()