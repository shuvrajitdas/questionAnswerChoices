import re

# Method which takes current question and choice as the parameter, and based on that it looks on the 
# rules_dictionary for the next question to display and returns that

# And if that choice of answer is not present in rules_dict then we ask user again for the choice of answer
def display_next_question(rules_dict, current_question_with_choice):

    if current_question_with_choice in rules_dict:
        next_question = rules_dict[current_question_with_choice]
        print(f"This is question {next_question}, enter your answer")
        return next_question
    else:
        current_question = current_question_with_choice.split("-")
        print(f"No rule defined for question {current_question}. Please try again.")
        return current_question[0]


# Main function
def main():

    # Taking the number of questions as input
    N = int(input("No. of questions (N) = "))
    questions = [f"Q{i}" for i in range(1, N + 1)]


    # Taking the list of rules as input 
    rules = input("List of rules (L) = ")

    # Using regex pattern for finding each individual rule from the string input
    pattern = r'“([^”]*)”'

    # Use findall to retrieve all matches of the pattern
    rules_segregated = re.findall(pattern, rules)

    # Print matches
    print("Matches:", rules_segregated)

    rules_dict = {}
    for rule in rules_segregated:

        # Splitting each rule on delimeter '-', because we need to store 
        # the question in which we have to proceed based on the choice of options
        question_from, choice, question_to = rule.split("-")
        rules_dict[f"{question_from}-{choice}"] = question_to

    # Starting point, where we start from question number 1 and then proceed
    current_question = "Q1"
    print(f"This is question {current_question}, enter your answer")

    while current_question != "Q6":
        answer = input("Input: ")
        current_question = display_next_question(rules_dict, f"{current_question}-{answer}")

    print("Thank You!")

if __name__ == "__main__":
    main()
