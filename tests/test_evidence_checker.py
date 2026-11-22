import unittest
from unittest.mock import patch

from langchain_core.documents import Document

from rag.evidence_checker import (
    check_evidence,
    EvidenceAssessment,
    SupportingEvidence
)


class TestEvidenceChecker(unittest.TestCase):

    def setUp(self):
        self.relevant_document = Document(
            page_content=(
                "Complementary feeding should begin "
                "at around six months of age."
            ),
            metadata={"source_file": "who_guideline.md"}
        )

        self.exclusion_document = Document(
            page_content=(
                "This summary does not contain: "
                "individual calorie requirements, "
                "individual protein requirements, "
                "or treatment recommendations for malnutrition."
            ),
            metadata={"source_file": "who_guideline.md"}
        )

    def test_no_documents(self):
        result = check_evidence(
            query="When should complementary feeding begin?",
            documents=[]
        )

        self.assertEqual(
            result["status"],
            "insufficient_evidence"
        )

    def test_explicitly_out_of_scope(self):
        result = check_evidence(
            query="What are the individual calorie requirements?",
            documents=[self.exclusion_document]
        )

        self.assertEqual(
            result["status"],
            "explicitly_out_of_scope"
        )

    @patch("rag.evidence_checker._evaluate_retrieved_evidence")
    def test_valid_supporting_evidence(self, mock_evaluator):

        mock_evaluator.return_value = EvidenceAssessment(
            status="supported",
            reason="The document directly answers the question.",
            supporting_evidence=[
                SupportingEvidence(
                    quote=(
                        "Complementary feeding should begin "
                        "at around six months of age."
                    ),
                    source_file="who_guideline.md"
                )
            ],
            missing_information=[]
        )

        result = check_evidence(
            query="When should complementary feeding begin?",
            documents=[self.relevant_document]
        )

        self.assertEqual(result["status"], "supported")
        self.assertEqual(len(result["supporting_evidence"]), 1)

    @patch("rag.evidence_checker._evaluate_retrieved_evidence")
    def test_fabricated_quote_rejected(self, mock_evaluator):

        mock_evaluator.return_value = EvidenceAssessment(
            status="supported",
            reason="The document directly answers the question.",
            supporting_evidence=[
                SupportingEvidence(
                    quote="Complementary feeding should begin at four months.",
                    source_file="who_guideline.md"
                )
            ],
            missing_information=[]
        )

        result = check_evidence(
            query="When should complementary feeding begin?",
            documents=[self.relevant_document]
        )

        self.assertEqual(
            result["status"],
            "insufficient_evidence"
        )
        self.assertEqual(result["supporting_evidence"], [])

    @patch("rag.evidence_checker._evaluate_retrieved_evidence")
    def test_incorrect_source_filename_rejected(self, mock_evaluator):

        mock_evaluator.return_value = EvidenceAssessment(
            status="supported",
            reason="The document directly answers the question.",
            supporting_evidence=[
                SupportingEvidence(
                    quote=(
                        "Complementary feeding should begin "
                        "at around six months of age."
                    ),
                    source_file="incorrect_source.md"
                )
            ],
            missing_information=[]
        )

        result = check_evidence(
            query="When should complementary feeding begin?",
            documents=[self.relevant_document]
        )

        self.assertEqual(
            result["status"],
            "insufficient_evidence"
        )
        self.assertEqual(result["supporting_evidence"], [])

    @patch("rag.evidence_checker._evaluate_retrieved_evidence")
    def test_partially_supported_evidence(self, mock_evaluator):

        mock_evaluator.return_value = EvidenceAssessment(
            status="partially_supported",
            reason="The document answers only part of the question.",
            supporting_evidence=[
                SupportingEvidence(
                    quote=(
                        "Complementary feeding should begin "
                        "at around six months of age."
                    ),
                    source_file="who_guideline.md"
                )
            ],
            missing_information=["Specific meal quantities."]
        )

        result = check_evidence(
            query=(
                "When should complementary feeding begin "
                "and how much should I give?"
            ),
            documents=[self.relevant_document]
        )

        self.assertEqual(
            result["status"],
            "partially_supported"
        )

    @patch("rag.evidence_checker._evaluate_retrieved_evidence")
    def test_insufficient_evidence(self, mock_evaluator):

        mock_evaluator.return_value = EvidenceAssessment(
            status="insufficient_evidence",
            reason="The retrieved content does not answer the question.",
            supporting_evidence=[],
            missing_information=["Required information is absent."]
        )

        result = check_evidence(
            query="What medicine treats severe malnutrition?",
            documents=[self.relevant_document]
        )

        self.assertEqual(
            result["status"],
            "insufficient_evidence"
        )


if __name__ == "__main__":
    unittest.main()