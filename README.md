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
├── database.py
├── dependencies.py
├── models/
│   ├── __init__.py
│   ├── rastreios.py
│   ├── pessoas.py
│   ├── quartos.py
│   └── registros.py
├── schemas/
│   ├── hospede.py
│   ├── quarto.py
│   └── reserva.py
├── services/
│   ├── tarifas.py
│   └── relatorios.py
└── routes/
    ├── hospedes.py
    ├── quartos.py
    ├── reservas.py
    └── bloqueios.py
tests/
```
---
## UML TEXTUAL

```mermaid
classDiagram

%% Definição das Classes

   %% ==================== Super Classe Pessoas ===================

   class Pessoa <<abstrata>> {
      -str nome
      -str documento
      -str email
      -str telefone
      -str id
      +cadastrarPessoa() str
   }

   class Hospede <<concreta>> {
      +gerenciarHospedes() str
      +requisitarHospede() str
  }

   class Funcionario <<concreta>> {
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

      class Rastreabilidade <<abstrata>> {
      -date criado_em
      -date editado_em
      -str criado_por
      -str editado_por
      +rastrearCriacao() str
      +rastrearEdicao() str
   }

   %% =================== Super Classe Registro ===================
   
   class Registro <<abstrata>> {
      -str id
      -str origem
      -date data
      -char tipo
      -char status
      +novoRegistro() str
   }

   class Reserva <<concreta>> {
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

   class Pagamento <<concreta>> {
      -char forma
      -str reserva
      -float valor
      +registrarPagamento() str
      +editarPagamento() str
      +statusPagamento() char
   }

   class Adicional <<concreta>> {
      -str descricao
      -float valor
      +registrarAdicional() str
      +editarAdicinoal() str
      +gerenciarDescricao() str
   }

   class Bloqueio <<concreta>> {
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

   class Quarto <<abstrata>> {
      -str numero
      -int capacidade
      -float diaria
      -char status
      -list bloqueios
      -str observacoes
      +requisitarQuarto() str
   }

   class Simples <<concreta>> {
      -str diferencial
      +diferenciarSimples() str
      +observacoesSimples() str
   }
   class Duplo <<concreta>> {
      -str diferencial
      +diferenciarDuplo() str
      +observacoesDuplo() str
   }
   class Luxo <<concreta>> {
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

   class Tarifa <<concreta>> {
      -char tipo
      +calcularDiaria() float
      +aplicarDesconto() float
   }

   class Relatorio <<concreta>> {
      -char tipo
      +taxa_ocupacao() float
      +adr() float
      +revpar() float
   }

   %% ==== Relações ====

   Reserva ..> Tarifa : Usa
   Relatorio ..> Reserva : Lê
   ```
