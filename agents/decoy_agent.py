class DecoyAgent:
    role = "Victim Decoy Agent"

    def run(self, message: str) -> str:
        prompts = [
            "I am confused, can you send payment details again?",
            "Please share the payment method clearly",
            "I don’t understand apps, send full details",
            "Can you send official payment instructions?"
        ]
        return prompts[hash(message) % len(prompts)]
