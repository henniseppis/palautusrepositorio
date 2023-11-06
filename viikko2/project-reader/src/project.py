class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def list_items(self, y):
        return "".join([f"- {x} \n" for x in y])
            

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors:\n{self.list_items(self.authors)}"
            f"\nDependencies:\n{self.list_items(self.dependencies)}"
            f"\nDevelopment dependencies:\n{self.list_items(self.dev_dependencies)}"
        )
