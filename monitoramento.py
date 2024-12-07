class Usuario:
    def __init__(self, id, nome, email, senha, perfil):  
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfil = perfil

class Medidor:
    def __init__(self, id, numero_serie, localizacao, tipo):  
        self.id = id
        self.numero_serie = numero_serie
        self.localizacao = localizacao
        self.tipo = tipo
        self.leituras = []

class Leitura:
    def __init__(self, id, medidor_id, data_leitura, consumo, status):  
        self.id = id
        self.medidor_id = medidor_id
        self.data_leitura = data_leitura
        self.consumo = consumo
        self.status = status

class Consumo:
    def __init__(self, id, leitura_id, valor, unidade):  
        self.id = id
        self.leitura_id = leitura_id
        self.valor = valor
        self.unidade = unidade

class Alerta:
    def __init__(self, id, medidor_id, tipo, limite, status):  
        self.id = id
        self.medidor_id = medidor_id
        self.tipo = tipo
        self.limite = limite
        self.status = status

class HistoricoConsumo:
    def __init__(self, id, medidor_id, data_inicio, data_fim, consumo_total): 
        self.id = id
        self.medidor_id = medidor_id
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.consumo_total = consumo_total

class ConfiguracaoSistema:
    def __init__(self, id, limite_consumo_diario, limite_consumo_mensal, unidade_medida):  
        self.id = id
        self.limite_consumo_diario = limite_consumo_diario
        self.limite_consumo_mensal = limite_consumo_mensal
        self.unidade_medida = unidade_medida

class Notificacao:
    def __init__(self, id, alerta_id, usuario_id, mensagem, data_envio):  
        self.id = id
        self.alerta_id = alerta_id
        self.usuario_id = usuario_id
        self.mensagem = mensagem
        self.data_envio = data_envio

class SistemaMonitoramento:
    def __init__(self):  
        self.usuarios = []
        self.medidores = []
        self.leituras = []
        self.consumos = []
        self.alertas = []
        self.historico_consumo = []
        self.configuracao_sistema = ConfiguracaoSistema(1, 100, 3000, "m3")
        self.notificacoes = []

    def adicionar_usuario(self, usuario):  
        self.usuarios.append(usuario)  

    def adicionar_medidor(self, medidor):
        self.medidores.append(medidor)

    def adicionar_leitura(self, leitura):
        self.leituras.append(leitura)

    def gerar_consumo(self, leitura_id):
        leitura = next((l for l in self.leituras if l.id == leitura_id), None)
        if leitura:
            consumo = Consumo(len(self.consumos) + 1, leitura_id, leitura.consumo, "m3")
            self.consumos.append(consumo)

    def gerar_alerta(self, medidor_id):
        medidor = next((m for m in self.medidores if m.id == medidor_id), None)
        if medidor:
            alerta = Alerta(len(self.alertas) + 1, medidor_id, "consumoAlto", 150, "Ativo")
            self.alertas.append(alerta)
    
    def enviar_notificacao(self, alerta_id, usuario_id, datetime):
        alerta = next((a for a in self.alertas if a.id == alerta_id), None)
        if alerta:
            notificacao = Notificacao(len(self.notificacoes) + 1, alerta_id, usuario_id, "Consumo alto detectado!", datetime)
            self.notificacoes.append(notificacao)

from datetime import datetime

sistema = SistemaMonitoramento()
usuario1 = Usuario(1, "João", "joao@exemplo.com", "senha123", "admin")  
sistema.adicionar_usuario(usuario1)

medidor1 = Medidor(1, "123456", "Casa", "residencial")
sistema.adicionar_medidor(medidor1)

leitura1 = Leitura(1, 1, "2024-12-07", 100, "valido")
sistema.adicionar_leitura(leitura1)

sistema.gerar_consumo(1)
sistema.gerar_alerta(1)
sistema.enviar_notificacao(1, 1, datetime.now())  

print("Usuários:")
for usuario in sistema.usuarios:
    print(f"ID: {usuario.id}, Nome: {usuario.nome}")

print("\nMedidores:")
for medidor in sistema.medidores:
    print(f"ID: {medidor.id}, Número Série: {medidor.numero_serie}")

print("\nLeituras:")
for leitura in sistema.leituras:
    print(f"ID: {leitura.id}, Consumo: {leitura.consumo}")

print("\nConsumos:")
for consumo in sistema.consumos:
    print(f"ID: {consumo.id}, Valor: {consumo.valor}")

print("\nAlertas:")
for alerta in sistema.alertas:
    print(f"ID: {alerta.id}, Tipo: {alerta.tipo}")

print("\nNotificações:")
for notificacao in sistema.notificacoes:
    print(f"ID: {notificacao.id}, Mensagem: {notificacao.mensagem}")