""" This module helps extracting data from Hugging face """

from datasets import load_dataset_builder
from datasets import load_dataset


class HuggingFaceDataLoad:
    """This class load data from HF"""

    def __init__(self, name, lang):
        """Initialization

        Parameters
        ----------
        name :
            name of the dataset on HF
        lang :
            language of the documents

        Returns
        -------
        """
        self.name = name
        self.lang = lang
        self.ds_builder = load_dataset_builder(name, lang)

    def inspectdatadescription(self):
        """Get data description

        Parameters
        ----------

        Returns
        -------
            Returns dataset description
        """
        print("Loading dataset description")
        print()
        description = self.ds_builder.info.description
        with open(
            f"../data/source/dataset_desc_{self.lang}.txt", "w", encoding="utf-8"
        ) as desc:
            desc.write(description)

        print(f"Dataset description loaded in ./data/source/dataset_desc_{self.lang}.txt")

    def inspectdatafeatures(self):
        """Get data features

        Parameters
        ----------

        Returns
        -------
            Returns features info
        """
        features = self.ds_builder.info.features

        return features

    def getdata(self, split_name):
        """Load the data from HF

        Parameters
        ----------
        split_name :
            split name, either 'train', 'test' or 'validation'

        Returns
        -------
        data :
            data from HF
        """
        data = load_dataset(self.name, split=split_name, lang=self.lang)

        return data
