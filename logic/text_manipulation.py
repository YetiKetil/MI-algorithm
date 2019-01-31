import csv
from logic.sentsim_mihalcea_bnc import MihalceaSentSimBNC

class text_manipulation(object):

    def __init__(self, upload_folder):
        self.input_list = ""
        self.upload_folder = upload_folder
        self.filename = ""
        self.save_filename = ""
        self.save_file_full_path = ""
        open_file_full_path = self.upload_folder + "/" + self.filename

        if len(self.filename) != 0:
            save_filename = self.filename.replace(".", "_result.")
        else:
            save_filename = "manual_result.csv"
        self.save_file_full_path = self.upload_folder + "/" + save_filename

    def print_input_list(self):
        print(self.input_list)

    def read_from_file(self, file):
        """
        Function reads whole content from a file and puts it in a string
        :param file: full path to the file
        :return: whole text from file as a string
        """
        print("PATH TO READ FILE:" + file)
        whole_text = ""
        with open(file) as f:
            read_obj = csv.reader(f, delimiter='\n')
            for row in read_obj:
                if len(row) != 0:
                    print("row:", row)
                    whole_text += "\n".join(row)
        print(whole_text)
        print("a\nb")
        return whole_text

    def save_to_file(self, text):
        """

        :param text:
        :return:
        """

        text = text.replace("\n", "\t")  # prepare text as tab delimited

        f = open(self.save_file_full_path, 'wt', encoding='utf-8')
        f.write(text)
        f.close()

    def text_analysis(self, text_analysis):
        """
        :param text_analysis:
        :return:
        """
        sentsim = MihalceaSentSimBNC()
        sentsim.download_nltk_resources()

        print("TEXT FOR ANALYSIS:")
        print(text_analysis)
        print("***********************************")
        list_text = text_analysis.split("\n")
        print("Antall rader:", len(list_text))
        text_1 = list_text[0]
        text_2 = list_text[1]

        score = round(sentsim.similarity(text_1, text_2), 4)

        text_analysis = text_analysis + "\n" + str(score)

        self.save_to_file(text_analysis)
        text_analysis = text_analysis.replace('\n', '<br>')

        return text_analysis

