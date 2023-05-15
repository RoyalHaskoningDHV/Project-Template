import shutil
from pathlib import Path


def remove_file_folder(filepath: Path) -> None:
    """Removes a file or folder

    Parameters
    ----------
    filepath : Pathlib Path
        The filepath that needs to be removed, either
        a file or folder (doesn't have to be empty)
    """
    if filepath.is_file():
        filepath.unlink()
    elif filepath.is_dir():
        shutil.rmtree(filepath)


if __name__ == "__main__":
    print(f"Created the project in: '{Path().resolve()}'")

    pkg_name = "{{cookiecutter.pkg_name}}"
    language = "{{cookiecutter.language}}".lower()

    if pkg_name == "not applicable" or language != "python":
        remove_file_folder(Path("{{cookiecutter.pkg_name}}"))
        remove_file_folder(Path("setup.py"))
        remove_file_folder(Path("pipelines") / "build-python-package.yaml")
    else:
        print(
            "Please follow the instructions in 'pipelines/build-python-package.yaml' "
            "to set up an automatic package build"
        )
        remove_file_folder(Path("src"))

    if language == "r":
        remove_file_folder(Path("setup.cfg"))
        remove_file_folder(Path("conftest.py"))
        remove_file_folder(Path("pipelines") / "lint-python.yaml")
        remove_file_folder(Path("pipelines") / "test-python.yaml")

    if language == "python":
        print(
            "Please create new 'Pipelines' in Azure Devops, and use the existing pipeline files "
            "found in the pipeline folder. A pipeline for each .yaml."
        )

    if "{{cookiecutter.documentation}}" != "y" or language == "r":
        if language == "r":
            print(
                "The RHDHV DDC cookiecutter part for automatic documentation in R is currently "
                "not supported."
            )
        print("Removing documentation files...")
        remove_file_folder(Path("docs") / "source")
        remove_file_folder(Path("docs") / "build")
    else:
        print(
            "For information on how to create documentation, please see the Digital wiki:"
        )
        print(
            "https://wikiddc.corporateroot.net/doku.php?id=python_styleguide#documentation"
        )
