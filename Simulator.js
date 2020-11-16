import Game from './Game';

class Simulator {
    constructor(startState) {
        this.setBaseState({
            inning: 1,
            outs: 0,
            awayOrHome: 0,
            bases: [0,0,0],
            score: [0,0],
            gameOn: true
        });
        this.setBaseState(startState); 
    }
    
    setBaseState(newState) {
        Object.assign(this, newState);
    }
    
    simulate(its=100) {
        const gameLog = [];
        let wins = 0;
        for (let i = 0; i < its; i++) {
            const baseState = JSON.parse(JSON.stringify(this));
            let game = new Game(baseState);
            const rez = game.playGame();
            wins += rez.winner;
            gameLog.push(rez);
        }
        console.log(`The home team won ${wins} out of ${its}, for a winning percentage of ${wins / its * 100}%!`);
        return gameLog;
    }

}