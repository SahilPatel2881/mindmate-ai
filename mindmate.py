import random
import datetime

class MindMateAI:
    def __init__(self):
        self.user_name = ""
        self.mood_history = []
        
    def greet_user(self):
        print("🧠 Welcome to MindMate AI - Your Mental Wellness Companion!")
        print("=" * 55)
        self.user_name = input("What's your name? ")
        print(f"\nHello {self.user_name}! I'm here to listen and support you.")
        print("You can type: 'quit' to exit, 'technique' for CBT exercise, or 'mood' for progress\n")
    
    def get_response(self, user_input):
        user_input_lower = user_input.lower()
        
        # Response logic
        if any(word in user_input_lower for word in ['hello', 'hi', 'hey']):
            return f"Hello {self.user_name}! How are you feeling today?"
        elif any(word in user_input_lower for word in ['sad', 'depressed', 'unhappy', 'down']):
            return "I'm sorry you're feeling this way. Remember that feelings are temporary. 💙"
        elif any(word in user_input_lower for word in ['anxious', 'worried', 'nervous', 'stress']):
            return "Let's try breathing: Inhale for 4 seconds, hold for 4, exhale for 6. Repeat. 🌬️"
        elif any(word in user_input_lower for word in ['happy', 'good', 'great', 'awesome']):
            return "That's wonderful! Celebrating good moments is important. 😊"
        elif 'thank' in user_input_lower:
            return "You're welcome! I'm glad I could help."
        elif any(word in user_input_lower for word in ['tired', 'exhausted', 'sleep']):
            return "Rest is important for mental health. Remember to hydrate and take breaks. 💤"
        else:
            responses = [
                "Thank you for sharing. How does that make you feel?",
                "I'm listening. Tell me more about that.",
                "That sounds important. How can I support you with this?",
                "I appreciate you opening up. What's been on your mind lately?"
            ]
            return random.choice(responses)
    
    def provide_technique(self):
        techniques = [
            "🌬️ Deep Breathing: Inhale for 4 counts, hold for 4, exhale for 6. Repeat 5 times.",
            "📝 Thought Journaling: Write down your thoughts without judgment for 5 minutes.",
            "🚶 Mindful Walk: Take a 10-minute walk while noticing your surroundings.",
            "🎯 Progressive Relaxation: Tense and relax each muscle group from toes to head."
        ]
        return random.choice(techniques)
    
    def show_mood_summary(self):
        if len(self.mood_history) > 0:
            return f"We've had {len(self.mood_history)} conversations. Keep sharing to see patterns!"
        else:
            return "Share how you're feeling to build your mood history!"
    
    def run(self):
        self.greet_user()
        
        while True:
            user_input = input(f"{self.user_name}: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print(f"\nTake care {self.user_name}! Remember: Progress over perfection. 🌈")
                break
            elif user_input.lower() in ['technique', 'exercise', 'help', 'tool']:
                print(f"MindMate AI: {self.provide_technique()}")
            elif user_input.lower() in ['mood', 'progress', 'summary', 'stats']:
                print(f"MindMate AI: {self.show_mood_summary()}")
            elif user_input == "":
                print("MindMate AI: I'm here when you're ready to talk.")
            else:
                response = self.get_response(user_input)
                print(f"MindMate AI: {response}")
                # Track conversation
                self.mood_history.append({
                    'timestamp': datetime.datetime.now(),
                    'input': user_input
                })

# Start the AI
if __name__ == "__main__":
    bot = MindMateAI()
    bot.run()