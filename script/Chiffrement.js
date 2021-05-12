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
    /* chiffrement */

    /* changement de m */
    const button_cm = document.querySelector('#bouton_cm');
    button_cm.onclick = function(){
      var input_cm = document.querySelector('#cm');
      cm = parseInt(input_cm.value);
      document.querySelector('#afichage_cm').innerHTML = cm;
    };
    /* changement de e */
    const button_ce = document.querySelector('#bouton_ce');
    button_ce.onclick = function(){
      var input_ce = document.querySelector('#ce');
      ce = parseInt(input_ce.value);
      document.querySelector('#afichage_ce').innerHTML = ce;
    };
    /* changement de n*/
    const button_cn = document.querySelector('#bouton_cn');
    button_cn.onclick = function(){
      var input_cn = document.querySelector('#cn');
      cn = parseInt(input_cn.value);
      document.querySelector('#afichage_cn').innerHTML = cn;
    };
    /*chiffrement*/
    const bouton_cx = document.querySelector('#bouton_cx');
    bouton_cx.onclick = function(){
      cx = Math.pow(cm, ce) % cn;
      document.querySelector('#afichage_cx').innerHTML = cx;
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