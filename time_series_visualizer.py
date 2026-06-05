{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOaKb0q76NbVa9q9F5SClWP",
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
        "<a href=\"https://colab.research.google.com/github/Vamsikrishna329-in/Data-Analysis-Projects/blob/main/time_series_visualizer.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "t_fydfuTZIB1"
      },
      "outputs": [],
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import pandas as pd\n",
        "import seaborn as sns\n",
        "from pandas.plotting import register_matplotlib_converters\n",
        "\n",
        "register_matplotlib_converters()\n",
        "\n",
        "# Import data (Make sure to parse dates. Consider setting index column to 'date'.)\n",
        "df = pd.read_csv(\"fcc-forum-pageviews.csv\", parse_dates=[\"date\"], index_col=\"date\")\n",
        "\n",
        "# Clean data (filter out days when page views were in top 2.5% or bottom 2.5%)\n",
        "df = df[\n",
        "    (df[\"value\"] >= df[\"value\"].quantile(0.025)) &\n",
        "    (df[\"value\"] <= df[\"value\"].quantile(0.975))\n",
        "]\n",
        "\n",
        "def draw_line_plot():\n",
        "    # Draw line plot\n",
        "    fig, ax = plt.subplots(figsize=(15, 5))\n",
        "    ax.plot(df.index, df['value'], color='red', linewidth=1)\n",
        "\n",
        "    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')\n",
        "    ax.set_xlabel('Date')\n",
        "    ax.set_ylabel('Page Views')\n",
        "\n",
        "    # Save image and return fig (don't change this part)\n",
        "    fig.savefig('line_plot.png')\n",
        "    return fig\n",
        "\n",
        "def draw_bar_plot():\n",
        "    # Copy and modify data for monthly bar plot\n",
        "    df_bar = df.copy()\n",
        "    df_bar['year'] = df_bar.index.year\n",
        "    df_bar['month'] = df_bar.index.month_name()\n",
        "\n",
        "    # Group by year and month, calculating the mean, then unstack to plot\n",
        "    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()\n",
        "\n",
        "    # Order the columns by month chronologically\n",
        "    months = ['January', 'February', 'March', 'April', 'May', 'June',\n",
        "              'July', 'August', 'September', 'October', 'November', 'December']\n",
        "    df_bar_grouped = df_bar_grouped[months]\n",
        "\n",
        "    # Draw bar plot\n",
        "    fig = df_bar_grouped.plot(kind='bar', figsize=(10, 6), ylabel='Average Page Views', xlabel='Years').figure\n",
        "    plt.legend(title='Months')\n",
        "\n",
        "    # Save image and return fig (don't change this part)\n",
        "    fig.savefig('bar_plot.png')\n",
        "    return fig\n",
        "\n",
        "def draw_box_plot():\n",
        "    # Prepare data for box plots (this part is done!)\n",
        "    df_box = df.copy()\n",
        "    df_box.reset_index(inplace=True)\n",
        "    df_box['year'] = [d.year for d in df_box.date]\n",
        "    df_box['month'] = [d.strftime('%b') for d in df_box.date]\n",
        "\n",
        "    # Draw box plots (using Seaborn)\n",
        "    fig, axes = plt.subplots(1, 2, figsize=(15, 6))\n",
        "\n",
        "    # Year-wise Box Plot\n",
        "    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])\n",
        "    axes[0].set_title('Year-wise Box Plot (Trend)')\n",
        "    axes[0].set_xlabel('Year')\n",
        "    axes[0].set_ylabel('Page Views')\n",
        "\n",
        "    # Month-wise Box Plot\n",
        "    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',\n",
        "                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']\n",
        "    sns.boxplot(x='month', y='value', data=df_box, order=month_order, ax=axes[1])\n",
        "    axes[1].set_title('Month-wise Box Plot (Seasonality)')\n",
        "    axes[1].set_xlabel('Month')\n",
        "    axes[1].set_ylabel('Page Views')\n",
        "\n",
        "    # Save image and return fig (don't change this part)\n",
        "    fig.savefig('box_plot.png')\n",
        "    return fig"
      ]
    }
  ]
}