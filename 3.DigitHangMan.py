if __name__ == "__main__":
    # inputs and initial values
    answer = list(input().split())
    guesses = []
    for i in range(5):
        guesses.append(input())
    answerSheet = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
    wrongGuesses = []
    score = 0

    # printing blank answer sheet
    for slot in answerSheet:
        print(slot, end=" ")
    print()

    # guesses evaluation
    for guess in guesses:
        correct = False
        for i in range(len(answer)):
            if answerSheet[i] == '_' and answer[i] == guess:
                answerSheet[i] = guess
                score += 1
                correct = True
        if not correct:
            wrongGuesses.append(guess)

        # printing results
        for slot in answerSheet:
            print(slot, end=" ")
        for wrong in wrongGuesses:
            print(wrong, end=" ")
        print()
    print(score)
