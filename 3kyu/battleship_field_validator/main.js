function validateBattlefield(field) {
    ships = {"Battleship":0,"Cruiser":0,"Destroyer":0,"Submarine":0}
    size = {"4":"Battleship","3":"Cruiser","2":"Destroyer"}
    counted = {}
    
    for (var i=0;i<=9;i++){
        for (var j=0;j<=9;j++) {      
            if (field[i][j] == 1){
                if (j.toString() in counted){ if (counted[j.toString()].indexOf(i)>=0) { continue }}
                var x = 0
                var y = 0

                if (i>0 && i<9 && j>0 && (field[i-1][j-1] == 1 || field[i+1][j-1] == 1)) return false;

                while (field[i][j+x] == 1){
                    x += 1
                    if (field[i][j+x] == 1 && i<9 && field[i+1][j+x] == 1 ) return false;
                }
                while (field[i+y][j] == 1){
                    y += 1
                    if (field[i+y][j] == 1 && j<9 && field[i+y][j+1] == 1 ) return false;
                }


                if (x > 1 && y > 1) return false;

                if (x > 1 && y == 1) {
                    var ship = size[x]
                    ships[ship] += 1
                    j = j+x-1
                }

                if (x == 1 && y > 1) {
                    var ship = size[y]
                    ships[ship] += 1
                    counted[j] = []
                    for (var p=0;p<y;p++){counted[j].push(i+p)}
                }

                if (x == 1 && y == 1) { ships["Submarine"] += 1 }

                if (i>0 && i<9 && j<9 && (field[i-1][j+1] == 1 || field[i+1][j+1] == 1)) return false;
            }
        }
    }
    
    if (ships["Battleship"]==1 && ships["Cruiser"]==2 && ships["Destroyer"]==3 && ships["Submarine"]==4) return true;
    else { return false }
}