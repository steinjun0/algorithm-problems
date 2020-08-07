i = input().split(" ")

i = list(map(int, i))

N, newScore, P = i[0], i[1], i[2]

flag = False

if N > 0:
    nowRanking = input().split(" ")

elif N == 0:
    print(1)
    flag = True
    exit()

if P == 0:
    print(-1)
    flag = True
    exit()

nowRanking = list(map(int, nowRanking))

nowRanking.sort()
nowRanking.reverse()

nowRankingMember = list(set(nowRanking))
nowRankingMember = list(map(int, nowRankingMember))
nowRankingMember.sort()
nowRankingMember.reverse()

rankSum = 1
rankReal = 1
newScoreRank = -1

for i in nowRankingMember:

    if newScore > i:
        newScoreRank = rankSum
        break

    elif newScore == i:
        newScoreRank = rankSum

        rankSum += nowRanking.count(i)

        if rankSum > P:
            newScoreRank = -1
            break

        else:
            break


    rankSum += nowRanking.count(i)
    
    if rankSum > P:
        break
    
if newScoreRank == -1 and rankSum <= P:
    newScoreRank = rankSum

if flag != True:
    print(newScoreRank)

