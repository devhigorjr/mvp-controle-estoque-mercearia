
from pathlib import Path
import subprocess
import sys


def test_main_sintaxe_valida():
    arquivo = Path("main.py")
    assert arquivo.exists(), "O arquivo main.py não foi encontrado"

    resultado = subprocess.run(
        [sys.executable, "-m", "py_compile", str(arquivo)],
        capture_output=True,
        text=True,
    )

    assert resultado.returncode == 0, resultado.stderr
