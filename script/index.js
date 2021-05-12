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
      output = output.substring(1);
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