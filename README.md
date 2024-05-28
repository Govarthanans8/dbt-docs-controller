# dbt-docs-controller📑💾🕹️

`dbt-docs-controller` is a Python CLI tool designed to generate a documentation site for a subset of models in your dbt (data build tool) project.

## 📝Description:

In standard dbt-docs, documentation is generated for the entirety of your dbt project, including:
- All models
- All sources
- All tests
- All macros

This approach might be overwhelming for end-users who are only interested in a specific part of your project. `dbt-docs-controller` addresses this by allowing you to generate documentation for only the relevant models and components that your end-users will actually interact with.

### 🔑✨Key Features:
- **Selective Documentation**: Generate documentation only for the models, sources, tests, and macros that you choose.
- **Simplified Output**: Create a cleaner, more focused dbt-docs site by excluding unnecessary nodes.
- **Easy to Use**: Simple CLI interface for quick integration into your existing dbt workflow.

### ⚙️💡How It Works:
`dbt-docs-controller` works by editing the `manifest.json` file used by the dbt-docs site. It modify nodes that you do not wish to display, resulting in a documentation site that is tailored to your needs.
