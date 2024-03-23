from model import Bracket
from tqdm import tqdm
import pickle
import pandas as pd
import os

#model sportsballbracket accuracy
#espn winners:
#https://www.printyourbrackets.com/past-bracket-challenge-winning-scores.html
#https://fantasy.espn.com/tournament-challenge-bracket/2022/en/

#avg scores:
#https://www.ncaa.com/news/basketball-men/bracketiq/2021-02-12/heres-how-your-march-madness-bracket-will-do-if-you-only-pick-better-seeded

root = os.path.join("path","to","project","folder") #path to project folder
save_root = os.path.join(root, "results","predictions")
bracket_root = os.path.join(root, "results","truth_brackets")
years = ['2022','2021','2019','2018','2017','2016']
methods = ['highseed','cointoss','sportsball']
col = ['Method','BracketScoreTotal','BracketScoreRounds','NumGamesWon']
for year in years:
    print("Year:", year)
    results = {c: [] for c in col}
    with open(bracket_root, "truth_" + year + ".pkl",'rb') as f: #load the real brackets
        truth = pickle.load(f)
    TruthBracket = Bracket(known = truth[year])
    for method in methods:
        tmp_score = []
        tmp_gameswon = [] #in percent
        count = 1000000
        for g in tqdm(range(count)):
            sportsball = Bracket()
            sportsball.Generate(method=method)
            res = sportsball.score(TruthBracket)
            gameswon = res[1]['round1'] + res[1]['round2']/2 + res[1]['round3']/4 + res[1]['round4']/8 + res[1]['round5']/16 + res[1]['round6']/32 
            results['Method'].append(method)
            results['BracketScoreTotal'].append(res[0])
            results['BracketScoreRounds'].append(list(res[1].values()))
            results['NumGamesWon'].append(gameswon)
            del sportsball
    df = pd.DataFrame(results)
    with open(os.path.join(save_root, "analysis_year-" + year + "_count-" + str(count) + ".pkl"),'wb') as f: 
        pickle.dump(df,f)