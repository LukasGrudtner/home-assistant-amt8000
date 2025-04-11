
# AMT8000 Integration for Home Assistant

Esta é uma integração personalizada para o Home Assistant que permite controlar e monitorar a central de alarme **Intelbras AMT 8000** via protocolo ISECNet e Receptor IP.

## 📦 Funcionalidades

- Armar/desarmar a central de alarme (total e parcial)
- Controle de PGMs (saídas programáveis)
- Recebimento e exibição de imagens de sensores com câmera
- Monitoramento de zonas/sensores via `binary_sensor`
- Comando manual via serviço `amt8000.send_raw_command`

## 🚀 Instalação

1. Baixe este repositório como ZIP ou clone com Git.
2. Copie o conteúdo da pasta `custom_components/amt8000/` para:
   ```
   /config/custom_components/amt8000/
   ```
3. Reinicie o Home Assistant.
4. Acesse *Configurações > Dispositivos e Serviços* e adicione a integração **AMT8000**.
5. Configure o IP e porta do seu Receptor IP Intelbras.

## 🛠️ Serviços disponíveis

Você pode usar o serviço `amt8000.send_raw_command` para enviar comandos adicionais:

```yaml
service: amt8000.send_raw_command
data:
  pgm_on: 1
```

```yaml
service: amt8000.send_raw_command
data:
  status_request: true
```

```yaml
service: amt8000.send_raw_command
data:
  request_photo: 2
```

## 📷 Integração com sensores de câmera

Ao receber eventos de sensores com câmera, é possível solicitar e exibir imagens via componente `camera`.

## 📚 Requisitos

- Central de Alarme Intelbras AMT 8000
- Receptor IP Intelbras com acesso à rede
- Home Assistant 2023.5 ou superior (recomendado)

## 👨‍💻 Contribuições

Pull Requests são bem-vindos! Você pode melhorar o parser de status, decodificação de eventos, ou adicionar cache local de imagens.

---

MIT License · Desenvolvido com ❤️ por [Seu Nome ou Organização]
