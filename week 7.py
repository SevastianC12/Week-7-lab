#Total Sales
#Design a program that ask the user to enter a store's sales for each day of the week. 
# Initialize an empty list to store daily sales
sales = []

# Days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through each day of the week
for day in days_of_week:
    while True:
        try:
            # Ask the user for sales input
            daily_sales = float(input(f"Enter the sales for {day}: "))
            sales.append(daily_sales)  # Append to the sales list
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Please enter a valid number.")

# Calculate total sales
total_sales = sum(sales)

# Display the total sales
print(f"\nTotal sales for the week: ${total_sales:.2f}")


#Design a program that generates 7 digit lottery numbers. It should generate numbers from range 0-9 and assing each number to a list element.
#Then write another loop that displays the contents of the list.
import random

MAX_DIGITS = 7
START = 0
END = 9

# Main function
def main():
    # Create a list.
    numbers = [0] * MAX_DIGITS

    # Populate the list with random numbers 
    for index in range(MAX_DIGITS):
        numbers[index] = random.randint(START, END)

    # Display the random numbers. 
    print('Here are your lottery numbers: ')
    for index in range(MAX_DIGITS):
        print(numbers[index], end=' ')
    print()

# Call the main function.
main()


#Write a program that lest the user enter the total rainfall for each of the 12 months.
#Then displays the total rainfall for the year and the average monthly rainfall. With the highest and lowest months.
def main():
    rainfall = []

    # Collect rainfall data for each month
    for month in range(1, 13):
        while True:
            try:
                rain = float(input(f'Enter the total rainfall for month {month} (in inches): '))
                if rain < 0:
                    print("Rainfall cannot be negative. Please enter a valid amount.")
                else:
                    rainfall.append(rain)  
                    break
            except ValueError:
                print('Invalid input. Please enter a numeric value.')

     
    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / 12

  
    highest_rainfall = max(rainfall) # Get the highest rainfall of the year
    lowest_rainfall = min(rainfall) # Get the lowest rainfall of the year
    month_highest = rainfall.index(highest_rainfall) + 1  
    month_lowest = rainfall.index(lowest_rainfall) + 1 

    
    print(f'\nTotal rainfall for the year: {total_rainfall:.2f} inches')
    print(f'Average monthly rainfall: {average_rainfall:.2f} inches')
    print(f'Month with highest rainfall: Month {month_highest} ({highest_rainfall:.2f} inches)')
    print(f'Month with lowest rainfall: Month {month_lowest} ({lowest_rainfall:.2f} inches)')

if __name__ == "__main__":
    main()


#Write a program that ask the user to enter a series of 20 numbers.Also displays the total,the average, the lowest and highest numbers
def main():
    numbers = []

    # Collect 20 numbers
    for i in range(20):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Please enter a valid number.")

    #Calculate everything asked for
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    #Print everything
    print(f"\nLowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total of numbers: {total}")
    print(f"Average of numbers: {average}")

if __name__ == "__main__":
    main()

#Write a program to the file named. The program should then ask the user to enter a 7 digit number and see if its valid if not it should print a message the number entered is incorrect.
def read_charge_accounts(filename):
    """Reads charge account numbers from a specified file and returns them as a list."""
    try:
        with open(filename, 'r') as file:
            # Read each line in the file
            accounts = [
                line.strip()  
                for line in file
                if line.strip().isdigit() and len(line.strip()) == 7  # Ensure it's a 7-digit number
            ]
        return accounts  
    except FileNotFoundError:
        print("The file was not found.")
        return []  # Return an empty list if the file is not found

def is_valid_account(account_number, valid_accounts):
    """Checks if the given account number is in the list of valid accounts.
    
    Args:
        account_number (str): The account number to check.
        valid_accounts (list): The list of valid account numbers.
    
    Returns:
        bool: True if the account number is valid, False otherwise.
    """
    return account_number in valid_accounts  # Check if the account number is in the list

def main():
    """Main function to execute the charge account validation program."""
    filename = 'charge_accounts.txt'  # Specify the filename containing valid accounts
    valid_accounts = read_charge_accounts(filename)  # Read the valid accounts from the file

    # Check if any valid accounts were found
    if not valid_accounts:
        print("No valid accounts found.") 
        return 

    # Ask the user to enter a charge account number
    account_number = input("Enter a charge account number: ").strip()

    # Check if the entered account number is valid
    if is_valid_account(account_number, valid_accounts):
        print(f"The account number {account_number} is valid.") 
    else:
        print(f"The account number {account_number} is invalid.") 

if __name__ == "__main__":
    main() 


