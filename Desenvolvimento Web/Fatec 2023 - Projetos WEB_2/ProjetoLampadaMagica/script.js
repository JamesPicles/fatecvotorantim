let lampada=document.getElementById("lampada");
function ligar()
{
    lampada.src="luzLigada.gif";
}

function desligar()
{
    lampada.setAttribute("src", "luzDesligada.gif");
}


function sumir()
{
    lampada.style.display="none";
}


function aparecer()
{
    lampada.style.display="inline";
}


function alternar()
{
   if (lampada.getAttribute("src") == "luzLigada.gif")  
   desligar();
   
   else if (lampada.getAttribute("src") == "luzDesligada.gif")  
   ligar();
}


function piscar()
{
    alternar() 

} setInterval(piscar, 1000)

document.getElementById("titulo").style.color="red";