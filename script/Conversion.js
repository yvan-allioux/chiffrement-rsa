/**
 * caccul ud pgcd etendu
 * @param {*} a 
 * @param {*} b 
 */
function euclide2(a,b){
// On sauvegarde les valeurs de a et b.
a0 = a;
b0 = b;
// Initialisations. On laisse invariant p*a0 + q*b0 = a et  r*a0 + s*b0 = b.
p = 1; q = 0;
r = 0; s = 1;
// La boucle principale:
while (b != 0) { 
  c = a % b;
  quotient = Math.floor(a/b);  //Javascript n'a pas d'opération de division entière.
  a = b;
  b = c;
  nouveau_r = p - quotient * r; nouveau_s = q - quotient * s;
  p = r; q = s;
  r = nouveau_r; s = nouveau_s;
}
// Affiche le résultat.
console.log("pgcd(" + a0 + "," + b0 + ")=" + p + "*" + a0 + "+(" + q + ")*" + b0 + "=" + a);
return p;
}

/**
 * calcul du pgcd
 * @param {*} a 
 * @param {*} b 
 * @returns 
 */
function pgcd(a,b) {  
    while (a!=b) {if (a>b) a-=b; else b-=a;}  
    return a;  
  }



document.addEventListener("DOMContentLoaded", function(event) {
    console.log("start"); 
    /*dechifrement */

    /* conversion */
    const bouton_conversion = document.querySelector('#bouton_conversion');
    bouton_conversion.onclick = function(){
      var input_conversion = document.querySelector('#conversion');
      conversion = input_conversion.value;
      var output = 0;
      for (var i = 0; i < conversion.length; i++) {
        var actuelle = conversion[i].charCodeAt(0);
        if(actuelle.toString().length == 1){
          console.log("leng 1");
          output += "00"+actuelle;
        }else if (actuelle.toString().length == 2){
          console.log("leng 2");
          output += "0"+actuelle;
        }else{
          output += actuelle;
          
        }
         
      }
      /* if(parseInt(output) < 99){
        output = output.substring(1);
        
      } */
      
      document.querySelector('#afichage_conversion').innerHTML = output;
    };

    /* conversion2 */
    const bouton_conversion2 = document.querySelector('#bouton_conversion2');
    bouton_conversion2.onclick = function(){
      var input_conversion2 = document.querySelector('#conversion2');
      conversion2 = input_conversion2.value;
      console.log('conversion2: ', conversion2);
      var output2 = 0;
      var flag = 0;
      var temp = "";
      for (var i = 0; i < conversion2.length; i++) {   
        flag++;
        temp = temp + conversion2[i];
        if (flag == 3){
          flag = 0;
          output2 = output2 + String.fromCharCode(parseInt(temp))
          console.log('parseInt(temp): ', parseInt(temp));
          temp = "";
        }
      }
      output2 = output2.substring(1);
      document.querySelector('#afichage_conversion2').innerHTML = output2;
    };


    /* var de test p = 5 q = 17 e = 5   */
    var p = 0;
    var q = 0;
    var n = 0;
    var fiN = 0;
    var e = 0;
    var d = 0;
    var m = 0;
    var x = 0;
    var x2 = 0;
    var x3 = 0;
    var cm = 0;
    var cx = 0;

});