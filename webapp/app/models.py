import csv

class Test(object):
    def __init__(self, text1, text2, score, save_path="/tmp/", filename="test.csv"):
        self.text1 = text1
        self.text2 = text2
        self.score = score
        self.save_path = save_path
        self.filename = filename

        self.save_string = [self.text1, self.text2, self.score]

        self.save_results()

    def __repr__(self):
        return '<Text 1: {}\nText 2: {}\nResult {}>'.format(self.text1, self.text2, self.score)

    def save_results(self):
        with open(self.save_path+self.filename, mode='w') as w_file:
            file_writer = csv.writer(w_file, delimiter='\t')

            file_writer.writerow(self.save_string)