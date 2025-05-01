from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Rota principal para exibir o formulário
@app.route('/')
def index():
    return render_template('index.html')

# Rota para consultar a API do PNCP
@app.route('/consulta', methods=['GET'])
def consulta_pncp():
    # Obter parâmetros da requisição
    data_inicial = request.args.get('dataInicial')
    data_final = request.args.get('dataFinal')
    pagina = request.args.get('pagina')
    cnpj_orgao = request.args.get('cnpjOrgao')  # Opcional

    # Validar parâmetros obrigatórios
    if not data_inicial or not data_final or not pagina:
        return jsonify({"error": "Parâmetros obrigatórios: dataInicial, dataFinal, pagina"}), 400

    # Montar a URL da API
    base_url = "https://pncp.gov.br/api/consulta/v1/contratos"
    params = {
        "dataInicial": data_inicial,
        "dataFinal": data_final,
        "pagina": pagina
    }
    if cnpj_orgao:
        params["cnpjOrgao"] = cnpj_orgao

    # Fazer a requisição para a API do PNCP
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Levantar exceção para códigos de erro HTTP
        data = response.json()

        # Log da resposta completa
        print("Resposta da API:", data)

        # Verificar a estrutura do JSON retornado
        print("Estrutura do JSON retornado:", data.keys())

        # Tratar os dados recebidos
        contratos = []
        for item in data.get('data', []):  # Acessar a chave correta 'data'
            contratos.append({
                "numeroContrato": item.get("numeroContratoEmpenho"),
                "nomeOrgao": item.get("orgaoEntidade", {}).get("razaoSocial"),
                "valor": item.get("valorGlobal"),
                "dataAssinatura": item.get("dataAssinatura"),
                "objetoContrato": item.get("objetoContrato")  # Adicione mais campos, se necessário
            })

        # Log dos contratos tratados
        print("Contratos tratados enviados ao frontend:", contratos)

        return jsonify(contratos)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/consulta-atas', methods=['GET'])
def consulta_atas():
    # Obter parâmetros da requisição
    data_inicial = request.args.get('dataInicial')
    data_final = request.args.get('dataFinal')
    pagina = request.args.get('pagina')
    cnpj_orgao = request.args.get('cnpjOrgao')  # Opcional

    # Validar parâmetros obrigatórios
    if not data_inicial or not data_final or not pagina:
        return jsonify({"error": "Parâmetros obrigatórios: dataInicial, dataFinal, pagina"}), 400

    # Montar a URL da API
    base_url = "https://pncp.gov.br/api/consulta/v1/atas"
    params = {
        "dataInicial": data_inicial,
        "dataFinal": data_final,
        "pagina": pagina
    }
    if cnpj_orgao:
        params["cnpjOrgao"] = cnpj_orgao

    # Fazer a requisição para a API do PNCP
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Levantar exceção para códigos de erro HTTP
        data = response.json()

        # Log da resposta completa
        print("Resposta da API (Atas):", data)

        # Tratar os dados recebidos
        atas = []
        for item in data.get('data', []):  # Certifique-se de usar a chave correta
            atas.append({
                "numeroAta": item.get("numeroAtaRegistroPreco"),  # Número da Ata
                "nomeOrgao": item.get("nomeOrgao"),  # Nome do Órgão
                "valor": item.get("valorGlobal"),  # Valor
                "dataPublicacao": item.get("dataPublicacaoPncp"),  # Data de Publicação
                "objetoAta": item.get("objetoContratacao")  # Objeto da Ata
            })

        # Log das atas tratadas
        print("Atas tratadas enviadas ao frontend:", atas)

        return jsonify(atas)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)