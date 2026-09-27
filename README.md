# SISTEMA DE RESERVAS DE HOTEL POR WELLINGTON D. ANGELO
Projeto individial da disciplina ES0008 - Programação Orientada a Objetos ministrada no semestre 2026.2

 ---
## Objetivo
O projeto consiste em desenvolver uma API de um sistema de reservas de hotel. Este permitirá acesso aos dados de hóspedes, quartos e reservas com check-in/check-out. Também devendo conter tratamentos para política de cancelamento, tarifas por temporada, bloqueios por manutenção e relatórios de desempenho.

---

## Estrutura planejada de classes
```
app/
├── main.py
│
├── models/
│   ├── pessoas.py
│   │   ├── pessoa
│   │   ├── Funcionario
│   │   └── Hospede
│   │
│   ├── quartos.py
│   │   ├── Quarto
│   │   ├── Simples
│   │   ├── Duplo
│   │   └── Luxo
│   │
│   ├── Registros.py
│   │   ├── Registro
│   │   ├── Reserva
│   │   ├── Pagamento
│   │   ├── Adicional
│   │   └── Bloqueio
│   │
│   └── Rastreabilidade.py
│       └── Rastreabilidade
│
├── Services/
│   ├── relatorios.py
│   └── tarifas.py
│
└── Routes/
    ├── hospedes.py
    ├── quartos.py
    └── reservas.py
```
---
## UML TEXTUAL

```mermaid
classDiagram

%% Definição das Classes

   %% ==================== Super Classe Pessoas ===================

   class Pessoa <<abstract>> {
      -str nome
      -str documento
      -str email
      -str telefone
      -str id
      +cadastrarPessoa() str
   }

   class Hospede {
      +gerenciarHospedes() str
      +requisitarHospede() str
  }

   class Funcionario {
      -str cargo
      +gerenciarFuncionario() str
      +requisitarFuncionario() str
   }

   %% ======= Heranças ========

   Pessoa <|-- Hospede
   Pessoa <|-- Funcionario

   %% ====== Associações ======

   Hospede "0..*" -- "0..*" Reserva : Realiza
   Funcionario "1" --> "0..*" Bloqueio : Autoriza/Remove

   %% ================= Classe para Rastreabilidade ===============

      class Rastreabilidade {
      -date criado_em
      -date editado_em
      -str criado_por
      -str editado_por
      +rastrearCriacao() str
      +rastrearEdicao() str
   }

   %% =================== Super Classe Registro ===================
   
   class Registro {
      -str id
      -str origem
      -date data
      -char tipo
      -char status
      +novoRegistro() str
   }

   class Reserva {
      -date data_entrada
      -date data_saida
      -int qtd_hospedes
      -float adicionais
      -list pagamentos
      +confirmar()
      +cancelarReserva() str
      +checkIn()
      +checkOut()
      +total_pago() float
      +total_devido() float
   }

   class Pagamento {
      -char forma
      -str reserva
      -float valor
      +registrarPagamento() str
      +editarPagamento() str
      +statusPagamento() char
   }

   class Adicional {
      -str descricao
      -float valor
      +registrarAdicional() str
      +editarAdicinoal() str
      +gerenciarDescricao() str
   }

   class Bloqueio {
      -char tipo_de_bloqueio
      -str motivo
      -date prazo_para_desbloqueio
      +bloquearQuarto() str
      +editarBloqueio() str
      +agendarDesbloqueio() date
   }

   %% ====== Heranças ======

   Registro <|-- Reserva
   Registro <|-- Bloqueio

   %% == Herança Múltipla ==
   Rastreabilidade <|-- Reserva
   Rastreabilidade <|-- Pagamento
   Rastreabilidade <|-- Bloqueio

   %% ==== Composições ======

   Reserva "1" *-- "0..*" Pagamento : Composição
   Reserva "1" *-- "0..*" Adicional : Composição

   %% ================= Super Classe Quarto ===============

   class Quarto {
      -str numero
      -int capacidade
      -float diaria
      -char status
      -list bloqueios
      -str observacoes
      +requisitarQuarto() str
   }

   class Simples {
      -str diferencial
      +diferenciarSimples() str
      +observacoesSimples() str
   }
   class Duplo {
      -str diferencial
      +diferenciarDuplo() str
      +observacoesDuplo() str
   }
   class Luxo {
      -str diferencial
      +observacoesLuxo() str
   }

   %% ======= Heranças =======

   Quarto <|-- Simples
   Quarto <|-- Duplo
   Quarto <|-- Luxo

   %% ====== Associações ======

   Quarto "1" --> "0..*" Registro : Pode ser vinculado

   %% ======================= Serviços ====================

   class Tarifa {
      -char tipo
      +calcularDiaria() float
      +aplicarDesconto() float
   }

   class Relatorio {
      -char tipo
      +taxa_ocupacao() float
      +adr() float
      +revpar() float
   }

   %% ==== Relações ====

   Reserva ..> Tarifa : Usa
   Relatorio ..> Reserva : Lê
   ```