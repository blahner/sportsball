import numpy as np

class Bracket(object):
    def __init__(self, known = None):
        #self.bracket defines all the boxes and which team goes in which box (either via prediction or ground truth)
        #self.ranking lists the ranks of each team. Typically this is the team's seed except for the 16 seeds, where it is artificially deflated
        #self.matchups defines which boxes play for which box i.e. the gameflow of the bracket
        #self.scoring defines how many points are assigned to each game
        #self.
        if known:
            self.bracket = known
        else:
            self.bracket = { #values are the team names e.g. QuadNWTeamA
                "round0QuadNWA": "QuadNWTeamA", #initial 64 teams and their boxes
                "round0QuadNWB": "QuadNWTeamB",
                "round0QuadNWC": "QuadNWTeamC",
                "round0QuadNWD": "QuadNWTeamD",
                "round0QuadNWE": "QuadNWTeamE",
                "round0QuadNWF": "QuadNWTeamF",
                "round0QuadNWG": "QuadNWTeamG",
                "round0QuadNWH": "QuadNWTeamH",
                "round0QuadNWI": "QuadNWTeamI",
                "round0QuadNWJ": "QuadNWTeamJ",
                "round0QuadNWK": "QuadNWTeamK",
                "round0QuadNWL": "QuadNWTeamL",
                "round0QuadNWM": "QuadNWTeamM",
                "round0QuadNWN": "QuadNWTeamN",
                "round0QuadNWO": "QuadNWTeamO",
                "round0QuadNWP": "QuadNWTeamP",

                "round0QuadNEA": "QuadNETeamA",
                "round0QuadNEB": "QuadNETeamB",
                "round0QuadNEC": "QuadNETeamC",
                "round0QuadNED": "QuadNETeamD",
                "round0QuadNEE": "QuadNETeamE",
                "round0QuadNEF": "QuadNETeamF",
                "round0QuadNEG": "QuadNETeamG",
                "round0QuadNEH": "QuadNETeamH",
                "round0QuadNEI": "QuadNETeamI",
                "round0QuadNEJ": "QuadNETeamJ",
                "round0QuadNEK": "QuadNETeamK",
                "round0QuadNEL": "QuadNETeamL",
                "round0QuadNEM": "QuadNETeamM",
                "round0QuadNEN": "QuadNETeamN",
                "round0QuadNEO": "QuadNETeamO",
                "round0QuadNEP": "QuadNETeamP",

                "round0QuadSWA": "QuadSWTeamA",
                "round0QuadSWB": "QuadSWTeamB",
                "round0QuadSWC": "QuadSWTeamC",
                "round0QuadSWD": "QuadSWTeamD",
                "round0QuadSWE": "QuadSWTeamE",
                "round0QuadSWF": "QuadSWTeamF",
                "round0QuadSWG": "QuadSWTeamG",
                "round0QuadSWH": "QuadSWTeamH",
                "round0QuadSWI": "QuadSWTeamI",
                "round0QuadSWJ": "QuadSWTeamJ",
                "round0QuadSWK": "QuadSWTeamK",
                "round0QuadSWL": "QuadSWTeamL",
                "round0QuadSWM": "QuadSWTeamM",
                "round0QuadSWN": "QuadSWTeamN",
                "round0QuadSWO": "QuadSWTeamO",
                "round0QuadSWP": "QuadSWTeamP",

                "round0QuadSEA": "QuadSETeamA",
                "round0QuadSEB": "QuadSETeamB",
                "round0QuadSEC": "QuadSETeamC",
                "round0QuadSED": "QuadSETeamD",
                "round0QuadSEE": "QuadSETeamE",
                "round0QuadSEF": "QuadSETeamF",
                "round0QuadSEG": "QuadSETeamG",
                "round0QuadSEH": "QuadSETeamH",
                "round0QuadSEI": "QuadSETeamI",
                "round0QuadSEJ": "QuadSETeamJ",
                "round0QuadSEK": "QuadSETeamK",
                "round0QuadSEL": "QuadSETeamL",
                "round0QuadSEM": "QuadSETeamM",
                "round0QuadSEN": "QuadSETeamN",
                "round0QuadSEO": "QuadSETeamO",
                "round0QuadSEP": "QuadSETeamP",

                "round1QuadNWA": '', #start round 1
                "round1QuadNWB": '', 
                "round1QuadNWC": '', 
                "round1QuadNWD": '', 
                "round1QuadNWE": '', 
                "round1QuadNWF": '', 
                "round1QuadNWG": '', 
                "round1QuadNWH": '', 

                "round1QuadNEA": '', 
                "round1QuadNEB": '', 
                "round1QuadNEC": '', 
                "round1QuadNED": '', 
                "round1QuadNEE": '', 
                "round1QuadNEF": '', 
                "round1QuadNEG": '', 
                "round1QuadNEH": '', 

                "round1QuadSWA": '', 
                "round1QuadSWB": '', 
                "round1QuadSWC": '', 
                "round1QuadSWD": '', 
                "round1QuadSWE": '', 
                "round1QuadSWF": '', 
                "round1QuadSWG": '', 
                "round1QuadSWH": '', 

                "round1QuadSEA": '', 
                "round1QuadSEB": '', 
                "round1QuadSEC": '', 
                "round1QuadSED": '', 
                "round1QuadSEE": '', 
                "round1QuadSEF": '', 
                "round1QuadSEG": '', 
                "round1QuadSEH": '',  #end round 1

                "round2QuadNWA": '',  #start round 2
                "round2QuadNWB": '', 
                "round2QuadNWC": '', 
                "round2QuadNWD": '', 

                "round2QuadNEA": '', 
                "round2QuadNEB": '', 
                "round2QuadNEC": '', 
                "round2QuadNED": '', 

                "round2QuadSWA": '', 
                "round2QuadSWB": '', 
                "round2QuadSWC": '', 
                "round2QuadSWD": '', 

                "round2QuadSEA": '', 
                "round2QuadSEB": '', 
                "round2QuadSEC": '', 
                "round2QuadSED": '',  #end round 2

                "round3QuadNWA": '',  #start round 3
                "round3QuadNWB": '', 

                "round3QuadNEA": '', 
                "round3QuadNEB": '', 

                "round3QuadSWA": '', 
                "round3QuadSWB": '', 

                "round3QuadSEA": '', 
                "round3QuadSEB": '',  #end round 3

                "round4QuadNWA": '',  #start round 4
                "round4QuadNEA": '', 
                "round4QuadSWA": '', 
                "round4QuadSEA": '',  #end round 4

                "round5SemiFinalsWest": '',  #start round 5
                "round5SemiFinalsEast": '',  #end round 5

                "round6Finals": '' #round 6 finals
            }
        self.ranking = { #defines the rank/seed of the 64 teams used in the calculations (not necessarily the truth)
            "QuadNWTeamA": 1,
            "QuadNWTeamB": 30, #artificially deflated ranking of 16th seed
            "QuadNWTeamC": 8,
            "QuadNWTeamD": 9,
            "QuadNWTeamE": 5,
            "QuadNWTeamF": 12,
            "QuadNWTeamG": 4,
            "QuadNWTeamH": 13,
            "QuadNWTeamI": 6,
            "QuadNWTeamJ": 11,
            "QuadNWTeamK": 3,
            "QuadNWTeamL": 14,
            "QuadNWTeamM": 7,
            "QuadNWTeamN": 10,
            "QuadNWTeamO": 2,
            "QuadNWTeamP": 15,

            "QuadNETeamA": 1,
            "QuadNETeamB": 30, #artificially deflated ranking of 16th seed
            "QuadNETeamC": 8,
            "QuadNETeamD": 9,
            "QuadNETeamE": 5,
            "QuadNETeamF": 12,
            "QuadNETeamG": 4,
            "QuadNETeamH": 13,
            "QuadNETeamI": 6,
            "QuadNETeamJ": 11,
            "QuadNETeamK": 3,
            "QuadNETeamL": 14,
            "QuadNETeamM": 7,
            "QuadNETeamN": 10,
            "QuadNETeamO": 2,
            "QuadNETeamP": 15,

            "QuadSWTeamA": 1,
            "QuadSWTeamB": 30, #artificially deflated ranking of 16th seed
            "QuadSWTeamC": 8,
            "QuadSWTeamD": 9,
            "QuadSWTeamE": 5,
            "QuadSWTeamF": 12,
            "QuadSWTeamG": 4,
            "QuadSWTeamH": 13,
            "QuadSWTeamI": 6,
            "QuadSWTeamJ": 11,
            "QuadSWTeamK": 3,
            "QuadSWTeamL": 14,
            "QuadSWTeamM": 7,
            "QuadSWTeamN": 10,
            "QuadSWTeamO": 2,
            "QuadSWTeamP": 15,

            "QuadSETeamA": 1,
            "QuadSETeamB": 30, #artificially deflated ranking of 16th seed
            "QuadSETeamC": 8,
            "QuadSETeamD": 9,
            "QuadSETeamE": 5,
            "QuadSETeamF": 12,
            "QuadSETeamG": 4,
            "QuadSETeamH": 13,
            "QuadSETeamI": 6,
            "QuadSETeamJ": 11,
            "QuadSETeamK": 3,
            "QuadSETeamL": 14,
            "QuadSETeamM": 7,
            "QuadSETeamN": 10,
            "QuadSETeamO": 2,
            "QuadSETeamP": 15,
        }
        self.matchup = {
            "round1QuadNWA": ["round0QuadNWA","round0QuadNWB"], #start round 1
            "round1QuadNWB": ["round0QuadNWC","round0QuadNWD"], 
            "round1QuadNWC": ["round0QuadNWE","round0QuadNWF"], 
            "round1QuadNWD": ["round0QuadNWG","round0QuadNWH"],
            "round1QuadNWE": ["round0QuadNWI","round0QuadNWJ"], 
            "round1QuadNWF": ["round0QuadNWK","round0QuadNWL"],
            "round1QuadNWG": ["round0QuadNWM","round0QuadNWN"], 
            "round1QuadNWH": ["round0QuadNWO","round0QuadNWP"],

            "round1QuadNEA": ["round0QuadNEA","round0QuadNEB"],
            "round1QuadNEB": ["round0QuadNEC","round0QuadNED"], 
            "round1QuadNEC": ["round0QuadNEE","round0QuadNEF"], 
            "round1QuadNED": ["round0QuadNEG","round0QuadNEH"],
            "round1QuadNEE": ["round0QuadNEI","round0QuadNEJ"],
            "round1QuadNEF": ["round0QuadNEK","round0QuadNEL"], 
            "round1QuadNEG": ["round0QuadNEM","round0QuadNEN"], 
            "round1QuadNEH": ["round0QuadNEO","round0QuadNEP"], 

            "round1QuadSWA": ["round0QuadSWA","round0QuadSWB"], 
            "round1QuadSWB": ["round0QuadSWC","round0QuadSWD"],
            "round1QuadSWC": ["round0QuadSWE","round0QuadSWF"],
            "round1QuadSWD": ["round0QuadSWG","round0QuadSWH"],
            "round1QuadSWE": ["round0QuadSWI","round0QuadSWJ"], 
            "round1QuadSWF": ["round0QuadSWK","round0QuadSWL"],
            "round1QuadSWG": ["round0QuadSWM","round0QuadSWN"], 
            "round1QuadSWH": ["round0QuadSWO","round0QuadSWP"], 

            "round1QuadSEA": ["round0QuadSEA","round0QuadSEB"],
            "round1QuadSEB": ["round0QuadSEC","round0QuadSED"], 
            "round1QuadSEC": ["round0QuadSEE","round0QuadSEF"],
            "round1QuadSED": ["round0QuadSEG","round0QuadSEH"],
            "round1QuadSEE": ["round0QuadSEI","round0QuadSEJ"], 
            "round1QuadSEF": ["round0QuadSEK","round0QuadSEL"],
            "round1QuadSEG": ["round0QuadSEM","round0QuadSEN"],
            "round1QuadSEH": ["round0QuadSEO","round0QuadSEP"],  #end round 1

            "round2QuadNWA": ["round1QuadNWA","round1QuadNWB"],  #start round 2
            "round2QuadNWB": ["round1QuadNWC","round1QuadNWD"], 
            "round2QuadNWC": ["round1QuadNWE","round1QuadNWF"],
            "round2QuadNWD": ["round1QuadNWG","round1QuadNWH"], 

            "round2QuadNEA": ["round1QuadNEA","round1QuadNEB"], 
            "round2QuadNEB": ["round1QuadNEC","round1QuadNED"], 
            "round2QuadNEC": ["round1QuadNEE","round1QuadNEF"],
            "round2QuadNED": ["round1QuadNEG","round1QuadNEH"],

            "round2QuadSWA": ["round1QuadSWA","round1QuadSWB"], 
            "round2QuadSWB": ["round1QuadSWC","round1QuadSWD"], 
            "round2QuadSWC": ["round1QuadSWE","round1QuadSWF"], 
            "round2QuadSWD": ["round1QuadSWG","round1QuadSWH"], 

            "round2QuadSEA": ["round1QuadSEA","round1QuadSEB"], 
            "round2QuadSEB": ["round1QuadSEC","round1QuadSED"],
            "round2QuadSEC": ["round1QuadSEE","round1QuadSEF"], 
            "round2QuadSED": ["round1QuadSEG","round1QuadSEH"],  #end round 2

            "round3QuadNWA": ["round2QuadNWA","round2QuadNWB"],  #start round 3
            "round3QuadNWB": ["round2QuadNWC","round2QuadNWD"], 

            "round3QuadNEA": ["round2QuadNEA","round2QuadNEB"], 
            "round3QuadNEB": ["round2QuadNEC","round2QuadNED"],

            "round3QuadSWA": ["round2QuadSWA","round2QuadSWB"], 
            "round3QuadSWB": ["round2QuadSWC","round2QuadSWD"], 

            "round3QuadSEA": ["round2QuadSEA","round2QuadSEB"], 
            "round3QuadSEB": ["round2QuadSEC","round2QuadSED"],  #end round 3

            "round4QuadNWA": ["round3QuadNWA","round3QuadNWB"],  #start round 4
            "round4QuadNEA": ["round3QuadNEA","round3QuadNEB"], 
            "round4QuadSWA": ["round3QuadSWA","round3QuadSWB"],
            "round4QuadSEA": ["round3QuadSEA","round3QuadSEB"],  #end round 4

            "round5SemiFinalsWest": ["round4QuadNWA","round4QuadSWA"],  #start round 5
            "round5SemiFinalsEast": ["round4QuadNEA","round4QuadSEA"], #end round 5

            "round6Finals": ["round5SemiFinalsWest","round5SemiFinalsEast"] #round 6 finals
        }

        self.scoring = {"round1": 1, "round2": 2, "round3": 4, "round4": 8, "round5": 16, "round6": 32} #points earned per win in each of the rounds

    def getBracket(self):
        return self.bracket.copy()

    def Generate(self, method="sportsball"):
        #generates probabilistic match winners
        for game in self.matchup.keys():
            if method == "sportsball":
                winner = self.play_game_sportsball(game)
            elif method == "cointoss":
                winner = self.play_game_cointoss(game)
            elif method == "highseed":
                winner = self.play_game_highseed(game)
            self.bracket[game] = winner #update the bracket with the team name that won this box
        return None

    def play_game_sportsball(self, game):
        #sportsball method.
        boxes = self.matchup[game] #get the boxes that are playing
        team1_name = self.bracket[boxes[0]] #get the team name in the box
        team2_name = self.bracket[boxes[1]]
        team1_rank = self.ranking[team1_name]
        team2_rank = self.ranking[team2_name]

        total_rank = team1_rank + team2_rank
        winner = np.random.choice([team1_name, team2_name], p=[team2_rank/total_rank, team1_rank/total_rank])
        return winner

    def play_game_cointoss(self, game):
        #50/50 chance each game
        boxes = self.matchup[game] #get the boxes that are playing
        team1_name = self.bracket[boxes[0]] #get the team name in the box
        team2_name = self.bracket[boxes[1]]
        assert(team1_name != team2_name)
        winner = np.random.choice([team1_name, team2_name], p=[0.5, 0.5])
        return winner

    def play_game_highseed(self, game):
        #high seed always wins. equal seed is a 50/50 tossup
        boxes = self.matchup[game] #get the boxes that are playing
        team1_name = self.bracket[boxes[0]] #get the team name in the box
        team2_name = self.bracket[boxes[1]]
        team1_rank = self.ranking[team1_name]
        team2_rank = self.ranking[team2_name]
        if team1_rank > team2_rank:
            winner = team2_name
        elif team1_rank < team2_rank:
            winner = team1_name
        elif team1_rank == team2_rank:
            winner = np.random.choice([team1_name, team2_name], p=[0.5, 0.5])
        
        return winner

    def score(self, truth):
        assert(isinstance(truth, Bracket))
        round_score = {"round1": 0, "round2": 0, "round3": 0, "round4": 0, "round5": 0, "round6": 0}
        pred_bracket = self.getBracket()
        truth_bracket = truth.getBracket()
        for game in self.matchup.keys():
            pred_winner = pred_bracket[game]
            truth_winner = truth_bracket[game]
            if pred_winner == truth_winner:
                round = game.split('round')[1][0] #only works since rounds are 1-6. find a better solution
                round_score["round" + round] += self.scoring["round" + round]
        final_score = np.array(list(round_score.values())).sum()
        return final_score, round_score

    def __str__(self):
        return print(self.getBracket())