🎮 Projeto de Automação de MOBA (Focado em LOL)

Bot de automação para jogos estilo MOBA, focado em simular ações humanas dentro do jogo (movimento, habilidades e interações), com estrutura modular e expansível.

🚀 Objetivo

Este projeto tem como objetivo automatizar ações repetitivas dentro do jogo, como:

Movimentação do personagem
Execução de habilidades
Interações com interface (menus/lobby)
Simulação de comportamento humano

Tudo isso de forma controlada, modular e fácil de expandir.



🧠 Estrutura do Projeto

BOT/
│
├── main.py
├── core/
│   └── input_controller.py
│
├── game/
│   ├── lobby_controller.py
│   └── game_controller.py
│
├── utils/
│   └── helpers.py
│
└── config/
    └── settings.py



📂 Descrição dos módulos
• main.py
Ponto de entrada do bot. Responsável por iniciar o fluxo principal.
• core/input_controller.py
Controla teclado e mouse (cliques, teclas pressionadas, delays).
• game/lobby_controller.py
Responsável por interações no lobby (entrar em partida, aceitar jogo, etc).
• game/game_controller.py
Lógica dentro da partida (movimentação, ações, rotação de habilidades).
• utils/helpers.py
Funções auxiliares reutilizáveis.
• config/settings.py
Configurações gerais (teclas, delays, tempos, etc).



⚙️ Tecnologias utilizadas
• Python 3.x
• Bibliotecas comuns:
  • pyautogui (controle de mouse/teclado)
  • keyboard (inputs)
  • timer (controle de delays)



🧩 Funcionalidades atuais

✔ Movimentação automatizada (W, A, S, D)
✔ Execução de sequência de ações
✔ Delay configurável entre ações
✔ Loop automático com tempo de espera
✔ Estrutura pronta para expansão



🛠️ Como executar
1 - Clone o repositório:
• git clone https://github.com/AlexManhes/Projeto-de-automacao-lol

2 - Acesse a pasta:
• cd Projeto-de-automação-LOL

3 - Instale as dependências: 
• pip install -r requirements.txt

4 - Execute o bot:
• python main.py



📌 Por que cada um?
• pyautogui → controle de mouse e teclado
• keyboard → captura/envio de teclas
• mouse → controle mais direto do mouse (opcional, mas útil)
• opencv-python → visão computacional (detectar elementos na tela)
• numpy → suporte ao OpenCV
• pillow → manipulação de imagens (usado pelo pyautogui também)



⚠️ Aviso importante

Este projeto é apenas para fins educacionais.

• Não é recomendado usar em jogos online competitivos.
• Pode violar os termos de uso de alguns jogos.
• Use por sua conta e risco.



🤝 Contribuição

Sinta-se livre para contribuir com melhorias.



📄 Licença

Este projeto está sob a licença MIT.
