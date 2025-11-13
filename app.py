from flask import Flask, jsonify
import os
import platform
import psutil

app = Flask(__name__)

# Informações dos integrantes da equipe
MEMBROS = "Luiz Fernando Brasão e João Pedro Giovannoni"

@app.route('/info')
def info():
    """Rota que retorna o nome dos integrantes da equipe"""
    response = {
        "Membros": MEMBROS,
    }
    
    return jsonify(response)

@app.route('/metricas')
def metricas():
    """Rota que retorna as métricas do sistema em formato JSON"""
    # Obtém o PID do processo atual
    pid = os.getpid()
    
    # Obtém informações do processo atual
    process = psutil.Process(pid)
    
    # Memória utilizada em MB
    memory_info = process.memory_info()
    memory_mb = memory_info.rss / (1024 * 1024)  # Convertendo bytes para MB
    
    # Uso de CPU (%)
    cpu_percent = process.cpu_percent(interval=0.1)
    
    # Sistema operacional
    os_name = platform.system()
    os_version = platform.version()
    
    # Detecta a distribuição (para Linux)
    if os_name == "Linux":
        try:
            with open('/etc/os-release') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith('PRETTY_NAME'):
                        os_info = line.split('=')[1].strip().strip('"')
                        break
                else:
                    os_info = f"{os_name} ({platform.release()})"
        except:
            os_info = f"{os_name} ({platform.release()})"
    elif os_name == "Darwin":
        os_info = f"macOS ({platform.mac_ver()[0]})"
    elif os_name == "Windows":
        os_info = f"Windows ({platform.release()})"
    else:
        os_info = f"{os_name} ({platform.release()})"
    
    # Monta o dicionário de resposta
    response = {
        "Nome": MEMBROS,
        "PID": pid,
        "Memória usada": f"{memory_mb:.1f} MB",
        "CPU": f"{cpu_percent}%",
        "Sistema Operacional": os_info
    }
    
    return jsonify(response)

if __name__ == '__main__':
    # Para desenvolvimento local
    app.run(debug=True, host='0.0.0.0', port=5000)