#Write a function that accepts two arguments: a list, and a  number n. Assume that the list contains numbers. 
def display_greater_than(numbers_list, n):
    # Iterate through each number in the list
    for number in numbers_list:
        # Check if the number is greater than n
        if number > n:
            print(number)  # Display the number if it's greater than n



#Write a program that read the a students drivers test out of 20 questions.
#Tell the student if they passed or failed the exam. It should display the total number of correct answers, and the total of incorrect.
#And a list of question numbers of the incorrectly answered questions.
def read_student_answers(filename):
    with open(filename, 'r') as file:
        answers = [line.strip() for line in file.readlines()]
    return answers

def grade_exam(correct_answers, student_answers):
    total_correct = 0
    incorrect_questions = []

    for i in range(len(correct_answers)):
        if student_answers[i] == correct_answers[i]:
            total_correct += 1
        else:
            incorrect_questions.append(i + 1)  # Store question numbers (1-indexed)

    return total_correct, len(correct_answers) - total_correct, incorrect_questions

def main():
    # List of correct answers
    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                       'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    
    # Read student answers from file
    filename = 'drivers_test.txt'  # Make sure this file exists and contains student answers
    student_answers = read_student_answers(filename)
    
    # Grade the exam
    total_correct, total_incorrect, incorrect_questions = grade_exam(correct_answers, student_answers)
    
    # Determine pass/fail status
    if total_correct >= 15:
        result = "passed"
    else:
        result = "failed"

    # Display results
    print(f"The student has {result} the exam.")
    print(f"Total correct answers: {total_correct}")
    print(f"Total incorrect answers: {total_incorrect}")
    print(f"Questions answered incorrectly: {incorrect_questions}")

if __name__ == "__main__":
    main()


#Write a program that reads the contesnts of the file popular_names. the user should be able to enter the name and display whether the name was among the most popular.
def load_names(filename):
    """Load names from a file into a list."""
    with open(filename, 'r') as file:
        names = [line.strip() for line in file]
    return names

def check_name_popularity(name, popular_names):
    """Check if the name is in the list of popular names."""
    return name in popular_names

def main():
    # Load names from the file
    filename = 'popular_names.txt'
    popular_names = load_names(filename)

    # Get user input
    user_input = input("Enter a name to check its popularity: ").strip()

    # Check if the name is popular
    if check_name_popularity(user_input, popular_names):
        print(f"{user_input} is among the most popular names!")
    else:
        print(f"{user_input} is not in the list of popular names.")

if __name__ == "__main__":
    main()



#Write a program that reads the file's contents into a list. The program should display the annual change in population during the time period.
#Also display the year the lowest and highest population and the time period.
def read_population_data(filename):
    with open(filename, 'r') as file:
        population = [int(line.strip()) for line in file]
    return population

def calculate_population_changes(population):
    changes = [population[i] - population[i - 1] for i in range(1, len(population))]
    return changes

def main():
    filename = 'USPopulation.txt'
    
    # Read the population data
    population = read_population_data(filename)
    
    # Calculate the annual changes
    changes = calculate_population_changes(population)

    # Calculate average annual change
    average_change = sum(changes) / len(changes)

    # Find the year with the greatest increase and smallest increase
    greatest_increase_index = changes.index(max(changes)) + 1  # +1 to get the year
    smallest_increase_index = changes.index(min(changes)) + 1  # +1 to get the year

    # Year calculation (years range from 1950 to 1990)
    greatest_year = 1950 + greatest_increase_index
    smallest_year = 1950 + smallest_increase_index

    # Display results
    print(f"Average annual change in population: {average_change:.2f} thousand")
    print(f"Year with greatest increase: {greatest_year} ({changes[greatest_increase_index - 1]} thousand)")
    print(f"Year with smallest increase: {smallest_year} ({changes[smallest_increase_index - 1]} thousand)")

if __name__ == '__main__':
    main()


#Write a program that lets the user enter the team name and displays the number of times that team won the world series and what years.
def count_world_series_wins(team_name, filename='WorldSeriesWinners.txt'):
    try:
        with open(filename, 'r') as file:
            # Read all lines from the file
            winners = file.readlines()
            
            # Strip newline characters and count occurrences of the team name
            wins = sum(1 for winner in winners if winner.strip().lower() == team_name.lower())
            return wins

    except FileNotFoundError:
        print("The file was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    team_name = input("Enter the name of the team: ")
    wins = count_world_series_wins(team_name)
    
    if wins is not None:
        print(f"{team_name} has won the World Series {wins} times from 1903 to 2009.")

if __name__ == "__main__":
    main()
