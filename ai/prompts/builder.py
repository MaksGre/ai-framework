from ai.models.file_content import FileContent

class PromptBuilder:
    def build_file_analysis_prompt(
        self,
        file: FileContent
    ) -> str:
        return f"""
Проанализируй следующий файл.

Файл: {file.path}
Расширение: {file.extension}

Содержимое:

{file.content}
""".strip()

    def build_files_analysis_prompt(
        self,
        files: list[FileContent],
     ) -> str:
        prompt = "Проанализируй следующие файлы. \n\n"
        
        for file in files:
            prompt += f"""
Файл: {file.path}
Расширение: {file.extension}

Содержимое:

{file.content}

{'=' * 80}

"""

        return prompt.strip()
