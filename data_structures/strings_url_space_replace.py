"""
    URL - Write a method to replace all spaces with '%20' when given
    the length of the string
"""

import unittest


class URLSpacesTest(unittest.TestCase):

    def test_spaces_front(self, myinput='   Mr. John', mylength=11):
        result = url_spaces(myinput, mylength)
        self.assertEqual(result, 'Mr.%20John')

    def test_spaces_back(self, myinput='Mr. John    ', mylength=12):
        result = url_spaces(myinput, mylength)
        self.assertEqual(result, 'Mr.%20John')


def url_spaces_with_builtins(myinput, mylength):

    myinput = myinput.strip()
    myinput = myinput.replace(' ', '%20')

    return myinput


def url_spaces(myinput, mylength):
    new_list = []
    cur_list = list(myinput)

    start = 0
    stop = 0

    for i in cur_list:  # front
        print "test", cur_list[i]
        if cur_list[i] == ' ':
            pass
        else:
            start = i
            break

    reverse_list = reversed(cur_list)
    for i in reverse_list:  # back
        if reverse_list[i] == ' ':
            pass
        else:
            stop = mylength - i
            break

    for i in range(start, stop):  # middlex
        if cur_list[i] == ' ':
            new_list.append('%20')
        else:
            new_list.append(cur_list[i])




if __name__ == '__main__':

    unittest.main()
