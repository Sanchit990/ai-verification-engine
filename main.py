from data.synthetic_data_generator import SyntheticDataGenerator
from workflow.error_injector import ErrorInjector
from workflow.data_processor import DataPreprocessor

# Pair 1
from agents.pair1.a1 import A1
from agents.pair1.a2 import A2
from agents.pair1.consensus import ConsensusEngine
from models.pair1 import Pair1Report

# Pair 2
from agents.pair2.a1 import A1 as Pair2A1
from agents.pair2.a2 import A2 as Pair2A2
from agents.pair2.consensus import ConsensusEngine as Pair2Consensus
from models.pair2 import Pair2Report

# Auditor
from agents.auditor import Auditor

# Judge
from agents.judge import Judge
from models.judge.verificationcase import VerificationCase


def main():

    print("=" * 80)
    print("AI VERIFICATION ENGINE")
    print("=" * 80)

    # =====================================================
    # Dataset
    # =====================================================

    print("\nGenerating Dataset...")

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

    print("✓ Dataset Ready")

    # =====================================================
    # Pair 1
    # =====================================================

    print("\nRunning Pair1 A1...")

    pair1_a1 = A1()
    pair1_a1_output = pair1_a1.analyze(full_records[0])

    print("✓ Pair1 A1")

    print("\nRunning Pair1 A2...")

    pair1_a2 = A2()
    pair1_a2_output = pair1_a2.analyze(full_records[0])

    print("✓ Pair1 A2")

    print("\nRunning Pair1 Consensus...")

    pair1_consensus = ConsensusEngine()

    pair1_consensus_report = pair1_consensus.analyze(
        pair1_a1_output,
        pair1_a2_output
    )

    pair1_report = Pair1Report(
        pair1_a1=pair1_a1_output,
        pair1_a2=pair1_a2_output,
        pair1_consensus=pair1_consensus_report
    )

    print("✓ Pair1 Consensus")
    print("=" * 80)
    print("PAIR 1 REPORT")
    print("=" * 80)
    print(pair1_report.model_dump_json(indent=2))

    # =====================================================
    # Pair 2
    # =====================================================

    print("\nRunning Pair2 A1...")

    pair2_a1 = Pair2A1()
    pair2_a1_output = pair2_a1.analyze(primary_records[0])

    print("✓ Pair2 A1")

    print("\nRunning Pair2 A2...")

    pair2_a2 = Pair2A2()
    pair2_a2_output = pair2_a2.analyze(primary_records[0])

    print("✓ Pair2 A2")

    print("\nRunning Pair2 Consensus...")

    pair2_consensus = Pair2Consensus()

    pair2_consensus_report = pair2_consensus.analyze(
        pair2_a1_output,
        pair2_a2_output
    )

    pair2_report = Pair2Report(
        pair2_a1=pair2_a1_output,
        pair2_a2=pair2_a2_output,
        pair2_consensus=pair2_consensus_report
    )

    print("✓ Pair2 Consensus")
    print("=" * 80)
    print("PAIR 2 REPORT")
    print("=" * 80)
    print(pair2_report.model_dump_json(indent=2))

    # =====================================================
    # Auditor
    # =====================================================

    print("\nRunning Auditor...")

    auditor = Auditor()

    auditor_report = auditor.analyze(
        pair1_report,
        pair2_report
    )

    print("✓ Auditor")
    print("=" * 80)
    print("AUDITOR REPORT")
    print("=" * 80)
    print(auditor_report.model_dump_json(indent=2))

    # =====================================================
    # Verification Case
    # =====================================================

    verification_case = VerificationCase(
        pair1_report=pair1_report,
        pair2_report=pair2_report,
        auditor_report=auditor_report
    )

    # =====================================================
    # Judge
    # =====================================================

    print("\nRunning Judge...")

    judge = Judge()

    judge_report = judge.analyze(
        verification_case
    )

    print("✓ Judge")
    print("=" * 80)
    print("JUDGE REPORT")
    print("=" * 80)
    print(judge_report.model_dump_json(indent=2))

    # =====================================================
    # Final Summary
    # =====================================================

    print("\n" + "=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)

    print(f"Pair1 Decision            : {pair1_report.pair1_consensus.final_decision}")
    print(f"Pair2 Decision            : {pair2_report.pair2_consensus.final_decision}")

    print(f"Auditor Recommendation    : {auditor_report.recommended_pair}")
    print(f"Auditor Next Action       : {auditor_report.next_action}")

    print(f"Judge Decision            : {judge_report.final_decision}")
    print(f"Judge Confidence          : {judge_report.final_confidence:.2f}")
    print(f"Judge Next Action         : {judge_report.next_action}")

    # =====================================================
    # Injected Errors
    # =====================================================

    print("\n" + "=" * 80)
    print("INJECTED ERRORS")
    print("=" * 80)

    for error in metadata:
        print(error)


if __name__ == "__main__":
    main()