"""Run the ADK glossary agent and display its tool calls and results."""

import argparse
import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from .agent import root_agent


async def run_with_trace(question: str) -> None:
    app_name = root_agent.name
    user_id = "local-user"
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=app_name, user_id=user_id)
    runner = Runner(
        agent=root_agent,
        app_name=app_name,
        session_service=session_service,
    )

    message = types.Content(role="user", parts=[types.Part(text=question)])
    async for event in runner.run_async(
        user_id=user_id,
        session_id=session.id,
        new_message=message,
    ):
        for function_call in event.get_function_calls():
            print(f"[tool call]   {function_call.name}({function_call.args})")
        for function_response in event.get_function_responses():
            print(
                f"[tool return] {function_response.name} -> "
                f"{function_response.response}"
            )
        if event.is_final_response() and event.content and event.content.parts:
            text = "".join(part.text or "" for part in event.content.parts)
            if text:
                print(text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask the ADK agent and trace tool calls")
    parser.add_argument("question", help="Question to send to the agent")
    args = parser.parse_args()
    asyncio.run(run_with_trace(args.question))


if __name__ == "__main__":
    main()