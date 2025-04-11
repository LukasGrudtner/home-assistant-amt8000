# 📝 Changelog - AMT 8000 Home Assistant Integration

## [1.0.0] - Lançamento inicial

### 🚀 Funcionalidades
- Integração nativa da central Intelbras AMT 8000 com Home Assistant
- Armar/desarmar a central (modo total e parcial) com autenticação
- Comando de controle de PGMs via serviço
- Leitura de status de zonas e zonas com suporte a até 64 zonas
- Requisição de imagens de sensores com câmera
- Interface traduzida para português e inglês
- Personalização de nomes das zonas via interface do usuário
- Serviço `amt8000.send_raw_command` para extensões futuras

### 🔒 Autenticação
- Suporte para **senhas de 4 ou 6 dígitos** para acessar e controlar a central AMT 8000

### 💥 Eventos e Automação
- Eventos `amt8000.zone_triggered` para automações baseadas em zonas ativadas/desativadas
- Notificações automáticas para ativação de zonas
- Execução de scripts (ex: ligar luzes, ativar sirene)

---

## 📆  Próximos lançamentos

- Suporte a **sensores com câmera**
- Integração com **teclados e controles remotos**
- Suporte para **repetidores e sirenes**