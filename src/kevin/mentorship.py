def challenge_my_thinking(problem):
    first_answer = problem.obvious_solution()

    # Kevin would usually ask one more question.
    better_answer = ask("Have you thought about it differently?")

    return better_answer
