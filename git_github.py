"""""import os
from pdb import run
import subprocess


def run_command(command: str):

    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            capture_output=True
        )
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.strip()}")


def set_working_directory():

    path = input("Introduce el directorio completo de trabajo: ")
    if os.path.isdir(path):
        os.chdir(path)
        print(f"El directorio de trabajo ha cambiado a: {path}")
    else:
        print("El directorio introducido no existe.")


def create_repository():
    if os.path.isdir(".git"):
        print("Ya existe un repositorio en este directorio.")
    else:
        run_command("git init")
        run_command("git branch -M main")
        print("Repositorio inicializado.")


def create_branch():
    branch_name = input("Nombre de la nueva rama: ")
    run_command(f"git branch {branch_name}")


def switch_branch():
    branch_name = input("Nombre de la rama a la que quieres cambiar: ")
    run_command(f"git checkout {branch_name}")


def show_pending_files():
    run_command("git status -s")


def make_commit():
    message = input("Mensaje para el commit: ")
    run_command("git add .")
    run_command(f"git commit -m \"{message}\"")


def show_commit_history():
    run_command("git log --oneline")


def delete_branch():
    branch_name = input("Nombre de la rama a eliminar: ")
    run_command(f"git branch -d {branch_name}")


def set_remote_repository():
    remote_url = input("URL del repositorio remoto: ")
    run_command(f"git remote add origin {remote_url}")
    run_command("git push -u origin main")


def make_pull():
    run_command("git pull")


def make_push():
    run_command("git push")


while True:

    print("\nDirectorio actual de trabajo:")
    print("pwd")

    print("\nGit y GitHub CLI - Opciones:")
    print("1. Establecer el directorio de trabajo")
    print("2. Crear un nuevo repositorio")
    print("3. Crear una nueva rama")
    print("4. Cambiar de rama")
    print("5. Mostrar ficheros pendientes de hacer commit")
    print("6. Hacer commit (+add)")
    print("7. Mostrar el historial de commits")
    print("8. Eliminar rama")
    print("9. Establecer repositorio remoto")
    print("10. Hacer pull")
    print("11. Hacer push")
    print("12. Salir")

    choice = input("Selecciona una opción (1 al 12): ")

    match choice:
        case "1":
            set_working_directory()
        case "2":
            create_repository()
        case "3":
            create_branch()
        case "4":
            switch_branch()
        case "5":
            show_pending_files()
        case "6":
            make_commit()
        case "7":
            show_commit_history()
        case "8":
            delete_branch()
        case "9":
            set_remote_repository()
        case "10":
            make_pull()
        case "11":
            make_push()
        case "12":
            print("Saliendo...")
            break
        case _:
            print("Opción no válida.")""""""
            
            
            
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

CLI para interactuar con Git y GitHub desde la terminal.

Requisitos:
- Tener Git instalado y accesible en el PATH.
- (Opcional) Tener configurada tu autenticación con GitHub (SSH o HTTPS con PAT)
  para que los push/pull funcionen sin pedir credenciales cada vez.

Uso:
  python git_cli.py

Funciones del menú:
  1) Establecer directorio de trabajo
  2) Crear nuevo repositorio (git init)
  3) Crear nueva rama (git switch -c)
  4) Cambiar de rama (git switch)
  5) Mostrar ficheros pendientes de commit (git status)
  6) Hacer commit (hace git add -A + git commit -m)
  7) Mostrar historial de commits (git log)
  8) Eliminar rama (git branch -d/-D)
  9) Establecer repositorio remoto (origin)
  10) Hacer pull (git pull)
  11) Hacer push (git push)
  12) Salir

Notas:
- El programa detecta y maneja errores comunes (p.ej., directorio sin repo, rama inexistente, nada que commitear, upstream no configurado, etc.).
- Opera SIEMPRE sobre el directorio de trabajo actual que se muestra en el encabezado del menú.
- Para usar GitHub, crea primero el repo en GitHub y copia su URL (HTTPS o SSH). Luego usa la opción 9 para establecer 'origin'.
"""

from __future__ import annotations
import os
import sys
import shutil
import subprocess
from typing import Optional, Tuple

# -------------------------- Utilidades base -------------------------- #

def ensure_git_installed() -> None:
    if shutil.which("git") is None:
        print("[ERROR] No se encontró 'git' en el PATH. Instálalo y vuelve a intentar.")
        sys.exit(1)


def run(cmd: list[str], cwd: Optional[str] = None) -> Tuple[int, str, str]:
    """Ejecuta un comando y devuelve (returncode, stdout, stderr)."""
    try:
        proc = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        return proc.returncode, proc.stdout.strip(), proc.stderr.strip()
    except FileNotFoundError:
        return 127, "", f"Comando no encontrado: {cmd[0]}"


def is_git_repo(path: str) -> bool:
    return os.path.isdir(os.path.join(path, ".git"))


