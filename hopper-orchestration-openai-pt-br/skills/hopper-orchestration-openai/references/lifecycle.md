# Ciclo de vida da etapa

Leia ao iniciar a coordenação e consulte a transição pertinente nas passagens,
devoluções, pausas e retomadas. O orquestrador registra decisões no `log.md` e
mantém o estado atual no `summary.md` e no índice.

## Estados e transições

| Situação comprovada | Ação e próximo estado |
| --- | --- |
| Missões, recursos e execução autorizados | Iniciar executor; `executando`. |
| Parte de um executor entregue | Registrar liberação; aguardar as outras partes necessárias. |
| Todas as partes entregues | Transferir ao integrador; continuar `executando`. |
| Versão integrada identificada e estável | Iniciar revisor; `em_revisao`. |
| Revisor aprovou e versão permanece igual | Iniciar validador; `em_validacao`. |
| Revisor ou validador encontrou falha | Devolver ao executor responsável; `executando`. |
| Falta prova, contexto ou recurso indispensável | Buscar a informação ou prova; `bloqueada` na parte dependente, preservando trabalho independente autorizado. |
| Todos os critérios comprovados e nenhum achado aberto | Conferir encerramento e registrar `aceita`. |
| Usuário pede pausa de toda a etapa | Interromper o alcance pedido; etapa `pausa_solicitada` até confirmar, depois `pausada`. |
| Usuário pede pausa de uma parte | A parte fica `pausa_solicitada` e depois `pausada`; a etapa continua `executando` se outra parte autorizada continua. |
| Usuário encerra sem aceite | Confirmar a parada e registrar `encerrada_sem_aceite`. |

Quando um único executor já entregar a versão integrada, encaminhe-a diretamente
à revisão; não abra uma rodada adicional de integração. Se uma parte estiver
bloqueada e outra continuar trabalhando, mantenha a etapa `executando` e
discrimine o bloqueio parcial no resumo.

Uma etapa começa `preparada`. Parecer `inconclusivo` não é aprovação e não
autoriza avançar para o aceite. Alterar o escopo exige compatibilizar critérios
e missões; requisito já contido no pedido pode ser esclarecido sem nova
autorização. Ampliação real depende do usuário.

## Passagem e identidade da entrega

Receba a conclusão do agente e confira o relatório, seus campos e a versão.
Passagem incompleta volta ao autor para complemento; não reinicie a tarefa.
Se houver repetição sem correção ou contexto novo, registre o bloqueio em vez
de criar um ciclo ilimitado de ajustes de formulário.

Antes de revisão, validação e aceite, execute a comparação do inventário completo
com o manifesto registrado, conforme [identidade verificável](contracts.md).
Confira adições, remoções e alterações; repetir somente os hashes conhecidos não
comprova igualdade. Registre o resultado real da comparação antes de acionar o
próximo papel. Se mudou, identifique os recursos afetados e obtenha revisão e
validação de seu impacto. Enquanto isso, a aprovação anterior só vale para
a versão anterior. A atualização dos relatórios não muda a versão do produto.

O executor só recebe recursos para integração após as liberações necessárias.
Ausência de resposta, timeout e interrupção solicitada não são liberação.

## Correções e progresso

Consolide achados do revisor e do validador por identificador, gravidade,
critério, versão e situação. Corrigir um achado não o encerra automaticamente:
o papel que o levantou confirma a resolução na rodada pertinente. Mantenha
referência entre relatos duplicados do mesmo problema, sem esconder nenhum.

Autorize nova tentativa quando houver diagnóstico ou ação específica e uma
verificação capaz de decidir seu resultado. Progresso é critério comprovado,
achado resolvido ou evidência que esclarece a causa; número bruto de achados
não decide continuidade. Avalie regressões pela gravidade, mesmo quando o
total de achados diminui.

Quando a mesma condição retornar sem hipótese, prova ou condição nova,
interrompa as tentativas dependentes, registre o parcial e indique a intervenção
necessária. Trocar de agente não zera o histórico. Continue partes independentes
que ainda tenham autorização e uma ação útil definida. Respeite os limites
de recursos disponíveis; não imponha um prazo arbitrário para classificar
uma tarefa longa como falha.

Prefira retomar o responsável para corrigir a mesma entrega. Substitua-o se
estiver indisponível, houver mudança autorizada de modelo ou outro motivo
técnico documentado. Transfira contexto e recursos somente após confirmar que
o anterior não continua atuando. Revisor e validador mantêm sua independência
do executor mesmo quando houver substituição.

## Pausa, cancelamento e operações pendentes

1. Identifique o alcance: parte bloqueada, etapa inteira ou pedido de parar
   toda a equipe. Em pedido explícito de parada, suspenda novos acionamentos
   e interrompa os agentes afetados pela ferramenta nativa.
2. Confira o estado retornado. Se a ferramenta apenas confirmar a solicitação,
   mantenha o alcance afetado em `pausa_solicitada` até obter prova da interrupção.
   Separe no resumo o estado da etapa e de cada parte; uma pausa parcial não
   transforma trabalho independente ativo em pausa global. Se não puder
   confirmar, declare essa limitação; não anuncie que todos pararam.
3. Confira operações iniciadas que possam sobreviver ao turno do agente, como
   comandos, serviços de teste ou tarefas externas. Interrompa ou acompanhe
   somente as que pertençam ao alcance autorizado; preserve trabalho alheio.
   Registre operações sem cancelamento disponível e efeitos de resultado incerto.
4. Confira o estado dos recursos e salve o parcial. Registre agentes, operações
   pendentes, versão e recursos ainda reservados. Libere recursos somente quando
   houver evidência de que nenhum responsável anterior continua alterando-os.
5. Atualize resumo e índice com o estado comprovado. Pare a parte solicitada;
   trabalho independente só continua quando estiver fora do alcance da parada.

Interromper um agente não desfaz efeitos já realizados. Observe o destino
antes de tentar novamente uma operação externa; use mecanismos de idempotência
quando disponíveis. Resultado incerto impede repetição cega.

## Retomada e encerramento

Na retomada, leia índice, resumo, missão e registros necessários. Confira
agentes, operações pendentes, recursos e versão reais. Preserve autorizações
vigentes; uma pausa explícita do usuário só é revogada por sua retomada.
Um bloqueio técnico pode ser resolvido dentro da autorização existente.

Reutilize decisões e provas válidas, registrando o que mudou. Após perda da
sessão, confirme que o agente anterior não segue ativo antes de substituí-lo.
Se isso não puder ser determinado, mantenha os recursos reservados e registre
a dependência. Compatibilize contratos legados por leitura; preserve o histórico.

Para encerrar, confira o estado de cada agente. Feche-o se a ferramenta oferecer
essa operação; caso contrário, registre conclusão ou interrupção confirmada,
sem afirmar que a sessão foi removida. Confira processos restantes, libere os
recursos seguros, atualize resumo e índice e remova apenas temporários próprios
sem finalidade. Critérios impedidos exigem estado parcial, não aceite.
