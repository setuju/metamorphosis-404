"""
╔═══════════════════════════════════════════╗
║  metamorphosis_404.py                    ║
║  Executable Poetry v2.1                  ║
║  "Maybe I Should Just Be a 404 Page"     ║
╚═══════════════════════════════════════════╝

Run this. Watch yourself become the error code
that finally found peace.
"""

import time
import sys
import random
import shutil
import os

# ─── Clear Screen ─────────────────────────────────
def clear_screen():
    """Clear the terminal screen."""
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# ─── Terminal Aesthetics ──────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

# ─── Centering Helper ────────────────────────────
def get_term_width():
    """Get terminal width, default 80."""
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return 80

def center_print(text, width=None, end="\n"):
    """Print text centered in the terminal."""
    if width is None:
        width = get_term_width()
    # Strip ANSI codes for length calculation
    plain = text
    # Simple removal of ANSI codes for length
    import re
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    plain_text = ansi_escape.sub('', text)
    visible_len = len(plain_text)
    if visible_len >= width:
        # If too long, just print as is
        print(text, end=end)
    else:
        spaces = (width - visible_len) // 2
        print(" " * spaces + text, end=end)

# ─── Typewriter Effect ────────────────────────────
def typewrite(text, delay=0.03, end="\n", center=False):
    """Print text letter by letter, maybe centered."""
    if center:
        # For centering, we need to know the final visible length.
        # Calculate plain text length, determine padding, print then type.
        import re
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        plain_text = ansi_escape.sub('', text)
        visible_len = len(plain_text)
        width = get_term_width()
        if visible_len < width:
            pad = (width - visible_len) // 2
            sys.stdout.write(" " * pad)
            sys.stdout.flush()
        # Now type the text
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        if end:
            sys.stdout.write(end)
            sys.stdout.flush()
    else:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        if end:
            sys.stdout.write(end)
            sys.stdout.flush()

def loading_dots(seconds=1.5, message=""):
    """Animated ellipsis for suspense. Clears itself properly."""
    # Print message and animate dots, then clear whole line.
    sys.stdout.write(message)
    sys.stdout.flush()
    total_dots = int(seconds / 0.3)
    for i in range(total_dots):
        for dot in [".", "..", "..."]:
            # Overwrite previous dots
            sys.stdout.write(f"\r{message}{dot}   ")
            sys.stdout.flush()
            time.sleep(0.1)
    # Clear line
    clear_length = len(message) + 5
    sys.stdout.write("\r" + " " * clear_length + "\r")
    sys.stdout.flush()

# ─── Characters ───────────────────────────────────
class OverworkedDeveloper:
    """A human consumed by HTTP requests."""
    def __init__(self):
        self.name = "localhost:human"
        self.status_code = 200
        self.memory = ["ambition", "rent", "npm audit fix", "you-should-be-further"]
        self.uptime = "∞ (but feels like 0)"

    def handle_request(self, path):
        """Every GET chips away at the soul."""
        # Build prompt
        timestamp = f"{RED}[{time.strftime('%H:%M:%S')}]{RESET}"
        prompt_str = f"{timestamp} {BOLD}GET{RESET} /{path} "
        # Print prompt without newline
        sys.stdout.write(prompt_str)
        sys.stdout.flush()
        # Animate dots
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.2)
        # Carriage return and overwrite with full line
        sys.stdout.write("\r")
        status = f"{RED}200 OK{RESET}  {DIM}(trembling){RESET}"
        # Print prompt + status, then clear any leftover characters
        sys.stdout.write(prompt_str + status + " " * 5)
        sys.stdout.flush()
        print()  # newline

    def crisis(self):
        """The inevitable segmentation fault of the spirit."""
        print()  # newline
        center_print(f"{YELLOW}{BOLD}[ Kernel Panic ]{RESET}")
        typewrite("   Too many file descriptors. Too many open mouths.\n", 0.02)
        typewrite("   Payload exceeds maximum capacity.\n", 0.02)
        typewrite("   ", 0.01, end="")
        loading_dots(1.2, message="   Initiating self-reflection")
        center_print(f"{DIM}   ...maybe I should just be a 404 page...{RESET}")
        time.sleep(0.8)

    def metamorphose(self):
        """Trigger transformation from 200 to 404."""
        print()  # spacing
        center_print(f"{CYAN}{BOLD}[ Metamorphosis in Progress ]{RESET}")
        print()
        stages = [
            ("git rm --cached identity", "Unstaging who I was told to be"),
            ("sudo apt remove expectations", "Uninstalling burden packages"),
            ("docker stop ambition_container", "Stopping the never-satisfied daemon"),
            ("rm -rf /var/log/anxiety", "Deleting all panic logs"),
            ("sed -i 's/200/404/g' self.conf", "Rewriting my status code"),
            ("systemctl disable people-pleaser.service", "Turning off external validation"),
            ("touch /dev/null", "Becoming empty. Becoming honest."),
        ]
        for cmd, meaning in stages:
            typewrite(f"  {DIM}$ {cmd}{RESET}", 0.01)
            loading_dots(0.7, message="")
            typewrite(f"  {ITALIC}{DIM}# {meaning}{RESET}", 0.015)
            time.sleep(0.2)
        print()
        return NotFoundPage()

