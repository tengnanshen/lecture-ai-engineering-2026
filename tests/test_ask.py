from types import SimpleNamespace

from app import ask as ask_module


def test_ask_sends_message_and_reports_response_time(monkeypatch, capsys):
    calls = []
    response = SimpleNamespace(
        usage_metadata=SimpleNamespace(prompt_token_count=3, candidates_token_count=4),
        text="answer",
    )

    class FakeModels:
        def send_message(self, message):
            calls.append(message)
            return response

    timestamps = iter((1.0, 2.25))
    monkeypatch.setattr(ask_module, "perf_counter", lambda: next(timestamps))

    answer = ask_module.ask("question", FakeModels())

    assert answer == "answer"
    assert calls == ["question"]
    output = capsys.readouterr().out
    assert "[入力トークン] 3" in output
    assert "[出力トークン] 4" in output
    assert "[応答時間] 1.25 秒" in output


def test_create_chat_passes_temperature():
    calls = []

    class FakeModels:
        def create(self, **kwargs):
            calls.append(kwargs)

    class FakeClient:
        chats = FakeModels()

    ask_module.create_chat(FakeClient(), temperature=0.7)

    assert calls[0]["model"] == ask_module.MODEL
    assert calls[0]["config"].temperature == 0.7


def test_main_keeps_client_open_until_chat_ends(monkeypatch):
    sent = []

    class FakeChat:
        def send_message(self, question):
            assert client.is_open
            sent.append(question)
            return SimpleNamespace(usage_metadata=None, text="answer")

    class FakeChats:
        def create(self, **kwargs):
            del kwargs
            assert client.is_open
            return FakeChat()

    class FakeClient:
        def __init__(self):
            self.is_open = False
            self.chats = FakeChats()

        def __enter__(self):
            self.is_open = True
            return self

        def __exit__(self, *args):
            del args
            self.is_open = False

    client = FakeClient()

    def fake_client(**kwargs):
        del kwargs
        return client

    monkeypatch.setattr(ask_module.genai, "Client", fake_client)
    monkeypatch.setattr(ask_module, "get_api_key", lambda: "test-key")
    monkeypatch.setattr("sys.argv", ["app.ask", "first question"])

    def fake_input(prompt):
        del prompt
        return "STOPSTOP"

    monkeypatch.setattr("builtins.input", fake_input)
    timestamps = iter((1.0, 1.0))
    monkeypatch.setattr(ask_module, "perf_counter", lambda: next(timestamps))

    ask_module.main()

    assert sent == ["first question"]
    assert not client.is_open


def test_chat_with_user_keeps_taking_questions_until_stop(monkeypatch, capsys):
    questions = iter(["follow-up", "STOPSTOP"])
    sent = []
    input_prompts = []

    class FakeChat:
        def send_message(self, question):
            sent.append(question)
            return SimpleNamespace(usage_metadata=None, text=f"answer to {question}")

    def fake_input(prompt):
        input_prompts.append(prompt)
        return next(questions)

    monkeypatch.setattr("builtins.input", fake_input)
    timestamps = iter((1.0, 1.0, 2.0, 2.0))
    monkeypatch.setattr(ask_module, "perf_counter", lambda: next(timestamps))

    ask_module.chat_with_user("first question", FakeChat())

    assert sent == ["first question", "follow-up"]
    assert input_prompts == ["> ", "> "]
    output = capsys.readouterr().out
    assert output.count("続けて質問を入力するか、「STOPSTOP」と入力して終了してください。") == 2
    assert "対話を終了します。" in output
