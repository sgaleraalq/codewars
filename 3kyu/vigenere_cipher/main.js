function getKeyword(ciphertext, keyLength) {
    const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    var final_key = ""
    var final_array = []
    for (let x = 0; x<keyLength; x++){
        var min = 0
        var final_index = 0
        var array = new Array(alphabet.length).fill(0)
        to_add = new Array(alphabet.length).fill(0)
        for (i=x; i<ciphertext.length; i+=keyLength){
            position = alphabet.indexOf(ciphertext[i])
            array[position] += 1
        }
        for (j in array){
            ind1 = parseInt(j) + 4 
            ind2 = parseInt(j) + 14
            ind3 = parseInt(j) + 19
            ind4 = parseInt(j) + 8
            
            if (ind1 >= array.length){ var ind1 = ind1-array.length }
            if (ind2 >= array.length){ var ind2 = ind2-array.length }
            if (ind3 >= array.length){ var ind3 = ind3-array.length }
            if (ind4 >= array.length){ var ind4 = ind4-array.length }
            value = array[j] + array[ind1] + array[ind2] + array[ind3] + array[ind4]
            to_add[j] = value
                if (value > min){
                    min = value
                    final_index = j
                }
            }
            final_key += alphabet[final_index]
            final_array.push(to_add)
        }
    return final_key
}