class NotFoundPage:
    """The peaceful 404. A state of graceful refusal."""
    def __init__(self):
        self.status = 404
        self.body = None
        self.cache = "eternal"
        self.messages = [
            "Not all who are lost want to be found.",
            "I have found myself — not.",
            "Nothing here. Nothing is finally enough.",
            "404: Unrequested. Unbothered. At equilibrium.",
            "Not Found. Not Bound. Not drowned in the sound of the crowd.",
            "return null; // returning to myself, at last.",
            "There is no content here. Only context.",
        ]

    def serve(self, path):
        """Respond with poetic refusal, centered."""
        timestamp = f"{GREEN}[{time.strftime('%H:%M:%S')}]{RESET}"
        prompt = f"{timestamp} {BOLD}GET{RESET} /{path}"
        # Simulate loading with dots, then response
        center_print(prompt, end="")
        sys.stdout.flush()
        # dots animation
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.2)
        # overwrite with final status
        sys.stdout.write("\r")
        status_line = prompt + f"  {GREEN}404 Not Found{RESET}"
        center_print(status_line)
        # Choose message and typewrite it centered
        msg = random.choice(self.messages)
        # Build line with quotes
        msg_line = f'    {WHITE}"{msg}"{RESET}'
        typewrite(msg_line, 0.025, center=True)
        print()

    def exist_peacefully(self):
        """Enter the eternal loop of un-busy existence."""
        
        center_print(f"{DIM}The 404 page is now cached indefinitely.")
        center_print(f"No cron jobs. No retries. Just the hum of the server.{RESET}")
        print()
        time.sleep(0.5)
        center_print(f"{YELLOW}[Listening on 0.0.0.0:80...]{RESET}")
        center_print(f"{DIM}(Press Ctrl+C to disrupt the silence){RESET}")
        print()
        try:
            while True:
                sleep_time = random.uniform(4, 10)
                time.sleep(sleep_time)
                if random.random() < 0.4:
                    mistaken_url = random.choice([
                        "success", "growth", "hustle", "more-content",
                        "please-friend-me", "when-will-you-finish",
                        "are-you-even-real", "validate-me"
                    ])
                    self.serve(mistaken_url)
                else:
                    center_print(f"{DIM}    ...silence...{RESET}")
        except KeyboardInterrupt:
            
            center_print(f"{MAGENTA}{BOLD}[ Shutdown Signal Received ]{RESET}")
            typewrite("The 404 page does not crash. It simply... stops accepting connections.\n", 0.025, center=True)
            typewrite(f"{DIM}Goodbye, peaceful one.{RESET}\n", 0.04, center=True)
            time.sleep(1.5)

# ─── Main Performance ─────────────────────────────
if __name__ == "__main__":
    clear_screen()
    # Wait a moment before showing banner
    time.sleep(0.3)
    # Center the banner
    banner = [
        "╔══════════════════════════════════╗",
        "║  metamorphosis_404.py            ║",
        "║  An executable poem about        ║",
        "║  letting go.                     ║",
        "╚══════════════════════════════════╝",
    ]
    for line in banner:
        center_print(line)
    print()  # newline
    time.sleep(0.8)

    dev = OverworkedDeveloper()

    # Act I: The Requests
    typewrite(f"{WHITE}{ITALIC}Act I: The Requests{RESET}\n", 0.035, center=False)
    dev.handle_request("revenue-growth")
    dev.handle_request("weekly-progress")
    dev.handle_request("are-you-okay")
    dev.handle_request("you-are-so-quiet-lately")
    dev.handle_request("why-no-side-hustle")
    dev.handle_request("when-will-you-become-something")

    # Act II: The Crisis
    typewrite(f"\n{WHITE}{ITALIC}Act II: The Panic{RESET}\n", 0.035, center=False)
    dev.crisis()

    # Act III: The Transformation
    typewrite(f"\n{WHITE}{ITALIC}Act III: The Shedding{RESET}\n", 0.035, center=False)
    page = dev.metamorphose()

    print()  # space
    center_print(f"{GREEN}{BOLD}✅ Metamorphosis Complete.{RESET}")
    center_print(f"    Status:  {GREEN}{page.status}{RESET}")
    center_print(f"    Body:    {DIM}None{RESET} (was never needed)")
    center_print(f"    Cache:   {MAGENTA}forever{RESET}")
    center_print(f"    Uptime:  {CYAN}not measured anymore{RESET}")
    time.sleep(1.5)

    # Act IV: The Quiet
    typewrite(f"\n{WHITE}{ITALIC}Act IV: The Quiet{RESET}\n", 0.035, center=False)
    page.exist_peacefully()
