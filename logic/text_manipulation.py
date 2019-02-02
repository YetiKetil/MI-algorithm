import csv, itertools, re
from logic.sentsim_mihalcea_bnc import MihalceaSentSimBNC

class text_manipulation(object):

    def __init__(self, upload_folder):
        self.input_list = ""
        self.upload_folder = upload_folder + "/"
        self.filename = ""
        self.save_filename = ""
        self.save_file_full_path = ""
        open_file_full_path = self.upload_folder + self.filename

        self.list_of_results = []

    def text_analysis(self, text1, text2):
        """

        :param text1:
        :param text2:
        :return:
        """
        sentsim = MihalceaSentSimBNC()
        sentsim.download_nltk_resources()

        score = round(sentsim.similarity(text1, text2), 4)
        text_analysis = text1 + "\t" + text2 + "\t" + str(score)
        self.list_of_results.append(text_analysis)

        return text_analysis


    def simple_two_text_analysis(self, text1, text2):
        """

        :param text1:
        :param text2:
        :return:
        """
        self.list_of_results = []
        self.text_analysis(text1, text2)

        # prepare text for display in HTML
        text_analysis = '\t'.join(self.list_of_results).replace('\t', '<br>')
        self.save_to_file()
        return text_analysis


    def analysis_from_pasted_text(self, pasted_text):
        """

        :param pasted_text:
        :return:
        """
        self.list_of_results = []  # empty global variable
        sentences = re.split(r"[~\r\n]+", pasted_text)
        for pair in itertools.combinations(sentences, 2):
            self.text_analysis(pair[0], pair[1])

        self.save_to_file()

        print(sentences)

    def analysis_from_file(self, filename):
        """

        :param filename:
        :return:
        """
        self.list_of_results = [] # empty global variable
        sentences = self.from_file_to_list(filename)
        for pair in itertools.combinations(sentences, 2):
            self.text_analysis(pair[0], pair[1])

        self.save_to_file()


    def from_file_to_list(self, filename):
        """
        Reads sentences from a file and puts them in a list
        :param filename: name of the uploaded file
        :return: List of sentences
        """
        self.filename = filename
        file_path = self.upload_folder + self.filename
        list_of_sentences = []
        with open(file_path) as f:
            read_obj = csv.reader(f, delimiter="\n")
            for row in read_obj:
                if len(row) != 0:
                    list_of_sentences.append(row[0])
        print(list_of_sentences)
        return list_of_sentences


    def save_to_file(self):
        """
        Save results to a tab delimited file
        :return:
        """
        # prepare the name of the save file
        if len(self.filename) != 0:
            save_filename = self.filename.replace(".", "_result.")
        else:
            save_filename = "manual_result.csv"
        self.save_file_full_path = self.upload_folder + save_filename

        wfile = open(self.save_file_full_path, 'wt')
        for l in self.list_of_results:
            wfile.write(l + "\n")
        wfile.close()



