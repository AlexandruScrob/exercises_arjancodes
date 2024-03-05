```mermaid
flowchart LR
Model --> |notifies| Presenter
Presenter --> |updates| Model
Presenter --> |updates| View
View --> |notifies| Presenter
```
