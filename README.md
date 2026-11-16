# 🏦 OOP Python Banking System

A clean, modular Python Banking System built using core Object-Oriented Programming principles.

## 🏗️ Class Diagram
```mermaid
classDiagram
    class BankAccount {
        <<Abstract>>
        +acc_no
        +name
        -__balance
        +history
        +deposit(amount)
        +withdraw(amount)*
        +show_history()
    }
    class SavingsAccount {
        +withdraw(amount)
    }
    class CurrentAccount {
        +withdraw(amount)
    }
    BankAccount <|-- SavingsAccount
    BankAccount <|-- CurrentAccount
