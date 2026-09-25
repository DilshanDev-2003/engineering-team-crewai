📌 Project Notes & Troubleshooting Guide
🤖 CrewAI Setup & Configuration
1. Dynamic Task Variables & KeyError
⚠️ Issue: When using placeholder variables like {module_name} inside task definitions, CrewAI expects those variables to be explicitly passed inside the inputs={...} dictionary when calling crew.kickoff().

💡 Solution: For dynamic workflows, construct task descriptions dynamically using Python f-strings rather than relying on standard string placeholders in tasks.yaml:

Python
# ✅ Dynamic task creation in Python
test_task = Task(
    description=f"Write unit tests for module '{module.module_name}'",
    expected_output="Raw Python test code.",
    agent=team.test_engineer(),
    context=[code_task],
    output_file=f"output/test_{module.module_name}.py"
)
2. Local LLM Integration
🦙 Local models (like llama3.2:latest running via Ollama) can be configured directly as the LLM provider for CrewAI agents to run full execution pipelines without relying on external cloud APIs.

🖼️ Gradio UI Integration
1. gr.Blocks() Context Manager Requirement
⚠️ Issue: Calling event handlers like button.click(...) outside of an active gr.Blocks() block causes an AttributeError: Cannot call click outside of a gradio.Blocks context.

💡 Solution: Always wrap component definitions and event bindings within a with gr.Blocks() as app: context manager:

Python
with gr.Blocks() as app:
    user_id = gr.Textbox(label="User ID")
    execute_btn = gr.Button("Execute")
    result = gr.Textbox(label="Result")

    # ✅ Event binding inside the context
    execute_btn.click(
        fn=execute_action,
        inputs=[user_id],
        outputs=result
    )
2. Event Handler Data Flow
❌ Component properties like .value cannot be directly accessed or modified inside event callbacks.

✅ Pass UI component instances directly to the inputs and outputs arguments of the event handler. The callback function accepts the raw values as parameters and returns the new output values:

Python
# Callback receives values directly
def execute_action(uid):
    # Process logic...
    return f"Updated result for {uid}"