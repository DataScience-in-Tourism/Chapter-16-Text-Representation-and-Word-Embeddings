import csv
import re
import random
import numpy as np


# load data from csv file
# label is assumed to be enclosed in ; and located at the beginning of a line after digit;digit
def load_data(file_name, n=-1):
    with open(file_name) as fh:
        reader = csv.reader(fh, delimiter='\n')
        lines = []
        line = ''
        labels = []
        for i, row in enumerate(reader):
            # skip first line
            if i == 0:
                continue
            if row and len(row[0]) > 3:
                row = row[0]
                row, label = clean(row)
                if label:
                    line += row
                    lines.append(line)
                    labels.append(label)
                    line = ''
                else:
                    line += row
                pass
            if i == n:
                break
    return lines, labels


# return randomly chosen n lines from lists 1 and 2, keeping the same index between them
def random_choose(ls1, ls2, n):
    l1 = len(ls1)
    l2 = len(ls2)
    if l1 != l2:
        raise ValueError(f'expected lists to be of equal length, but got {l1}, {l2}')
    nrs = random.sample(range(0, l1), n)
    ls1_ = []
    ls2_ = []
    for i in nrs:
        ls1_.append(ls1[i])
        ls2_.append(ls2[i])
    return ls1_, ls2_


# helpers
def clean(line):
    # label
    label = re.match(r'\d+;\d+;([A-Z][a-z]+);', line)
    if label:
        label = label.groups()[0]
    line = re.subn(r';[A-Z][a-z]+;', '', line, count=1)[0]
    # punctuation and numbers
    line = re.sub(r'["\(\)|*❤⭐,.!?\-:;0-9…]', ' ', line)
    # cyrillic (may take some time)
    # line = re.sub('[а-яА-Я]', '', line)
    line = re.sub('[\u0400-\u04FF]', ' ', line)
    # web adresses
    line = re.sub(r'^[A-Za-z._-][^/@]*$', ' ', line)
    # hashtags
    line = re.sub(r'#[a-z0-9]+', '', line)
    # extra whitespace
    line = re.sub(r'\s\s*', ' ', line)
    return line, label


def get_vectors(ls):
    vectors = []
    n = 0
    with open('glove.6B.300d.txt', 'r')as fh:
        for i, line in enumerate(fh.readlines()):
            n += 1
            # print(line)
            for l in ls:
                if l not in vectors and line.startswith(l):
                    if line[len(l)] == ' ':
                        vectors.append(line)
                if len(vectors) == len(ls):
                    break
        print(f'{n} runs')
        return vectors


def save_vectors(vectors, file_name):
    with open(file_name, 'w') as fh:
        fh.write(''.join(vectors))


if __name__ == '__main__':
    # lines, labels = load_data('Airbnb_total.csv', -1)
    # lines, labels = random_choose(lines, labels, 100)
    # lines_text = ' '.join(lines)
    # labels_text = ' '.join(labels)
    # unique_labels = np.unique(labels)
    # print(unique_labels)
    # city lists
    city_list_europe = ['Amsterdam', 'Athens', 'Berlin', 'Brussels', 'Copenhagen', 'Helsinki', 'London',
                        'Madrid', 'Oslo', 'Paris', 'Prague', 'Rome', 'Stockholm', 'Vienna', 'Warschau']
    city_list_europe = [w.lower() for w in city_list_europe]
    tourist_cities_list = ['miami', 'hamburg', 'zhuhai', 'los angeles', 'luanda', 'oslo', 'shanghai', 'guadalajara',
                           'mumbai', 'buenos', 'taipei city', 'beijing', 'nairobi', 'paris', 'alexandria',
                           'kuala lumpur', 'vienna', 'warsaw', 'kiev', 'mugla', 'saint petersburg', 'tianjin', 'delhi',
                           'sao paulo', 'dongguan', 'berlin', 'bogotá', "xi'an", 'brussels', 'ho chi minh city', 'doha',
                           'johannesburg', 'auckland', 'dubai', 'punta cana', 'vancouver', 'guilin', 'amman', 'surat',
                           'dallas', 'khartoum', 'new york', 'burgas', 'warschau', 'phuket', 'venice', 'guangzhou',
                           'djerba', 'wuhan', 'tokyo', 'chongqing', 'atlanta', 'antalya', 'dalian', 'rome', 'lagos',
                           'sharm el-sheikh', 'athens', 'kinshasa', 'cairo', 'baghdad', 'stockholm', 'santiago',
                           'macau', 'shenyang', 'belo horizinte', 'munich', 'baku', 'bangkok', 'rio de janeiro',
                           'harbin', 'houston', 'istanbul', 'hyderabad', 'mecca', 'osaka', 'sofia', 'manama', 'nanjing',
                           'moscow', 'pune', 'toronto', 'orlando', 'marrakech', 'nice', 'edirne', 'dhaka', 'suzhou',
                           'jakarta', 'cancun', 'chennai', 'madrid', 'chiang mai', 'melbourne', 'tehran', 'riyadh',
                           'lahore', 'mexico city', 'st petersburg', 'prague', 'chengdu', 'singapore', 'yangon',
                           'copenhagen', 'milan', 'london', 'pattaya', 'barcelona', 'dar es salaam', 'washington d.c.',
                           'manila', 'lisbon', 'bangalore', 'nagoya', 'helsinki', 'denpasar', 'frankfurt',
                           'east province', 'harare', 'las vegas', 'shenzhen', 'jinan', 'san francisco', 'hanoi',
                           'karachi', 'siem reap', 'budapest', 'ahmedabad', 'philadelphia', 'seoul', 'são paulo',
                           'kolkata', 'abu dhabi', 'agra', 'qingdao', 'hangzhou', 'dublin', 'lima', 'foshan', 'chicago',
                           'jaipur', 'sousse', 'amsterdam', 'florence', 'mexico', 'washington', 'honolulu', 'sydney',
                           'hong kong', 'new york city', 'christchurch', 'bucharest', 'buenos aires', 'fukuoka']
    vector = get_vectors(['new-york'])
    print(vector)

    # get vectors
    # vectors_cities = get_vectors(tourist_cities_list)
    # print(vectors_cities)
    # print(len(vectors_cities))

    countries_list = ['united kingdom', 'netherlands', 'dominican republic', 'japan', 'new zealand', 'romania',
                      'malaysia', 'hungary', 'jordan', 'czech republic', 'sweden', 'argentina', 'united arab emirates',
                      'poland', 'peru', 'bulgaria', 'china', 'ghana', 'canada', 'russia', 'brazil', 'macau', 'italy',
                      'nigeria', 'mexico', 'taiwan', 'thailand', 'greece', 'singapore', 'indonesia', 'belgium',
                      'saudi arabia', 'france', 'spain', 'switzerland', 'colombia', 'lebanon', 'uruguay', 'vietnam',
                      'germany', 'egypt', 'portugal', 'turkey', 'philippines', 'south korea', 'israel', 'denmark',
                      'iran', 'india', 'morocco', 'hong kong', 'united states', 'australia', 'ecuador', 'south africa',
                      'austria', 'ireland', 'sri lanka']
    print(len(countries_list))
    countries_vectors = get_vectors(countries_list)
    # print(countries_vectors)
    save_vectors(countries_vectors, 'vectors_countries.txt')
