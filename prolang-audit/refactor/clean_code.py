"""After: focused functions split validation, scoring, pricing, and formatting.
After: named constants replace magic numbers and guard clauses flatten nesting.
Before: see smelly_code.py for the original god function with arrow anti-pattern.
"""

LONG_REPORT_PAGE_THRESHOLD = 30
LONG_REPORT_SCORE = 25
SHORT_REPORT_SCORE = 10
HIGH_CITATION_THRESHOLD = 10
HIGH_CITATION_SCORE = 40
LOW_CITATION_SCORE = 15
CODE_INCLUDED_SCORE = 20
CODE_MISSING_SCORE = 5
RUSH_BASE_FEE = 500
STANDARD_BASE_FEE = 200
RUSH_PER_PAGE_FEE = 12
STANDARD_PER_PAGE_FEE = 8
APPROVAL_SCORE_THRESHOLD = 70


def validate_submission(submission: dict[str, object]) -> str | None:
    """Return an error message when submission data is invalid."""
    if not submission.get("title"):
        return "Title is required."
    if "pages" not in submission:
        return "Pages are required."
    if not isinstance(submission["pages"], int):
        return "Pages must be an integer."
    if submission["pages"] <= 0:
        return "Pages must be positive."
    if not submission.get("reviewer"):
        return "Reviewer is required."
    return None


def score_submission(submission: dict[str, object]) -> int:
    """Compute the quality score using named rules."""
    pages = int(submission["pages"])
    citations = int(submission.get("citations", 0))
    contains_code = bool(submission.get("contains_code"))

    score = LONG_REPORT_SCORE if pages > LONG_REPORT_PAGE_THRESHOLD else SHORT_REPORT_SCORE
    score += HIGH_CITATION_SCORE if citations > HIGH_CITATION_THRESHOLD else LOW_CITATION_SCORE
    score += CODE_INCLUDED_SCORE if contains_code else CODE_MISSING_SCORE
    return score


def calculate_fee(submission: dict[str, object]) -> int:
    """Calculate the review fee from submission settings."""
    pages = int(submission["pages"])
    is_rush = bool(submission.get("rush"))
    base_fee = RUSH_BASE_FEE if is_rush else STANDARD_BASE_FEE
    per_page_fee = RUSH_PER_PAGE_FEE if is_rush else STANDARD_PER_PAGE_FEE
    return base_fee + pages * per_page_fee


def format_result(submission: dict[str, object], score: int, fee: int) -> str:
    """Build the final user-facing result string."""
    status = "Approved" if score >= APPROVAL_SCORE_THRESHOLD else "Needs revision"
    return f"{status}: {submission['title']} for {submission['reviewer']} with fee {fee}"


def process_submission(submission: dict[str, object]) -> str:
    """Process a submission through small focused steps."""
    validation_error = validate_submission(submission)
    # Guard clauses return early so the happy path stays shallow and readable.
    if validation_error is not None:
        return validation_error

    score = score_submission(submission)
    fee = calculate_fee(submission)
    return format_result(submission, score, fee)


def main() -> None:
    """Run the cleaned example once."""
    submission = {
        "title": "Language Audit",
        "pages": 34,
        "reviewer": "Ari",
        "citations": 12,
        "contains_code": True,
        "rush": False,
    }
    print(process_submission(submission))


if __name__ == "__main__":
    main()
