import os
import subprocess
import sys


def current_commit_message():
    if len(sys.argv) > 1:
        return sys.argv[1]
    if os.environ.get("COMMIT_MESSAGE"):
        return os.environ["COMMIT_MESSAGE"]
    try:
        return subprocess.check_output(["git", "log", "-1", "--pretty=%B"], text=True).strip()
    except Exception:
        return ""


def main():
    msg = current_commit_message()
    print("方格 form engine fixture")
    print(f"commit message: {msg}")

    if "FAIL_NONE_TYPE" in msg:
        print("AttributeError: 'NoneType' object")
        raise AttributeError("'NoneType' object")
    if "FAIL_FLAKY_RENDER" in msg:
        print("test_field_render")
        print("flaky: race condition in renderer init")
        raise RuntimeError("flaky: race condition in renderer init")
    if "FAIL_DOCKER_TIMEOUT" in msg:
        print("network timeout to docker.io")
        raise RuntimeError("network timeout to docker.io")

    print("test pass")


if __name__ == "__main__":
    main()
