<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="styles/animations.css">

    <style>

        /* =========================
           MENU
        ========================= */

        #menu {
            width: 100%;
            box-sizing: border-box;

            background-color: #49D6B5;

            position: fixed;
            top: 0;
            left: 0;

            display: flex;
            justify-content: center;
            align-items: center;

            text-align: center;

            padding: 8px 2%;
            margin: 0;

            z-index: 50;

            flex-wrap: wrap;

            gap: 5px;
        }


        /* =========================
           LINKS
        ========================= */

        .estiloMenu {
            padding: 10px 15px;
            margin: 2px;

            color: black;
            text-decoration: none;

            font-family: Arial, sans-serif;

            border-radius: 8px;

            flex: 1 1 120px;

            transition:
                background-color 0.3s,
                color 0.3s,
                transform 0.2s;
        }


        .estiloMenu:hover {
            background-color: #599688;
            color: white;

            transform: translateY(-2px);
        }


        /* =========================
           BOTÃO
        ========================= */

        #but {
            flex-basis: 100%;

            display: flex;
            justify-content: center;
        }


        #but button {
            background-color: #599688;

            color: white;

            padding: 5px 18px;

            border: none;

            border-radius: 0 0 15px 15px;

            cursor: pointer;

            font-size: 16px;

            transition: 0.2s;
        }


        #but button:hover {
            background-color: #40776b;
        }


        /* =========================
           MENU ESCONDIDO
        ========================= */

        .baixo {
            transform: translateY(-70px);
            transition: transform 1s;
        }


        .normal {
            transform: translateY(0);
            transition: transform 0.5s;
        }


        /* =========================
           TABLET
        ========================= */

        @media (max-width: 768px) {

            #menu {
                padding: 6px 3%;
            }

            .estiloMenu {
                flex: 1 1 40%;
                padding: 9px;
            }

        }


        /* =========================
           CELULAR
        ========================= */

        @media (max-width: 480px) {

            #menu {
                padding: 5px;
                gap: 2px;
            }

            .estiloMenu {
                flex: 1 1 45%;

                padding: 10px 5px;

                font-size: 14px;
            }

            #but button {
                padding: 5px 20px;
            }

        }

    </style>
</head>
<body>

    <header>

        <nav id="menu" class="baixo">

            <div></div>

            <a href="#inicio" class="estiloMenu">
                Página Inicial
            </a>

            <a href="#sobre" class="estiloMenu">
                Sobre Nós
            </a>

            <a href="#julia" class="estiloMenu">
                Julia
            </a>

            <a href="#rafael" class="estiloMenu">
                Rafael
            </a>

            <a href="#kayllan" class="estiloMenu">
                Kayllan
            </a>

            <div id="but" onclick="desce()">
                <button>V</button>
            </div>

        </nav>

    </header>
    <script>
        function desce(){

            const menu = document.getElementById("menu");
        
            menu.style.transitionDelay = "0s";
        
            menu.classList.remove("baixo");
            menu.classList.add("normal");
        
            setTimeout(() => {
        
                menu.classList.remove("normal");
                menu.classList.add("baixo");
        
            }, 5000);
        
        }
    </script>
</body>

<html>
    <head>
        <link rel="stylesheet" href="styles/style.css">
        <link rel="stylesheet" href="animations.css">
    </head>
    <body>
        

        <section id="inicio">
            <div class="container">
                <div>
                    <h2>Bem-Vindos Ao Nosso Site</h2>
                    <p>
                        Eu, Rafael, junto de meus amigos Julia e Kayllan, criamos esse site para apresentarmos nossos projetos no dia D da tecnologia.<br>
                        Abaixo vocês escontraram informações sobre nós e alguns dos projetos que eu mencionei acima.
                    </p>
                </div>
            </div>
        </section>

        <section id="sobre">
            <div class="container">
                <h2>Sobre Nós</h2>
            </div>

            <section id="julia">
                <div class="container1">
                    <h3>Julia</h3>
                </div>
            </section>
            
            <section id="rafael">
                <div class="container1">
                    <h3>Rafael</h3>
                    <p>
                        Olá, eu sou Rafael e no momento sou um aluno do segundo ano. Gosto de jogos antigos e histórias de fantasias(Não é atoa que eu estou escrevendo uma).<br>
                        Sobre minhas criações, abaixo vocês encontrarão um link para uma página onde estão grande parte delas.
                    </p>
                    <a href="rafael.html" class="link">Click Aqui</a>
                </div>
                
                <div class="container1">
                    <p>Entre todas as minhas criações, as melhores e mais desenvolvidas são:</p>
                    <div>
                        
                        <h4>Elemental Hunters</h4>
                </div>
            </section>

            <section id="kayllan">
                <div class="container1">
                    <h3>Kayllan</h3>
                </div>
            </section>
        </section>
        <script src="scripts.js"></script>
    </body>
</html>
