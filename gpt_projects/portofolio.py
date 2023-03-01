name = input("Enter your name: ")
bio = input("Enter a short bio: ")

projects = []
while True:
    project_name = input("Enter project name (or type 'exit' to finish): ")
    if project_name.lower() == "exit":
        break
    project_description = input("Enter project description: ")
    projects.append((project_name, project_description))

html = f"""
<!DOCTYPE html>
<html>
<head>
	<title>{name}'s Portfolio</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<style>
		body {{
			font-family: sans-serif;
			max-width: 800px;
			margin: 0 auto;
			padding: 1rem;
		}}

		h1 {{
			text-align: center;
			margin-bottom: 0;
		}}

		p {{
			margin-top: 0;
			font-size: 1.2rem;
			line-height: 1.5;
		}}

		ul {{
			list-style: none;
			padding: 0;
		}}

		li {{
			margin-bottom: 1rem;
		}}

		h2 {{
			margin-top: 2rem;
			margin-bottom: 1rem;
		}}
	</style>
</head>
<body>
	<header>
		<h1>{name}</h1>
		<p>{bio}</p>
	</header>

	<main>
		<h2>Projects</h2>
		<ul>
			{"".join(f"<li><strong>{project[0]}:</strong> {project[1]}</li>" for project in projects)}
		</ul>
	</main>
</body>
</html>
"""

with open("portfolio.html", "w") as file:
    file.write(html)

print("Portfolio generated successfully!")
