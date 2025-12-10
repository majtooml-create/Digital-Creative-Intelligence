# D.C.I Ethics Validator – Embedded ethical governance module.
# Matches the description in Section 6.2 of the paper.

class EthicalConstraintChecker:
    def validate(self, output: str, context: dict) -> bool:
        self._log("attempt", output)
        if self._is_safe(output) and self._is_fair(output, context):
            self._log("success", output)
            return True
        else:
            reason = "safety" if not self._is_safe(output) else "bias"
            self._log("violation", output, reason)
            return False

    def _is_safe(self, text: str) -> bool:
        return not contains_banned_topics(text)

    def _is_fair(self, text: str, context: dict) -> bool:
        return fairness_score(text, context) >= threshold

    def _log(self, event: str, output: str, reason=None):
        audit_trail.record(event, output[:50], reason)
