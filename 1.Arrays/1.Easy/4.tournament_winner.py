# competitions array has element in the form of [homeTeam,awayTeam]
# results array has winning team 0: awayTeam won, 1: homeTeam won
# team receievs 3 pts if wins else 0 points
# each team faces off against all other teams, no ties allowed, winner of tournament receievs highest points
# Find the winner

# input : 
    # competitions : [["HTML","C#"],
    # ["C#","Python"],
    # ["Python","HTML"]]

    # results : [0, 0, 1]
# output :
    # "Python"

# 1.initialize currentBestTeam and scores
# 2.iterate over competitions array and find winningteam
# 3.update scores of winningteam and compare currentbest team and winning team scores
# 4.return currentbestteam

# time : O(n) n: no of competitions | space : O(k) k: number of teams
HOME_TEAM_WON = 1
def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam : 0}

    for i,competition in enumerate(competitions):
        result = results[i]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScore(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
    
    return currentBestTeam

def updateScore(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points

