
# GrantCrew

**GrantCrew** is a tool designed to help users search for both state and federal grants available in a specified field, using the autonomous agent framework **crewAI**. The program performs the search and compiles a report in markdown format on the available grant opportunities.

## Features

- **Autonomous Agent:** GrantCrew utilizes the **crewAI** autonomous agent framework.
- **State and Federal Grants:** It searches for grants at both state and federal levels.
- **Markdown Report:** Outputs a report in markdown format summarizing the available grants.
- **Powered by Open Source LLM:** It leverages the open-source **Llama3** model through the **Groq API**.

## Requirements

- **Python 3.8+**
- **Groq API Key:** Required for accessing the Llama3 model.
- **Serper API Key:** Required for performing the grant searches.

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/SpyderRex/GrantCrew
cd GrantCrew
```

### Step 2: Install the Required Dependencies

Ensure you have `pip` installed, then run:

```bash
pip install -r requirements.txt
```

## Usage

1. **Obtain API Keys**  
   You will need to obtain the following API keys:
   - **Groq API Key:** You can sign up for a free account and obtain an API key [here](https://console.groq.com/docs/quickstart).
   - **Serper API Key:** You can sign up and get your API key [here](https://serper.dev/).

2. **Run the Program**

   You can run the program using:

   ```bash
   python main.py
   ```

   Or, if your system uses Python 3:

   ```bash
   python3 main.py
   ```

3. **Specify State and Field**

   When prompted by the program:
   - First, specify the **state** for which you want to search for grants.
   - Then, specify the **field** or area of interest (e.g., education, healthcare, technology).

   The agent will then autonomously search for both state and federal grants based on your input.

4. **Receive Results in Markdown**

   Once the search is complete, the program will generate a report in markdown format, summarizing the available grants in the specified field.

## Example

```bash
python3 main.py
```

**Prompt:**
- Enter State: `California`
- Enter Field: `Renewable Energy`

**Output:**  
The program will return a markdown report containing relevant grants available for renewable energy in California.

## Contributing

If you'd like to contribute to **GrantCrew**, feel free to submit issues or pull requests on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
