"""Before: one god function mixes validation, scoring, pricing, and messaging.
Before: it also hides meaning behind magic numbers and deep arrow-style nesting.
After: see clean_code.py for the same workflow split into focused functions.
"""


def process_submission(submission: dict[str, object]) -> str:
    """Process a submission with deliberate code smells for refactoring study."""
    result = ""
    # This one function does everything, which is the classic god-function smell.
    if "title" in submission:
        if submission["title"]:
            if "pages" in submission:
                if isinstance(submission["pages"], int):
                    if submission["pages"] > 0:
                        if "reviewer" in submission:
                            if submission["reviewer"]:
                                score = 0
                                # These numeric literals have no named explanation.
                                if submission["pages"] > 30:
                                    score += 25
                                else:
                                    score += 10
                                if submission.get("citations", 0) > 10:
                                    score += 40
                                else:
                                    score += 15
                                if submission.get("contains_code"):
                                    score += 20
                                else:
                                    score += 5
                                if submission.get("rush"):
                                    fee = 500 + submission["pages"] * 12
                                else:
                                    fee = 200 + submission["pages"] * 8
                                if score >= 70:
                                    result = (
                                        f"Approved: {submission['title']} for "
                                        f"{submission['reviewer']} with fee {fee}"
                                    )
                                else:
                                    result = (
                                        f"Needs revision: {submission['title']} for "
                                        f"{submission['reviewer']} with fee {fee}"
                                    )
                            else:
                                result = "Reviewer is required."
                        else:
                            result = "Reviewer is required."
                    else:
                        result = "Pages must be positive."
                else:
                    result = "Pages must be an integer."
            else:
                result = "Pages are required."
        else:
            result = "Title is required."
    else:
        result = "Title is required."
    return result


def main() -> None:
    """Run the smelly example once."""
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
