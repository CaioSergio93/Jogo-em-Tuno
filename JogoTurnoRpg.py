import random
import sqlite3

# Função para criar a conexão com o banco de dados SQLite
def criar_conexao():
    # Conecta ao banco de dados ou cria um novo se não existir
    conn = sqlite3.connect('jogo_rpg.db')
    return conn

# Função para fechar a conexão com o banco de dados
def fechar_conexao(conn):
    conn.close()
    
def criar_tabelas(conn):
    cursor = conn.cursor()

    # Cria a tabela Jogadores
    cursor.execute('''CREATE TABLE IF NOT EXISTS Jogadores (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        classe TEXT,
                        nivel INTEGER,
                        pontos_vida INTEGER,
                        pontos_ataque INTEGER,
                        experiencia INTEGER
                    )''')
    
 # Cria a tabela Inimigos
    cursor.execute('''CREATE TABLE IF NOT EXISTS Inimigos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        classe TEXT,
                        nivel INTEGER,
                        pontos_vida INTEGER,
                        pontos_ataque INTEGER
                    )''')

    # Salva as alterações no banco de dados
    conn.commit()

class Jogador:
    def __init__(self, nome, classe, nivel):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.pontos_vida = 100 + (nivel * 25)
        self.pontos_ataque = 10 + (nivel * 5)
        self.experiencia = 0

    def esta_vivo(self):
        return self.pontos_vida > 0

    def atacar(self, alvo):
        alvo.pontos_vida -= self.pontos_ataque
        print(f"O jogador {self.nome} da classe {self.classe} causou {self.pontos_ataque} de dano ao inimigo {alvo.nome}.")

    def defender(self):
        self.pontos_vida += 10
        print(f"O jogador {self.nome} da classe {self.classe} defendeu-se e recuperou 10 pontos de vida.")

    def esquivar(self):
        chance_esquiva = random.randint(1, 100)
        if chance_esquiva <= 25:
            print(f"O jogador {self.nome} da classe {self.classe} esquivou-se do ataque inimigo!")
        else:
            self.pontos_vida -= 5
            print(f"O jogador {self.nome} da classe {self.classe} tentou esquivar-se, mas sofreu 5 pontos de dano.")

    def ganhar_experiencia(self, experiencia):
        self.experiencia += experiencia
        if self.experiencia >= 60:
            self.nivel += self.experiencia // 60
            self.experiencia %= 60
            self.pontos_vida = 100 + (self.nivel * 25)
            self.pontos_ataque = 10 + (self.nivel * 5)
            print(f"O jogador {self.nome} da classe {self.classe} avançou para o nível {self.nivel}!")

    def escolher_acao(self):
        opcoes_validas = [1, 2, 3]
        while True:
            print("Escolha uma ação:")
            print("0. Voltar")
            print("1. Atacar")
            print("2. Defender")
            print("3. Esquivar")
            escolha = int(input("Opção: "))
            if escolha == 1:
                return "atacar"
            elif escolha == 2:
                return "defender"
            elif escolha == 3:
                return "esquivar"
            elif escolha == 0:
                return "voltar"
            else:
                print("Opção inválida. Ação padrão 'Atacar' será realizada.")


class Inimigo:
    def __init__(self, nome, classe, nivel):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.pontos_vida = 50 + (nivel * 10)
        self.pontos_ataque = 10 + (nivel * 2)

    def esta_vivo(self):
        return self.pontos_vida > 0

    def atacar(self, alvo):
        alvo.pontos_vida -= self.pontos_ataque
        print(f"O inimigo {self.nome} da classe {self.classe} causou {self.pontos_ataque} de dano ao jogador {alvo.nome}.")


def gerar_nome_orc():
    return random.choice(["Uzgak", "Grommok", "Dargor", "Morgoth", "Azog"])


def gerar_nome_troll():
    return random.choice(["Zul'jin", "Gan'arg", "Mojjin", "Thra'kash", "Golgoth"])


def gerar_nome_goblin():
    return random.choice(["Zigzag", "Ratbag", "Snikch", "Gizmo", "Blitz"])


def gerar_nome_necromante():
    return random.choice(["Maldraxus", "Nefarian", "Zul'ras", "Balthazar", "Draven"])


def gerar_inimigos(num_jogadores, nivel):
    inimigos = []
    tipos_inimigos = ["Orc", "Troll", "Goblin", "Necromante"]
    for _ in range(num_jogadores):
        tipo_inimigo = random.choice(tipos_inimigos)
        if tipo_inimigo == "Orc":
            inimigos.append(Inimigo(gerar_nome_orc(), tipo_inimigo, nivel))
        elif tipo_inimigo == "Troll":
            inimigos.append(Inimigo(gerar_nome_troll(), tipo_inimigo, nivel))
        elif tipo_inimigo == "Goblin":
            inimigos.append(Inimigo(gerar_nome_goblin(), tipo_inimigo, nivel))
        elif tipo_inimigo == "Necromante":
            inimigos.append(Inimigo(gerar_nome_necromante(), tipo_inimigo, nivel))
    return inimigos


def gerar_fase(jogadores, nivel):
    print(f"--- Fase {nivel} ---")
    print("Jogadores:")
    for jogador in jogadores:
        print(f"Nome: {jogador.nome}, Classe: {jogador.classe}, Nível: {jogador.nivel}, Vida: {jogador.pontos_vida}, Level: {jogador.nivel}")

    inimigos = gerar_inimigos(len(jogadores), nivel)
    print("Inimigos:")
    for inimigo in inimigos:
        print(f"Nome: {inimigo.nome}, Classe: {inimigo.classe}, Nível: {inimigo.nivel}, Vida: {inimigo.pontos_vida}, Level: {inimigo.nivel}")

    return inimigos

