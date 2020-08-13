import re

from rich.console import Console
from rich.table import Table

show_ip_interface_brief = """
Router# show ip interface brief
Interface             IP-Address      OK?    Method Status     	Protocol
GigabitEthernet0/1    unassigned      YES    unset  up         	up
GigabitEthernet0/2    192.168.190.235 YES    unset  up         	up
GigabitEthernet0/3    unassigned      YES    unset  up         	up
GigabitEthernet0/4    192.168.191.2   YES    unset  up         	up
TenGigabitEthernet2/1 unassigned      YES    unset  up         	up
TenGigabitEthernet2/2 unassigned      YES    unset  up         	up
TenGigabitEthernet2/3 unassigned      YES    unset  up         	up
TenGigabitEthernet2/4 unassigned      YES    unset  down       	down
GigabitEthernet36/1   unassigned      YES    unset  down        down
GigabitEthernet36/2   unassigned      YES    unset  down        down
GigabitEthernet36/11  unassigned      YES    unset  down       	down
GigabitEthernet36/25  unassigned      YES    unset  down       	down 
Te36/45               unassigned      YES    unset  down       	down
Te36/46               unassigned      YES    unset  down       	down
Te36/47               unassigned      YES    unset  down       	down
Te36/48               unassigned      YES    unset  down       	down
Virtual36             unassigned      YES    unset  up         	up
"""

console = Console()

table = Table(show_header=True, header_style="bold cyan")
table.add_column("Interface", style='dim', justify='left')
table.add_column("IP-Address")
table.add_column("OK?")
table.add_column("Method", justify='center')
table.add_column("Status")
table.add_column("Protocol")

intf_pattern = "^[lLgGeEfF]\S+[0-9]/?[0-9]*"
regex = re.compile(intf_pattern)

for row in show_ip_interface_brief.splitlines():
    if not regex.search(row):
        continue
    table.add_row(
        row.split()[0],
        row.split()[1],
        row.split()[2],
        row.split()[3],
        "[green]up[/green]" if row.split()[4] == 'up' else "[red]down[/red]",
        "[green]up[/green]" if row.split()[5] == 'up' else "[red]down[/red]",
    )
console.print(table)
