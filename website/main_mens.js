var ready = (callback) => { //for the display image
    if (document.readyState != "loading") callback();
    else document.addEventListener("DOMContentLoaded", callback);
}
ready(() => {
    document.querySelector(".header").style.height = window.innerHeight + "px";
})
//const adjectives = ["Super","Curvy","Small","Terrific","Grumpy"]
//const nouns = ["Thomas","Giraffe","Turtle","Monk"]
const btn_mens = document.getElementById("btn_mens");
const competitors = { //defines which blocks play each other for each game in the bracket
    "QuadNWRound32LetterA": ["QuadNWRound64LetterA","QuadNWRound64LetterB"], //round32A
    "QuadNERound32LetterA": ["QuadNERound64LetterA","QuadNERound64LetterB"],
    "QuadSWRound32LetterA": ["QuadSWRound64LetterA","QuadSWRound64LetterB"],
    "QuadSERound32LetterA": ["QuadSERound64LetterA","QuadSERound64LetterB"],

    "QuadNWRound32LetterB": ["QuadNWRound64LetterC","QuadNWRound64LetterD"], //round32B
    "QuadNERound32LetterB": ["QuadNERound64LetterC","QuadNERound64LetterD"],
    "QuadSWRound32LetterB": ["QuadSWRound64LetterC","QuadSWRound64LetterD"],
    "QuadSERound32LetterB": ["QuadSERound64LetterC","QuadSERound64LetterD"],

    "QuadNWRound32LetterC": ["QuadNWRound64LetterE","QuadNWRound64LetterF"], //round32C
    "QuadNERound32LetterC": ["QuadNERound64LetterE","QuadNERound64LetterF"],
    "QuadSWRound32LetterC": ["QuadSWRound64LetterE","QuadSWRound64LetterF"],
    "QuadSERound32LetterC": ["QuadSERound64LetterE","QuadSERound64LetterF"],

    "QuadNWRound32LetterD": ["QuadNWRound64LetterG","QuadNWRound64LetterH"], //round32D
    "QuadNERound32LetterD": ["QuadNERound64LetterG","QuadNERound64LetterH"],
    "QuadSWRound32LetterD": ["QuadSWRound64LetterG","QuadSWRound64LetterH"],
    "QuadSERound32LetterD": ["QuadSERound64LetterG","QuadSERound64LetterH"],

    "QuadNWRound32LetterE": ["QuadNWRound64LetterI","QuadNWRound64LetterJ"], //round32E
    "QuadNERound32LetterE": ["QuadNERound64LetterI","QuadNERound64LetterJ"],
    "QuadSWRound32LetterE": ["QuadSWRound64LetterI","QuadSWRound64LetterJ"],
    "QuadSERound32LetterE": ["QuadSERound64LetterI","QuadSERound64LetterJ"],

    "QuadNWRound32LetterF": ["QuadNWRound64LetterK","QuadNWRound64LetterL"], //round32F
    "QuadNERound32LetterF": ["QuadNERound64LetterK","QuadNERound64LetterL"],
    "QuadSWRound32LetterF": ["QuadSWRound64LetterK","QuadSWRound64LetterL"],
    "QuadSERound32LetterF": ["QuadSERound64LetterK","QuadSERound64LetterL"],

    "QuadNWRound32LetterG": ["QuadNWRound64LetterM","QuadNWRound64LetterN"], //round32G
    "QuadNERound32LetterG": ["QuadNERound64LetterM","QuadNERound64LetterN"],
    "QuadSWRound32LetterG": ["QuadSWRound64LetterM","QuadSWRound64LetterN"],
    "QuadSERound32LetterG": ["QuadSERound64LetterM","QuadSERound64LetterN"],

    "QuadNWRound32LetterH": ["QuadNWRound64LetterO","QuadNWRound64LetterP"], //round32H
    "QuadNERound32LetterH": ["QuadNERound64LetterO","QuadNERound64LetterP"],
    "QuadSWRound32LetterH": ["QuadSWRound64LetterO","QuadSWRound64LetterP"],
    "QuadSERound32LetterH": ["QuadSERound64LetterO","QuadSERound64LetterP"],

    "QuadNWRound16LetterA": ["QuadNWRound32LetterA","QuadNWRound32LetterB"], //round16A
    "QuadNERound16LetterA": ["QuadNERound32LetterA","QuadNERound32LetterB"],
    "QuadSWRound16LetterA": ["QuadSWRound32LetterA","QuadSWRound32LetterB"],
    "QuadSERound16LetterA": ["QuadSERound32LetterA","QuadSERound32LetterB"],

    "QuadNWRound16LetterB": ["QuadNWRound32LetterC","QuadNWRound32LetterD"], //round16B
    "QuadNERound16LetterB": ["QuadNERound32LetterC","QuadNERound32LetterD"],
    "QuadSWRound16LetterB": ["QuadSWRound32LetterC","QuadSWRound32LetterD"],
    "QuadSERound16LetterB": ["QuadSERound32LetterC","QuadSERound32LetterD"],

    "QuadNWRound16LetterC": ["QuadNWRound32LetterE","QuadNWRound32LetterF"], //round16C
    "QuadNERound16LetterC": ["QuadNERound32LetterE","QuadNERound32LetterF"],
    "QuadSWRound16LetterC": ["QuadSWRound32LetterE","QuadSWRound32LetterF"],
    "QuadSERound16LetterC": ["QuadSERound32LetterE","QuadSERound32LetterF"],

    "QuadNWRound16LetterD": ["QuadNWRound32LetterG","QuadNWRound32LetterH"], //round16D
    "QuadNERound16LetterD": ["QuadNERound32LetterG","QuadNERound32LetterH"],
    "QuadSWRound16LetterD": ["QuadSWRound32LetterG","QuadSWRound32LetterH"],
    "QuadSERound16LetterD": ["QuadSERound32LetterG","QuadSERound32LetterH"],

    "QuadNWRound8LetterA": ["QuadNWRound16LetterA","QuadNWRound16LetterB"], //round8A
    "QuadNERound8LetterA": ["QuadNERound16LetterA","QuadNERound16LetterB"],
    "QuadSWRound8LetterA": ["QuadSWRound16LetterA","QuadSWRound16LetterB"],
    "QuadSERound8LetterA": ["QuadSERound16LetterA","QuadSERound16LetterB"],

    "QuadNWRound8LetterB": ["QuadNWRound16LetterC","QuadNWRound16LetterD"], //round8B
    "QuadNERound8LetterB": ["QuadNERound16LetterC","QuadNERound16LetterD"],
    "QuadSWRound8LetterB": ["QuadSWRound16LetterC","QuadSWRound16LetterD"],
    "QuadSERound8LetterB": ["QuadSERound16LetterC","QuadSERound16LetterD"],

    "QuadNWRound4LetterA": ["QuadNWRound8LetterA","QuadNWRound8LetterB"], //round4A
    "QuadNERound4LetterA": ["QuadNERound8LetterA","QuadNERound8LetterB"],
    "QuadSWRound4LetterA": ["QuadSWRound8LetterA","QuadSWRound8LetterB"],
    "QuadSERound4LetterA": ["QuadSERound8LetterA","QuadSERound8LetterB"],

    "SemiFinalsWest": ["QuadNWRound4LetterA","QuadSWRound4LetterA"], //Semi-Finals
    "SemiFinalsEast": ["QuadNERound4LetterA","QuadSERound4LetterA"],

    "Finals": ["SemiFinalsWest","SemiFinalsEast"], //Finals
}; 
let ranking = { //defines the initial rankings of each box
    "QuadNWRound64LetterA": 1, //NW Round 64
    "QuadNWRound64LetterB": 30, //artificially deflate the chances that a 16 seed will win. 1/17 is too big
    "QuadNWRound64LetterC": 8,
    "QuadNWRound64LetterD": 9,
    "QuadNWRound64LetterE": 5,
    "QuadNWRound64LetterF": 12,
    "QuadNWRound64LetterG": 4,
    "QuadNWRound64LetterH": 13,
    "QuadNWRound64LetterI": 6,
    "QuadNWRound64LetterJ": 11,
    "QuadNWRound64LetterK": 3,
    "QuadNWRound64LetterL": 14,
    "QuadNWRound64LetterM": 7,
    "QuadNWRound64LetterN": 10,
    "QuadNWRound64LetterO": 2,
    "QuadNWRound64LetterP": 15,
    "QuadNWRound32LetterA": 0, //NW Round 32
    "QuadNWRound32LetterB": 0, 
    "QuadNWRound32LetterC": 0,
    "QuadNWRound32LetterD": 0,
    "QuadNWRound32LetterE": 0,
    "QuadNWRound32LetterF": 0,
    "QuadNWRound32LetterG": 0,
    "QuadNWRound32LetterH": 0,
    "QuadNWRound16LetterA": 0, //NW Round 16
    "QuadNWRound16LetterB": 0,
    "QuadNWRound16LetterC": 0,
    "QuadNWRound16LetterD": 0,
    "QuadNWRound8LetterA": 0, //NW Round 8
    "QuadNWRound8LetterB": 0,
    "QuadNWRound4LetterA": 0, //NW Round 4

    "QuadSWRound64LetterA": 1, //SW Round 64
    "QuadSWRound64LetterB": 30, //artificially deflate the chances that a 16 seed will win. 1/17 is too big
    "QuadSWRound64LetterC": 8,
    "QuadSWRound64LetterD": 9,
    "QuadSWRound64LetterE": 5,
    "QuadSWRound64LetterF": 12,
    "QuadSWRound64LetterG": 4,
    "QuadSWRound64LetterH": 13,
    "QuadSWRound64LetterI": 6,
    "QuadSWRound64LetterJ": 11,
    "QuadSWRound64LetterK": 3,
    "QuadSWRound64LetterL": 14,
    "QuadSWRound64LetterM": 7,
    "QuadSWRound64LetterN": 10,
    "QuadSWRound64LetterO": 2,
    "QuadSWRound64LetterP": 15,
    "QuadSWRound32LetterA": 0, //SW Round 32
    "QuadSWRound32LetterB": 0,
    "QuadSWRound32LetterC": 0,
    "QuadSWRound32LetterD": 0,
    "QuadSWRound32LetterE": 0,
    "QuadSWRound32LetterF": 0,
    "QuadSWRound32LetterG": 0,
    "QuadSWRound32LetterH": 0,
    "QuadSWRound16LetterA": 0, //SW Round 16
    "QuadSWRound16LetterB": 0,
    "QuadSWRound16LetterC": 0,
    "QuadSWRound16LetterD": 0,
    "QuadSWRound8LetterA": 0, //SW Round 8
    "QuadSWRound8LetterB": 0,
    "QuadSWRound4LetterA": 0, //SW Round 4

    "QuadNERound64LetterA": 1, //NE Round 64
    "QuadNERound64LetterB": 30, //artificially deflate the chances that a 16 seed will win. 1/17 is too big
    "QuadNERound64LetterC": 8,
    "QuadNERound64LetterD": 9,
    "QuadNERound64LetterE": 5,
    "QuadNERound64LetterF": 12,
    "QuadNERound64LetterG": 4,
    "QuadNERound64LetterH": 13,
    "QuadNERound64LetterI": 6,
    "QuadNERound64LetterJ": 11,
    "QuadNERound64LetterK": 3,
    "QuadNERound64LetterL": 14,
    "QuadNERound64LetterM": 7,
    "QuadNERound64LetterN": 10,
    "QuadNERound64LetterO": 2,
    "QuadNERound64LetterP": 15,
    "QuadNERound32LetterA": 0, //NE Round 32
    "QuadNERound32LetterB": 0,
    "QuadNERound32LetterC": 0,
    "QuadNERound32LetterD": 0,
    "QuadNERound32LetterE": 0,
    "QuadNERound32LetterF": 0,
    "QuadNERound32LetterG": 0,
    "QuadNERound32LetterH": 0,
    "QuadNERound16LetterA": 0, //NE Round 16
    "QuadNERound16LetterB": 0,
    "QuadNERound16LetterC": 0,
    "QuadNERound16LetterD": 0,
    "QuadNERound8LetterA": 0, //NE Round 8
    "QuadNERound8LetterB": 0,
    "QuadNERound4LetterA": 0, //NE Round 4

    "QuadSERound64LetterA": 1, //SE Round 64
    "QuadSERound64LetterB": 30, //artificially deflate the chances that a 16 seed will win. 1/17 is too big
    "QuadSERound64LetterC": 8,
    "QuadSERound64LetterD": 9,
    "QuadSERound64LetterE": 5,
    "QuadSERound64LetterF": 12,
    "QuadSERound64LetterG": 4,
    "QuadSERound64LetterH": 13,
    "QuadSERound64LetterI": 6,
    "QuadSERound64LetterJ": 11,
    "QuadSERound64LetterK": 3,
    "QuadSERound64LetterL": 14,
    "QuadSERound64LetterM": 7,
    "QuadSERound64LetterN": 10,
    "QuadSERound64LetterO": 2,
    "QuadSERound64LetterP": 15,
    "QuadSERound32LetterA": 0, //SE Round 32
    "QuadSERound32LetterB": 0,
    "QuadSERound32LetterC": 0,
    "QuadSERound32LetterD": 0,
    "QuadSERound32LetterE": 0,
    "QuadSERound32LetterF": 0,
    "QuadSERound32LetterG": 0,
    "QuadSERound32LetterH": 0,
    "QuadSERound16LetterA": 0, //SE Round 16
    "QuadSERound16LetterB": 0,
    "QuadSERound16LetterC": 0,
    "QuadSERound16LetterD": 0,
    "QuadSERound8LetterA": 0, //SE Round 8
    "QuadSERound8LetterB": 0,
    "QuadSERound4LetterA": 0, //SE Round 4

    "SemiFinalsWest": 0, //SemiFinals west
    "SemiFinalsEast": 0, //SemiFinals east
    "Finals": 0,
};  //maps the bracket to seed
const match_list = [ //Do the rounds first
    "QuadNWRound32LetterA", //NW first round
    "QuadNWRound32LetterB",
    "QuadNWRound32LetterC",
    "QuadNWRound32LetterD",
    "QuadNWRound32LetterE",
    "QuadNWRound32LetterF",
    "QuadNWRound32LetterG",
    "QuadNWRound32LetterH",
    "QuadNERound32LetterA", //NE first round
    "QuadNERound32LetterB",
    "QuadNERound32LetterC",
    "QuadNERound32LetterD",
    "QuadNERound32LetterE",
    "QuadNERound32LetterF",
    "QuadNERound32LetterG",
    "QuadNERound32LetterH",
    "QuadSWRound32LetterA", //SW first round
    "QuadSWRound32LetterB",
    "QuadSWRound32LetterC",
    "QuadSWRound32LetterD",
    "QuadSWRound32LetterE",
    "QuadSWRound32LetterF",
    "QuadSWRound32LetterG",
    "QuadSWRound32LetterH",
    "QuadSERound32LetterA", //SE first round
    "QuadSERound32LetterB",
    "QuadSERound32LetterC",
    "QuadSERound32LetterD",
    "QuadSERound32LetterE",
    "QuadSERound32LetterF",
    "QuadSERound32LetterG",
    "QuadSERound32LetterH",
    "QuadNWRound16LetterA", //NW second round
    "QuadNWRound16LetterB",
    "QuadNWRound16LetterC",
    "QuadNWRound16LetterD",
    "QuadNERound16LetterA", //NE second round
    "QuadNERound16LetterB",
    "QuadNERound16LetterC",
    "QuadNERound16LetterD",
    "QuadSWRound16LetterA", //SW second round
    "QuadSWRound16LetterB",
    "QuadSWRound16LetterC",
    "QuadSWRound16LetterD",
    "QuadSERound16LetterA", //SE second round
    "QuadSERound16LetterB",
    "QuadSERound16LetterC",
    "QuadSERound16LetterD",
    "QuadNWRound8LetterA", //NW third round
    "QuadNWRound8LetterB",
    "QuadNERound8LetterA", //NE third round
    "QuadNERound8LetterB",
    "QuadSWRound8LetterA", //SW third round
    "QuadSWRound8LetterB",
    "QuadSERound8LetterA", //SE third round
    "QuadSERound8LetterB",
    "QuadNWRound4LetterA", //NW fourth round, quad champion
    "QuadNERound4LetterA", //NE fourth round, quad champion
    "QuadSWRound4LetterA", //SW fourth round, quad champion
    "QuadSERound4LetterA", //SE fourth round, quad champion
    "SemiFinalsWest", //Semifinals West
    "SemiFinalsEast", //Semifinals East
    "Finals", //Finals
]
btn_mens.addEventListener("click", function () { //with each match, both the text (team name) and the ranking of the winning team need to propagate forward and get assigned to the next box.
    for (let m = 0; m<match_list.length; m++) {
        let match = match_list[m] //define the box that we are deciding the winners of
        let contest = competitors[match] //grab the IDs of the two boxes (teams) competing for the current box
        let winner = playGame(contest, ranking)  
        document.getElementById(match).innerHTML = winner[1]; //propagate the winner's box text (i.e. team name) forward
        ranking[match] = ranking[winner[0]] //assign the current box's ranking as the winners ranking
    }
    let finalScore = predictFinalScore(65,90)
    document.getElementById("FinalScore").innerHTML = "Final Score: " + finalScore[0] + " - " + finalScore[1]
    //let bracketName = generateBracketName(adjectives, nouns)
    let bracketName = generateBracketName(adjectiveList, nounList) //lists are from external javascript file
    document.getElementById("BracketName").innerHTML = bracketName
});
function playGame(contest, ranking) { //teamA_seed/total_seed represents team B's chance of winning
    let total_rank = ranking[contest[0]] + ranking[contest[1]] //adds the two teams' seeds together
    let randNumber = Math.random() //generate random number between 0 and 1
    let boxID
    let winnerBoxText
    if (randNumber < ranking[contest[0]]/total_rank) { //if the random number is below the percent of total rank from the first team,
        boxID = contest[1]
        winnerBoxText = document.getElementById(boxID).textContent; //grab the winners box text to propagate forward
    } else {
        boxID = contest[0]
        winnerBoxText = document.getElementById(boxID).textContent; //grab the winners box text to propagate forward
    }
    const winner = [boxID, winnerBoxText]
    return winner
}
function predictFinalScore(min, max) { //predicts the final score of the championship game for a tiebreaker
    let score1 = Math.floor(Math.random() * (max - min + 1) + min)
    let score2 = Math.floor(Math.random() * (max - min + 1) + min)
    if (score1 == score2) {
        score2 = score2 - 1
    }
    if (score1 > score2) {
        return [score1, score2] //winning score first in array
    } else {
        return [score2, score1]
    }
}
function generateBracketName(adj, noun) { //generates a random bracket name from an adjective and noun
    let randAdjSmall = adj[Math.floor(Math.random() * adj.length)]
    let randAdj = randAdjSmall.charAt(0).toUpperCase() + randAdjSmall.slice(1); //make first letter uppercase
    let randNounSmall = noun[Math.floor(Math.random() * noun.length)]
    let randNoun = randNounSmall.charAt(0).toUpperCase() + randNounSmall.slice(1); 
    return randAdj + randNoun
}