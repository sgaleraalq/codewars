function nextSmaller(n) {
    let myFunc = num => Number(num);
    let num = n.toString()
    for (var w = num.length-2;w>=0;w--){
      var number = num.substring(w,num.length)
      for (var i = number.length-1; i>=0; i--){
        for (var j = i-1; j>=0; j--){
          if (number[j]>number[i]){
            var final_number = num.substring(0,w) + number.substring(0,j) + number[i] + number.substring(j,i) + number.substring(i+1,number.length)
            if (final_number[0]!=0){
              var second_part = Array.from(String(final_number.substring(w+j+1,final_number.length)), myFunc);
              second_part.sort(function(a, b) {return b-a;});
              final_number = final_number.substring(0,w+j+1) + second_part.join("").toString()
            }
            if (final_number[0] == "0") return -1;
            else{ return parseInt(final_number) }
          }
        }
      }
    }
    return -1;
  }