import requests
from datetime import datetime, timedelta


def cotar():
    data_final = datetime.now().date()
    data_inicial = data_final - timedelta(days=365)

    resultados = []
    data = data_inicial

    while data <= data_final:
        data_formatada = data.strftime("%m-%d-%Y")

        url = (
            "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/"
            "odata/CotacaoDolarDia(dataCotacao=@dataCotacao)"
            f"?@dataCotacao='{data_formatada}'"
            "&$top=100&$format=json&$select=cotacaoCompra"
        )

        try:
            resposta = requests.get(url, timeout=10)
            resposta.raise_for_status()
            dados = resposta.json()

            if dados.get("value"):
                cotacao = dados["value"][0]["cotacaoCompra"]
            else:
                cotacao = None

        except (requests.RequestException, ValueError, KeyError, IndexError):
            cotacao = None

        resultados.append((data, cotacao))
        data += timedelta(days=1)

    print(
        f"\nCotações de compra do dólar: "
        f"{data_inicial.strftime('%d/%m/%Y')} a "
        f"{data_final.strftime('%d/%m/%Y')}\n"
    )

    for data, cotacao in resultados:
        if cotacao is not None:
            print(
                f"Data: {data.strftime('%d/%m/%Y')} | "
                f"Cotação de compra: R$ {cotacao:.4f}"
            )
        else:
            print(
                f"Data: {data.strftime('%d/%m/%Y')} | "
                "Sem cotação disponível"
            )


cotar()
