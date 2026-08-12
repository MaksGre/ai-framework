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

    def build_files_analysis_prompt(
        self,
        files: list[FileContent],
        task: str
     ) -> str:
        prompt = f"""Задача:

{task}

Проанализируй следующие файлы.

"""
        for file in files:
            prompt += f"""Файл {file.path}
Расширение: {file.extension}

Содержимое:

{file.content}

{'=' * 80}

"""

        return prompt.strip()
