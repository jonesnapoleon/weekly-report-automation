import numpy as np
from matplotlib import pyplot as plt

from constants.data import DEFAULT_JIRA_STATUS_IMAGE_PATH, PIECHART_MESSAGE


class PieChart:
    def __init__(self, jira_status={}, title=PIECHART_MESSAGE):
        self.data = []
        self.labels = []
        self.title = title

        for label, value in jira_status.items():
            self.data.append(value)
            self.labels.append(label)

    def __obtain_pie_label(self, percentage):
        absolute = int(np.round(percentage/100.*np.sum(self.data)))
        return f'{percentage:.1f}%\n({absolute:d} issue)'

    def generate_and_save_image(self, save_filename=DEFAULT_JIRA_STATUS_IMAGE_PATH):
        _, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

        wedges, _, autotexts = ax.pie(self.data, autopct=self.__obtain_pie_label,
                                      wedgeprops=dict(width=0.5))

        ax.legend(wedges, self.labels,
                  title="Jira task status",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))
        ax.set_title(self.title)

        plt.setp(autotexts, size=8, weight="bold")
        plt.savefig(save_filename)
