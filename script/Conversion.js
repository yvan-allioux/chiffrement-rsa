document.addEventListener("DOMContentLoaded", function (event) {

  /*dechifrement */

  /* conversion */
  const bouton_conversion = document.querySelector('#bouton_conversion');
  bouton_conversion.onclick = function () {
    var input_conversion = document.querySelector('#conversion');
    conversion = input_conversion.value;

    output = "";
    for (var i = 0; i < conversion.length; i++) {
      var actuelle = conversion[i].charCodeAt(0);
      if (actuelle.toString().length == 1) {
        output += "00" + actuelle;
      } else if (actuelle.toString().length == 2) {
        output += "0" + actuelle;
      } else if (actuelle.toString().length == 3) {
        output += actuelle;
      } else {
      }
    }
    document.querySelector('#afichage_conversion').innerHTML = output;
  };

  /* conversion2 */
  const bouton_conversion2 = document.querySelector('#bouton_conversion2');
  bouton_conversion2.onclick = function () {
    var input_conversion2 = document.querySelector('#conversion2');
    conversion2 = input_conversion2.value;

    var output2 = 0;
    var flag = 0;
    var temp = "";
    for (var i = 0; i < conversion2.length; i++) {
      flag++;
      temp = temp + conversion2[i];
      if (flag == 3) {
        flag = 0;
        output2 = output2 + String.fromCharCode(parseInt(temp))

        temp = "";
      }
    }
    output2 = output2.substring(1);
    document.querySelector('#afichage_conversion2').innerHTML = output2;
  };


  /* var de test p = 5 q = 17 e = 5   */
  var output = "";

});