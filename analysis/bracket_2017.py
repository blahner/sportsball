import numpy as np
import os
import pickle

def transform_bracket(bracket):
    #goes from bracket seed to letter
    seed2letter = {"1": "A", "2": "O", "3": "K", "4": "G", "5": "E", "6": "I", "7": "M", "8": "C", "9": "D", "10": "N", "11": "J", "12": "F", "13": "H", "14": "L", "15": "P", "16": "B"} #branket seed to letter 
    bracket_tsfm = bracket.copy()
    for k,v in bracket.items():
        if "round0" in k:
            continue
        tmp = v.split("Team")
        num = tmp[1]
        prefix = tmp[0]
        bracket_tsfm[k] = prefix + "Team" + seed2letter[num]
    return bracket_tsfm

bracket = { #values are the team names e.g. QuadNWTeamA
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

    "round1QuadNWA": 'QuadNWTeam1', #start round 1
    "round1QuadNWB": 'QuadNWTeam8',
    "round1QuadNWC": 'QuadNWTeam5',
    "round1QuadNWD": 'QuadNWTeam4',
    "round1QuadNWE": 'QuadNWTeam11', 
    "round1QuadNWF": 'QuadNWTeam3', 
    "round1QuadNWG": 'QuadNWTeam7', 
    "round1QuadNWH": 'QuadNWTeam2',

    "round1QuadNEA": 'QuadNETeam1',
    "round1QuadNEB": 'QuadNETeam9', 
    "round1QuadNEC": 'QuadNETeam5',
    "round1QuadNED": 'QuadNETeam4', 
    "round1QuadNEE": 'QuadNETeam11', 
    "round1QuadNEF": 'QuadNETeam3', 
    "round1QuadNEG": 'QuadNETeam7',
    "round1QuadNEH": 'QuadNETeam2', 

    "round1QuadSWA": 'QuadSWTeam1',
    "round1QuadSWB": 'QuadSWTeam8', 
    "round1QuadSWC": 'QuadSWTeam5', 
    "round1QuadSWD": 'QuadSWTeam4', 
    "round1QuadSWE": 'QuadSWTeam11', 
    "round1QuadSWF": 'QuadSWTeam3', 
    "round1QuadSWG": 'QuadSWTeam7',
    "round1QuadSWH": 'QuadSWTeam2', 

    "round1QuadSEA": 'QuadSETeam1', 
    "round1QuadSEB": 'QuadSETeam8',
    "round1QuadSEC": 'QuadSETeam12',
    "round1QuadSED": 'QuadSETeam4',
    "round1QuadSEE": 'QuadSETeam6', 
    "round1QuadSEF": 'QuadSETeam3', 
    "round1QuadSEG": 'QuadSETeam10',
    "round1QuadSEH": 'QuadSETeam2',  #end round 1

    "round2QuadNWA": 'QuadNWTeam8',  #start round 2
    "round2QuadNWB": 'QuadNWTeam4', 
    "round2QuadNWC": 'QuadNWTeam3', 
    "round2QuadNWD": 'QuadNWTeam7', 

    "round2QuadNEA": 'QuadNETeam1', 
    "round2QuadNEB": 'QuadNETeam4', 
    "round2QuadNEC": 'QuadNETeam3',
    "round2QuadNED": 'QuadNETeam7', 

    "round2QuadSWA": 'QuadSWTeam1', 
    "round2QuadSWB": 'QuadSWTeam4', 
    "round2QuadSWC": 'QuadSWTeam11',
    "round2QuadSWD": 'QuadSWTeam2',

    "round2QuadSEA": 'QuadSETeam1', 
    "round2QuadSEB": 'QuadSETeam4', 
    "round2QuadSEC": 'QuadSETeam3', 
    "round2QuadSED": 'QuadSETeam2',  #end round 2

    "round3QuadNWA": 'QuadNWTeam4',  #start round 3
    "round3QuadNWB": 'QuadNWTeam7', 

    "round3QuadNEA": 'QuadNETeam1', 
    "round3QuadNEB": 'QuadNETeam3',

    "round3QuadSWA": 'QuadSWTeam1', 
    "round3QuadSWB": 'QuadSWTeam11',

    "round3QuadSEA": 'QuadSETeam1', 
    "round3QuadSEB": 'QuadSETeam2',  #end round 3

    "round4QuadNWA": 'QuadNWTeam7',  #start round 4
    "round4QuadNEA": 'QuadNETeam3', 
    "round4QuadSWA": 'QuadSWTeam1', 
    "round4QuadSEA": 'QuadSETeam1',  #end round 4

    "round5SemiFinalsWest": 'QuadSWTeam1',  #start round 5
    "round5SemiFinalsEast": 'QuadSETeam1',  #end round 5

    "round6Finals": 'QuadSETeam1' #round 6 finals
}
root = os.path.join("path","to","project","folder") # change to your path
save_root = os.path.join(root, "results","truth_brackets")
truth = {'2017': transform_bracket(bracket)}
with open(os.path.join(save_root, "truth_2017.pkl"),'wb') as f:
    pickle.dump(truth, f)