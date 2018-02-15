# https://www.reddit.com/r/dailyprogrammer/comments/7s888w/20180122_challenge_348_easy_the_rabbit_problem/

m_rabbits = [0]*96
f_rabbits = [0]*96

m_start = 2
f_start = 4
total_needed = 15000000000
months = 0

m_rabbits[2] = m_start
f_rabbits[2] = f_start

while 1:
    months += 1
    f_fertile = sum(f_rabbits[4:])
    m_rabbits = [f_fertile*5] + m_rabbits[:-1]
    f_rabbits = [f_fertile*9] + f_rabbits[:-1]
    n = sum(m_rabbits) + sum(f_rabbits)
    if n > total_needed:
        print(n, months)
        break
    
    
    



