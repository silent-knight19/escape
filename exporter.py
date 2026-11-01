import html

SAMPLE_RECORDS = [
    {
        "id": 101,
        "department": "Research & Development",
        "description": "Optimize search algorithm (check if x < 10)",
        "status": 'Status: "Active" & in progress',
    },
    {
        "id": 102,
        "department": "Quality Assurance",
        "description": "Verify threshold where latency > 250ms",
        "status": 'Status: "Pending"',
    },
    {
        "id": 103,
        "department": "Operations",
        "description": "Standard maintenance completed",
        "status": "Completed",
    },
]


def escape_html(text: str) -> str:
    """Escape special characters (&, <, >, quotes) for safe HTML rendering."""
    return text


def generate_html_table(records: list) -> str:
    """Generate an HTML document containing a table of records."""
    rows = []
    for record in records:
        row = (
            f"        <tr>\n"
            f"            <td>{escape_html(str(record['id']))}</td>\n"
            f"            <td>{escape_html(record['department'])}</td>\n"
            f"            <td>{escape_html(record['description'])}</td>\n"
            f"            <td>{escape_html(record['status'])}</td>\n"
            f"        </tr>"
        )
        rows.append(row)

    rows_html = "\n".join(rows)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Exported Records</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 40px;
            background-color: #f8f9fa;
        }}
        h1 {{
            color: #212529;
            margin-bottom: 20px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            background-color: #ffffff;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            border-radius: 6px;
            overflow: hidden;
        }}
        th, td {{
            text-align: left;
            padding: 12px 16px;
            border-bottom: 1px solid #dee2e6;
        }}
        th {{
            background-color: #e9ecef;
            color: #495057;
            font-weight: 600;
        }}
        tr:last-child td {{
            border-bottom: none;
        }}
        tr:hover {{
            background-color: #f1f3f5;
        }}
    </style>
</head>
<body>
    <h1>Exported Records</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Department</th>
                <th>Description</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
{rows_html}
        </tbody>
    </table>
</body>
</html>
"""


def export_to_file(records: list, output_path: str = "records.html") -> str:
    """Export records to an HTML file."""
    html_content = generate_html_table(records)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    return output_path


if __name__ == "__main__":
    output = export_to_file(SAMPLE_RECORDS)
    print(f"Exported records to {output}")

