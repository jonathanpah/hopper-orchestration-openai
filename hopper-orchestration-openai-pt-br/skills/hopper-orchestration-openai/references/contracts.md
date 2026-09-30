# Contratos e documentos — versão 2

O orquestrador lê esta referência antes de criar a etapa. Cada agente a recebe
com a missão. Os modelos em `assets/` são pontos de partida; substitua campos
entre chaves na missão real e não invente valores indisponíveis.

## Destino e identificação

Use `docs-by-hopper-orchestration-openai/` na raiz do projeto atendido, confirmada pela
missão. A raiz da skill só é o destino quando ela própria for o projeto atendido.
Em tarefa sem projeto, use um diretório de trabalho autorizado e informe-o.

```text
docs-by-hopper-orchestration-openai/
  index.md
  AAAAMMDD-HHMMSS-tema/
    mission-executor.md
    mission-reviewer.md
    mission-validator.md
    r1-executor.md
    r1-reviewer.md
    r1-validator.md
    log.md
    summary.md
    evidence/
```

Use data e hora locais do início e tema curto em minúsculas com hífens. Registre
fuso e deslocamento UTC. Evite colisões sem sobrescrever etapas existentes.
Papéis adicionais usam `executor-2`, `executor-3` etc. A rodada de cada papel
começa em 1 e aumenta em novas entregas. Crie documentos conforme forem usados;
ausência de relatório significa papel ainda não executado, nunca aprovação.

## Missão

O [modelo de missão](../assets/mission-template.md) deve conter:

- **Identidade:** versão do contrato, etapa, papel, rodada, raiz do trabalho,
  caminho do relatório e referências absolutas dos contratos, papel e modelo
  de resultado. Separe `criada_em`, `revisao` e `revisada_em`, usando a hora
  observada com fuso. Atualizar a missão preserva sua criação e muda sua revisão
  e data; indisponibilidade de hora deve ser declarada, nunca preenchida com
  uma data antiga como se fosse atual.
- **Objetivo e entrada:** pedido e decisões aplicáveis, entrega esperada,
  versão de partida, arquivos de entrada e dependências.
- **Critérios:** identificadores estáveis `C1`, `C2` etc., condição observável,
  ambiente/destino, método de comprovação e autoridade para efeitos externos.
- **Recursos:** itens que pode ler, alterar ou executar, temporários, contas,
  restrições e responsável pela integração. O que a ferramenta não isola deve
  constar como limitação, não como proteção confirmada.
- **Passagem:** caminho do relatório, estado esperado, provas necessárias e
  destinatário. Cada agente retorna ao orquestrador, sem criar outros agentes.

Critério local ou externo descreve o ambiente da prova, não dispensa validação.
Para critérios cuja prova pode causar efeito externo, documente autorização,
destino e como observar o resultado sem duplicar a operação.

## Responsabilidade e versão

Cada recurso alterável tem um responsável por vez. Considere também recursos
compartilhados fora do Git: banco, serviço, porta, conta e destino publicado.
Transfira responsabilidade no `log.md` após a liberação e a conferência de
atividade pendente. Use separação de arquivos ou ambientes de trabalho quando
necessária ao paralelismo; Git worktrees não isolam serviços externos.

O orquestrador mantém índice, missões, log e resumo. Agentes gravam seus próprios
relatórios e provas, além dos recursos autorizados na missão. Evidências usam
`evidence/r<N>-<papel>-*`; o orquestrador usa `evidence/orchestrator-*`.
Quando um agente não puder escrever, a transcrição fiel de seu resultado pelo
orquestrador identifica ambos e preserva o conteúdo original.

## Identidade verificável

Identifique a entrega de modo verificável. Um commit basta somente se contiver
toda a entrega e não houver mudanças relevantes fora dele. Caso contrário,
registre caminhos e hashes, incluindo arquivos novos, removidos e mudanças
não commitadas. Inclua a composição do artefato para detectar adições posteriores;
hashes de alguns arquivos não provam que a entrega inteira permaneceu igual.
Exclua registros da orquestração da identidade do produto, salvo se forem parte
da entrega solicitada. Para destinos externos, registre também revisão instalada,
identificador da publicação ou outra identidade observável.

Para uma árvore local estável, use o auxiliar determinístico
[`scripts/manifest.py`](../scripts/manifest.py), com Python 3.9 ou superior.
Após a liberação dos escritores, registre uma linha de base uma vez e confira-a
antes de cada passagem. Substitua os caminhos absolutos de exemplo:

```bash
python3 /skill/scripts/manifest.py snapshot /projeto /projeto/docs-by-hopper-orchestration-openai/etapa/evidence/product-v1.json --exclude .git --exclude docs-by-hopper-orchestration-openai
python3 /skill/scripts/manifest.py verify /projeto /projeto/docs-by-hopper-orchestration-openai/etapa/evidence/product-v1.json
```

