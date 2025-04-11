
# 📖 AMT 8000 - Integração com Home Assistant

Este é o guia oficial de instalação e uso da integração nativa da central de alarme **Intelbras AMT 8000** com o Home Assistant.

## 📦 Instalação via HACS

1. Acesse **HACS > Integrações > 3 pontos > Repositórios personalizados**
2. Adicione:
   ```
   https://github.com/SEU_USUARIO/home-assistant-amt8000
   ```
   Selecione o tipo `Integration`
3. Reinicie o Home Assistant
4. Vá até **Configurações > Dispositivos e Serviços** e clique em “Adicionar Integração”
5. Procure por **AMT8000** e configure com o IP e a porta do seu Receptor IP

## ⚙️ Serviços Disponíveis

Você pode usar o serviço `amt8000.send_raw_command` para enviar comandos manuais:

```yaml
service: amt8000.send_raw_command
data:
  pgm_on: 1
```

## 🧠 Recursos suportados

- Armar/desarmar central
- Controle de PGMs
- Requisição de imagens de sensores com câmera
- Leitura de status de zonas/sensores
- Interface traduzida para português

## 🛠️ Requisitos

- Home Assistant 2023.5+
- Receptor IP Intelbras configurado em rede
- Central de Alarme AMT 8000 com firmware atualizado

---

Desenvolvido com ❤️ por [Seu Nome]
