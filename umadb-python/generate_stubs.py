"""
DON"T RUN THIS DIRECTLY: USE `make maturin-python-stubs` from the repo root.

Generate .pyi stubs for the umadb Python package, using py03-stub-gen crate.
Requires the extension to be already built and installed in the current venv.
"""
import os
from umadb._umadb import _generate_umadb_pyi_stubs  # type: ignore


STUB_PATH = "./umadb-python/python/umadb/_umadb.pyi"

os.environ["CARGO_MANIFEST_DIR"] = "./umadb-python"  # for the py03-stub-gen crate

def append_exception_stubs():
    """
    Appends stubs for the exception class. Don't know how else to do this.
    """
    exception_stubs = """
class IntegrityError(ValueError):
    \"\"\"Raised when the event store detects integrity violations.\"\"\"
    ...

class TransportError(RuntimeError):
    \"\"\"Raised when the client fails to communicate with the server.\"\"\"
    ...

class CorruptionError(RuntimeError):
    \"\"\"Raised when on-disk data corruption is detected.\"\"\"
    ...

class AuthenticationError(RuntimeError):
    \"\"\"Raised when on-disk data corruption is detected.\"\"\"
    ...
"""
    with open(STUB_PATH, "a", encoding="utf8") as f:
        f.write("\n")
        f.write(exception_stubs)

def fix_generated_stubs():
    """
    Fix the ReadResponse.__next__() method stub. Don't know how else to do this.
    """

    lines = []
    with open(STUB_PATH, "r", encoding="utf8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line == "    def __next__(self) -> typing.Optional[SequencedEvent]: ...\n":
            lines[i] = line.replace("typing.Optional[SequencedEvent]", "SequencedEvent")

    with open(STUB_PATH, "wt", encoding="utf8") as f:
        f.writelines(lines)

def main():
    _generate_umadb_pyi_stubs()
    append_exception_stubs()
    fix_generated_stubs()

if __name__ == "__main__":
    main()