As exclusões são explícitas: não exclua documentos que pertençam ao produto.
O auxiliar compara nomes, tipos, permissões e conteúdo, incluindo arquivos novos
fora do Git. Retorno 0 confirma igualdade; 1 mostra diferenças; 2 indica que a
comparação não pôde ser concluída. Preserve a saída e o manifesto; não gere uma
nova linha de base só para apagar a divergência. Nova versão precisa da análise
do impacto e das passagens afetadas.

O auxiliar não segue links simbólicos nem cobre serviços, dependências externas
ou escritores concorrentes. Nesses casos, ou sem Python disponível, produza
um inventário verificável adequado ao artefato e a suas dependências. Explique
o limite; não declare igualdade se faltar parte relevante da composição.
A dupla leitura do auxiliar detecta mudanças observadas, mas não cria um lock
nem substitui a liberação dos recursos.

## Resultado e evidência

Use o [modelo de resultado](../assets/result-template.md). Diferencie:

- **Estado do trabalho:** `concluido`, `bloqueado` ou `interrompido`.
- **Parecer:** `aprovado`, `reprovado`, `inconclusivo` ou `nao_aplicavel`.
  O executor usa `nao_aplicavel`; revisor e validador emitem os demais.
- **Estado de critério:** `comprovado`, `falhou`, `inconclusivo` ou
  `nao_aplicavel`, este último com justificativa aceita pelo orquestrador.
  Um critério do pedido não pode ser dispensado por conveniência.

O resultado identifica agente, papel, etapa, rodada, versão, evidências,
critérios pendentes, achados abertos, recursos liberados, operações pendentes,
relatório e próximo responsável. Retorne também estado e caminho ao orquestrador.

Cada prova relaciona critério, versão, método, ambiente, esperado, observado e
referência consultável. Preserve saídas relevantes sem segredos nem transcrições
integrais desnecessárias. Use `não confirmado` para metadados que a ferramenta
não expõe; não confunda esse valor com `nao_aplicavel`.

Achados usam identificadores estáveis por papel (`R1`, `V1`), requisito ou
critério, evidência, impacto, gravidade e resultado esperado. Classifique a
gravidade como crítica, alta, média ou baixa, justificando pelo impacto concreto.
Sugestões não violam requisito e não impedem aceite; qualquer achado aberto
impede aceite, independentemente da gravidade.

## Registros proporcionais

Mantenha uma fonte canônica para critérios, manifesto e configuração. Missões
autossuficientes podem apontar para ela com caminhos absolutos; passagens
referenciam provas existentes, sem copiar logs e tabelas inteiros. Em nova rodada,
registre a diferença, os achados afetados e as provas reaproveitadas. Não crie
relatórios intermediários redundantes nem reexecute provas para preencher um
formulário. Preserve o comando ou método relevante quando ele for executado.

Cite arquivos e seções realmente consultados. Use os valores de estado previstos
no contrato; coloque a explicação em campo separado. Estado da etapa, estado
de cada parte, estado do trabalho e parecer são informações distintas.

## Registros do orquestrador

- **`index.md`:** uma linha por etapa, com identificador, objetivo, estado,
  versão, link para resumo e próxima ação. No topo, indique etapas ativas e
  recursos ainda reservados. Preserve etapas anteriores e a estrutura legada
  quando ela já existir; registre a versão do contrato de cada etapa.
- **`log.md`:** eventos com data/hora e UTC, ação, estado `decidido`, `tentado`
  ou `realizado`, motivo, responsável e evidência. Inclua acionamentos,
  transferências, mudanças de missão, devoluções, pausas, retomadas e aceite.
  Diferencie a hora do evento da hora de gravação do registro. Se o horário
  exato do evento não estiver disponível, marque-o como não confirmado e
  preserve a sequência observada; não use a hora de registro como se fosse
  um timestamp fornecido pela ferramenta.
- **`summary.md`:** resultado; equipe; versão e estado atual; critérios e
  evidências; achados e limitações; próxima ação. Registre contrato, versão e
  hashes do pacote da skill usado. Na equipe, registre identificadores, modelo
  e esforço solicitados/aplicados/confirmados e estado real de cada papel.
  Na próxima ação, indique responsável e eventual dependência do usuário.

Registre duração e consumo quando o ambiente os mostrar, informando a cobertura
(orquestrador, agentes ou total) e evitando somas duplicadas. Dados ausentes são
`não disponíveis`; não estime tokens a partir do tamanho do relatório.

Os registros permitem continuidade, mas não substituem a inspeção do estado
atual nem concedem autorização. Ao receber registros de outro fabricante,
registre origem, versão do contrato e divergências; reutilize decisões e provas
válidas sem presumir que sessões antigas são agentes da equipe atual.
