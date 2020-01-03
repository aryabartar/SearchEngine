"""
Django settings for SearchEngine project.

Generated by 'django-admin startproject' using Django 2.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import math
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8$%rd8pk-48w32=x(tvfwk(xc860+wv+w9ws++!!#%na1x8l*g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'search',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SearchEngine.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SearchEngine.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR + "/static",
    '/var/www/static/',
]

# -------
# -------


"""
Django settings for SearchEngine project.

Generated by 'django-admin startproject' using Django 2.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8$%rd8pk-48w32=x(tvfwk(xc860+wv+w9ws++!!#%na1x8l*g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'search',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SearchEngine.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SearchEngine.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR + "/static",
    '/var/www/static/',
]

# -------
# -------


import csv
from .string_manipulating_functions import remove_haye, remove_ha, remove_tar, remove_shenase_fel_mazi_mozare, \
    remove_aan, remove_ye, remove_tarin, remove_shenase, manipulate_query, combination_connector

FUTURE = ['نخواهند', 'نخواهید', 'نخواهیم', 'نخواهد', 'نخواهی', 'نخواهم', 'بخواهند', 'بخواهید', 'بخواهیم', 'بخواهد',
          'بخواهی', 'بخواهم', 'خواهند', 'خواهید', 'خواهیم', 'خواهد', 'خواهی', 'خواهم']
PREFIX_MOZARE = ["می", "نمی", "ب", "ن"]
SUFFIX_MOZARE = ['م', 'ی', 'د', 'یم', 'ید', 'ند']
PAST = ['باشند', 'باشید', 'باشیم', 'باشد', 'باشی', 'باشم', 'بودند', 'بودید', 'بودیم', 'بود', 'بودی', 'بودم', 'اند',
        'اید', 'ایم', 'است', 'ای', 'ام', 'ند', 'ید', 'یم', '', 'ی', 'م']
PRESENT_ROOT = ['شو', 'کن', 'خور']
STOP_WORDS_LIST = ['از', 'با', 'را', 'و', 'ها', 'هایی', 'ترین', 'عمر', 'به', 'تر']

COMBINATIONAL_WORDS = ['عن قریب', 'من جمله', 'فی ذلک', 'مع هذا', 'علی حده', 'فی مابین', 'نیروی انتظامی جمهوری اسلامی',
                       'جمهوری اسلامی']

SYNONYM_WORDS_DICT = {'تهران': ['طهران'], 'ماشین': ['اتومبیل'], 'بلیت': ['بلیط'], 'توفان': ['طوفان'], 'زغال': ['ذغال'],
                      'پطرزبورگ': ['پترزبورگ'], 'اتاق': ['اطاق'], 'امپراتور': ['امپراطور'], 'تراز': ['طراز'],
                      'تپش': ['طپش'], 'تئاتر': ['تاتر'], 'پروفسور': ['پرفسور'], 'هیئت': ['هیات'],
                      'مسئول': ['مسوول'], 'مسئله': ['مساله'], 'لوت': ['لوط'], 'تاق': ['طاق'],
                      'اختاپوس': ['اخطاپوس'], 'اتو': ['اطو'], 'توسی': ['طوسی'], 'نیرویانتظامیجمهوریاسلامی': ['ناجا'],
                      'جمهوری اسلامی': ['ج.ا.']}

not_list = list(range(1, 1731))
posts_list = []
rows = []
all_tokens_set = set()
len_for_each_doc = list()


class Post:
    def __init__(self, id, publish_date, title, url, summary, meta_tags, content, thumbnail):
        self.id = id
        self.publish_date = publish_date
        self.title = title
        self.url = url
        self.summary = summary
        self.meta_tags = meta_tags
        self.content = content
        self.thumbnail = thumbnail
        self.content_token_list = []

    def _get_allowed_ascii_codes(self):
        PERSIAN_CHARS_START = 1570
        PERSIAN_CHARS_END = 1800

        allowed_ascii_codes_list = []
        for ascii_code in range(PERSIAN_CHARS_START, PERSIAN_CHARS_END + 1):
            allowed_ascii_codes_list.append(ascii_code)

        allowed_ascii_codes_list.append(8204)

        return allowed_ascii_codes_list

    def _get_token_from_inputs(self, user_input):
        ALLOWED_ASCII_CODES = self._get_allowed_ascii_codes()
        i = 0

        token_list = []
        while i < len(user_input):
            if ord(user_input[i]) in ALLOWED_ASCII_CODES:
                j = i
                while j < len(user_input) and ord(user_input[j]) in ALLOWED_ASCII_CODES:
                    j += 1

                token = user_input[i:j]
                token_list.append(token)
                all_tokens_set.add(token)
                i = j + 1

            else:
                i += 1

        return token_list

    def remove_plural_from_token(self):
        for i in range(0, len(self.content_token_list)):
            self.content_token_list[i] = remove_haye(self.content_token_list[i])
            self.content_token_list[i] = remove_ha(self.content_token_list[i])
            self.content_token_list[i] = remove_aan(self.content_token_list[i], all_tokens_set)
            # self.content_token_list[i] = remove_ye(self.content_token_list[i], all_tokens_set)
            self.content_token_list[i] = remove_tarin(self.content_token_list[i], all_tokens_set)
            self.content_token_list[i] = remove_tar(self.content_token_list[i], all_tokens_set)
            self.content_token_list[i] = remove_shenase(self.content_token_list[i], all_tokens_set)
            self.content_token_list[i] = remove_shenase_fel_mazi_mozare(self.content_token_list[i], all_tokens_set)

    def delete_stop_words(self):
        j = len(self.content_token_list) - 1
        i = 0
        while i <= j:
            if self.content_token_list[i] in STOP_WORDS_LIST:
                self.content_token_list.pop(i)
                i -= 1
                j -= 1
            i += 1

    def set_token_list(self):
        self.content_token_list = self._get_token_from_inputs(self.content)

    def case_folding(self):
        for item_i, item in enumerate(self.content_token_list):
            for key, value in SYNONYM_WORDS_DICT.items():
                if item in value:
                    self.content_token_list[item_i] = key

    def _concat_based_on_list(self, word_list):
        temp_array = []
        for i in range(0, len(self.content_token_list) - 1):
            if self.content_token_list[i] in word_list:
                temp_str = self.content_token_list[i] + self.content_token_list[i + 1]
                temp_array.append(temp_str)
                i += 1
            elif self.content_token_list[i - 1] not in word_list:
                temp_array.append(self.content_token_list[i])
        self.content_token_list = temp_array

    def _derive_bon_from_ayande(self, word_list):
        temp_array = []
        for i in range(0, len(self.content_token_list) - 1):
            if self.content_token_list[i] in word_list:
                temp_str = self.content_token_list[i + 1]
                temp_array.append(temp_str)
                i += 1
            else:
                temp_array.append(self.content_token_list[i])
        self.content_token_list = temp_array

    def present_verb_correction(self):
        self._concat_based_on_list(["می", "نمی"])

    def concat_nim_fasele(self):
        for i in range(0, len(self.content_token_list) - 1):
            item = self.content_token_list[i]

            if len(item) > 2:
                if item[0:2] == "می" and ord(item[2]) == 8204:
                    self.content_token_list[i] = item[0:2] + item[3:]
                    i += 1
            if len(item) > 3:
                if item[0:3] == "نمی" and ord(item[3]) == 8204:
                    self.content_token_list[i] = item[0:3] and item[4:]
                    i += 1

    def concat_ayande(self):
        self._concat_based_on_list(FUTURE)

    def derive_bon_ayande(self):
        self._derive_bon_from_ayande(FUTURE)

    def derive_bon_from_mozare(self):
        def get_bon_from_word(word):
            for prefix in PREFIX_MOZARE:

                if prefix == word[0: len(prefix)]:

                    for suffix in SUFFIX_MOZARE:

                        if suffix == word[len(word) - len(suffix):]:

                            if word[len(prefix): len(word) - len(suffix)] in PRESENT_ROOT:
                                return word[len(prefix): len(word) - len(suffix)]
            return None

        for i in range(0, len(self.content_token_list)):
            new_word = get_bon_from_word(self.content_token_list[i])
            if new_word is not None:
                self.content_token_list[i] = new_word

    def __repr__(self):
        return str(self.title)

    def __str__(self):
        return "Title: " + str(self.title) + " | Number: " + str(self.id)


def save_xlx_to_csv(xlx_address, csv_address):
    import pandas as pd
    data_xls = pd.read_excel(xlx_address, index_col=None)
    data_xls.to_csv(csv_address, encoding='utf-8', index=False)


def create_post_objects(csv_path):
    posts_list = []

    with open(csv_path, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rows = list(csv_reader)
        id = 1

        for row in rows[1:]:
            post_obj = Post(id, *row)
            post_obj.set_token_list()
            posts_list.append(post_obj)
            id += 1

        for post_obj in posts_list:
            post_obj.remove_plural_from_token()
            post_obj.case_folding()
            combination_connector(post_obj.content_token_list, COMBINATIONAL_WORDS)
            post_obj.present_verb_correction()
            post_obj.concat_nim_fasele()
            # post_obj.concat_ayande()
            post_obj.derive_bon_ayande()
            post_obj.delete_stop_words()
            post_obj.derive_bon_from_mozare()
            len_for_each_doc.append(post_obj.content_token_list.__len__())
            # print(post_obj.content_token_list.__len__())

    return posts_list


def parse_input(user_input):
    def find_double_quotation(string):
        i = 0
        first_list = []

        while i < len(string):
            if string[i] == '"':
                j = i + 1
                while string[j] != '"':
                    j += 1

                first_list.append(string[i + 1:j])
                string = string[0:i] + user_input[j + 1:]
            i += 1

        return string, first_list

    def find_not(string):
        second_list = []

        i = 0
        while i < len(string):
            if string[i] == "!" and string[i + 1] != '"':
                j = i + 1
                while j < len(string) and string[j] != " ":
                    j += 1
                second_list.append(string[i + 1: j])
                string = string[0:i] + string[j:]

            elif string[i] == "!" and string[i + 1] == '"':
                i = i + 2
                start_loc = i
                while string[i] != '"':
                    i += 1
                second_list.append(string[start_loc:i])
                string = string[0:start_loc - 2] + string[i + 1:]
                i = start_loc - 2
            i += 1

        return string, second_list

    def find_other_words(string):
        parsed_string = string.split(" ")
        new_parsed_string = []

        for item in parsed_string:
            if item != '':
                new_parsed_string.append(item)

        return new_parsed_string

    def cat_and_source_finder(user_input):
        SOURCE_STR = "source:"
        CAT_STR = "cat:"

        user_input_array = user_input.split(" ")

        cat_value = None
        if CAT_STR in user_input:
            cat_id = user_input_array.index(CAT_STR)
            cat_value = user_input_array[cat_id + 1]
            user_input_array.remove(CAT_STR)
            user_input_array.remove(cat_value)

        source_value = None
        if SOURCE_STR in user_input:
            source_id = user_input_array.index(SOURCE_STR)
            source_value = user_input_array[source_id + 1]
            user_input_array.remove(SOURCE_STR)
            user_input_array.remove(source_value)

        changed_user_input = ""
        for item in user_input_array:
            changed_user_input = changed_user_input + " " + item

        return changed_user_input, source_value, cat_value

    user_input, second_list = find_not(user_input)
    user_input, first_list = find_double_quotation(user_input)
    user_input, source_value, cat_value = cat_and_source_finder(user_input)
    third_list = find_other_words(user_input)

    dict = {
        "with_quotation": first_list,
        "with_exclamation_mark": second_list,
        "source_value": source_value,
        "cat_value": cat_value,
        "others": third_list,
    }

    return dict


def create_data_dict(posts_list):
    for post in posts_list:
        content_token_list = post.content_token_list
        for word_index, word in enumerate(content_token_list):
            word_in_data_dict_value = DATA_DICT.get(word, None)
            # agar word vojod dasht
            if word_in_data_dict_value is not None:
                # shomare post ro migereft (shomare news)
                word_position_array = word_in_data_dict_value.get(post.id, None)
                # age bud be tahesh ezafe mikard
                if word_position_array is None:
                    DATA_DICT[word][post.id] = [word_index]
                    # age nabod misazatesh
                else:
                    DATA_DICT[word][post.id].append(word_index)
            # age WORD nabod bia besazesh
            else:
                DATA_DICT[word] = {post.id: [word_index]}


# def create_vector():
#     for post in posts_list:
#         content_token_list = post.content_token_list
#
#         for word_index, word in enumerate(content_token_list):
#             word_in_data_dict_value = DATA_DICT.get(word, None)
#             # agar word vojod dasht
#             if word_in_data_dict_value is not None:
#                 # shomare post ro migereft (shomare news)
#                 word_position_array = word_in_data_dict_value.get(post.id, None)
#                 print("WWWW")
#                 print(word_position_array.len)
#                 print("aaaaa")
#                 # age bud be tahesh ezafe mikard
#                 if word_position_array is None:
#                     DATA_DICT[word][post.id] = [word_index]
#                     # age nabod misazatesh
#                 else:
#                     DATA_DICT[word][post.id].append(word_index)
#             # age WORD nabod bia besazesh


def search_in_dict_one_word(word):
    global DATA_DICT
    data_row = [k for k in DATA_DICT.get(word, [])]
    return data_row


def search_in_not_dict(word):
    global DATA_DICT

    if len(word.split(" ")) > 1:
        list_keys = search_in_dict_statement(word)
    else:
        list_keys = search_in_dict_one_word(word)
    list_not = set(not_list) - set(list_keys)
    return list_not


def print_posts_list(posts_list):
    for post in posts_list:
        print(post.content_token_list)


def search_in_dict_statement(statement):
    global DATA_DICT

    word_list = statement.split(" ")

    if len(word_list) < 2:
        raise ValueError('Statement contains less than 2 numbers')

    for word in word_list:
        if DATA_DICT.get(word, None) is None:
            return None

    common_posts = list(DATA_DICT.get(word_list[0], None).keys())

    for word in word_list:
        word_positions = DATA_DICT.get(word, None)

        if word_positions is None:
            common_posts = []

        i = 0
        while i < len(common_posts):

            for w in word_list[1:]:

                if common_posts[i] not in DATA_DICT[w].keys():
                    common_posts.pop(i)
                    i -= 1
                    break
            i += 1

    # Here we know that every post in common_posts contains all statement
    # words.

    result = []

    for post_num in common_posts:
        word_position_pointers = DATA_DICT[word_list[0]][post_num]

        for i in word_position_pointers:
            found = True

            for word in word_list[1:]:
                i += 1

                if i not in DATA_DICT[word][post_num]:
                    found = False
                    break

            if found:
                result.append(post_num)
    return result


def get_input(u_input):
    flag1 = 0
    flag2 = 0
    flag3 = 0
    print(u_input)
    for item in FUTURE:
        if u_input.__contains__(item):
            u_input = u_input.replace(item, '')

    for bon in PRESENT_ROOT:
        if u_input.__contains__(bon):
            result = u_input.find(bon)
            if u_input[result - 3:result] == "نمی":
                if u_input[result + bon.__len__()] == "م":
                    temp = u_input[result - 3: result + bon.__len__() + 1]
                elif u_input[result + bon.__len__()] == "ی":
                    temp = u_input[result - 3: result + bon.__len__() + 1]
                elif u_input[result + bon.__len__()] == "د":
                    temp = u_input[result - 3: result + bon.__len__() + 1]
                elif u_input[result + bon.__len__():result + bon.__len__() + 1] == "یم":
                    temp = u_input[result - 3: result + bon.__len__() + 2]
                elif u_input[result + bon.__len__():result + bon.__len__() + 1] == "ید":
                    temp = u_input[result - 3: result + bon.__len__() + 2]
                elif u_input[result + bon.__len__():result + bon.__len__() + 1] == "ند":
                    temp = u_input[result - 3: result + bon.__len__() + 2]
                u_input = u_input.replace(temp, bon)

    for bon in PRESENT_ROOT:
        if u_input.__contains__(bon):
            result = u_input.find(bon)
            if u_input[result - 2:result] == "می":
                if u_input[result + bon.__len__()] == "م":
                    temp = u_input[result - 2: result + bon.__len__() + 1]
                elif u_input[result + bon.__len__()] == "ی":
                    temp = u_input[result - 2: result + bon.__len__() + 1]
                elif u_input[result + bon.__len__()] == "د":
                    temp = u_input[result - 2: result + bon.__len__() + 1]
                elif u_input[result + bon.__len__():result + bon.__len__() + 1] == "یم":
                    temp = u_input[result - 2: result + bon.__len__() + 2]
                elif u_input[result + bon.__len__():result + bon.__len__() + 1] == "ید":
                    temp = u_input[result - 2: result + bon.__len__() + 2]
                elif u_input[result + bon.__len__():result + bon.__len__() + 1] == "ند":
                    temp = u_input[result - 2: result + bon.__len__() + 2]
                u_input = u_input.replace(temp, bon)

    for bon in PRESENT_ROOT:
        if u_input.__contains__(bon):
            result = u_input.find(bon)
            if u_input[result - 1] == "ب" or u_input[result - 1] == "ن":
                if u_input[result + bon.__len__()] == "م":
                    temp = u_input[result - 1: result + bon.__len__() + 1]
                elif u_input[result + bon.__len__()] == "ی":
                    temp = u_input[result - 1: result + bon.__len__() + 1]
                elif u_input[result + bon.__len__()] == "د":
                    temp = u_input[result - 1: result + bon.__len__() + 1]
                elif u_input[result + bon.__len__():result + bon.__len__() + 1] == "یم":
                    temp = u_input[result - 1: result + bon.__len__() + 2]
                elif u_input[result + bon.__len__():result + bon.__len__() + 1] == "ید":
                    temp = u_input[result - 1: result + bon.__len__() + 2]
                elif u_input[result + bon.__len__():result + bon.__len__() + 1] == "ند":
                    temp = u_input[result - 1: result + bon.__len__() + 2]
                u_input = u_input.replace(temp, bon)

    u_input = manipulate_query(u_input, all_tokens_set, COMBINATIONAL_WORDS)

    for key, value in SYNONYM_WORDS_DICT.items():
        if u_input.__contains__(''.join(value)):
            u_input = u_input.replace(''.join(value), key)

    result_dict = parse_input(u_input)
    first_list = result_dict.get("with_quotation", None)
    second_list = result_dict.get("with_exclamation_mark", None)
    source_value = result_dict.get("source_value", None)
    cat_value = result_dict.get("cat_value", None)
    third_list = result_dict.get("others", None)

    first_list = list(first_list)
    second_list = list(second_list)
    third_list = list(third_list)

    if first_list.__len__() == 0 and second_list.__len__() != 0 and third_list.__len__() != 0:
        flag3 = 1
    if first_list.__len__() == 0 and second_list.__len__() == 0 and third_list.__len__() != 0:
        flag3 = 1
        flag2 = 1
    if first_list.__len__() == 0 and second_list.__len__() != 0 and third_list.__len__() == 0:
        flag3 = 1
        flag1 = 1
    if first_list.__len__() == 0 and second_list.__len__() == 0 and third_list.__len__() == 0:
        flag3 = 1
        flag2 = 1
        flag1 = 1
    if first_list.__len__() != 0 and second_list.__len__() == 0 and third_list.__len__() != 0:
        flag2 = 1
    if first_list.__len__() != 0 and second_list.__len__() != 0 and third_list.__len__() == 0:
        flag1 = 1
    if first_list.__len__() != 0 and second_list.__len__() == 0 and third_list.__len__() == 0:
        flag1 = 1
        flag2 = 1
    temp = []
    temp2 = []
    temp3 = []
    final_not = []
    final_statement = []
    final_one = []
    count = 0
    for i in third_list:
        count = count + 1
        if count == 1:
            final_one = search_in_dict_one_word(i)
            continue
        else:
            temp.extend(list(set(search_in_dict_one_word(i)).intersection(set(final_one))))
            final_one = temp
            temp = []
    final_one = list(dict.fromkeys(final_one))

    count = 0
    for i in second_list:
        count = count + 1

        if count == 1:
            final_not = search_in_not_dict(i)
            continue
        else:
            temp2.extend(list(set(search_in_not_dict(i)).intersection(set(final_not))))
            final_one = temp2
            temp2 = []
    final_not = list(dict.fromkeys(final_not))

    count = 0
    for i in first_list:
        count = count + 1
        if count == 1:
            final_statement = search_in_dict_statement(i)
            continue
        else:
            temp3.extend(list(set(search_in_dict_statement(i)).intersection(set(final_statement))))
            final_statement = temp3
            temp3 = []

    if final_statement is None:
        final_statement = []
    final_statement = list(final_statement)

    if flag1 == 1 and flag2 == 0 and flag3 == 0:
        my_result = set(final_not).intersection(set(final_statement))
    elif flag1 == 1 and flag2 == 1 and flag3 == 0:
        my_result = set(final_statement)
    elif flag1 == 1 and flag2 == 0 and flag3 == 1:
        my_result = set(final_not)
    elif flag1 == 1 and flag2 == 1 and flag3 == 1:
        my_result = []
    elif flag1 == 0 and flag2 == 0 and flag3 == 1:
        my_result = set(final_one).intersection(set(final_not))
    elif flag1 == 0 and flag2 == 1 and flag3 == 0:
        my_result = set(final_one).intersection(set(final_statement))
    elif flag1 == 0 and flag2 == 1 and flag3 == 1:
        my_result = set(final_one)
    elif flag1 == 0 and flag2 == 0 and flag3 == 0:
        my_result = set(final_one).intersection(set(final_not), set(final_statement))

    result_list = []
    for item in my_result:
        post = posts_list[item - 1]
        result_list.append([post.title, post.thumbnail, post.summary, post.id, post.publish_date, post.url])

    return result_list


print("PROCESSING DATA, please wait.")

XLX_PATH = 'data/input.xlsx'
CSV_PATH = 'data/input.csv'

# save_xlx_to_csv(XLX_PATH, CSV_PATH)
posts_list = create_post_objects(CSV_PATH)
# print(len_for_each_doc)

DATA_DICT = {}
# print(sum(len_for_each_doc))
create_data_dict(posts_list)


def get_lengths(dict, token):
    return len(dict.get(token, {}).keys())


def get_len_char(dict, token, docid):
    key = dict.get(token, {})
    result = key.get(docid, [])
    return len(result)


def calculate():
    ROW_NUM = len(posts_list)
    COL_NUM = len(DATA_DICT.keys())

    result = [None] * (ROW_NUM + 1)
    for i in range(0, ROW_NUM + 1):
        result[i] = [None] * COL_NUM

    for i, key in enumerate(DATA_DICT.keys()):
        for j in range(0, ROW_NUM + 1):
            len_char = get_len_char(DATA_DICT, key, j)
            length = get_lengths(DATA_DICT, key)

            w = (math.log10(1 + len_char)) * (
                math.log10(len(posts_list) / length))

            result[j][i] = w
    return result


final = calculate()
print(len(DATA_DICT.keys()))
print(final[0])
