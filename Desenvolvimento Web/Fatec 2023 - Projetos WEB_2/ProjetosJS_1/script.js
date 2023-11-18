
function calcularNovoSalario() {
    salario = parseFloat(document.getElementById("salario").value);
    percentual = parseFloat(document.getElementById("percentual").value);

    aumento = salario * (percentual / 100);
    novoSalario = salario + aumento;

    document.getElementById("novoSalario").textContent = "O novo salário é de R$ " + novoSalario.toFixed(2);
}


function calcularArea() {
    base = parseFloat(document.getElementById("base").value);
    altura = parseFloat(document.getElementById("altura").value);

    area = (base * altura) / 2;

    document.getElementById("area").value = "A área do triângulo é de: " + area.toFixed(2);
}


function calcularMedia() {
    nota1 = parseFloat(document.getElementById("nota1").value);
    nota2 = parseFloat(document.getElementById("nota2").value);

    media = (nota1 * 0.3) + (nota2 * 0.7);

    document.getElementById("media").textContent = "A média é: " + media.toFixed(2);
}


function calcularIdade() {
    var anoNascimento = parseInt(document.getElementById("ano-nascimento").value);
    var dataAtual = new Date();
    var anoAtual = dataAtual.getFullYear();

    var idadeAnos = anoAtual - anoNascimento;
    var idadeMeses = (idadeAnos * 12) + dataAtual.getMonth();
    var idadeDias = Math.floor((dataAtual - new Date(anoNascimento, dataAtual.getMonth(), dataAtual.getDate())) / (1000 * 60 * 60 * 24));
    var idadeHoras = idadeDias * 24;
    var idadeMinutos = idadeHoras * 60;
    var idadeSemanas = Math.floor(idadeDias / 7);

    console.log("Idade Aproximada:");
    console.log("Anos: " + idadeAnos);
    console.log("Meses: " + idadeMeses);
    console.log("Dias: " + idadeDias);
    console.log("Horas: " + idadeHoras);
    console.log("Minutos: " + idadeMinutos);
    console.log("Semanas: " + idadeSemanas);

    var idade2050 = 2050 - anoNascimento;
    console.log("Idade em 2050: " + idade2050);
}


function calcularConsumo() {
    distancia = parseFloat(document.getElementById("distancia").value);
    volume = parseFloat(document.getElementById("volume").value);

    consumoMedio = distancia / volume; 

    document.getElementById("consumo-medio").value = "O consumo médio é de: " + consumoMedio.toFixed(2) + "Km/L";
}


function calcularSalario() {
    horasTrabalhadas = parseInt(document.getElementById("horas-trabalhadas").value);

    valorHora = 10.00;
    valorHoraExtra = valorHora * 3;
    valorRefeicao = 1.50;
    salarioBruto = 0;
    descontoRefeicao = 0;

    if (horasTrabalhadas <= 40) {
      salarioBruto = horasTrabalhadas * valorHora;
    } else {
      salarioBruto = (40 * valorHora) + ((horasTrabalhadas - 40) * valorHoraExtra);
    }

    descontoRefeicao = Math.floor(horasTrabalhadas / 24) * valorRefeicao;
    salarioLiquido = salarioBruto - descontoRefeicao;

    document.getElementById("salario-bruto").value = salarioBruto.toFixed(2);
    document.getElementById("desconto-refeicao").value = descontoRefeicao.toFixed(2);
    document.getElementById("salario-liquido").value = salarioLiquido.toFixed(2);
}


function gerarNumero() {
    numero = Math.floor(Math.random() * 100) + 1;
    document.getElementById("numero-aleatorio").value = numero;

    if (numero % 2 === 0) {
      document.getElementById("par-impar").value = "O número " + numero + " é par.";
    } else {
      document.getElementById("par-impar").value = "O número " + numero + " é ímpar.";
    }
}
