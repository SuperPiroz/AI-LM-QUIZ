import json
import random
import sys

# Define paths for question files
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define absolute paths to question files
path_eda = os.path.join(script_dir, "questions_eda.json")
path_cnn_kafka = os.path.join(script_dir, "questions_cnn_kafka.json")
path_transferlearning = os.path.join(script_dir, "questions_transferlearning.json")
path_supervised_unsupervised = os.path.join(script_dir, "questions_supervised_unsupervised.json")
path_tcn_autoencoders = os.path.join(script_dir, "question_TCN_Autoencoders.json")
path_all_tests = os.path.join(script_dir, "questions_alla_kunskapstester.json")

# Function to load questions from a file
def load_questions(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list) and all("question" in item and "answer" in item for item in data):
                return data
            else:
                print(f"Error: Unexpected JSON format in {file_path}. Expected a list of objects with 'question' and 'answer' keys.")
                return []
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}.")
        return []

# Main program loop
while True:
    # Display menu for selecting question set
    print("Välkommen till Quiz-programmet!")
    print("----------------------------------------")
    print("Välj vilka frågor du vill plugga:")
    print("1. Jag vill plugga allt")
    print("2. Jag vill plugga EDA")
    print("3. Jag vill plugga Supervised och Unsupervised ML")
    print("4. Jag vill plugga CNN och Kafka")
    print("5. Jag vill plugga Transfer Learning")
    print("6. TCN och AutoEncoders")
    print("7. Jag vill plugga alla kunskapstest")
    print("----------------------------------------")

    # Get user choice for question set
    question_set_choice = input("Välj alternativ (1-7) eller 'q' för att avsluta: ")
    print("----------------------------------------")

    if question_set_choice.lower() == 'q':
        break

    # Load questions based on user choice
    questions = []
    if question_set_choice == "1":
        questions_eda = load_questions(path_eda)
        questions_cnn_kafka = load_questions(path_cnn_kafka)
        questions_transferlearning = load_questions(path_transferlearning)
        questions_supervised = load_questions(path_supervised_unsupervised)
        questions_tcn = load_questions(path_tcn_autoencoders)
        questions_all_tests = load_questions(path_all_tests)
        questions = questions_eda + questions_cnn_kafka + questions_transferlearning + questions_supervised + questions_tcn + questions_all_tests
        print(f"Laddat {len(questions)} frågor totalt.")
    elif question_set_choice == "2":
        questions = load_questions(path_eda)
        print(f"Laddat {len(questions)} EDA-frågor.")
    elif question_set_choice == "3":
        questions = load_questions(path_supervised_unsupervised)
        print(f"Laddat {len(questions)} Supervised/Unsupervised ML-frågor.")
    elif question_set_choice == "4":
        questions = load_questions(path_cnn_kafka)
        print(f"Laddat {len(questions)} CNN/Kafka-frågor.")
    elif question_set_choice == "5":
        questions = load_questions(path_transferlearning)
        print(f"Laddat {len(questions)} Transfer Learning-frågor.")
    elif question_set_choice == "6":
        questions = load_questions(path_tcn_autoencoders)
        print(f"Laddat {len(questions)} TCN/AutoEncoders-frågor.")
    elif question_set_choice == "7":
        questions = load_questions(path_all_tests)
        print(f"Laddat {len(questions)} kunskapstest-frågor.")
    else:
        print("Ogiltigt val. Försök igen.")
        continue

    print("----------------------------------------")
    def quiz_loop(questions):
        if not questions:
            print("Inga frågor laddade, återgår till huvudmenyn.")
            return

        # Create a copy of the questions to avoid modifying the original list
        current_questions = questions[:]
        random.shuffle(current_questions)

        while True:
            # If we've run out of questions, reshuffle and start again
            if not current_questions:
                print("Alla frågor har visats. Börjar om...")
                current_questions = questions[:]
                random.shuffle(current_questions)

            selected = current_questions.pop(0)

            # Show question
            print(f"\n\nFråga: {selected['question']}\n")
            print("----------------------------------------")
            
            # Wait for spacebar to show answer
            action = input("Tryck [Mellanslag] + [Enter] för svar, [M] + [Enter] för meny, [Q] + [Enter] för att avsluta: ")
            if action.lower() == 'q':
                sys.exit("Programmet avslutas.")
            if action.lower() == 'm':
                return # Go back to main menu

            # Show answer
            print(f"\nSvar: {selected['answer']}\n")
            print("----------------------------------------")

            # Wait for spacebar to show next question
            action = input("Tryck [Mellanslag] + [Enter] för nästa fråga, [M] + [Enter] för meny, [Q] + [Enter] för att avsluta: ")
            if action.lower() == 'q':
                sys.exit("Programmet avslutas.")
            if action.lower() == 'm':
                return # Go back to main menu

    quiz_loop(questions)