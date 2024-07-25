#import necessary madules
import re


#Main function to handle user input and output
def main():
    # prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ")
    
    # check if the input is empty
    if not user_input.strip():
        print("Error: Input cannot be empty. Please enter some text.")
    else:
        #count the word in the input
        word_count = count_words(user_input)
        
        # Display the word count to the user
        print(f"The number of words in your input is:{word_count}")


# Function to count the number of words in the input
def count_words(text):
    #use regular expressions to find all words in the text
    words = re.findall(r'\b\w+\b', text)
    return len(words)


# Run the main function to start the program
if __name__ == "__main__":
    main() 
