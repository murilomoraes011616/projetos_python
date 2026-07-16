from playwright.sync_api import sync_playwright

caminho_da_sessao = r'C:\Users\murilo.oliveira\Desktop\sessao_whatsapp'
nome_do_contato = "Murilo , da MITRA Assessoria IA"
caminho_do_pdf = r'C:\Users\murilo.oliveira\OneDrive - Greentech\Perfil\Desktop\lugar dos pdf para autoamação\tabela.pdf'

with sync_playwright() as p:
    navegador = p.chromium.launch_persistent_context(
        caminho_da_sessao,
        headless=False,
        channel="chrome"
    )
    pagina = navegador.new_page()
    pagina.set_default_timeout(60000)

    try:
        pagina.goto("https://web.whatsapp.com")
        pagina.wait_for_load_state("networkidle")
        pagina.wait_for_timeout(10000)   # espera 10s extra pra tudo carregar de vez

        caixa_de_pesquisa = pagina.get_by_role("textbox", name="Pesquisar ou começar uma nova conversa")
        caixa_de_pesquisa.wait_for()
        caixa_de_pesquisa.click()
        caixa_de_pesquisa.fill(nome_do_contato)

        print("Nome digitado, esperando 10 segundos antes de entrar na conversa...")
        pagina.wait_for_timeout(10000)   # a pausa principal que você pediu

        pagina.keyboard.press("Enter")

        print("Enter pressionado, esperando mais 10 segundos pra conversa carregar...")
        pagina.wait_for_timeout(10000)   # espera a conversa "assentar" de vez

        pagina.screenshot(path=r'C:\Users\murilo.oliveira\Desktop\debug_apos_entrar_conversa.png')
        print("Print de debug salvo: debug_apos_entrar_conversa.png")

        botao_anexar = pagina.get_by_role("button", name="Anexar")
        botao_anexar.click()
        pagina.wait_for_timeout(3000)

        pagina.screenshot(path=r'C:\Users\murilo.oliveira\Desktop\debug_menu_anexar.png')
        print("Print de debug salvo: debug_menu_anexar.png")

        with pagina.expect_file_chooser() as info_seletor_arquivo:
            opcao_documento = pagina.get_by_role("menuitem", name="Documento")
            opcao_documento.wait_for()
            opcao_documento.click()

        seletor_arquivo = info_seletor_arquivo.value
        seletor_arquivo.set_files(caminho_do_pdf)

        print("Arquivo anexado, esperando 5 segundos pro preview carregar...")
        pagina.wait_for_timeout(5000)

        pagina.screenshot(path=r'C:\Users\murilo.oliveira\Desktop\debug_preview_pdf.png')
        print("Print de debug salvo: debug_preview_pdf.png")

        botao_enviar = pagina.get_by_role("button", name="Enviar 1 item selecionado")
        botao_enviar.wait_for()
        botao_enviar.click()

        input("Confira se a mensagem foi enviada, e pressione Enter para fechar...")

    except Exception as erro:
        print(f"Deu erro: {erro}")
        try:
            pagina.screenshot(path=r'C:\Users\murilo.oliveira\Desktop\debug_erro.png')
            print("Print do erro salvo: debug_erro.png")
        except Exception:
            print("Não consegui tirar o print de debug (navegador já estava fechado).")
        input("Deu erro, mas o navegador vai ficar aberto pra você investigar. Pressione Enter para fechar...")

    finally:
        navegador.close()