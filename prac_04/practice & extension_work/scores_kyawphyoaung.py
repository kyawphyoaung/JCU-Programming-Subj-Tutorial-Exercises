"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    # print(subjects)
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    # print(score_values)
    for subject in range(len(subjects)):
        print("")
        print(subjects[subject] + ", Scores:")
        max_num = 0
        min_num = 100
        total = 0
        avg_num = 0
        curr = 0
        for i in range(len(score_values)):
            curr +=1
            print("{:3d}".format(score_values[i][subject]), end="|")
            if curr == 5:
                print()
                curr=0
            if score_values[i][subject] > max_num:
                max_num = score_values[i][subject]
            if score_values[i][subject] < min_num:
                min_num = score_values[i][subject]
            total += score_values[i][subject]
            avg_num = total / 10

        print("Max: " + str(max_num))
        print("Min: " + str(min_num))
        print("Average: " + str(avg_num))


main()
