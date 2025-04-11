# 🛡️ Intelbras AMT 8000 - Integração com Home Assistant

Integração nativa com a central de alarme **Intelbras AMT 8000**, via protocolo ISECNet, diretamente no Home Assistant. Permite controle, automações, sensores e notificações com suporte total a senha e até 64 zonas.

---

## ✅ Funcionalidades

- Armar / Desarmar a central com senha
- Suporte completo a até **64 zonas**
- Criação automática de `binary_sensor` por zona
- Painel Lovelace com status, sensores e câmera
- Disparo de eventos personalizados: `amt8000.zone_triggered`
- Personalização dos nomes das zonas via interface
- Execução de scripts com base na ativação de zonas
- Automação integrada com `scripts.yaml` e `automations.yaml`
- Suporte à autenticação com senhas de 4 ou 6 dígitos

---

## 🔒 Autenticação

Você deve fornecer:
- **IP** da central
- **Porta TCP** (ex: 9009)
- **Senha de acesso** (4 ou 6 dígitos)

---

## 🧰 Instalação via HACS (repositório customizado)

1. Acesse **HACS > Integrações > 3 pontos > Repositórios personalizados**
2. Adicione: `https://github.com/sergiobaiao/home-assistant-amt8000`
3. Tipo: `Integration`
4. Reinicie o HA e adicione a integração pela interface

---

## ⚙️ Serviços e Eventos

### Serviço disponível

```yaml
service: amt8000.send_raw_command
data:
  pgm_on: 1
```

### Evento emitido

```yaml
event_type: amt8000.zone_triggered
event_data:
  zone: Z01
  state: on
  name: Sala
```

---

## 🖼️ Painel Lovelace

Veja exemplo pronto em [`examples/lovelace_dashboard.yaml`](examples/lovelace_dashboard.yaml):

![Painel Lovelace AMT 8000](https://github.com/sergiobaiao/home-assistant-amt8000/raw/main/docs/amt8000_panel_example.png)

---

## 🧪 Exemplos incluídos

Veja a pasta [`examples/`](examples/) com:
- `automations.yaml`
- `scripts.yaml`
- `lovelace_dashboard.yaml`

---

## 🧩 Suporte futuro

A integração está preparada para:
- PGMs (atuadores)
- Sensores com câmera
- Sirenes
- Teclados e controles remotos
- Repetidores

---

## 👨‍💻 Desenvolvido por

**Sérgio Baião** – GitHub: [@sergiobaiao](https://github.com/sergiobaiao)  
Contribuições e pull requests são bem-vindos!

---

MIT License