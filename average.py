if __name__ == '__main__':
    n = int(input())
    total=float(0)
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] =scores
    query_name = input()
    for i in range(len(student_marks[query_name])):
        total+=float(student_marks[query_name][i])

    ave=float(total/(i+1))
    print("%.2f" %ave)