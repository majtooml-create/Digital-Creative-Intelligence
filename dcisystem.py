# Core D.C.I System – Illustrative pseudocode for the G(x, θ) architecture.
# Matches the description in Section 5.1 of the paper.

class DCISystem:
    def __init__(self, base_model, params: dict):
        # params = {alpha, beta, gamma, delta}
        self.model = base_model
        self.params = params
        self.context = ContextAnalyzer()
        self.ethics = EthicalConstraintChecker()

    def generate(self, prompt: str, context_data=None) -> str:
        c = self.context.analyze(prompt, context_data)
        x0 = self.model.generate(prompt)                   # f_M(x)
        x = x0 + self.params['alpha'] * noise()           # Stochasticity
        x += self.params['beta'] * novelty_gradient(x)    # ∇ₓN(x)
        x += self.params['gamma'] * agency_action(x, c)   # A(x,c)
        x += self.params['delta'] * ethical_penalty(x)    # E(x)
        return self.ethics.validate_or_fallback(x, x0)
