## https://www.reddit.com/r/dailyprogrammer/comments/759fha/20171009_challenge_335_easy_consecutive_distance/
## executes at the bottom

def consecutive_distance(data):
    for row in data.split("\n"):
        total_distance = 0
        row = [int(n) for n in row.strip().split(" ")]
        array = dict(zip(row, range(0, len(row))))
        keys = sorted(list(array.keys()))

        for n in range(0, len(keys)-1):
            if keys[n+1] == keys[n]+1:
                total_distance += abs(array[keys[n+1]] - array[keys[n]])
        yield(total_distance)

data = """76 74 45 48 13 75 16 14 79 58 78 82 46 89 81 88 27 64 21 63
37 35 88 57 55 29 96 11 25 42 24 81 82 58 15 2 3 41 43 36
54 64 52 39 36 98 32 87 95 12 40 79 41 13 53 35 48 42 33 75
21 87 89 26 85 59 54 2 24 25 41 46 88 60 63 23 91 62 61 6
94 66 18 57 58 54 93 53 19 16 55 22 51 8 67 20 17 56 21 59
6 19 45 46 7 70 36 2 56 47 33 75 94 50 34 35 73 72 39 5"""


for distance in consecutive_distance(data):
    print(distance)

    
