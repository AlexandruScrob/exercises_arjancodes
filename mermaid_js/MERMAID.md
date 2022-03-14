# Mermaid

Extension: Markdown Preview Mermaid Support.
Mermaid live editor: https://mermaid.live
CheatSheet: https://jojozhuang.github.io/tutorial/mermaid-cheat-sheet/

1. Flowchart
```mermaid
flowchart LR
    S[Start] --> A;
    A(Enter your email address) --> B{Existing user?};
    B -->|No| C(Enter name)
    C --> D{Accept conditions?}
    D -->|No| A
    D -->|Yes| E(Send email with magic link)
    B -->|Yes| E
    E --> End;
```


2. SequenceDiagram
```mermaid
sequenceDiagram
autonumber
    participant Client
    participant OAuthProvider
    participant Server
    Client ->> OAuthProvider: Request access token
    activate OAuthProvider
    OAuthProvider ->> Client: Send access token
    deactivate OAuthProvider
    Client ->> Server: Request resource
    activate Server
    Server ->> OAuthProvider: Validate token
    activate OAuthProvider
    OAuthProvider->>Server: Token valid
    deactivate OAuthProvider
    Server ->> Client: Send resource
    deactivate Server
```


3. ClassDiagram
```mermaid
classDiagram
    class Order {
        +OrderStatus status
    }
    class OrderStatus {
        <<enumeration>>
        FAILED
        PENDING
        PAID
    }
    class PaymentProcessor {
        <<interface>>
        -String apiKey
        #connect(String url, JSON header)
        +processPayment(Order order) OrderStatus
    }
    class Customer {
        +String name
    }
    Customer <|-- PrivateCustomer
    Customer <|-- BusinessCustomer
    PaymentProcessor <|-- StripePaymentProcessor
    PaymentProcessor <|-- PayPalPaymentProcessor

    Order o-- Customer
    Car *-- Engine
```


4. EntityRelationshipDiagram
```mermaid
erDiagram
    Customer ||--o{ Order : places
    Order ||--|{ LineItem : contains
    Customer {
        String id
        String name
    }
    Order {
        String id
        OrderStatus status
    }
    LineItem {
        String code
        String description
        int quantity
        int price
    }
```