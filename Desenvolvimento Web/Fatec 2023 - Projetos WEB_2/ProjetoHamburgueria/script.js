let valorCombo=0;
let totalAdicionais=0;
let valorTaxa=0;
let totalFinal =0 
 
function calcularTotalPedido()
{
    valorCombo = Number(document.getElementById('combos').value);
    taxaEntrega = Number(document.querySelector('input[type="radio"]:checked').value);
    calcularAdicionais();
        totalFinal = totalAdicionais + valorCombo + taxaEntrega;
    document.getElementById("pagamento").value = `Seu combo custará R$ ${valorCombo} com R$ ${totalAdicionais} de adicionais e R$ ${taxaEntrega} de taxa de entrega`;
    document.getElementById("total").value = totalFinal;  
}


  
 
function calcularAdicionais()
{
    totalAdicionais = 0;
 
    let adicionais= document.querySelectorAll("input[name='adicionais']");
    console.log(adicionais);
    for (let i = 0; i < adicionais.length; i = i+1)
    {
        if (adicionais[i].checked == true)
        {
            totalAdicionais = totalAdicionais + parseFloat(adicionais[i].value);
        }
    }
    alert(`Adicionais: ${totalAdicionais}`);
}
 

/*function calcularCombos()
{
    let co=0;
     
    for (var i = 0; i < combos.length; i++)
    {
        if (   combos[i].checked == true    )
        {
            valorCombo = Number(combos[i].value);
            break;
        }
    }
}*/

