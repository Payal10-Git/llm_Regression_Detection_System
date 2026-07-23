from src.prompt_manager.prompt_loader import PromptLoader


def main():
    prompt = PromptLoader.load("prompts/v1.yaml")

    print("=" * 50)
    print("Prompt Loaded Successfully")
    print("=" * 50)

    print(f"Version      : {prompt.version}")
    print(f"Author       : {prompt.author}")
    print(f"Provider     : {prompt.provider}")
    print(f"Model        : {prompt.model}")
    print(f"Temperature  : {prompt.temperature}")
    print(f"Max Tokens   : {prompt.max_tokens}")

    print("\nSystem Prompt:")
    print("-" * 40)
    print(prompt.system_prompt)


if __name__ == "__main__":
    main()