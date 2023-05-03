# Metrics Consumer

Este proyecto es un Cron Job que corre cada 1 minuto.
Es el Consumer de las metricas guardadas en Redis por el proyecto `metrics-queue`.
Su trabajo es, para todas las métricas, procesarlas levantándolas desde Redis, agregarlas, y guardarlas ya procesadas en un documento JSON en una base de datos MongoDB.

Si se quiere cambiar el intervalo en el que corre el cron, modificar el archivo de kubernetes.
