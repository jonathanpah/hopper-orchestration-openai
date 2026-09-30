# Contribuindo com hopper-orchestration-openai

Contribuições podem melhorar a clareza da skill, identificar falhas no fluxo, verificar o comportamento em um ambiente ou melhorar a documentação. A documentação fica em inglês em `hopper-orchestration-openai-en/` e em português brasileiro em `hopper-orchestration-openai-pt-br/`. As políticas e os modelos compartilhados do GitHub permanecem na raiz do repositório. Os textos da skill ficam em `hopper-orchestration-openai-en/skills/hopper-orchestration-openai/` e `hopper-orchestration-openai-pt-br/skills/hopper-orchestration-openai/`. Mantenha as duas versões equivalentes; cada release inclui os dois idiomas.

## Comece pelo problema

Para suspeitas de vulnerabilidade, siga a [Política de Segurança](SECURITY.md) e relate de forma privada. Não inclua detalhes sensíveis de segurança em issues, discussões ou pull requests públicos antes de coordenar a divulgação.

Use um relato de bug para uma falha reproduzível e uma proposta para uma alteração específica. Use [Discussions](https://github.com/jonathanpah/hopper-orchestration-openai/discussions) para dúvidas ou ideias iniciais. Pesquise as issues existentes antes de abrir outro relato sobre o mesmo comportamento.

Para mudanças na política de orquestração, explique a regra atual, o problema que ela causa, o comportamento desejado, as evidências e as consequências das alternativas. Uma proposta não é aprovação para alterar a política do projeto. Pequenas correções documentais podem ir diretamente para um pull request.

## Preserve o desenho da skill

- Mantenha a skill focada no que fazer. Coloque comandos específicos de cada ambiente e detalhes de instalação no README.
- Preserve a ativação somente para uma tarefa de orquestração solicitada, os quatro papéis, os esforços admitidos (`high`, `xhigh`, `max`), os limites de escopo, o responsável por cada recurso, as exigências de evidências e as decisões registradas, salvo aprovação de uma mudança de política pelo mantenedor.
- Mantenha a skill principal concisa, com referências aos contratos, instruções dos papéis e modelos. O pacote não deve depender de um `AGENTS.md` separado nem deste guia de contribuição para executar seu fluxo.
- Mantenha um corpo da skill por idioma, usado pelo Codex. Atualize os dois idiomas juntos ao alterar uma regra.
- Não acrescente versões fixas de modelos, limites arbitrários de duração ou limites de consumo como edições incidentais.
- Diferencie comportamento observado de afirmações da documentação, suposições e comportamentos propostos. Não alegue melhorias de desempenho ou custo sem medições comparáveis.
- Use linguagem clara em português e em inglês. Não acrescente comentários a exemplos de código ou arquivos de configuração, nem comentários HTML ocultos ao Markdown. Coloque as explicações na documentação visível.

## Abra um pull request

1. Crie um fork do repositório na sua conta do GitHub. Um fork é uma cópia sua, que você pode editar.
2. Crie uma branch no seu fork para uma alteração coerente.
3. Edite os arquivos e registre a alteração em um commit com mensagem descritiva.
4. Abra um pull request da sua branch para a branch `main` deste repositório. Vincule a issue pertinente, se houver.
5. Explique o problema, o comportamento resultante, as verificações e as limitações. Responda à revisão na mesma branch.

Um pull request propõe uma mudança; ele não altera este repositório até que o mantenedor o integre. Você também pode contribuir revisando propostas, reproduzindo falhas relatadas ou fornecendo evidências sem alterar arquivos.

## Verifique de forma proporcional

Confira se as instruções alteradas continuam coerentes, se os links funcionam e se os exemplos YAML ou JSON têm sintaxe válida. Para uma tradução ou mudança de redação, compare o significado e as obrigações antes e depois. Uma correção apenas de redação não exige repetir uma orquestração que não foi afetada.

Para mudanças no fluxo, registre um pequeno cenário pertinente e seu resultado observável. Casos úteis incluem um pedido que não deve acionar a skill, combinação de modelo e esforço não suportada, um critério de destino marcado como local, uma correção devolvida pelo validador e uma nova tentativa bloqueada sem mudança de condição. Escolha os casos afetados pela sua alteração; não execute trabalho sem relação com ela apenas para completar uma lista.

Para alegar compatibilidade com um ambiente, identifique o ambiente e sua versão, a configuração solicitada e a confirmada, o que você observou e as limitações. Mantenha separadas as afirmações sobre leitura do formato, reconhecimento, política de acionamento e comportamento real do fluxo. Comprovar um desses pontos não comprova os demais.

Use recursos descartáveis nos experimentos. Compartilhe uma reprodução concisa, com informações sensíveis removidas, ou um exemplo sintético. Nunca envie senhas, tokens de acesso, chaves privadas, dados pessoais, histórico privado de conversas ou registros de produção sem remoção de informações sensíveis.

## Revisão e releases

hopper-orchestration-openai contributors mantém o projeto e decide se uma alteração será aceita. As revisões consideram o problema descrito, as evidências, a consistência com o desenho da skill e o custo de manutenção. A revisão não implica promessa de prazo de resposta ou de aceite.

As alterações aceitas são integradas à `main`. Uma release identifica uma versão selecionada do repositório e descreve suas mudanças e limitações conhecidas. Instalar ou atualizar continua sendo uma decisão do usuário; um pull request ou uma discussão em aberto não é uma alteração lançada.

Ao enviar uma contribuição, você concorda em fornecê-la sob a [Licença MIT](LICENSE) deste repositório. Siga o [Código de Conduta](CODE_OF_CONDUCT.md).
