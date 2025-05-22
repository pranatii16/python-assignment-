def create_gradebook():
    gradebook = {}
    n = int(input("Enter number of students: "))

    for _ in range(n):
        name = input("Enter student name: ").strip().lower()
        marks = float(input(f"Enter marks for {name}: "))
        gradebook[name] = marks

    return gradebook

def query_gradebook(gradebook):
    while True:
        name = input("\nEnter student name to get marks (or type 'exit' to quit): ").strip().lower()
        if name == 'exit':
            break
        elif name in gradebook:
            print(f"{name.title()}'s marks: {gradebook[name]}")
        else:
            print("Student not found.")

# Main program
gradebook = create_gradebook()
query_gradebook(gradebook)
