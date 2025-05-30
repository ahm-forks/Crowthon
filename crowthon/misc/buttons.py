# Import the Button class from Telethon's custom module for creating inline buttons
from telethon.tl.custom import Button

# Define the main categories menu with inline buttons for navigation
categories_menu = [
    [
        Button.inline("👤 Account", b'account'),
        Button.inline("👥 Group", b'group')
    ],
    [
        Button.inline("🤖 System", b'system')
    ]
]

# Define the main account menu with inline buttons
account_menu = [
    [
        Button.inline("AFK", b'afk')
    ],
    [
        Button.inline("Main Menu", b'main_menu')
    ]
]

# Define a return button layout to go back to the account menu
return_to_the_account_menu = [
    [
        Button.inline("Back", b'back_to_the_account')
    ]
]

# Define the system menu with inline buttons for system-related commands
system_menu = [
    [   
        Button.inline("Alive", b'alive'),
        Button.inline("Ping", b'ping')
    ],
    [
        Button.inline("Main Menu", b'main_menu')
    ]
]

# Define a button layout that provides a "Back" button to return to the System menu
return_to_the_system_menu = [
    [
        Button.inline("Back", b'back_to_the_system')
    ]
]