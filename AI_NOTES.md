## 1. Which parts of the code were AI-generated vs. written by you

*AI (ChatGPT and Claude) was used as a development assistant throughout the project to improve productivity and accelerate development, similar to how many professional software engineers use AI-assisted tools in their daily workflow.
*Some repetitive and boilerplate code—such as parts of the Django ModelForm implementation, view function scaffolding, template structure, and project configuration suggestions—was initially generated with AI assistance. 
*AI was also used to explain Django concepts, suggest implementation approaches, and help troubleshoot development issues.
*The overall application design, project structure, database model, business logic, URL routing, template integration, CRUD workflow, project configuration, debugging, testing, and final integration were implemented and completed by me. 
*Every AI-generated snippet was reviewed, modified where necessary, and integrated manually to ensure it followed Django best practices, matched the project's architecture, and met the assignment requirements.

I treated AI as a productivity tool rather than a replacement for development, taking full responsibility for understanding, validating, and maintaining all code included in the final submission.

## 2. What you validated, tested, or changed in the AI's output, and why

AI-generated code was not used directly. I reviewed, modified, and tested every suggestion before integrating it into the project.

The main validations and changes included:

*Verified that the generated code followed Django best practices and fit my project's architecture.
*Refactored AI-generated code to improve readability, maintainability, and consistency with the rest of the codebase.
*Removed unnecessary code, duplicate logic, and unused imports suggested by AI.
Updated forms, views, and templates to match the application's functional requirements and user flow.
*Verified form validations, database updates, URL routing, and template rendering through manual testing.
*Fixed issues identified during testing, including validation errors, edge cases, and UI inconsistencies.

These steps ensured that every AI-assisted contribution met the project's requirements, maintained code quality, and reflected my understanding of the final implementation.


## 3. Any AI suggestion you decided not to use, and why

Yes. I evaluated every AI suggestion before deciding whether to use it.

During development, AI occasionally suggested additional abstractions, helper functions, and extra features that were not necessary for a project of this size. I chose not to include those suggestions because they increased complexity without improving the core functionality.

I also avoided implementations that duplicated functionality already provided by Django's built-in features. Whenever a simpler or more idiomatic Django solution was available, I preferred that approach.

My decision was based on three principles:
- Keep the code simple and easy to understand.
- Use Django's built-in capabilities whenever possible.
- Stay focused on the assignment requirements instead of adding unnecessary complexity.

Rather than accepting every AI suggestion, I evaluated each one based on readability, maintainability, and its value to the project before deciding whether to include it.