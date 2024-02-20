1. Logic :
    - First, we parse the rules string and based on regex we retreive each rule and then make the rules_dict 
    - Rules_dict holds the value of next question based on the previous_question and the choice user puts 


2. Time Complexity analysis :

    Constructing the rules_dict:
        In the main() function, there's a loop iterating over the rules provided as input.

        Inside the loop, The time complexity of searching for all occurrences of the pattern in the input string is typically O(n), where n is the length of the input string.
        Therefore, the overall time complexity of re.findall() is O(m + n).

        Then, each rule is inserted into the rules_dict, which is implemented as a dictionary in Python. Inserting an item into a dictionary has an average time complexity of O(1).

        Therefore, constructing the rules_dict takes O(m) time, where m is the number of rules.

    Iterating through questions and answering:
        The loop in the main() function iterates until the current question is "Q6".
        Inside the loop, the display_next_question() function is called. Accessing an item in a dictionary has an average time complexity of O(1).
        Thus, for each iteration of the loop, the time complexity is O(1).

        Since the loop iterates at most N times (where N is the total number of questions), the time complexity of this part is O(N).