def rodada(jogadores, inimigos):
    print("--- Rodada ---")
    

    for jogador in jogadores:
        if jogador.esta_vivo():
            print(f"\nTurno do jogador {jogador.nome} ({jogador.classe}), Nível: {jogador.nivel}")
            print("Escolha um inimigo para atacar:")
            for i, inimigo in enumerate(inimigos):
                print(f"{i + 1}. {inimigo.nome} ({inimigo.classe}), Nível: {inimigo.nivel}")

            while True:
                escolha = input("Opção: ")
                if escolha.isdigit() and 0 < int(escolha) <= len(inimigos):
                    alvo = inimigos[int(escolha) - 1]
                    acao = jogador.escolher_acao()

                    if acao == "atacar":
                        jogador.atacar(alvo)
                        if not alvo.esta_vivo():
                            inimigos.remove(alvo)
                            jogador.ganhar_experiencia(50)
                            print(f"O inimigo {alvo.nome} foi derrotado!")
                    elif acao == "defender":
                        jogador.defender()
                        print(f"O jogador {jogador.nome} escolheu se defender.")
                    elif acao == "esquivar":
                        jogador.esquivar()
                        print(f"O jogador {jogador.nome} escolheu esquivar-se.")
                    else:
                        print("Opção inválida. O jogador perdeu a vez.")
                    break
                else:
                    print("Opção inválida. Tente novamente.")

    for inimigo in inimigos:
        if inimigo.esta_vivo():
            print(f"\nTurno do inimigo {inimigo.nome} ({inimigo.classe}), Nível: {inimigo.nivel}")
            alvo = random.choice(jogadores)
            inimigo.atacar(alvo)
            if not alvo.esta_vivo():
                jogadores.remove(alvo)
                print(f"O jogador {alvo.nome} foi derrotado!")

    print("\n--- Status ---")
    print("Jogadores:")
    for jogador in jogadores:
        print(f"Nome: {jogador.nome}, Vida: {jogador.pontos_vida}, Experiência: {jogador.experiencia}, Level: {jogador.nivel}")

    for inimigo in inimigos:
        if inimigo.esta_vivo():
            print(f"\nTurno do inimigo {inimigo.nome} ({inimigo.classe})")
            alvo = random.choice(jogadores)
            inimigo.atacar(alvo)
            if not alvo.esta_vivo():
                jogadores.remove(alvo)
                print(f"O jogador {alvo.nome} foi derrotado!")

    print("\n--- Status ---")
    print("Jogadores:")
    for jogador in jogadores:
        print(f"Nome: {jogador.nome}, Vida: {jogador.pontos_vida}, Experiência: {jogador.experiencia}")

    print("Inimigos:")
    for inimigo in inimigos:
        print(f"Nome: {inimigo.nome}, Vida: {inimigo.pontos_vida}")

    print("\n--- Fim da rodada ---")

def reiniciar_jogo():
    while True:
        resposta = input("Deseja iniciar um novo jogo? (S/N): ")
        if resposta.upper() == "S" or resposta.upper() == "N":
            return resposta.upper() == "S"
        else:
            print("Opção inválida. Digite 'S' para sim ou 'N' para não.")

def avancar_para_proxima_fase():
    while True:
        resposta = input("Deseja avançar para a próxima fase? (S/N): ")
        if resposta.upper() == "S" or resposta.upper() == "N":
            return resposta.upper() == "S"
        else:
            print("Opção inválida. Digite 'S' para sim ou 'N' para não.")

def validar_nome(nome):
    return nome.isalpha() and len(nome) > 0

def jogar():
    print("=== Batalha de RPG ===")
    conn = criar_conexao()  # Criar a conexão com o banco de dados
    criar_tabelas(conn)  # Criar as tabelas no banco de dados
    
    while True:
        try:
            num_jogadores = int(input("Quantos jogadores irão jogar? "))
            nivel = 1
            jogadores = []
            
            for i in range(num_jogadores):
                while True:
                    nome = input(f"Digite o nome do jogador {i + 1}: ")
                    if validar_nome(nome.strip()):
                        break
                    else:
                        print("O nome deve conter apenas letras. Tente novamente.")

                print("Escolha a classe do jogador:")
                print("1. Cavaleiro")
                print("2. Bárbaro")
                print("3. Druida")
                print("4. Feiticeiro")
                print("5. Arqueiro")
                while True:
                    try:
                        escolha = int(input("Opção: "))
                        if escolha in [1, 2, 3, 4, 5]:
                            break
                        else:
                            print("Opção inválida. Tente novamente.")
                    except ValueError:
                        print("Opção inválida. Digite um número inteiro.")

                if escolha == 1:
                    classe = "Cavaleiro"
                elif escolha == 2:
                    classe = "Bárbaro"
                elif escolha == 3:
                    classe = "Druida"
                elif escolha == 4:
                    classe = "Feiticeiro"
                elif escolha == 5:
                    classe = "Arqueiro"
                else:
                    print("Opção inválida. Classe padrão 'Cavaleiro' será escolhida.")
                    classe = "Cavaleiro"

                jogador = Jogador(nome.strip(), classe, nivel)
                jogadores.append(jogador)

            while True:
                inimigos = gerar_fase(jogadores, nivel)
                while len(jogadores) > 0 and len(inimigos) > 0:
                    rodada(jogadores, inimigos)

                if len(jogadores) == 0:
                    print("\n--- Fim de jogo ---")
                    print("Todos os jogadores foram derrotados.")
                    break

                if not avancar_para_proxima_fase():
                    break
                else:
                    nivel += 1
        except ValueError:
            print("Quantidade inválida. Digite um número inteiro positivo.")
            continue

        if not reiniciar_jogo():
            break
    
        conn.close()

jogar()
