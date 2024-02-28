# Sustainable Travel Assistant

## Environment Setup

1. **Install Poetry**: Poetry is a Python dependency management tool. It can be installed by running the following command in the terminal:

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
   
2. **Start a Poetry shell**: Navigate to the project directory and run the following command to start a Poetry shell:

    ```bash
    poetry shell
    ```
   
3. **Create .env file**: Create a `.env` file in the root directory of the project and add the following environment variables:

    ```env
    OPENAI_API_KEY=<your_openai_api_key>
    ```

4. **Start up the App**: Run the following command to start the app:

    ```bash
   chainlit run app.py -w
    ```
   

