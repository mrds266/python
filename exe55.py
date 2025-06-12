print("Seu conhecimento de Excel é")
print("[1] básico")
print("[2] intermediário")
print("[3] avançado")
re= int(input(""))

match re:
    case 1:
        print("pergunte para que serve as formulas")
        print("[1] SOMA [2] MÉDIA [3] MAXIMO")
        ba = int(input(""))
        match ba:
            case 1:
                print("As fórmulas de soma em uma linha no Excel servem para somar valores distribuídos horizontalmente, ou seja, em células que estão lado a lado na mesma linha. Isso é útil, por exemplo, para calcular o total de vendas de um produto ao longo de vários meses, onde cada mês está em uma coluna diferente da mesma linha.")
            case 2:
                print("A fórmula MÉDIA no Excel serve para calcular a média aritmética dos valores em uma linha — ou seja, ela soma os valores e divide pela quantidade de células com números.")
            case 3:
                print("A fórmula MÁXIMO no Excel serve para encontrar o maior valor em um intervalo de células — neste caso, em uma linha. Ela é muito útil quando você quer saber qual foi o maior número registrado em uma sequência de dados horizontais.")
    case 2:
        print("pergunte para que serve as formulas")
        print("[1]se [2] somase [3] cont.se]")
        int = int(input(""))

        match int:
            case 1:
                print("A fórmula SE no Excel é usada para fazer testes lógicos e tomar decisões automáticas com base em condições. Quando aplicada em uma linha, ela avalia os valores horizontais (em células lado a lado) e retorna um resultado diferente dependendo se a condição for verdadeira ou falsa.")
            case 2:
                print("A fórmula SOMASE no Excel é usada para somar valores com base em uma condição específica. Quando aplicada em uma linha, ela permite somar apenas os valores que atendem a um critério, dentro de um intervalo horizontal.")
            case 3:
                print("A fórmula CONT.SE no Excel serve para contar quantas vezes um determinado valor aparece em um intervalo — e quando usada em uma linha, ela verifica os valores horizontalmente (de célula em célula na mesma linha).")
    case 3:
        print("pergunte para que serve as formulas")
        print("[1]ordem.eq [2] procv [3] procH")
        ava = int(input(""))

        match ava:
            case 1:
                print("A fórmula ORDENAR.EQ (em inglês, RANK.EQ) no Excel serve para classificar um número dentro de um conjunto de valores, ou seja, ela mostra qual é a posição (ou ranking) de um valor em relação aos outros. Quando usada em uma linha, ela compara os valores horizontalmente.")
            case 2:
                print("A fórmula PROCV (ou VLOOKUP em inglês) no Excel serve para procurar um valor em uma coluna e retornar um valor correspondente de outra coluna, na mesma linha da tabela. Apesar de o nome significar “procura vertical”, ela pode ser usada em conjunto com dados organizados em linhas, desde que a estrutura da tabela esteja adequada.")
            case 3:
                print("A fórmula PROCH (ou HLOOKUP em inglês) no Excel serve para procurar um valor em uma linha e retornar um valor correspondente de outra linha, dentro da mesma")