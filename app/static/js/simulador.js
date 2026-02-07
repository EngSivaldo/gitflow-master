// Lógica simples para simular comandos Git
function executarComando() {
  const input = document.getElementById("terminal-input").value.trim();
  const output = document.getElementById("terminal-output");

  if (input === "git clone") {
    output.innerHTML += `<p class="text-white mt-2">Cloning into 'gitflow-master'...</p>`;
    output.innerHTML += `<p class="text-green-400">remote: Counting objects: 100% (10/10), done.</p>`;
    output.innerHTML += `<p class="text-blue-400">✓ Sucesso! Agora entre na pasta com 'cd'.</p>`;
  } else if (input === "git status") {
    output.innerHTML += `<p class="text-white mt-2 italic">On branch main. Your branch is up to date.</p>`;
  } else {
    output.innerHTML += `<p class="text-red-500 mt-2">Comando '${input}' não reconhecido neste estágio.</p>`;
  }

  document.getElementById("terminal-input").value = "";
}
