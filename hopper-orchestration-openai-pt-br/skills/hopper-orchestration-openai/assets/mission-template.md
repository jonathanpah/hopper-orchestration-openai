# Missão — {papel}

Contrato: 2
Etapa: {identificador}
Rodada: {numero}
Criada em: {data e hora observadas, com fuso}
Revisão da missão: {numero}
Revisada em: {data e hora da revisão atual, com fuso}
Raiz do projeto: {caminho absoluto}
Pasta da etapa: {caminho absoluto}
Relatório de saída: {caminho absoluto de rN-papel.md}
Destinatário: orquestrador

## Instruções do papel

Leia {caminho absoluto de references/contracts.md},
{caminho absoluto da referência do seu papel} e
{caminho absoluto de assets/result-template.md}.
Execute somente esta missão. A criação de agentes e a coordenação pertencem
ao orquestrador. Se faltar informação ou acesso, retorne o impedimento a ele.

## Objetivo e entrada

{Pedido autorizado e resultado esperado. Decisões aplicáveis e seus motivos.}

- Entrega: {artefato ou resultado observável}
- Versão de partida/avaliada: {identidade e prova}
- Especificação e entradas: {caminhos ou referências verificáveis}
- Dependências: {partes necessárias e estado; nenhum quando não houver}
- Passagem anterior pertinente: {caminho ou nenhum}

## Critérios de aceitação

| ID | Condição observável | Ambiente ou destino | Método de comprovação |
| --- | --- | --- | --- |
| C1 | {condição} | {ambiente} | {método} |

## Recursos e autorização

- Leitura: {recursos necessários}
- Alteração: {recursos atribuídos; nenhum se não houver}
- Execução e temporários: {operações e área autorizadas}
- Efeitos externos: {ação, destino e autorização existente; nenhum se não houver}
- Observação de efeitos: {como conferir sem duplicar operação; nao_aplicavel se couber}
- Integração: {responsável e dependências; nao_aplicavel se couber}
- Restrições e permissões efetivas: {limites confirmados e limitações conhecidas}
- Configuração do agente: {modelo e esforço solicitados; confirmação pelo orquestrador}

## Passagem

Entregue o relatório e provas conforme os contratos. Informe a versão, os
critérios atendidos e pendentes, os achados, as operações ainda em andamento
e quais recursos libera. Se não puder gravar, retorne o conteúdo completo
para transcrição fiel, explicando a limitação.

Na resposta final ao orquestrador, informe estado, parecer quando aplicável
e caminho do relatório ou conteúdo a transcrever. Não apresente efeito
planejado ou configuração solicitada como resultado confirmado.
