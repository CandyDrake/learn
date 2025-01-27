import time

import pytest

ARTIFACTS = "artifact.txt"
LOGS = "logs.txt"


@pytest.fixture(scope="session", autouse=True)
def clear_artifacts():
    with open(ARTIFACTS, "w"):
        pass


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.when == "call":
        status = "PASSED" if report.outcome == "passed" else "FAILED"
        with open(ARTIFACTS, "a") as f:
            f.write(f'{report.nodeid}: {status}\n')


@pytest.fixture(scope="session")
def clear_logs():
    with open(LOGS, "w"):
        pass


@pytest.fixture(scope="function")
def time_log(clear_logs, request):
    if "time_calc" in request.node.keywords:
        start = time.time()
        yield
        end = time.time()
        duration = end - start
        result = f"тест: {request.node.name}, длительность: {duration:.4f} сек.\n"
        with open(LOGS, "a", encoding="utf-8") as logs:
            logs.write(result)
    else:
        yield

