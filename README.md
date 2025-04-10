# 🐍 Snake Game com Ranking em Python (Pygame)

Bem-vindo ao **Jogo Snake com Ranking**, uma versão moderna do clássico jogo Snake desenvolvida em Python com a biblioteca Pygame.

Neste jogo, você controla uma cobrinha que cresce ao comer alimentos, enquanto tenta alcançar a maior pontuação possível. O diferencial é o sistema de ranking, que salva as 5 melhores pontuações!

---

## 🚀 Funcionalidades

- **Jogabilidade clássica:** Controle a cobrinha com as setas do teclado e coma alimentos para crescer.
- **Sistema de pontuação:** Cada alimento consumido vale 10 pontos.
- **Dificuldade progressiva:** A velocidade da cobrinha aumenta a cada 50 pontos.
- **Ranking:** Salva automaticamente as 5 melhores pontuações em `highscores.txt`.
- **Tela inicial:** Mensagem de boas-vindas ao iniciar o jogo.
- **Fim de jogo:** Opções para sair (Q) ou reiniciar o jogo (C).

---

## 📥 Instalação e Execução

### 📋 Pré-requisitos:
- Python 3.x ([Baixar Python](https://www.python.org/downloads/))
- Biblioteca Pygame

### 📦 Instalação:

Clone o repositório:
```bash
git clone https://github.com/K-Galvao-Filho/game-snake_clone.git
```

Entre no diretório do projeto:
```bash
cd game-snake_clone
```

Instale as dependências com:
```bash
pip install -r requirements.txt
```

### ▶️ Execução:

Inicie o jogo com:
```bash
python snake.py
```

---

## 🎮 Instruções para Jogar

- **Iniciar:** Pressione qualquer tecla na tela inicial.
- **Controles:** Use as setas para movimentar a cobrinha:
  - ⬆️ Seta para cima
  - ⬇️ Seta para baixo
  - ⬅️ Seta para esquerda
  - ➡️ Seta para direita

- **Objetivo:** Coma o alimento (quadrado vermelho) para crescer e acumular pontos.

- **Fim de jogo:** Termina se a cobrinha colidir com as paredes ou com o próprio corpo.

Após perder:
- Pressione **Q** para sair.
- Pressione **C** para jogar novamente.

---

## 🏆 Ranking das Pontuações

O ranking é exibido ao final do jogo:

**Exemplo:**
```
Sua pontuação: 120

Ranking:
1. 200
2. 150
3. 120
4. 80
5. 50

Você perdeu! Q-Sair  C-Jogar novamente
```

O arquivo `highscores.txt` é criado automaticamente após o primeiro jogo.

---

## 📁 Estrutura do Projeto

```
game-snake_clone
│
├── snake.py
├── highscores.txt (gerado automaticamente)
├── README.md
├── requirements.txt
└── screenshot.png (opcional)
```

---

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pygame](https://www.pygame.org/)

---

## 📚 Sugestão para Aprendizado

Ideal para quem deseja aprender conceitos fundamentais em jogos:
- Eventos do teclado
- Renderização gráfica básica
- Armazenamento simples de dados

---

## 📜 Licença

Este projeto está sob licença MIT.

---

Desenvolvido por [K-Galvao-Filho](https://github.com/K-Galvao-Filho).