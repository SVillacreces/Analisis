# Crear el primer gráfico: Madrid vs. Media Nacional
plt.figure(figsize=(10, 5))
plt.plot(years, madrid_values, label="Madrid", color="blue")
plt.plot(years, media_nacional_values, label="Media Nacional", color="orange")
plt.title("Evolución de la Estancia Media: Madrid vs. Media Nacional")
plt.xlabel("Año")
plt.ylabel("Estancia Media (días)")
plt.xticks(np.arange(2019, 2024, 1))  # Mostrar solo años enteros en el eje x
plt.legend()
plt.grid(True)
plt.show()

# Crear el segundo gráfico: Madrid vs. Barcelona
plt.figure(figsize=(10, 5))
plt.plot(years, madrid_values, label="Madrid", color="blue")
plt.plot(years, barcelona_values, label="Barcelona", color="green")
plt.title("Evolución de la Estancia Media: Madrid vs. Barcelona")
plt.xlabel("Año")
plt.ylabel("Estancia Media (días)")
plt.xticks(np.arange(2019, 2024, 1))  # Mostrar solo años enteros en el eje x
plt.legend()
plt.grid(True)
plt.show()

# Crear un dataframe simulado basado en los datos de estancia media en Madrid y Barcelona
boxplot_data = pd.DataFrame({
    "Categoría": ["Madrid"] * len(madrid_values) + ["Barcelona"] * len(barcelona_values),
    "Estancia Media (días)": np.concatenate([madrid_values, barcelona_values])
})

# Crear un boxplot para comparar la estancia media entre Madrid y Barcelona
plt.figure(figsize=(8, 6))
boxplot_data.boxplot(by="Categoría", column="Estancia Media (días)", grid=False)

# Personalizar el gráfico
plt.title("Distribución de la Estancia Media en Madrid y Barcelona")
plt.suptitle("")  # Eliminar título automático de pandas
plt.xlabel("Ciudad")
plt.ylabel("Estancia Media (días)")

# Mostrar el gráfico
plt.show()