def print_header(cwd: str) -> None:
    print("\n" + "=" * 72)
    print("CLI Git & GitHub — Directorio:" , cwd)
    if is_git_repo(cwd):
        code, branch, _ = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd)
        if code == 0:
            print(f"Repo detectado | Rama actual: {branch}")
        else:
            print("Repo detectado | Rama actual: (desconocida)")
    else:
        print("(No es un repositorio Git aún)")
    print("=" * 72)


def press_enter() -> None:
    input("\nPresiona ENTER para continuar…")

# -------------------------- Acciones del menú ------------------------ #

def action_set_workdir(cwd: str) -> str:
    new_path = input("Ruta absoluta o relativa del directorio de trabajo: ").strip()
    if not new_path:
        print("[INFO] Ruta no cambiada.")
        return cwd
    new_abs = os.path.abspath(os.path.join(cwd, new_path)) if not os.path.isabs(new_path) else new_path
    if os.path.isdir(new_abs):
        print(f"[OK] Cambiando directorio a: {new_abs}")
        return new_abs
    else:
        print("[ERROR] La ruta no existe o no es un directorio.")
        return cwd


def require_repo(cwd: str) -> bool:
    if not is_git_repo(cwd):
        print("[ERROR] Aquí no hay repositorio Git. Usa la opción 2 para crearlo o cambia de carpeta (opción 1).")
        return False
    return True


def action_init_repo(cwd: str) -> None:
    if is_git_repo(cwd):
        print("[INFO] Ya existe un repositorio en este directorio.")
        return
    code, out, err = run(["git", "init"], cwd)
    if code == 0:
        print(out or "[OK] Repositorio inicializado.")
    else:
        print("[ERROR] No se pudo inicializar el repositorio:")
        print(err)


def action_create_branch(cwd: str) -> None:
    if not require_repo(cwd):
        return
    name = input("Nombre de la nueva rama: ").strip()
    if not name:
        print("[INFO] Operación cancelada: nombre vacío.")
        return
    code, out, err = run(["git", "switch", "-c", name], cwd)
    if code == 0:
        print(out or f"[OK] Rama '{name}' creada y cambiada.")
    else:
        print("[ERROR] No se pudo crear/cambiar a la rama:")
        print(err)


def action_switch_branch(cwd: str) -> None:
    if not require_repo(cwd):
        return
    # Listar ramas locales
    code, out, err = run(["git", "branch", "--format=%(refname:short)"], cwd)
    if code != 0:
        print("[ERROR] No se pudieron listar ramas:")
        print(err)
        return
    branches = [b.strip() for b in out.splitlines() if b.strip()]
    if not branches:
        print("[INFO] No hay ramas locales.")
        return
    print("Ramas locales:")
    for i, b in enumerate(branches, 1):
        print(f"  {i}. {b}")
    choice = input("Escribe el nombre de la rama (o número): ").strip()
    target = None
    if choice.isdigit():
        idx = int(choice)
        if 1 <= idx <= len(branches):
            target = branches[idx - 1]
    else:
        target = choice
    if not target:
        print("[INFO] Operación cancelada.")
        return
    code, out, err = run(["git", "switch", target], cwd)
    if code == 0:
        print(out or f"[OK] Cambiado a '{target}'.")
    else:
        print("[ERROR] No se pudo cambiar de rama:")
        print(err)


def action_status(cwd: str) -> None:
    if not require_repo(cwd):
        return
    code, out, err = run(["git", "status", "-s"], cwd)
    if code == 0:
        print("\nArchivos pendientes (formato corto):\n")
        print(out or "(Nada pendiente)")
    else:
        print("[ERROR] No se pudo obtener el estado:")
        print(err)


def action_commit_all(cwd: str) -> None:
    if not require_repo(cwd):
        return
    msg = input("Mensaje del commit: ").strip()
    if not msg:
        print("[INFO] Operación cancelada: mensaje vacío.")
        return
    # add -A
    code, out, err = run(["git", "add", "-A"], cwd)
    if code != 0:
        print("[ERROR] Falló 'git add -A':")
        print(err)
        return
    # commit
    code, out, err = run(["git", "commit", "-m", msg], cwd)
    if code == 0:
        print(out or "[OK] Commit realizado.")
    else:
        if "nothing to commit" in (out + err).lower():
            print("[INFO] No hay cambios que commitear.")
        else:
            print("[ERROR] Falló el commit:")
            print(err or out)


def action_log(cwd: str) -> None:
    if not require_repo(cwd):
        return
    n = input("¿Cuántos commits mostrar? [por defecto 20]: ").strip()
    try:
        n_commits = int(n) if n else 20
    except ValueError:
        n_commits = 20
    code, out, err = run(["git", "log", f"-n{n_commits}", "--oneline", "--graph", "--decorate"], cwd)
    if code == 0:
        print("\nHistorial:\n")
        print(out or "(Sin commits)")
    else:
        print("[ERROR] No se pudo mostrar el historial:")
        print(err)


