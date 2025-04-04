
```mermaid
graph LR
    A[Extract PDF] --> B[PDFs]
    B --> C[MDS Marker]
    C --> D[MDS Clean Marker]
    D --> E[Generate Samples with Model]
    E --> F[Generated Samples Dataframe]
```