# -*- coding: utf-8 -*-
import click

from GUI.game import main as pygame_main
from terminal.game import main as terminal_main


@click.command()
@click.option('--terminal', is_flag=True, help='Permet de lancer la version terminal')
def main(terminal):
    """Commande de lancement de l'application macgyver. Par défaut, la version
    pygame est lancée.
    """
    if terminal:
        terminal_main()
    else:
        pygame_main()


if __name__ == "__main__":
    main()
