import sys
from rich import print


languages_extensions = {
    "python": ".py",
    "c++": ".cpp",
    "cpp": ".cpp",
    "c": ".c",
    "java": ".java",
    "ruby": ".rb",
    "c#": ".cs",
    "cs": ".cs",
    "csharp": ".cs",
    "php": ".php",
    "rust": ".rs",
    "go": ".go",
    "golang": ".go",
    "lua": ".lua",
    "swift": ".swift",
    "kotlin": ".kt",
    "dart": ".dart",
    "gdscript": ".gd",
    "js": ".js",
    "javascript": ".js",
    "zig": ".zig",
    "julia": ".jl",
    "f#": ".fs",
    "fsharp": ".fs",
    "cython": "pyx"
}  # Notice: the languages names were lower() before this dictionary


def check_lang(language_name, language_file):
    """
    Checks if the file is .language_extension file and the name of Programmig language
    """

    try:
        file_and_extension = language_file.split(".")

        extension = languages_extensions[language_name]  # Language name's extension

        if not language_file.endswith(extension):  # Ex: name: Rust file: .lua
            print(
                f"""[red]File <[italic blue]{language_file}[/italic blue]> is not [italic blue]{language_name.title()}[/italic blue] file[/red]\n[green]Do you mean <[yellow]{language_file.replace(file_and_extension[1], languages_extensions[language_name].replace(".", ""))}[/yellow]>?[/green]""")
            return False

    except KeyError:
        print(
            f"[red]Language [italic blue]{language_name.title()}[/italic blue] is not allowed or not real language[/red]")
        return False

    return True
