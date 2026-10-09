"""Abre um editor de texto e salva um registro usando PyAutoGUI."""

import platform
import time

import pyautogui
import pyperclip


MENSAGEM = "Relatório de Execução Automática - RPA PyAutoGUI Ativo!"
NOME_ARQUIVO = "status_bot.txt"


def main() -> None:
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.5

    sistema = platform.system()
    if sistema == "Windows":
        aplicativo = "notepad"
        tecla_launcher = "win"
    elif sistema == "Linux":
        aplicativo = "gedit"
        tecla_launcher = "super_l"
    else:
        raise RuntimeError(f"Sistema operacional não suportado: {sistema}")

    pyautogui.press(tecla_launcher)
    pyautogui.write(aplicativo, interval=0.1)
    pyautogui.press("enter")
    time.sleep(2)

    pyperclip.copy(MENSAGEM)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("ctrl", "s")
    time.sleep(1)
    pyautogui.write(NOME_ARQUIVO, interval=0.1)
    pyautogui.press("enter")


if __name__ == "__main__":
    main()
