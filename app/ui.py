# ui.py
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()

class GymUI:
    # Colors
    PRIMARY = "bold cyan"
    SECONDARY = "bold cyan"
    SUCCESS = "bold green"
    ERROR = "bold red"
    HIGHLIGHT = "bold yellow"
    BOLD_INPUT = "bold white"

    
    @staticmethod
    def clear_screen():
        """Clear the console"""
        console.clear()
    
    @staticmethod
    def show_menu(title, options, error_message=None):
        """Display a simple menu with optional error message"""
        GymUI.clear_screen()
        console.print(f"[{GymUI.PRIMARY}]{title}[/]\n")

    # Show error above the menu if provided
        if error_message:
            GymUI.show_message(error_message, "error")

        for key, option in options.items():
            console.print(f"[bold][{GymUI.SECONDARY}]{key}[/] {option}[/bold]")
    
        return Prompt.ask("\n[bold]Choose:[/] ")

    
    @staticmethod
    def show_message(message, message_type="info"):
        """Show styled messages"""
        styles = {
            "success": GymUI.SUCCESS,
            "error": GymUI.ERROR,
            "info": GymUI.SECONDARY
        }
        style = styles.get(message_type, GymUI.SECONDARY)
        console.print(f"[{style}]{message}[/]")
    
    @staticmethod
    def get_input(prompt):
        """Get user input with styling"""
        return console.input(f"[{GymUI.BOLD_INPUT}]{prompt}: [/]")
    
    @staticmethod
    def pause():
        """Wait for user to continue"""
        console.input("\n[bold]Press Enter to continue...[/]")

    @staticmethod
    def show_table(columns, data):
        """Display data in a simple table format"""
        table = Table(show_header=True, header_style="bold cyan")
        for col in columns:
            table.add_column(col)
        for row in data:
            table.add_row(*[f"[bold]{item}[/bold]" for item in row])
        console.print(table)
