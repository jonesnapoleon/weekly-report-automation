import base64
import io

import numpy as np
from matplotlib import pyplot as plt

from constants import DEFAULT_IMAGE_PATH


class PieChart:
    def __init__(self, jira_status={}, title=''):
        self.data = []
        self.labels = []
        self.title = title

        for label, value in jira_status.items():
            self.data.append(value)
            self.labels.append(label)

    def __generate_image(self):
        _, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

        wedges, _, autotexts = ax.pie(self.data, autopct=lambda x: f'{x}%')

        ax.legend(wedges, self.labels,
                  title="Jira task status",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))
        ax.set_title(self.title)

        plt.setp(autotexts, size=8, weight="bold")
        plt.savefig(DEFAULT_IMAGE_PATH)

    def process(self):
        self.__generate_image()

        return f'<p><img src="data:image/jpeg;base64"/></p>'
