# Jogo-em-Tuno
Jogo de RPG em Turnos

Este código implementa uma batalha de RPG em que jogadores e inimigos lutam entre si. Cada personagem possui pontos de vida, pontos de ataque, classe e nível. Os jogadores podem escolher alvos para atacar, enquanto os inimigos atacam jogadores aleatoriamente. A cada rodada, os pontos de vida são atualizados, e os jogadores ganham experiência ao derrotar inimigos, aumentando seu nível

Classes

Jogador

A classe Jogador representa um jogador na batalha de RPG.

Atributos

nome: O nome do jogador.
classe: A classe do jogador.
nivel: O nível do jogador.
pontos_vida: Os pontos de vida do jogador, calculados com base no nível.
pontos_ataque: Os pontos de ataque do jogador, calculados com base no nível.
experiencia: A experiência total adquirida pelo jogador.

Métodos

esta_vivo(): Verifica se o jogador está vivo com base nos pontos de vida.
atacar(alvo): Realiza um ataque ao alvo, reduzindo seus pontos de vida.
defender(): Aumenta os pontos de vida do jogador em 10.
esquivar(): Tenta esquivar-se de um ataque inimigo.
ganhar_experiencia(experiencia_ganha): Incrementa a experiência total do jogador com base na experiência ganha.
atualizar_level(): Atualiza o nível do jogador com base na experiência total adquirida.
escolher_acao(): Permite que o jogador escolha uma ação entre atacar, defender ou esquivar.

Inimigo

A classe Inimigo representa um inimigo na batalha de RPG.

Atributos

nome: O nome do inimigo.
classe: A classe do inimigo.
nivel: O nível do inimigo.
pontos_vida: Os pontos de vida do inimigo, calculados com base no nível.
pontos_ataque: Os pontos de ataque do inimigo, calculados com base no nível.

Métodos

esta_vivo(): Verifica se o inimigo está vivo com base nos pontos de vida.
atacar(alvo): Realiza um ataque ao alvo, reduzindo seus pontos de vida.

Funções auxiliares

gerar_nome_orc(): Gera um nome aleatório para um orc.
gerar_nome_troll(): Gera um nome aleatório para um troll.
gerar_nome_goblin(): Gera um nome aleatório para um goblin.
gerar_nome_necromante(): Gera um nome aleatório para um necromante.
gerar_inimigos(num_jogadores, nivel): Gera uma lista de inimigos com base no número de jogadores e no nível da fase.
gerar_fase(jogadores, nivel): Gera uma fase com jogadores e inimigos, exibindo suas informações na tela.
rodada(jogadores, inimigos): Realiza uma rodada da batalha, permitindo que os jogadores escolham alvos para atacar e atualizando as informações dos personagens na tela.
avancar_para_proxima_fase(): Solicita ao jogador se deseja avançar para a próxima fase.
validar_nome(nome): Valida se o nome do jogador contém apenas letras.
jogar(): Inicia o jogo.