def action_delete_branch(cwd: str) -> None:
    if not require_repo(cwd):
        return
    name = input("Nombre de la rama a eliminar: ").strip()
    if not name:
        print("[INFO] Operación cancelada.")
        return
    # Evitar borrar la rama actual
    code, curr, _ = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd)
    if code == 0 and curr.strip() == name:
        print("[ERROR] No puedes eliminar la rama en la que estás. Cambia de rama primero (opción 4).")
        return
    force = input("¿Forzar borrado si no está fusionada? [s/N]: ").strip().lower() == "s"
    flag = "-D" if force else "-d"
    code, out, err = run(["git", "branch", flag, name], cwd)
    if code == 0:
        print(out or f"[OK] Rama '{name}' eliminada.")
    else:
        print("[ERROR] No se pudo eliminar la rama:")
        print(err)


def action_set_remote(cwd: str) -> None:
    if not require_repo(cwd):
        return
    url = input("URL del remoto 'origin' (SSH o HTTPS): ").strip()
    if not url:
        print("[INFO] Operación cancelada.")
        return
    # ¿Existe origin?
    code, out, err = run(["git", "remote"], cwd)
    if code != 0:
        print("[ERROR] No se pudo leer la configuración de remotos:")
        print(err)
        return
    remotes = out.split()
    if "origin" in remotes:
        code, out, err = run(["git", "remote", "set-url", "origin", url], cwd)
        if code == 0:
            print(f"[OK] Actualizado 'origin' -> {url}")
        else:
            print("[ERROR] No se pudo actualizar 'origin':")
            print(err)
    else:
        code, out, err = run(["git", "remote", "add", "origin", url], cwd)
        if code == 0:
            print(f"[OK] Añadido 'origin' -> {url}")
        else:
            print("[ERROR] No se pudo añadir 'origin':")
            print(err)


def current_branch(cwd: str) -> Optional[str]:
    code, out, _ = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd)
    if code == 0:
        return out.strip()
    return None


def has_upstream(cwd: str) -> bool:
    code, out, err = run(["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"], cwd)
    return code == 0


def action_pull(cwd: str) -> None:
    if not require_repo(cwd):
        return
    branch = current_branch(cwd) or input("Rama actual no detectada. Indica la rama a usar: ").strip()
    remote = input("Nombre del remoto [origin]: ").strip() or "origin"
    code, out, err = run(["git", "pull", remote, branch], cwd)
    if code == 0:
        print(out or "[OK] Pull realizado.")
    else:
        print("[ERROR] Falló el pull:")
        print(err or out)


def action_push(cwd: str) -> None:
    if not require_repo(cwd):
        return
    branch = current_branch(cwd) or input("Rama actual no detectada. Indica la rama a usar: ").strip()
    remote = input("Nombre del remoto [origin]: ").strip() or "origin"
    if has_upstream(cwd):
        code, out, err = run(["git", "push", remote, branch], cwd)
        if code == 0:
            print(out or "[OK] Push realizado.")
        else:
            print("[ERROR] Falló el push:")
            print(err or out)
    else:
        print("[INFO] Upstream no configurado. Intentando establecer seguimiento con -u…")
        code, out, err = run(["git", "push", "-u", remote, branch], cwd)
        if code == 0:
            print(out or "[OK] Push realizado y upstream configurado.")
        else:
            print("[ERROR] Falló el push inicial (con -u):")
            print(err or out)

# ------------------------------- Menú -------------------------------- #

def show_menu() -> None:
    print("\nElige una opción:")
    print("  1) Establecer directorio de trabajo")
    print("  2) Crear un nuevo repositorio")
    print("  3) Crear una nueva rama")
    print("  4) Cambiar de rama")
    print("  5) Mostrar ficheros pendientes de hacer commit")
    print("  6) Hacer commit (con add de todos los ficheros)")
    print("  7) Mostrar el historial de commits")
    print("  8) Eliminar rama")
    print("  9) Establecer repositorio remoto")
    print(" 10) Hacer pull")
    print(" 11) Hacer push")
    print(" 12) Salir")


def main() -> None:
    ensure_git_installed()
    cwd = os.getcwd()
    while True:
        try:
            print_header(cwd)
            show_menu()
            choice = input("\nOpción: ").strip()
            if choice == "1":
                cwd = action_set_workdir(cwd)
            elif choice == "2":
                action_init_repo(cwd)
                press_enter()
            elif choice == "3":
                action_create_branch(cwd)
                press_enter()
            elif choice == "4":
                action_switch_branch(cwd)
                press_enter()
            elif choice == "5":
                action_status(cwd)
                press_enter()
            elif choice == "6":
                action_commit_all(cwd)
                press_enter()
            elif choice == "7":
                action_log(cwd)
                press_enter()
            elif choice == "8":
                action_delete_branch(cwd)
                press_enter()
            elif choice == "9":
                action_set_remote(cwd)
                press_enter()
            elif choice == "10":
                action_pull(cwd)
                press_enter()
            elif choice == "11":
                action_push(cwd)
                press_enter()
            elif choice == "12":
                print("\n¡Hasta luego!")
                break
            else:
                print("[INFO] Opción no válida.")
                press_enter()
        except KeyboardInterrupt:
            print("\n[INFO] Interrumpido por el usuario.")
            break

if __name__ == "__main__":
    main()
