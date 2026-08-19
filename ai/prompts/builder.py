from ai.models.file_content import FileContent


class PromptBuilder:
    def build_file_analysis_prompt(
        self,
        file: FileContent,
        task: str
    ) -> str:
        return f"""Задача:

{task}
        
Проанализируй следующий файл.

Файл: {file.path}
Расширение: {file.extension}

Содержимое:

{file.content}
"""
