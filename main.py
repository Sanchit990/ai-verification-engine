from data.synthetic_data_generator import SyntheticDataGenerator
from workflow.error_injector import ErrorInjector
from workflow.data_processor import DataPreprocessor

# Pair 1
from agents.pair1.a1 import A1
from agents.pair1.a2 import A2
from agents.pair1.consensus import ConsensusEngine

# Pair 2
from agents.pair2.a1 import A1 as Pair2A1
from agents.pair2.a2 import A2 as Pair2A2
from agents.pair2.consensus import ConsensusEngine as Pair2Consensus

# Auditor
from agents.auditor import Auditor

# Judge
from agents.judge import Judge


def main():

    print("=" * 80)
    print("AI VERIFICATION ENGINE")
    print("=" * 80)


    # Generate Dataset


    generator = SyntheticDataGenerator()

    invoices, transactions = generator.generate_batch(5)

    working_invoices, working_transactions = (
        generator.create_working_copy(
            invoices,
            transactions
        )
    )

    injector = ErrorInjector()

    metadata = injector.inject_errors(
        working_invoices,
        working_transactions
    )

    processor = DataPreprocessor()

    full_records = processor.create_full_records(
        working_invoices,
        working_transactions
    )

    primary_records = processor.create_primary_records(
        full_records
    )


    # Pair 1


    pair1_a1 = A1()
    pair1_a2 = A2()

    pair1_a1_output = pair1_a1.analyze(full_records[0])
    pair1_a2_output = pair1_a2.analyze(full_records[0])

    pair1_consensus = ConsensusEngine()

    pair1_report = pair1_consensus.analyze(
        pair1_a1_output,
        pair1_a2_output
    )


    # Pair 2


    pair2_a1 = Pair2A1()
    pair2_a2 = Pair2A2()

    pair2_a1_output = pair2_a1.analyze(primary_records[0])
    pair2_a2_output = pair2_a2.analyze(primary_records[0])

    pair2_consensus = Pair2Consensus()

    pair2_report = pair2_consensus.analyze(
        pair2_a1_output,
        pair2_a2_output
    )


    # Auditor


    auditor = Auditor()

    auditor_report = auditor.analyze(
        pair1_report,
        pair2_report
    )


    # Judge


    judge = Judge()

    judge_report = judge.analyze(
        pair1_report,
        pair2_report,
        auditor_report
    )


    # Summary


    print("\n" + "=" * 80)
    print("PAIR 1")
    print("=" * 80)
    print(
        f"Decision   : {pair1_report.final_decision}\n"
        f"Confidence : {pair1_report.final_confidence:.2f}"
    )

    print("\n" + "=" * 80)
    print("PAIR 2")
    print("=" * 80)
    print(
        f"Decision   : {pair2_report.final_decision}\n"
        f"Confidence : {pair2_report.final_confidence:.2f}"
    )

    print("\n" + "=" * 80)
    print("AUDITOR")
    print("=" * 80)
    print(
        f"Recommended Pair : {auditor_report.recommended_pair}\n"
        f"Next Action      : {auditor_report.next_action}\n"
        f"Confidence       : {auditor_report.final_confidence:.2f}"
    )

    print("\n" + "=" * 80)
    print("JUDGE")
    print("=" * 80)
    print(
        f"Final Decision : {judge_report.final_decision}\n"
        f"Confidence     : {judge_report.final_confidence:.2f}\n"
        f"Next Action    : {judge_report.next_action}"
    )

    print("\n" + "=" * 80)
    print("INJECTED ERRORS")
    print("=" * 80)

    for error in metadata:
        print(error)


if __name__ == "__main__":
    main()