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
   

## Hackathon Submission Information

### Challenge name:
12. Sustainable travel planner

### Members:
- **Qilan Lin** _k21204786_
- **Yi Lu** _k23001215_
- **Zhaoqi He** _k23004818_
- **Jingwen Guo** _k23006143_
- **Rokas Tarasevicius** _k22048691_

### Link to the slide deck:
[Slide Deck](https://emckclac-my.sharepoint.com/:p:/g/personal/k23001215_kcl_ac_uk/ERpTTJmMKKFLglfhX8aZwLEB6jSlH9Mp_Um_vJk6l5rJGQ?e=MUpaKU)

### Description:

#### Overview

The Sustainable Travel Assistant is crafted to guide users in planning their journeys with an emphasis on environmental sustainability. It achieves this by comparing the carbon footprints of different transportation modes for specific routes and advocating for the use of public transport and bicycles. Additionally, it offers advice on carbon offsetting to encourage more eco-conscious travel decisions.

#### Features

- **Carbon Footprint Analysis**: Provides comparisons of carbon emissions across various transport options.
- **Eco-Friendly Route Suggestions**: Highlights public transportation and biking as preferred options.
- **Carbon Offsetting Tips**: Offers guidance on how to neutralize travel-related carbon emissions.
- **User-Friendly Interface**: Simple input fields for journey details to receive instant eco-friendly travel advice.

#### How It Works

1. **Input Journey Details**: Users provide their starting point, destination, and travel preferences.
2. **Calculate Emissions**: The assistant calculates emissions using up-to-date emission factors for each transport mode.
3. **Offer Eco-Friendly Options**: It suggests the most sustainable routes and methods for travel.
4. **Educate on Carbon Offsetting**: Users receive tips on how to offset the carbon footprint of their chosen travel method.




