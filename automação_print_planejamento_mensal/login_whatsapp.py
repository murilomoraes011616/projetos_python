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

        caixa_de_pesquisa = pagina.get_by_role("textbox", name="Pesquisar ou começar uma nova conversa")
        caixa_de_pesquisa.wait_for()
        caixa_de_pesquisa.click()
        caixa_de_pesquisa.fill(nome_do_contato)
        pagina.wait_for_timeout(1000)

        primeiro_resultado = pagina.get_by_test_id("list-item-0")
        primeiro_resultado.wait_for()
        primeiro_resultado.click()

        # Confirma que a conversa certa realmente abriu
        cabecalho_conversa = pagina.get_by_role("heading", name=nome_do_contato)
        cabecalho_conversa.wait_for()

        botao_anexar = pagina.get_by_role("button", name="Anexar")
        botao_anexar.click()

        with pagina.expect_file_chooser() as info_seletor_arquivo:
            opcao_documento = pagina.get_by_role("menuitem", name="Documento")
            opcao_documento.click()

        seletor_arquivo = info_seletor_arquivo.value
        seletor_arquivo.set_files(caminho_do_pdf)

        botao_enviar = pagina.get_by_role("button", name="Enviar 1 item selecionado")
        botao_enviar.wait_for()
        botao_enviar.click()

        input("Confira se a mensagem foi enviada, e pressione Enter para fechar...")

    except Exception as erro:
        print(f"Deu erro: {erro}")
        input("Deu erro, mas o navegador vai ficar aberto pra você investigar. Pressione Enter para fechar...")

    finally:
        navegador.close()