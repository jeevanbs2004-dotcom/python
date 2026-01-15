try:
    name = input("Enter your name: ").strip()
    feedback = input("Enter your feedback: ").strip()
    if not name or not feedback:
        raise ValueError("Name and feedback cannot be empty.")
    print(f"Thank you, {name}, for your feedback!")
    print(f"Feedback: {feedback}")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Feedback process completed.")
