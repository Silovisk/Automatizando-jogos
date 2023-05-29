# Automatização do Jogo do Dinossauro

Este é um projeto que automatiza o famoso jogo do dinossauro disponível no navegador. O objetivo do projeto é criar um script que seja capaz de jogar o jogo do dinossauro automaticamente, sem intervenção humana.

## Funcionalidades

- O script utiliza a biblioteca `pyautogui` para controlar o mouse e o teclado.
- A captura de tela é realizada usando a biblioteca `PIL` (Python Imaging Library).
- A detecção de obstáculos é baseada na análise de pixels em uma determinada região da tela.
- O script pressiona a tecla de espaço para fazer o dinossauro pular sempre que um obstáculo é detectado.
- O jogo é reiniciado automaticamente após a perda.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Bibliotecas Python: `pyautogui` e `PIL`

## Como executar o projeto

1. Clone o repositório para o seu ambiente local:

   ```
   git clone <URL_DO_REPOSITÓRIO>
   ```

2. Acesse o diretório do projeto:

   ```
   cd nome-do-projeto
   ```

3. Execute o script Python:

   ```
   python main.py
   ```

4. Abra o jogo do dinossauro no seu navegador usando o seguinte link: [https://fivesjs.skipser.com/trex-game/](https://fivesjs.skipser.com/trex-game/)

5. O script automatizará o jogo e fará o dinossauro pular sempre que necessário.

## Aviso

Certifique-se de que o jogo esteja visível na tela e posicionado corretamente antes de executar o script. Caso contrário, a detecção de obstáculos pode não funcionar corretamente.

## Contribuição

Sinta-se à vontade para contribuir para o projeto, abrindo problemas (issues) ou enviando solicitações de pull (pull requests). Toda contribuição é bem-vinda!

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).