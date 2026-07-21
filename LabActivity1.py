def check_borrowing(overdue_books, status):
    if overdue_books:
        return "Not allowed: overdue books"
    elif status == "suspended":
        return "Not allowed: suspended account"
    else:
        return "Borrowing allowed"


def run_kiosk():
    students_helped = 0

    while True:
        name = input("Enter student name (or 'exit' to quit): ").strip()
        if name.lower() == "exit":
            break

        overdue_input = input("Do you have overdue books? (yes/no): ").strip().lower()
        overdue_books = overdue_input == "yes"

        status = input("What is your borrower status? (active/suspended): ").strip().lower()

        result = check_borrowing(overdue_books, status)

        if result == "Borrowing allowed":
            try:
                num_books = int(input("How many books do you want to borrow? "))
            except ValueError:
                print("Please enter a valid number. Skipping this student.\n")
                continue

            if num_books <= 0:
                print(f"{name}, you need to request at least 1 book to borrow.\n")
                continue
            elif num_books > 3:
                print(f"{name}, you can only borrow up to 3 books at a time. Capping your request to 3.")
                num_books = 3
                students_helped += 1
            else:
                print(f"{name}, you are approved to borrow {num_books} book(s).")
                students_helped += 1
        else:
            print(f"{name}, {result}.")

        print()  # blank line for readability

    print(f"Kiosk session ended. Total students who successfully borrowed: {students_helped}")


if __name__ == "__main__":
    run_kiosk()