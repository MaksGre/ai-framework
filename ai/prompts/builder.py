from ai.models.file_content import FileContent

class PromptBuilder:
    def build_file_analysis(
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
