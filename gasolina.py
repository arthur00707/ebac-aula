import pandas as pd
import matplotlib.pyplot as plt

# Cria o DataFrame a partir dos dados
data = pd.read_csv('gasolina.csv')

# Calcular a média acumulada
data['media_acumulada'] = data['venda'].expanding().mean()

# Plotar o gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(data['dia'], data['media_acumulada'], marker='o', linestyle='-', color='b', label='Média Acumulada')
plt.xlabel('Dia')
plt.ylabel('Média da Venda')
plt.title('Média Acumulada da Venda de Gasolina')
plt.grid(True)
plt.legend()
plt.savefig('gasolina.png')
plt.show()