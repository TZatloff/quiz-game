# Making a quiz game
print("Welcome to the quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")

questions_and_answers = {
    "What is the main ingredient in coffee? ": "coffee beans",
    "Which country is the largest producer of coffee? ": "Brazil",
    "What is the term for coffee without milk? ": "black coffee",
    "What is the name of the process of brewing coffee by forcing hot water through ground coffee? ": "espresso",
    "What is the name of the coffee drink that combines espresso with steamed milk? ": "latte",
    "What is the name of the method where coffee is brewed by pouring water over coffee in a filter? ": "pour over",
    "Which country is believed to have discovered coffee in the 9th century? ": "Ethiopia",
}

score = 0

for question, correct_answer in questions_and_answers.items():
    answer = input(question).strip().lower()
    if answer == correct_answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is:", correct_answer)

print(f"You got {score}/{len(questions_and_answers)} questions correct!")
print("Thanks for playing!")
