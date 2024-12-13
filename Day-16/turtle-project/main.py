from prettytable import PrettyTable
df = PrettyTable()
df.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
df.add_row(["Adelaide", 1295, 1158259, 600.5])
df.add_row(["Brisbane", 5905, 1857594, 1146.4])
df.add_row(["Darwin", 112, 120900, 1714.7])
df.add_row(["Hobart", 1357, 205556, 619.5])
df.add_row(["Sydney", 2058, 4336374, 1214.8])
df.add_row(["Melbourne", 1566, 3806092, 646.9])
df.add_row(["Perth", 5386, 1554769, 869.4])
print(df)
