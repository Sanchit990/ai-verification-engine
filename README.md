                           
                          AI Verification Engine v1.0
                      Hierarchical Consensus Architecture



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
             A1            A2                 A3              A4
              │             │                  │               │
              └──── Consensus Engine ──────────┘               │
                     │                                 └─ Consensus Engine ─┘
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





## Design Philosophy

The system follows a hierarchical consensus architecture.

- Pair 1 performs semantic reconciliation using both primary and secondary evidence.
- Pair 2 performs deterministic reconciliation using only primary business rules.
- Each pair reaches an internal consensus before publishing a Pair Consensus Report.
- The Auditor compares the two consensus reports, performs evidence analysis, and issues a reasoned recommendation.
- The Judge validates whether the Auditor's recommendation is supported by the available evidence. If unconvinced, one auditor re-evaluation is requested. Persistent disagreement results in human review.