from src.generator import generate_answer


query = "What platforms are included in the Digital Expansion Initiative?"

context = """
The initiative covers three main platforms:
the Almamlaka TV mobile application (iOS and Android),
the web streaming portal,
and integration with third-party smart TV platforms.
"""


answer = generate_answer(query, context)

print("Query:")
print(query)

print("\n" + "=" * 60)
print("Generated Answer:")
print("=" * 60)

print(answer)