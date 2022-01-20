# FACTORY
Dando sequência nos posts relacionado a Design Patterns. Hoje vou falar sobre Criacionais/Factory Method.

### Imagem o seguinte problema:
Temos um sistema de pagamento onde toda transação é feita por um unico gateway, vamos supor que usamos a CIELO. E todo o seu código relacionado a transação, validação, cancelamento, esta em uma classe chamada "Cielo". 

Só que com o passar do tempo surge a necessidade de implementar mais de um gateway, por questão de custo ou até mesmo um plano de contingência. E além do mais como nosso sistema de pagamento tende a expandir, podem surgir novos clientes que queiram integrarem com outros gateways.

Dado isso a manutenção ou criação das novas classes será muito trabalhosa, pois toda regra de negócio está acoplada ama unica classe. E a proposta do Factory Method é resolver esse tipo de problema.

### Como resolver esse problema:
Antes de resolver esse problema usando Criacionais/Factory Method, vamos trazer um dicionário do que é cada componente desse Pattern.

**Fabrica/Factory:** É a classe principal (superclass) que contem os métodos que devem ser abstraidos pelas classes criadoras, define a interface do produto que é retornado e pode conter métodos auxiliares para as subiclasses (criadoras).

**Criador/Creator:** Essas são as classes que abstraem a superclase (Fabrica) e que criam os seus respectivos produtos

**Produto/Product:** Esses são os objetos que contem a regra de negócio especifica do seu tipo de produto.

**Obs.** O produto deve implementar uma interface que seja compátivel e reconhecida tanto pelas classes criadoras quanto pelas classes de fabricas.

Estarei publicando e exemplo no meu github para que seja melhor a visualização e estudo do código. Desta vez para os amentes de python fiz esse exemplo com essa stack, vou fazer algumas variáções de em linguagens até mesmo para que seja possível aprender o conceito e enteder que pode ser aplicado em qualquer stack.

Fico grato a todos, e embreve publicarei o próximo post falando sobre Criacionais/Abstract Factory