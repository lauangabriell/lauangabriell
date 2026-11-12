# Redesign do perfil de Lauan Gabriell

Validação realizada em 12 de novembro de 2026.

## Implementação

O perfil abre com o nome, a formação e um estúdio em pixel art ao anoitecer. Os quatro projetos receberam ilustrações que representam seus fluxos. O texto de cada projeto descreve o problema, a contribuição de Lauan, a implementação e os caminhos para conhecer o trabalho.

A folha de sprites anterior definiu a escala e a silhueta. As duas fotos serviram de referência para o rosto e a roupa. As poses de ação foram geradas com essas referências e ajustadas à mesma grade e paleta. A passada, os quadros intermediários e a cena foram reconstruídos no código. O aceno também aparece no encerramento como ilustração estática.

O ciclo do README tem caminhada, pausa com respiração e piscada, olhar para os lados, reflexão, consulta ao celular, programação, comemoração e aceno. A edição com controles fica no HTML separado. O alongamento ficou pendente nesta versão.

## Evidências de conteúdo

- **VETOR** · O README e o código de treinamento documentam o Random Forest. A documentação de arquitetura mostra a separação entre diálogo e inferência e a confirmação dos dados. [Repositório](https://github.com/lauangabriell/Delivery-Intelligence-Agent)
- **DIKE** · A contribuição e a decisão de paginação foram descritas pelo autor. O site institucional confirma questões, filtros e flashcards. O código da plataforma tem acesso privado, então o perfil encaminha visitantes ao site. [DIKE](https://dike-estudos-juridicos.pages.dev/)
- **Observatório** · O pipeline e a diferença entre acurácia e recall positivo aparecem na documentação pública dos experimentos. [Repositório](https://github.com/lauangabriell/observatorio-reputacao)
- **TEIA** · O README e o servidor do MVP público documentam o fluxo de adaptação, Node.js e Gemini. O autor informou sua participação na idealização, liderança, prompts e integração. [Repositório](https://github.com/lauangabriell/TEIA-MVPv1) · [MVP](https://teia-henna.vercel.app/)

A referência do DenverCoder1 mostrou como o README pode concentrar conteúdo profissional e contato em seções reconhecíveis. Pretty GitHub mostrou o valor de publicar fontes visuais ao lado dos assets renderizados. Neste perfil, a cena e os cards foram desenhados para a identidade e os projetos de Lauan. [DenverCoder1](https://github.com/DenverCoder1/DenverCoder1) · [Pretty GitHub](https://github.com/Jenesyx/pretty-github)

## Testes

| Verificação | Resultado |
| --- | --- |
| Renderização no GitHub | A prévia foi conferida na branch `redesign-perfil` e a versão publicada abriu na página pública do perfil. Foram conferidos títulos, ilustrações e a navegação para projetos. |
| GIF | 768 × 268 px, 198 quadros, 35,23 s e 329.214 bytes. A decodificação conferiu cores e duração de cada quadro com o render de origem. |
| Caminhada | O teste das coordenadas confirmou que o pé de apoio mantém a posição durante a passada. A alternância de braços, pernas e direções foi inspecionada em uma folha de quadros. |
| Sprites | 36 poses com alfa de 0 ou 255. As áreas claras dos tênis, da camisa e do rosto foram conferidas em fundos claros, escuros e coloridos. |
| Compatibilidade | O GitHub conservou os elementos `picture`, `source` e `img`, resolveu os caminhos para `main` e aplicou largura máxima de 100% às imagens. A captura real é de desktop em tema claro. O tema escuro e um viewport de celular no GitHub seguem pendentes de verificação no navegador. |
| Acessibilidade | Cabeçalhos e links são texto nativo. A cena e o aceno têm descrições. Os SVGs decorativos têm alternativa vazia. O README oferece link para a imagem estática e uma fonte com a preferência de movimento reduzido. |
| Links | Repositórios públicos, documentação do VETOR, site da DIKE e MVP da TEIA foram verificados. O LinkedIn recusou a consulta automatizada. Foi usado o endereço fornecido pelo autor. |
| Estúdio interativo | No navegador, conferi programação, aceno, reprodução, pausa e reinício. O teste da lógica JavaScript cobriu os cinco trechos e o início pausado com movimento reduzido. O estúdio hospedado usa acesso privado. O HTML com as imagens incorporadas pode ser baixado pelo README e aberto localmente. |

O GitHub documenta a sanitização do HTML e os controles de reprodução de GIF. A cena usa GIF para a animação e PNG para a alternativa estática. O HTML separado usa Canvas e JavaScript para oferecer os controles. [GitHub Markup](https://github.com/github/markup) · [Acessibilidade no GitHub](https://docs.github.com/pt/account-and-profile/how-tos/account-settings/managing-accessibility-settings)

## Avaliação

| Critério | Peso | Nota | Evidência |
| --- | ---: | ---: | --- |
| Identidade visual e originalidade | 20% | 9,0 | Estúdio próprio, suéter vinho e elementos de projeto com a mesma direção visual. |
| Animação pixel art | 20% | 8,5 | Passada com apoio verificável, pausas e oito ações. Alguns gestos usam poucos quadros. |
| Apresentação profissional dos projetos | 20% | 9,0 | Contribuição, stack, decisão técnica e link para cada projeto. |
| UX, legibilidade e responsividade | 15% | 8,0 | Hierarquia e navegação verificadas em desktop. Validação visual em celular pendente. |
| Implementação técnica | 15% | 9,0 | Assets no repositório, paleta determinística e fontes de edição. |
| Performance e acessibilidade | 10% | 8,5 | GIF de aproximadamente 322 KiB, SVGs pequenos e opção estática. |

**Nota ponderada · 8,7/10**

## Arquivos e manutenção

| Caminho | Conteúdo |
| --- | --- |
| `README.md` | Texto, links e estrutura do perfil. |
| `assets/branding/studio.png` | Primeiro quadro da cena para leitura com movimento reduzido. |
| `assets/pixel-character/animations/studio.gif` | Sequência exibida no perfil. |
| `assets/pixel-character/sprites/base-poses.png` e `action-poses.png` | Células de origem com 58 × 68 px, alfa e base dos pés na linha 64. |
| `assets/pixel-character/sprites/atlas.png` e `atlas.json` | Atlas gerado e coordenadas das poses. |
| `assets/projects/` | Quatro ilustrações em SVG editável. |
| `scripts/` | Fontes da composição, da animação e do HTML interativo. |
| `docs/estudio.html` | [Estúdio com controles para abrir no navegador](estudio.html). |

Para recompilar no Windows a partir da raiz do repositório:

```powershell
py -3.12 -m pip install -r scripts/requirements.txt
py -3.12 scripts/build_profile_art.py
```

Em Linux ou macOS, use `python3` com a mesma dependência.

Para adicionar uma pose, edite a folha transparente e registre a célula em `scripts/sprite_poses.py`. Depois, ajuste a sequência e as durações em `storyboard()` dentro de `scripts/build_profile_art.py`. A recompilação atualiza o GIF, o atlas, o PNG estático e o estúdio interativo. Para disponibilizar um trecho adicional no seletor, registre seu intervalo em `export_preview()` e inclua a opção em `scripts/estudio.template.html`.

Para adicionar um projeto, crie uma subseção em **Projetos** no README e coloque a ilustração em `assets/projects/`. Mantenha a contribuição, o detalhe técnico e os links como texto do README.
