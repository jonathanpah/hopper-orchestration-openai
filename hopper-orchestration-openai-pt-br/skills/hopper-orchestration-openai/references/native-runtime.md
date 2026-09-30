# Operação nativa do Codex

Leia antes do primeiro acionamento e quando ferramentas ou ambiente mudarem.
Use os recursos realmente expostos pela sessão. Documentação de API ou SDK
não define os argumentos das ferramentas locais.

## Preparação

1. Confira ferramentas para criar, acompanhar, continuar e interromper agentes.
   Identifique o significado do limite disponível: agentes ativos ou sessões
   abertas, incluindo ou excluindo o orquestrador. Agente ocioso pode continuar
   ocupando uma sessão aberta; considere isso antes de criar outro.
2. Confira modelos OpenAI e esforços aceitos, configuração herdada, diretório
   de trabalho e acesso aos caminhos da missão. Referências devem existir e
   ser legíveis para o agente.
3. Confira permissões efetivas e limites de escrita, execução, rede e contas.
   Uma missão delimita responsabilidade, mas não cria uma barreira técnica.
4. Se faltar capacidade indispensável, prepare o trabalho independente e
   registre a limitação. Não substitua silenciosamente o mecanismo nativo por
   processos de terminal, API, SDK ou outro executor.

Preserve modelo e esforço da conversa principal. Se o esforço mostrado estiver
fora de `high`, `xhigh` e `max`, informe o conflito antes de iniciar a equipe;
a skill não muda a configuração da conversa. Se não estiver visível, registre
`não confirmado`, sem inferi-lo pelo nome do modelo.

## Escolha dos subagentes

Preserve escolhas explícitas para a tarefa. Na ausência delas, selecione um
modelo OpenAI disponível e adequado ao papel; o modelo principal é uma opção
de partida quando suportado. Considere dificuldade, recursos e avaliações
existentes, sem pressupor superioridade pelo nome do modelo.

Use `high` como padrão desta skill para novos subagentes. Use `xhigh` ou
`max` quando a dificuldade ou avaliações sustentarem a escolha. Essa política
é local, não uma recomendação universal da OpenAI. Valide a combinação antes
de oferecê-la ou aplicá-la. Se ela não for suportada, informe as alternativas;
escolha explícita do usuário só muda por nova decisão dele.

Informe a composição com justificativa breve. Comece com um executor. Aumente
a quantidade quando as partes puderem avançar independentemente, sem disputa
de recursos e dentro da capacidade. O revisor e o validador são instâncias
distintas do executor; inicie-os nas passagens correspondentes. A configuração
da equipe não cria subdelegação: somente o orquestrador aciona agentes.

Registre limites de recursos já definidos pelo usuário ou pelo ambiente.
Estime custo ou duração somente com base suficiente. Uma espera longa não
comprova falha; um limite efetivamente atingido exige registrar o parcial.

## Perfil com ferramentas `collaboration`

Quando esta superfície estiver disponível, confira seu esquema e use:

| Operação | Ferramenta e condição |
| --- | --- |
| Criar | `collaboration.spawn_agent`: `task_name`, `fork_turns`, `model`, `reasoning_effort`, `message`, conforme o esquema exposto. |
| Complementar trabalho ativo | `collaboration.send_message`; a mensagem não inicia uma nova rodada por si só. |
| Dar nova rodada | `collaboration.followup_task`, preferencialmente após a passagem do agente ocioso. |
| Aguardar | `collaboration.wait_agent`; diferencie aviso, resultado final, interrupção pelo usuário e timeout. |
| Conferir estado | `collaboration.list_agents`, quando houver uma dúvida concreta ou transição a confirmar. |
| Interromper | `collaboration.interrupt_agent`, conforme o alcance da parada e o ciclo de vida. |

Acione essas ferramentas diretamente quando exigido pelo ambiente, sem
envolvê-las em `functions.exec`. Use o nome canônico ou identificador retornado
nas chamadas seguintes. Nomes de tarefas devem ser únicos na sessão; nesta
superfície, use letras minúsculas, dígitos e `_`.

Comece com `fork_turns: "none"` e uma missão autossuficiente. A mensagem de
criação informa a raiz autorizada e a primeira leitura antes de qualquer busca.
Use os caminhos reais, por exemplo:

> Atue como revisor. Sua raiz de trabalho é /projeto; use-a como workdir nas
> buscas e comandos. Primeiro leia
> /projeto/docs-by-hopper-orchestration-openai/etapa/mission-reviewer.md e somente as
> referências nela indicadas. Use a cópia da skill indicada nessa missão; não
> inicie outra orquestração. Respeite as instruções superiores herdadas.
> Entregue o relatório no caminho indicado e retorne seu caminho e estado.

Esse formato reduz o histórico copiado; não isola arquivos, ferramentas,
credenciais ou instruções gerais herdadas. Consulte as restrições de
`fork_turns` antes de combinar herança com substituições de modelo ou esforço.
Forneça provas e contexto necessários, sem antecipar o parecer esperado.

Outras versões do Codex podem expor ferramentas e identificadores diferentes.
Mapeie as operações acima para o esquema real e registre a diferença. Não
invente argumentos nem presuma que existe uma ferramenta para fechar agentes.

## Confirmação e espera

Para cada agente, registre identificador, modelo e esforço solicitados, o que
a ferramenta informou aplicar e o que os metadados permitem confirmar.
Ausência de metadados significa `não confirmado`, não aplicação comprovada.
Se a configuração exata for um critério de aceitação, essa ausência impede
confirmar o critério, mas não transforma uma chamada bem-sucedida em falha.

O retorno da criação confirma o acionamento, não a entrega. Aguarde a mensagem
final e confira o relatório e a versão correspondentes. Use esperas por eventos
nos limites do ambiente; timeout de espera não autoriza recriar ou interromper
o agente. Dê atualizações ao usuário na cadência exigida pelo ambiente, sem
converter isso em consultas repetidas ao estado do agente.

Em falha ambígua de criação, confira se o agente já existe antes de tentar
novamente. Em resultado incompleto, peça somente o complemento necessário.

## Perfis e permissões

`agents/openai.yaml` configura a apresentação e a ativação da skill. Não
configura modelo, esforço ou permissões dos subagentes.

Clientes compatíveis podem carregar agentes personalizados de `.codex/agents/`
ou `~/.codex/agents/`. Use perfis existentes quando a seleção for suportada,
conferindo a configuração efetiva: valores do perfil e substituições do ambiente
podem afetar o resultado. Não instale perfis nem modifique configurações globais
como efeito implícito de uma execução desta skill.

Prefira o revisor sem permissão de modificar a entrega e o validador com acesso
somente aos recursos necessários à prova. Se um perfil somente leitura impedir
gravar relatórios, o agente retorna o conteúdo e o orquestrador o transcreve
fielmente, marcando autor e responsável pela gravação. Não enfraqueça a proteção
apenas para cumprir o formato documental.

Quando a ferramenta não oferecer isolamento por papel, registre a limitação.
Se a tarefa exigir esse isolamento como requisito, suspenda a parte dependente.
