# AI Research CLI Tool

## Overview

The AI Research CLI Tool is a command-line interface designed to assist users in generating structured, tabular data for research purposes. By leveraging the Bing Web Search API and the GPT-4o model, this tool transforms raw research topics into organized data that can be easily exported and utilized.

## Installation

You can install the package directly from PyPI:
```bash
pip install grid-research
```

## Quick Start

```python
from grid import Grid
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

# Create a Grid instance
grid = Grid(
    client=client,
    num_rows=100,
    research_topic="promising manufacturing startups",
    headers=["Name", "Funding", "Revenue", "Description"]
)

# Generate research data
data = grid.research()

# Save to CSV
data.to_csv('manufacturing_startups.csv', index=False)
```

## Features

- **AI-Suggested Column Headers**: Automatically generate relevant column headers and descriptions for your research data.
- **Custom Header Editing**: Modify or create your own headers to suit your specific research needs.
- **Data Generation**: Generate between 1 to 100 rows of structured research data based on your queries.
- **Beautiful Terminal Interface**: Enjoy a visually appealing and user-friendly command-line interface.
- **Export-Ready Data**: Easily export the generated data in a structured format for further analysis.

## CLI Usage

1. **Start the Application**: Run the CLI tool from your terminal.
   ```bash
   python grid/cli.py
   ```

2. **Input Research Topic**: When prompted, enter the topic you would like to research.

3. **Choose Header Creation Method**:
   - **Get AI Suggestions**: Use the AI to generate suggested headers.
   - **Create Manually**: Input your own headers.

4. **Specify Number of Rows**: Indicate how many rows of data you wish to generate.

5. **Data Generation**: The tool will perform a web search using the Bing API and generate structured data based on the retrieved information.

6. **Export Data**: The generated data will be returned in a pandas.DataFrame, ready for your use.

## Requirements

- Python 3.8 or higher
- OpenAI API Key
- Bing Search API Key

## Environment Variables

Make sure to set the following environment variables in your `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
BING_SEARCH_V7_SUBSCRIPTION_KEY=your_bing_search_api_key
```

## Example Use Cases

1. **Market Research**:
```python
grid = Grid(client, 50, "top AI startups in healthcare", 
    ["Company", "Funding", "Product", "Target Market"])
```

2. **Competitive Analysis**:
```python
grid = Grid(client, 30, "electric vehicle manufacturers", 
    ["Company", "Market Cap", "Annual Production", "Key Technologies"])
```

3. **Investment Research**:
```python
grid = Grid(client, 20, "renewable energy companies", 
    ["Company", "Revenue", "Growth Rate", "Technology Focus"])
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request on our [GitHub repository](https://github.com/bobcoi03/grid).

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- [OpenAI](https://openai.com) for providing the models
- [Bing Web Search API](https://www.microsoft.com/en-us/bing/apis/bing-search-api-v7) for enabling web search capabilities