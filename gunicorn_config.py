# Configuração do Gunicorn
import multiprocessing

# Número de workers (processos)
# Recomendação: (2 x núcleos de CPU) + 1
workers = multiprocessing.cpu_count() * 2 + 1

# Tipo de worker
worker_class = "sync"

# Timeout para requisições (em segundos)
timeout = 30

# Nível de log
loglevel = "info"

# Arquivo de log de acesso
accesslog = "-"  # - significa stdout

# Arquivo de log de erros
errorlog = "-"  # - significa stderr

# Recarregar automaticamente quando o código mudar (apenas para desenvolvimento)
reload = False
