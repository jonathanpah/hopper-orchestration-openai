# hopper-orchestration-openai

[English](https://github.com/jonathanpah/hopper-orchestration-openai/blob/v0.2.2/hopper-orchestration-openai-en/README.md) | **Português (Brasil)**

Uma skill para coordenar agentes OpenAI no Codex CLI e no aplicativo, com
entrega identificada, revisão independente e critérios comprovados.

O orquestrador mantém a conversa e decide o aceite. O executor produz a entrega.
O revisor examina sua correção e as verificações. O validador comprova o resultado,
inclusive quando inteiramente local. Somente o orquestrador cria agentes.

## Funcionamento

- Quatro papéis: orquestrador, executor, revisor e validador.
- Esforços admitidos: `high`, `xhigh` e `max`. O modelo e o esforço da conversa
  principal são preservados. Escolhas explícitas do usuário prevalecem.
- Sem escolha explícita, o orquestrador seleciona modelos OpenAI disponíveis
  e usa `high` como ponto de partida dos subagentes. Essa é uma política desta
  skill, não uma recomendação universal da OpenAI.
- Um executor inicialmente; paralelismo somente com benefício concreto e
  recursos separados. A equipe não exige um painel de aprovação rotineiro.
- Missões autossuficientes, um responsável por recurso e transferência explícita.
- Comparação da composição completa antes de revisão, validação e aceite.
- Correções com revisão e validação dos impactos; provas válidas são reaproveitadas.
- Pausas distinguem agentes, processos, partes e estado da etapa.

Leia a [skill](skills/hopper-orchestration-openai/SKILL.md) e o
[índice documental](index.md). Analisar, traduzir, publicar ou instalar esta
skill não inicia seu fluxo de orquestração.

## Instalação no Codex

A distribuição usa um plugin com `plugin.json` portátil, `skills/`, metadados
`agents/openai.yaml` e manifest compatível `.codex-plugin/plugin.json`, conforme
a [documentação da OpenAI](https://developers.openai.com/plugins/build/plugins).
O nome instalado e de exibição é `hopper-orchestration-openai`. Esta pasta é o
pacote em português, versão `0.2.2`.

Para instalar a versão publicada em português:

```sh
codex plugin marketplace add jonathanpah/hopper-orchestration-openai --ref v0.2.2
codex plugin add hopper-orchestration-openai@hopper-orchestration-openai
```

Como alternativa, clone o repositório e cadastre esta pasta:

```sh
git clone --branch v0.2.2 https://github.com/jonathanpah/hopper-orchestration-openai.git
codex plugin marketplace add ./hopper-orchestration-openai/hopper-orchestration-openai-pt-br
codex plugin add hopper-orchestration-openai@hopper-orchestration-openai
```

Use uma alternativa por conta. Confira destino, origem e alterações locais
antes de atualizar um checkout existente. Não instale também uma cópia avulsa
em `.agents/skills` ou `.codex/skills`, nem os dois idiomas na mesma conta.

O app e a CLI compartilham a configuração local da mesma conta e máquina.
Uma instalação na VPS não instala o pacote na conta local do Mac. Confira a
descoberta nativa em cada destino e a lista de skills do app. Conversas abertas
podem manter instruções anteriores; não precisam ser interrompidas para instalar.

## Nomes e acionamento

Selecione `hopper-orchestration-openai` no seletor de skills ou invoque seu
identificador nativo, qualificado pelo plugin:

```text
$hopper-orchestration-openai:hopper-orchestration-openai
```

Descreva a entrega e seu escopo autorizado. Um pedido de orquestração também
pode ativar a skill: `allow_implicit_invocation: true` permite esse reconhecimento.
Discussões sobre a própria skill não iniciam agentes.

O Codex pode apresentar o identificador qualificado
`hopper-orchestration-openai:hopper-orchestration-openai`. O prefixo identifica
o plugin; não é outra skill nem uma versão de idioma. Os metadados de interface
não configuram modelos, esforços ou permissões dos subagentes.

## Migração e remoção

Após conferir a nova instalação, retire a antiga somente do Codex:

```sh
codex plugin remove hopper-orchestration@hopper-orchestration
codex plugin marketplace remove hopper-orchestration
```

Inspecione e retire cópias antigas de `hopper-orchestration` dos caminhos de
skills do Codex. Referências obrigatórias em AGENTS.md precisam ser atualizadas
com autorização do proprietário; apagar a instalação não corrige essas
instruções. Preserve os registros das tarefas anteriores e instalações em
outros produtos que não estejam no escopo.

Para remover a nova versão:

```sh
codex plugin remove hopper-orchestration-openai@hopper-orchestration-openai
codex plugin marketplace remove hopper-orchestration-openai
```

## Documentos produzidos

Cada etapa usa `docs-by-hopper-orchestration-openai/AAAAMMDD-HHMMSS-tema/` na
raiz do projeto atendido. Contém missões, relatórios por rodada, `log.md`,
`summary.md` e `evidence/`. O índice fica na raiz da coleção. Data e hora usam
o fuso observado e o deslocamento UTC. A raiz da instalação não recebe registros
de outros projetos.

Registros antigos em `docs-by-hopper-orchestration/` permanecem históricos.
Consulte-os quando necessários à continuidade e registre a origem; não os
renomeie nem trate sessões antigas como agentes atuais.

## Atualizações e limites

Para uma fonte Git cadastrada, confira a nova release, atualize a referência
do marketplace e execute `codex plugin add` novamente. Para fonte local,
inspecione alterações, atualize o checkout com `git pull --ff-only` e reinstale.
Confira versão, conteúdo e descoberta após cada atualização.

O fluxo depende das capacidades nativas da sessão. Não presuma modelos, número
de agentes, isolamento por papel nem metadados que a ferramenta não exponha.
O auxiliar de inventário requer Python 3.9 ou superior; sem ele, os contratos
exigem outra identidade verificável apropriada ao artefato.

Os manifests Claude são mantidos para compatibilidade de formato. Esta release
é destinada ao Codex; não instala nem comprova o fluxo no Claude.

Consulte [verificação e limites](VALIDATION.md) para a cobertura real dos testes.

## Participação e licença

Use [Issues](https://github.com/jonathanpah/hopper-orchestration-openai/issues)
para falhas reproduzíveis e propostas concretas, e
[Discussions](https://github.com/jonathanpah/hopper-orchestration-openai/discussions)
para dúvidas. Consulte [Contribuição](CONTRIBUTING.md),
[Segurança](SECURITY.md) e [Código de Conduta](CODE_OF_CONDUCT.md).

Copyright (c) 2026 hopper-orchestration-openai contributors. [Licença MIT](LICENSE).
Projeto independente, sem alegação de vínculo ou endosso da OpenAI.
