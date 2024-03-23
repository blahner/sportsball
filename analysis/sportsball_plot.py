import numpy as np
from model import Bracket
from tqdm import tqdm
import os
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#model sportsballbracket accuracy
#espn winners:
#https://www.printyourbrackets.com/past-bracket-challenge-winning-scores.html
#https://fantasy.espn.com/tournament-challenge-bracket/2022/en/

#avg scores:
#https://www.ncaa.com/news/basketball-men/bracketiq/2021-02-12/heres-how-your-march-madness-bracket-will-do-if-you-only-pick-better-seeded

def hist_plot(data, year, external_scores, savefig = False):
    sns.histplot(data=data, x="BracketScoreTotal", hue="Method", bins=192)
    plt.axvline(np.array(external_scores[year]), color='k', linestyle='dashed') #winners of major bracket challenges
    plt.axvline(192, color='k', linestyle='solid') #perfect bracket line
    
    plt.xlim([0,192])
    plt.title(year)
    plt.xticks(ticks = list(range(0,193,16)))
    if savefig:
        plt.savefig(savefig)
    plt.clf()

def violin_plot(data, year, external_scores, savefig = False):
    sns.violinplot(data=data, x="BracketScoreTotal", y="Method", cut=0, scale='count')
    external_arr = np.array(external_scores[year])
    assert(external_arr.shape[0] > 0)
    plt.vlines([external_arr.min(), external_arr.max()], ymin=0.5, ymax=1.5, color='k', linestyle='dashed') #winners of major bracket challenges
    method2y = {'sportsball': 2, 'cointoss': 1, 'highseed': 0}
    for method in method2y.keys():
        data_meth = data[data["Method"]==method]
        if external_arr.shape[0] == 1: #don't have good external data for these years - estimate a spread
            data_top = data_meth[data_meth["BracketScoreTotal"] > external_arr.min() - 8]
        else:
            data_top = data_meth[data_meth["BracketScoreTotal"] > external_arr.min()]
        #plot points of sportsball brackets in money zone
        if data_top.shape[0] > 0:
            data_top_arr = np.array(data_top['BracketScoreTotal'])
            plt.plot(data_top_arr, np.ones((data_top_arr.shape)) * method2y[method], 'k*')
    
    plt.vlines(192, ymin=0.5, ymax=1.5, color='k', linestyle='solid') #perfect bracket line

    plt.xlim([0,192])
    plt.title(year)
    plt.xticks(ticks = list(range(0,193,16)))
    if savefig:
        plt.savefig(savefig)
    plt.clf()

root = os.path.join("path","to","project","folder") #path to project folder
save_root = os.path.join(root,"results","plots")
pred_root = os.path.join(root, "results", "predictions")
espn_winningscores = {'2022': 171,'2021': 169,'2019': 185,'2018': 167, '2017': 176, '2016':173}  #espn scores mutliply by 10
winningscores = {'2022': [171, 163],'2021': [169, 161],'2019': [185, 184, 178, 177],'2018': [167, 162, 163, 164],
 '2017': [176,170,174,166,171], '2016': [173, 167, 171, 175, 170]}  #change years 2022 and 2021 with info of other brakcet challenges, not estimating the spread
years = ['2022','2021','2019','2018','2017','2016']
methods = ['highseed','cointoss','sportsball']
col = ['Method','BracketScoreTotal','BracketScoreRounds','NumGamesWon']
count = 1000000
for year in years:
    with open(pred_root, "analysis_year-" + year + "_count-" + str(count) + ".pkl",'rb') as f: 
        df = pickle.load(f)
    for method in methods: #print some stats
        data = df[df['Method'] == method]
        tmp_score = np.array(data['BracketScoreTotal'])
        tmp_gameswon = np.array(data['NumGamesWon'])
        print("Method {}: Min - {}, Max - {}, Avg - {}, Median - {}, Avg Perc. Games Won - {}, Number in Money Zone - {}".format(
            method, np.min(tmp_score), np.max(tmp_score), np.mean(tmp_score), np.median(tmp_score),
             np.mean(tmp_gameswon)/63, np.sum(tmp_score>=np.array(winningscores[year]).min())))
        
    #plot a histogram
    #avepath = os.path.join(save_root, "histogram_year-" + year + "_count-" + str(count) + ".svg")
    #hist_plot(df,year, winningscores, savefig = savepath)
    
    #pot a violin plot - better than histogram to see the few top scoring brackets
    savepath = os.path.join(save_root, "violin_year-" + year + "_count-" + str(count) + ".svg")
    violin_plot(df,year, winningscores, savefig = savepath)
