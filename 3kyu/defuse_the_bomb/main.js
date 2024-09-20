// 10
Bomb.diffuse(Bomb.key)

// 9
while (Bomb.hint === "just keep trying") {
  Bomb.diffuse(Bomb.key)
}

// 8
Bomb.diffuse(global.BombKey)

// 7
function diffuseTheBomb(){
  return true;
}
Bomb.diffuse(diffuseTheBomb())

// 6
console.log(atob('VGhlIGtleSBpcyAiMy4xNDE1OSI'))
Bomb.diffuse("3.14159")

// 5
var date = new Date();
date.setDate( date.getDate() );
date.setFullYear( date.getFullYear() - 4 );
Bomb.diffuse(date)

// 4
Bomb.diffuse(Object.freeze({key: 43}));

// 3
Bomb.diffuse(obj = {
  i: 0,
  valueOf: function() {
    let res = this.i > 0 ? 11 : 9
    this.i++;
    return res;
  }
});

// 2
const MathRandom = Math.random