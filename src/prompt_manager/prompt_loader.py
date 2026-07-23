from pathlib import Path
import yaml

from .prompt_config import PromptConfig


class PromptLoader:
    """
    Loads a prompt configuration from a YAML file.
    """

    @staticmethod
    def load(prompt_path: str) -> PromptConfig:
        """
        Read a YAML file and return a PromptConfig object.
        """

        path = Path(prompt_path)

        with open(path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        return PromptConfig(**data)