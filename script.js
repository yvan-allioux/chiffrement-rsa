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
    /* changement de p avec le formulaire */
    const button_p = document.querySelector('#bouton_p');
    button_p.onclick = function(){
      var input_p = document.querySelector('#p');
      p = parseInt(input_p.value);
      document.querySelector('#afichage_p').innerHTML = p;
      console.log('p: ', p);
    };
    /* changement de q avec le formulaire */
    const button_q = document.querySelector('#bouton_q');
    button_q.onclick = function(){
      var input_q = document.querySelector('#q');
      q = parseInt(input_q.value);
      document.querySelector('#afichage_q').innerHTML = q;
      console.log('q: ', q); 
    };
    /* calcul de n avec le formulaire */
    const button_n = document.querySelector('#bouton_n');
    button_n.onclick = function(){
      n = p*q; 
      document.querySelector('#afichage_n').innerHTML = n;
      document.querySelector('#afichage_n2').innerHTML = n;
      fiN = (p - 1)*(q - 1);
      document.querySelector('#afichage_fiN').innerHTML = fiN;
    };
    /* changement de e avec le formulaire */
    const button_e = document.querySelector('#bouton_e');
    button_e.onclick = function(){
      var input_e = document.querySelector('#e');
      e = parseInt(input_e.value);
      document.querySelector('#afichage_e').innerHTML = e;
      document.querySelector('#afichage_e2').innerHTML = e;
      console.log('e: ', e); 
      document.querySelector('#afichage_pgcden').innerHTML = pgcd(e,fiN);
      d = euclide2(e,fiN);
      document.querySelector('#afichage_d').innerHTML = d;
      document.querySelector('#afichage_d2').innerHTML = d;
    };
    /* calcul de m avec le formulaire */
    const button_m = document.querySelector('#bouton_m');
    button_m.onclick = function(){
      var input_m = document.querySelector('#m');
      m = parseInt(input_m.value);
      document.querySelector('#afichage_m').innerHTML = m;
      x = Math.pow(m, e) % n;
      document.querySelector('#afichage_x').innerHTML = x;
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

});