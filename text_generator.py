from transformers import pipeline, set_seed

# Load text generation pipeline with GPT-2
generator = pipeline("text-generation", model="gpt2")
set_seed(42)  # Optional: make results repeatable

# Ask the user for a topic or prompt
prompt = input("Enter a topic or sentence to generate text: ")

# Generate text
results = generator(prompt, max_length=100, num_return_sequences=1)

# Print the output
print("\nGenerated Text:\n")
print(results[0]['generated_text'])