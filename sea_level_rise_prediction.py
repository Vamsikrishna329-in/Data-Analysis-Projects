{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNxGVmoOSmwvzr4Z4IQcKWQ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Vamsikrishna329-in/Data-Analysis-Projects/blob/main/sea_level_rise_prediction.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "mzNJO3tB6dQb"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "from scipy.stats import linregress\n",
        "\n",
        "def draw_plot():\n",
        "    # 1. Read data from file\n",
        "    df = pd.read_csv('epa-sea-level.csv')\n",
        "\n",
        "    # 2. Create scatter plot\n",
        "    fig, ax = plt.subplots(figsize=(10, 6))\n",
        "    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10, label='Data')\n",
        "\n",
        "    # 3. Create first line of best fit (1880 - 2050)\n",
        "    # Get the slope and intercept using all data\n",
        "    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])\n",
        "\n",
        "    # Create an extended range of years through 2050 for the prediction\n",
        "    x_pred_all = pd.Series(range(1880, 2051))\n",
        "    y_pred_all = res_all.slope * x_pred_all + res_all.intercept\n",
        "\n",
        "    # Plot the line\n",
        "    plt.plot(x_pred_all, y_pred_all, color='red', label='Best Fit: 1880-2050')\n",
        "\n",
        "    # 4. Create second line of best fit (2000 - 2050)\n",
        "    # Filter the dataframe for years 2000 and onwards\n",
        "    df_recent = df[df['Year'] >= 2000]\n",
        "\n",
        "    # Get the slope and intercept using only recent data\n",
        "    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])\n",
        "\n",
        "    # Create an extended range of years from 2000 through 2050\n",
        "    x_pred_recent = pd.Series(range(2000, 2051))\n",
        "    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept\n",
        "\n",
        "    # Plot the line\n",
        "    plt.plot(x_pred_recent, y_pred_recent, color='green', label='Best Fit: 2000-2050')\n",
        "\n",
        "    # 5. Add labels and title\n",
        "    plt.xlabel('Year')\n",
        "    plt.ylabel('Sea Level (inches)')\n",
        "    plt.title('Rise in Sea Level')\n",
        "    plt.legend()\n",
        "\n",
        "    # Save plot and return data for testing (DO NOT MODIFY)\n",
        "    plt.savefig('sea_level_plot.png')\n",
        "    return plt.gca()"
      ]
    }
  ]
}