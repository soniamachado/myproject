# Instalei um Docker em vez de instalar o SQL Server da microsof, devido à incompatabilidade de sql com o meu ubuntu versão para correr no wsl que possuo,
O wsl que tenho correr na VERSION_ID="24.04" comando: cat /etc/os-release
de acordo com o site https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-wsl-2?view=sql-server-ver17 explicação da instalação de um docker para o ubuntu 22.04. 
Um dia depois ao ler apercebi-me que sql server 2025 serve para o ubuntu 24.04 "Ubuntu 24.04 is supported in preview starting with SQL Server 2025 (17.x) Preview." sessão install tht SQL server command-line toola no install and connect (UBUNTU): https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-ubuntu?view=sql-server-ver17&tabs=ubuntu2004%2C2505ubuntu2404%2Codbc-ubuntu-1804

De qualquer forma é uma maneira de aprender algo diferente, desafiar para trabalhar com docker. O docker como sabem:
O Docker serve para correr aplicações em containers, que são ambientes isolados e leves (como mini-máquinas virtuais).

É muito usado para programação, cibersegurança e infraestrutura porque:

Evita problemas de instalação (já vem tudo empacotado).

Funciona igual em qualquer PC/servidor.

Permite criar laboratórios de teste rápidos e descartáveis.

Estava a trabalhar com SQL Server (MSSQL).
👉 Em vez de instalar o SQL no teu PC, usaste Docker para levantar uma instância rápida:
docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=<password>" \
   -p 1433:1433 --name sql1 --hostname sql1 \
   -d mcr.microsoft.com/mssql/server:2025-latest
Assim, tens um SQL Server 2025 a correr em container sem “poluir” o sistema.

Funcionamento do docker:
docker run só é usado 1ª vez (para criar o container).
Depois, basta usar docker start ou docker stop.
docker pull → só faz download da imagem (sem criar container). comando:docker pull mcr.microsoft.com/mssql/server:2025-latest
docker run → cria um container novo (a partir da imagem).comando:docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=<password>" \ -p 1433:1433 --name sql1 --hostname sql1 \ -d \ mcr.microsoft.com/mssql/server:2025-latest

O SQL Server para Linux funciona em modo serviço e é gerido por linha de comando ou por ferramentas externas.

Se não tens a parte gráfica (GUI), não há SQL Server Management Studio (SSMS), porque ele só funciona em Windows.
No Linux/Ubuntu, usas:sqlcmd → cliente de linha de comando para executar queries.Azure Data Studio → editor gráfico (tipo VS Code) que funciona em Linux, Windows e macOS.
3. Se não tivesses o WSL

👉 Mesmo sem o WSL, desde que estejas em Linux (Ubuntu físico ou em VM), consegues correr SQL Server para Linux.
A diferença é que não terias o SSMS (que é gráfico e exclusivo do Windows).
Mas podes:
Gerir por linha de comando (sqlcmd).
Ou instalar Azure Data Studio no Ubuntu (GUI).
Ou ainda ligar remotamente a partir de outro PC com SSMS.
O SQL Server 2025 tem suporte oficial para Ubuntu 22.04, mas ainda não há suporte oficial direto para Ubuntu 24.04 (que é versão mais recente), então usar Docker no Ubuntu 24.04 é uma forma confiável de rodar o SQL Server sem problemas de compatibilidade ou dependências.
No seu caso, com Ubuntu 24.04 WSL, usar Docker foi uma escolha correta para garantir estabilidade e compatibilidade do SQL Server 2025. No Ubuntu 22.04 com suporte oficial, poderia preferir instalar diretamente o SQL Server sem Docker, mas o Docker continua sendo uma opção muito válida e prática para ambientes WSL e desenvolvimento.Se está a usar Ubuntu 24.04 no WSL e o SQL Server 2025 suporta oficialmente Ubuntu 22.04, usar Docker para rodar SQL Server 2025 não foi desnecessário.

Isso porque:

Ubuntu 24.04 pode não ter suporte oficial ainda para SQL Server 2025, então a instalação direta pode apresentar incompatibilidades.

Docker isola o ambiente, garantindo que o SQL Server rode em ambiente controlado e compatível, independentemente da versão do Ubuntu no host.

Mesmo em Ubuntu 22.04, usar Docker é comum para facilitar gerenciamento, portabilidade e evitar possíveis problemas de configuração.



Neste moento, já corri o docker

Verifica se o container está a correr,comando: docker ps
Se o container não estiver a correr (mas existe parado), arranca-o com:docker start sql1
Liga-te ao SQL Server com sqlcmd: docker exec -it sql1 /opt/mssql-tools/bin/sqlcmd \
   -S localhost -U SA -P 'Your_password123'

