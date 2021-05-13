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
    
   
    /*dechifrement */
    /* changement de x */
    const bouton_dx = document.querySelector('#bouton_dx');
    bouton_dx.onclick = function(){
      var input_dx = document.querySelector('#dx');
      dx = parseInt(input_dx.value);
      document.querySelector('#afichage_dx').innerHTML = dx;
    };
    /* changement de dd */
    const button_dd = document.querySelector('#bouton_dd');
    button_dd.onclick = function(){
      var input_dd = document.querySelector('#dd');
      dd = parseInt(input_dd.value);
      document.querySelector('#afichage_dd').innerHTML = dd;
    };
    /* changement de dn*/
    const button_dn = document.querySelector('#bouton_dn');
    button_dn.onclick = function(){
      var input_dn = document.querySelector('#dn');
      dn = parseInt(input_dn.value);
      document.querySelector('#afichage_dn').innerHTML = dn;
    };
    /*déchiffrement*/
    const bouton_dx2 = document.querySelector('#bouton_dx2');
    bouton_dx2.onclick = function(){
      dx2 = Math.pow(dx, dd) % dn;
      document.querySelector('#afichage_dx2').innerHTML = dx2;
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