1.    Borras la carpeta .venv
 
2 Crear un nuevo entorno virtual
En la terminal integrada de VS Code:
python -m venv .venv
Esto creará una nueva carpeta .venv dentro del proyecto.

3 Activar el nuevo entorno
Luego actívalo:
.\.venv\Scripts\activate

4 Instalar dependencias 
 instálalas con:
pip install -r requirements.txt

💡 5️⃣ (Opcional) Configurar VS Code para usar el nuevo entorno

Pulsa     Ctrl + Shift + P 
Escribe     “Python: Select Interpreter” 
Elige     el que diga algo como: 
.venv\Scripts\python.exe
Así VS Code usará ese entorno para ejecutar y depurar tu código.