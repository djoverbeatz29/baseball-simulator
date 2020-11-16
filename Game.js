class Game {
    constructor(params) {
        this.inning=1;
        this.outs=0;
        this.awayOrHome=0;
        this.bases=[0,0,0];
        this.score=[0,0];
        this.gameOn=true;
        this.setGameState(params);
    }
    
    atBat() {
        const outcome = Math.random() * 186518;
        if (outcome < 126600) return 'Out';
        else if (outcome < 144479) return 'BB';
        else if (outcome < 170426) return '1B';
        else if (outcome < 178957) return '2B';
        else if (outcome < 179742) return '3B';
        else return 'HR';
    }
    
    arraySum(array) {
        return array.reduce((sum,element)=>sum+element,0);
    }
    
    walker() {
        this.setGameState({bases: this.bases.concat(0)});
        this.setGameState({bases: this.bases.map((elm,i)=>i===0? elm+1:elm)});
        for (let i = 0; i < 3; i++) {
            if (this.bases[i]==2) {
                this.setGameState({
                    bases: this.bases.map((elm,j)=>{
                        if (j===i) return this.bases[j] - 1;
                        else if (j===i+1) return this.bases[j] + 1;
                        else return this.bases[j];
                    })
                })
            }
        }
        const runs = this.bases[this.bases.length-1];
        this.setGameState({
            bases: this.bases.slice(0,3),
            score: this.score.map((elm,i)=>i===this.awayOrHome ? elm + runs : elm)
        });
    }
    
    hitter(hitType) {
        if (hitType === '1B') this.bases = [1,0].concat(this.bases);
        else if (hitType === '2B') this.setGameState({bases: [0,1].concat(this.bases)});
        else if (hitType === '3B') this.setGameState({bases: [0,0,1].concat(this.bases)});
        else if (hitType === 'HR') this.setGameState({bases: [0,0,0,1].concat(this.bases)});
        const runs = this.arraySum(this.bases.slice(3,this.bases.length));
        this.setGameState({
            bases: this.bases.slice(0,3),
            score: this.score.map((elm,i)=>i===this.awayOrHome ? elm + runs : elm)
        });
    }
    
    atBatResult() {
        const myAtBat = this.atBat();
        if (myAtBat === 'Out') this.setGameState({outs: this.outs + 1});
        else if (myAtBat === 'BB') this.walker();
        else this.hitter(myAtBat);
        if ((this.inning >= 9 && ((this.outs >= 3 && this.awayOrHome === 0) || this.awayOrHome === 1) && this.score[0] < this.score[1]) || 
        (this.inning >= 9 && this.outs >= 3 && this.awayOrHome === 1 && this.score[0] > this.score[1])) {
            this.setGameState({gameOn: false});
        }
        if (this.outs >= 3) {
            if (this.awayOrHome === 1) {
                this.setGameState({inning: this.inning + 1});
            }
            this.setGameState({
                outs: 0,
                awayOrHome: (this.awayOrHome + 1) % 2,
                bases: [0,0,0]
            })
        }
    }
    
    playGame() {
        while (this.gameOn) {
            this.atBatResult();
        }
        const finalScore = JSON.parse(JSON.stringify(this.score));
        const winner = this.score[0] > this.score[1] ? 0 : 1;
        this.setGameState({
            inning: 1,
            outs: 0,
            awayOrHome: 0,
            bases: [0,0,0],
            score: [0,0],
            gameOn: true
        });
        return {finalScore, winner};
    }
    
    setGameState(params) {
        Object.assign(this, params);
    }

}