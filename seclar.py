if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        findscore =max(score)
        a=sorted(set(score))
        second_score = max(score)
        if second_score==max(score):
            print([y,1])
