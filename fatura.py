import pdfkit

# Indicar onde o wkhtmltopdf está instalado
caminho_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=caminho_wkhtmltopdf)

# Criando um HTML simples para gerar um PDF
html = """
<html>
<head>
<meta charset="UTF-8">
<title>Fatura</title></head>
<body>
    <h1>Fatura</h1>
    <p>Cliente: João Silva</p>
    <p>Valor: R$ 650,00</p>
    <p>Vencimento: 30/03/2025</p>
    <p>Observações: ... </p>
    

</body>
</html>
"""

# Gerar o PDF com a configuração correta
pdfkit.from_string(html, "fatura.pdf", configuration=config)

print("Fatura gerada com sucesso!")
