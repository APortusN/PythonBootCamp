// Siempre hambriento
function siempreHambriento(arr){
    var count = 0;
    for(var i =0; i<arr.length; i++){
    if(arr[i] == "comida"){
    count++;
    console.log("delicioso") ;
    }
    }
    if(count == 0){
    console.log("Tengo hambre");
    }
}
var result = siempreHambriento([3.14, "comida", "pastel", true, "comida"]); // esto debería mostrar "delicioso, "delicioso"
var result = siempreHambriento([4, 1, 5, 7, 2]); // esto debería mostrar "Tengo hambre"


// // Filtro paso alto
function highPass(arr, cutoff) {
    var filteredArr = [];
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > cutoff){
            filteredArr.push(arr[i])
        }    
    }
    return filteredArr;
    }
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); // esperamos de vuelta [6, 8, 10, 9]

// Mejor que el promedio
function betterThanAverage(arr) {
    var promedio;
    var sum = 0; 
    var count = 0;   
    for (var i=0; i<arr.length; i++){
        sum += arr[i];
        }
        promedio = sum/arr.length;     
        for(var i = 0; i<arr.length; i++){
            if(arr[i] > promedio){                
                count++;   
            } 
        }
        return count; // cuenta cuántas variables son mayores que el promedio
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // esperamos 4 de vuelta
        

// Arreglo invertido
function reverse(arr) {
    var temp = arr[0];
    arr[0] = arr[arr.length-1];
    arr[arr.length-1] = temp;
    return arr;
}
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // esperamos de vuelta ["e", "d", "c", "b", "a"]   

// Arreglo de Fibonacci
function fibonacciArray(n) {  // [0, 1] son los valores inciales del arreglos para calcular el resto    
    var fibArr = [0, 1];
    for (var i=2; i<n; i++) {
        fibArr[i] = fibArr[i - 2] + fibArr[i - 1];
    }
    return fibArr;
}   
var result = fibonacciArray(10);
console.log(result); // esperamos de vuelta[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

