/*
Ceci est un algorithme facile qui génère des nombres premiers par test de division non-gourmand en mémoire
*/
function test(nbr) { //test de primalité auto
    pr = 0;
    for (i = 2; i < nbr; i++) {
        z = nbr % i
        if (z == 0) {
            pr++
        } else {}
    }
    if (pr == 0) {
        return nbr
    } else {
        return ""
    }
}

function gen() { //Génère des nombres dans [a,b]
    a = document.getElementById("deb").value
    b = document.getElementById("fin").value
    document.getElementById("result").value = ""
    if ((b - a) > 10000) {
        alert("Interval trop grand")
    } else {
        for (k = a; k <= b; k++) {
            t = test(k)
            if (t != "") {
                document.getElementById("result").value = document.getElementById("result").value + "-" + t
            }
        }
    }
}

function tester() { //test le nombre entré ;)
    lg = document.getElementById("nbr_test").value
    if (lg < 1000000) {
        if (test(lg) == lg) {
            document.getElementById("result").value = lg + " est premier"
        } else {
            document.getElementById("result").value = lg + " n'est pas premier"
        }
    } else {
        document.getElementById("result").value = lg + " est trop grand!!! entrer un nombre plus petit"
    }
}