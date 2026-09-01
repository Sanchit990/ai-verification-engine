                           
                          AI Verification Engine v1.0
                    Hierarchical Multi-Agent Verification Architecture

A hierarchical multi-agent financial reconciliation framework that combines independent AI reasoning, consensus generation, auditing, 
and hierarchical decision-making to produce reliable and explainable reconciliation decisions.
## Architecture 
```text
                                 Raw Dataset
                                      │
                                      ▼
                             Data Preprocessor
                   (Validation • Cleaning • Normalization)
                                      │
                     ┌────────────────┴────────────────┐
                     │                                 │
                     ▼                                 ▼
               Full Dataset                    Primary Dataset
          (Primary + Secondary)             (Primary Rules Only)
                     │                                 │
                     ▼                                 ▼
                Pair 1 (Semantic)               Pair 2 (Deterministic)
                     │                                 │
              ┌──────┴──────┐                  ┌───────┴───────┐
              │             │                  │               │
             A1            A2                 A1              A2
              │             │                  │               │
              └─────────────┘──────────────────└───────────────┘     
                     │                                         |
                     ▼                                         ▼            
               Consensus Engine                           Consensus Engine
                     │                                         |
                     ▼                                         ▼
           Pair 1 Consensus Report                 Pair 2 Consensus Report
                     │                                         │
                     └──────────────────┬──────────────────────┘
                                        ▼
                                 Auditor Report
                       (Comparison • Risk • Recommendation
                         • Reasoning • Evidence Analysis)
                                        │
                                        ▼
                                     Judge
                                        │
                  ┌─────────────────────┴──────────────────────┐
                  │                                            │
                  ▼                                            ▼
      Recommendation Supported?                     Not Convinced
                  │                                            │
            ┌─────┴─────┐                                      ▼
            │           │                            Auditor Re-evaluation
            ▼           ▼                                      │
         Accept       Retry                            Same Recommendation?
                                                              │
                                                     ┌────────┴────────┐
                                                     │                 │
                                                     ▼                 ▼
                                                Human Review       Continue

```


## Design Philosophy

The system follows a hierarchical consensus architecture.

- Pair 1 performs semantic reconciliation using both primary and secondary evidence.
- Pair 2 performs deterministic reconciliation using only primary reconciliation fields.
- Each pair reaches an internal consensus before publishing a Pair Consensus Report.
- The Auditor compares the two consensus reports, performs evidence analysis, and issues a reasoned recommendation.
- The Judge validates whether the Auditor's recommendation is supported by the available evidence. If unconvinced, one auditor re-evaluation is requested. Persistent disagreement results in human review.


## Workflow

Raw Dataset
    ↓
Data Preprocessor
    ↓
Pair 1 (Semantic Analysis)
    ↓
Pair 2 (Deterministic Analysis)
    ↓
Consensus Generation
    ↓
Auditor
    ↓
Judge
    ↓
Final Decision


## Key Features

- Hierarchical multi-agent reasoning
- Independent semantic and deterministic reconciliation
- Consensus-driven reconciliation
- Independent audit layer
- Final judicial decision layer
- Structured Pydantic outputs
- Synthetic dataset generation with controlled error injection

## Tech Stack

- Python 3.14
- Google Gemini API
- Pydantic
- Faker
- dotenv


## Project Structure 

```text
ai-verification-engine/
│
├── agents/
├── models/
├── workflow/
├── data/
├── prompts/
├── reports/
└── tests/
```

## Future Improvements

- Retry mechanism with exponential backoff
- BaseAgent refactoring to reduce duplicate code
- Human feedback integration
- Performance benchmarking
- Dashboard for report visualization

## Current Status

- [x] Synthetic data generation
- [x] Error injection
- [x] Hierarchical AI reasoning
- [x] Pair consensus generation
- [x] Auditor layer
- [x] Judge layer
- [ ] Evaluation metrics