import idom

victory = idom.Module("victory")

VictoryBar = victory.Import("VictoryBar", fallback="loading...")

display(VictoryBar, {"style": {"parent": {"width": "500px"}}})
