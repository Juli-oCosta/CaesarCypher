# CaesarCypher

---

✨ Funcionalidades

- Criptografia: Transforma um texto legível em um texto cifrado com base em uma chave (shift).

- Descriptografia: Reverte o processo, transformando o texto cifrado de volta ao original.

- Lógica Circular: Utiliza o operador de módulo (%) para garantir que o alfabeto "dê a volta" corretamente (ex: 'z' com shift 2 vira 'b').

- Interface Interativa: Permite que o usuário execute o programa repetidamente sem precisar reiniciar o script.

---

🚀 Como Usar

Execute o script Python em seu terminal: Bash python main.py

- O programa solicitará que você escolha a direção: encode para criptografar ou decode para descriptografar.

- Digite a mensagem que deseja processar.

- Digite o número de posições para o deslocamento (a "chave" da cifra).

- O resultado será exibido na tela.

- Você será perguntado se deseja executar o programa novamente. Digite yes para continuar ou no para sair.

---

⚠️ Limitações e Melhorias Futuras

- O programa em seu estado atual possui algumas limitações que abrem portas para melhorias futuras:

- Caracteres Limitados: O script atualmente só funciona com letras minúsculas do alfabeto (a-z). Ele irá gerar um erro se a mensagem contiver espaços, números, pontuação ou letras maiúsculas.

- Melhoria Sugerida: Implementar uma verificação dentro do loop para identificar se um caractere pertence ao alfabeto. Se não pertencer, ele deve ser mantido no texto final sem alterações.
