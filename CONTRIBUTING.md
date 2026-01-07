# Contribuyendo a ETL para Ingenieros Pesqueros 🎣

¡Gracias por tu interés en contribuir! Este documento proporciona pautas para contribuir al proyecto.

## 🌟 Código de Conducta

Este proyecto se adhiere a un Código de Conducta. Al participar, te comprometes a mantener un ambiente respetuoso y acogedor para todos.

## 🚀 ¿Cómo puedo contribuir?

### 🐛 Reportar Bugs

Si encuentras un bug, por favor crea un issue incluyendo:
- Descripción clara del problema
- Pasos para reproducirlo
- Comportamiento esperado vs. comportamiento actual
- Capturas de pantalla (si aplica)
- Versión de Python y sistema operativo

### 💡 Sugerir Mejoras

¿Tienes una idea para mejorar el proyecto? ¡Genial! Crea un issue con:
- Descripción clara de la mejora
- Por qué sería útil para la comunidad
- Ejemplos de implementación (si es posible)

### 📝 Contribuir con Código

1. **Fork el repositorio**
2. **Crea una rama** para tu feature:
   ```bash
   git checkout -b feature/mi-nueva-caracteristica
   ```
3. **Realiza tus cambios** siguiendo las convenciones de estilo
4. **Escribe tests** (si aplica)
5. **Commit tus cambios**:
   ```bash
   git commit -m "Add: descripción clara de la mejora"
   ```
6. **Push a tu fork**:
   ```bash
   git push origin feature/mi-nueva-caracteristica
   ```
7. **Crea un Pull Request** con descripción detallada

### 📚 Mejorar la Documentación

La documentación es crucial. Puedes ayudar:
- Corrigiendo errores tipográficos
- Mejorando explicaciones
- Añadiendo ejemplos
- Traduciendo a otros idiomas

### 🎓 Crear Notebooks

Si tienes expertise en análisis pesquero, puedes:
- Crear nuevos notebooks de ejemplo
- Mejorar los notebooks existentes
- Añadir casos de estudio reales

## 📋 Estándares de Código

### Python

- Seguir PEP 8
- Usar nombres descriptivos de variables
- Documentar funciones con docstrings
- Comentar código complejo

Ejemplo:
```python
def transform_landings_data(df):
    """
    Transforma y limpia datos de desembarques
    
    Args:
        df (pd.DataFrame): DataFrame con datos crudos de desembarques
        
    Returns:
        pd.DataFrame: DataFrame transformado y limpio
        
    Raises:
        ValueError: Si el DataFrame está vacío
    """
    # Tu código aquí
    pass
```

### Commits

Usa mensajes descriptivos:
- `Add: nueva funcionalidad`
- `Fix: corrección de bug`
- `Update: actualización de contenido`
- `Refactor: mejora de código`
- `Docs: cambios en documentación`

## 🧪 Testing

Antes de enviar tu PR, asegúrate de:
- [ ] El código funciona correctamente
- [ ] No hay errores de sintaxis
- [ ] Los notebooks se ejecutan sin problemas
- [ ] La documentación está actualizada

Ejecuta el script de prueba:
```bash
python test_project.py
```

## 🎯 Áreas Prioritarias

Actualmente necesitamos ayuda en:

1. **Datos Reales**: Ejemplos con datos pesqueros reales (anonimizados)
2. **Visualizaciones**: Gráficos interactivos con Plotly
3. **Análisis Avanzados**: Notebooks de ML aplicado a pesquerías
4. **Traducciones**: Versiones en inglés, portugués
5. **Documentación**: Tutoriales en video, infografías

## 📞 ¿Preguntas?

Si tienes dudas sobre cómo contribuir:
- Abre un issue con la etiqueta `question`
- Contacta en nuestro Discord (próximamente)
- Envía un email a: fisheries.ai@comunidad.com

## 🙏 Reconocimientos

Todos los contribuyentes serán reconocidos en el proyecto. Tu nombre aparecerá en:
- Lista de contribuyentes en el README
- Sección de agradecimientos en la documentación
- Badges especiales en la comunidad

---

**¡Gracias por ayudar a hacer crecer la comunidad de Ingenieros Pesqueros en IA!** 🌊🤖
