from datetime import datetime, timedelta

tipo_carro = "P" # P, M ou G
tempo_pequeno = 30
tempo_médio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou às {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_médio)
    print(f"O carro chegou às {data_atual} e ficará pronto ás {data_estimada}")
elif tipo_carro == "G":
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou às {data_atual} e ficará pronto ás {data_estimada}")
else:
    print("Tipo de carro inválido") 