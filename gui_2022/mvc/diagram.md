```mermaid
flowchart LR
    View --> |notifies| Controller
    View --> |reads| Model;
    Controller --> |updates| Model
```
