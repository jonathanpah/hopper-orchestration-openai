# Verificação e limites — 0.2.2

Esta release recupera o resumo público de verificação, corrige os links dos
pacotes por idioma e sincroniza a identidade de distribuição. As regras de
orquestração e o auxiliar de inventário são os mesmos da versão anterior.
Uma auditoria encontrou conteúdos diferentes identificados como `0.2.1`;
a correção usa uma versão nova, sem substituir novamente os assets antigos.

## Evidência comportamental anterior

O protótipo português corrigido passou por três cenários focais: detecção de
arquivo acrescentado depois da revisão, revisão e validação independentes de
uma entrega CSV corrigida e pausa/retomada parcial enquanto trabalho independente
continuava.

O cenário CSV revelou falhas na entrega sintética. Sua versão final passou em
sete verificações direcionadas e dez regressões existentes, seguidas de revisão
e validação independentes. São verificações dessa entrega, não dezessete cenários
adicionais da skill. Foram necessárias duas correções do produto de teste.

A campanha anterior de 21 casos usou outro protótipo e incluiu falhas. Não foi
repetida integralmente na candidata corrigida nem nesta release. Os três casos
focais foram aprovados nas versões finais, dentro das condições do ensaio.
As provas de pausa e retomada usaram observação parcial, não rastreio integral.

O empacotamento posterior mudou versão, apresentação, pasta dos registros e
prompt qualificado de invocação. O auxiliar permaneceu igual. A tradução foi
comparada quanto às obrigações; não houve nova campanha completa em inglês.

## Conferências de distribuição

As verificações distinguem:

- Estrutura: validador oficial da skill, YAML/JSON, schema portátil,
  consistência dos manifests e links dentro de cada pacote.
- Integridade: composição completa, conteúdo, commit e SHA256SUMS dos ZIPs.
- Instalação: conteúdo do plugin inteiro e descoberta de uma única entrada
  de orquestração habilitada em cada conta e runtime conferidos.
- Comportamento: decisões, passagens, execução e efeitos efetivamente observados.

As conferências de descoberta usam `skills/list` do app-server nativo e não
enviam pedidos a modelos. Portanto, não comprovam seleção implícita pelo modelo,
execução completa da skill instalada ou interação gráfica. Consulte a nota da
[release](https://github.com/jonathanpah/hopper-orchestration-openai/releases/tag/v0.2.2)
para a cobertura de verificação da distribuição publicada.

Antes de atualizar, confira commit e SHA256SUMS. Uma mudança de conteúdo exige
uma nova versão; não trate somente o número da versão como prova de identidade.
Compare o pacote completo instalado, incluindo manifests e documentação.

## Base e limites

O desenho considera as orientações oficiais para
[skills](https://learn.chatgpt.com/docs/build-skills),
[empacotamento](https://developers.openai.com/plugins/build/plugins),
[orquestração](https://developers.openai.com/api/docs/guides/agents/orchestration)
e [múltiplos agentes](https://developers.openai.com/api/docs/guides/agents-api/multi-agent).
Quatro papéis e somente `high`, `xhigh`, `max` são requisitos deste projeto,
não exigências universais da OpenAI. `agents/openai.yaml` configura apresentação
e ativação, não modelo, esforço ou sandbox dos subagentes.

Configuração solicitada não comprova modelo/esforço efetivos sem metadados.
Instruções não criam isolamento técnico por papel. Manifestos locais não cobrem
serviços externos nem escritores concorrentes. A descoberta nativa não equivale
a uma execução comportamental. Não há certificação da OpenAI nem garantia de
ausência de erros em toda tarefa, modelo e ambiente.
