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
│   ├── Usuarios.py
│   │   ├── Usuario
│   │   ├── Funcionario
│   │   └── Hospede
│   │
│   ├── quartos.py
│   │   ├── Quarto
│   │   ├── Simples
│   │   ├── Duplo
│   │   └── Luxo
│   │
│   ├── registros.py
│   │   ├── Registro
│   │   ├── Reserva
│   │   ├── Pagamento
│   │   ├── Adicional
│   │   └── Bloqueio
│   │
│   └── auditavel.py
│       └── Rastreabilidade
│
├── services/
│   └── relatorios.py
│
└── routes/
    ├── hospedes.py
    ├── quartos.py
    └── reservas.py
```
---
## UML TEXTUAL

```mermaid
classDiagram

%% Definição das Classes

%% Super Classe Pessoas
   class Pessoas{
      -str nome
      -str documento
      -str email
      -str telefone
      -str id
      +cadastrarPessoa() str
   }

   class Hospede{
      -List reservas
      +gerenciarHospedes() str
      +requisitarHospede() str
  }

   class Funcionario{
      -str cargo
      +gerenciarFuncionario() str
      +requisitarFuncionario() str
   }

   %% Super Classe Registro
   class Registro{
      -str id
      -str origem
      -char tipo
      -char status
      +novoRegistro() str
   }

   class Reserva{
      -str id
      -str origem
      -char tipo
      -char status
      -str data_entrada
      -str data_saida
      -int qtd_hospedes
      -list hospedes
      -float adicionais
      -list pagamentos
      +confirmar()
      +cancelarReserva() str
      +checkIn()
      +checkOut()
      +pagamentoTotal() float
   }

   class Pagamento{
      -str id
      -char tipo
      -str data
      -char forma
      -str reserva
      -float valor
      +registrarPagamento() str
      +editarPagamento() str
      +statusPagamento() char
   }

   class Adicional{
      -str id
      -str descricao
      -str data
      -float valor
      +registrarAdicional() str
      +editarAdicioal() str
      +gerarDescricao() str
   }

   class Bloqueio{
      -str id
      -str origem
      -char status
      -char tipo
      -str motivo
      -str responsável
      -str desbloqueio
      +bloquearQuarto() str
      +editarBloqueio() str
      +agendarDesbloqueio() str
   }

   %% Super Classe Quarto
   class Quarto{
      -str numero
      -int capacidade
      -float diaria
      -char status
      -list bloqueios
      -str observacoes
      +requisitarQuarto() str
   }

   class Simples{
      -str numero
      -int capacidade
      -float diaria
      -char status
      -list bloqueios
      -str observacoes
      +observacoesSimples() str
   }

   class Duplo{
      -str numero
      -int capacidade
      -float diaria
      -char status
      -list bloqueios
      -str observacoes
      +observacoesDuplo() str
   }

   class Luxo{
      -str numero
      -int capacidade
      -float diaria
      -char status
      -list bloqueios
      -str observacoes
      +observacoesLuxo() str
   }

   class Auditavel{
      -str objeto_rastreado
      -str id_do_objeto
      -str criado_em
      -str editado_em
      -str criado_por
      -str editado_por
      +rastrearCriacao() str
      +rastrearEdicao() str
   }