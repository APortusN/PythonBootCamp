var IngredintesParaPizzas = {
    preparacionMasa: ["lanzada a mano","de molde"],
    tipoCorteza: ["masa tradicional","masa delgada","masa estilo Chicago"],
    proteinas:  ["pepperomi","chorizo picante","beicon","atún","jamón iberico","salchicha"],
    quesos:   ["mozzarella","gorgonzola", "provola", "parmesano","queso de cabra","feta"],
    salsas: ["tomate", "pesto", "crema"],
    especias: ["oregano","aceite oliva","ajo","albahaca","cebolla","champiñones","aceitunas"],
};

function PizzaOven(preparacionMasa,tipoCorteza,proteinas,quesos,salsas,especias) {
    var IngredintesPizzas = {};
    IngredintesPizzas.preparacionMasa = preparacionMasa;
    IngredintesPizzas.tipoCorteza = tipoCorteza;
    IngredintesPizzas.proteinas = proteinas;
    IngredintesPizzas.quesos = quesos;
    IngredintesPizzas.salsas = salsas;
    IngredintesPizzas.especias = especias;
    return IngredintesPizzas;
}

var pizzaEstiloChicago = PizzaOven("de molde", "masa estilo Chicago", ["pepperomi","salchicha"], "mozzarella", "tomate", "oregano");
console.log(pizzaEstiloChicago);

var pizzaMarinara = PizzaOven("lanzada a mano", "masa delgada","",["mozzarella","feta"], "tomate", ["champiñones","aceitunas", "cebolla"]);
console.log(pizzaMarinara);

var preparacionMasa = ["lanzada a mano", "de molde"];
var tipoCorteza = ["masa tradicional","masa delgada","masa estilo Chicago"];
var proteinas = ["pepperomi","chorizo picante","beicon","atún","jamón iberico","salchicha"];
var quesos = ["mozzarella","gorgonzola", "provola", "parmesano","queso de cabra","feta"];
var salsas = ["tomate", "pesto", "crema"];
var especias = ["oregano","aceite oliva","ajo","albahaca","cebolla","champiñones","aceitunas"];

function randomItem(arr) {
    var i = Math.floor(arr.length * Math.random());
    return arr[i];
}

function pizzaSorpresa(){
    var pizzaS = {};
    pizzaS.preparacionMasa = randomItem(preparacionMasa);
    pizzaS.tipoCorteza = randomItem(tipoCorteza);
    pizzaS.proteinas = randomItem(proteinas);
    pizzaS.quesos = randomItem(quesos);
    pizzaS.salsas = randomItem(salsas);
    pizzaS.especias = randomItem(especias);    
    return pizzaS;
}
console.log(pizzaSorpresa());