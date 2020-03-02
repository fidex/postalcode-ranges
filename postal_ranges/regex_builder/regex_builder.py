# Author Fide Schuermeyer
# fs@tztt.de
#
#

import logging
# import re

Logger = logging.getLogger("test")
Logger.setLevel('DEBUG')

# this function creates a regular expression matching the range from p_low to p_high
# for postalcodes/integers of equal length


def createIntRegex(p_low, p_high):

    # make sure the numbers are of equal length
    # this is necessary for the rest of the algorithm to work properly
    # as is makes use of the position of a number.
    if len(p_high) == len(p_low):

        # eaqual part of both post codes
        eq = []
        # unequal part of both post codes
        ue = []

        # go through both post codes and bevide into equal and unequal
        for i in range(len(p_low)):
            if p_low[i] == p_high[i] and len(ue) == 0:
                eq.append(p_low[i])
            else:
                ue.append([p_low[i], p_high[i]])

        if ue and len(ue) >= 1:
            # _l is the lower number
            # _h is the hight number
            _l = ''.join([x[0] for x in ue])
            _h = ''.join([x[1] for x in ue])

            # regex string matching the lower part of the range
            _l_rg = '('
            # regex string matching the mid part of of the range
            _m_rg = ''
            # regex string matching the upper part of the range
            _h_rg = '('
            # this is necessary based on the following idea to biuld the regex
            # lets say we wanted to match 123 to 234
            # the lower part would be a regex matching the range from 123-199
            # the upper part would be a regex matching the range from 200-234
            # if the example was 123-312 we would also need a mid part matching everything from 200-299

            # if only the last digit is different
            # ex 11-13 results in /1[1-3]/
            if len(_l) == 1:
                _l_rg = '[' + str(_l)
                _h_rg = '-' + str(_h) + ']'

                rex = '^' + ''.join(eq) + '(' + _l_rg \
                    + _h_rg + ')'

                return rex

            # at least 2 unequal digits
            if len(_l) >= 2:

                # if the first digits are apart by more then one a part matching the numbers in between is needed
                if int(_h[0]) - int(_l[0]) > 1:
                    _m_rg = '([' + str(int(_l[0]) + 1) + '-' + \
                        str(int(_h[0]) - 1) + ']' + '[0-9]' + \
                        '{' + str(len(_l) - 1) + '})'

                for ii in range(len(_l) - 1, 0, -1):
                    # Logger.info(ii)
                    __l = _l[:ii]
                    _p = len(_l) - (ii + 1)

                    if _p >= 1:
                        _l_rg += '' + __l + \
                            '[' + str(int(_l[ii]) + 1) + '-9]'
                        _l_rg += '[0-9]' * _p
                    else:
                        _l_rg += '' + __l + \
                            '[' + str(_l[ii]) + '-9]'

                    Logger.info(f'lower:{_l_rg}')

                    if ii - 1 > 0:
                        _l_rg += '|'

                for ii in range(1, len(_h)):
                    # _h_rg += '[0-' + str(_h[ii]) + ']'

                    __h = _h[:ii]
                    _p = len(_l) - (ii + 1)

                    if _p >= 1:
                        upto = int(_h[ii]) - 1
                        if upto < 0:
                            upto = 0
                            _h_rg += '' + __h + \
                                '[0-' + str(upto) + ']'
                            _h_rg += ('[0-' + str(upto) + ']') * _p
                        else:
                            _h_rg += '' + __h + \
                                '[0-' + str(upto) + ']'
                            _h_rg += '[0-9]' * _p
                    else:
                        _h_rg += '' + __h + \
                            '[0-' + str(_h[ii]) + ']'
                    if ii + 1 < len(_h):
                        _h_rg += '|'
                    Logger.info(f'upper:{_h_rg}')

                # combine the different parts into one regex
                if len(_m_rg) > 1:
                    rex = '^' + ''.join(eq) + '(' + _l_rg + ')|' + \
                        _m_rg + '|' + _h_rg + '))$'
                else:
                    rex = '^' + ''.join(eq) + '(' + _l_rg + \
                        ')|' + _h_rg + '))$'
                # Logger.info(rex)
                return rex
        else:
            # both are equal
            rex = '^' + ''.join(eq) + '$'
            # Logger.info(rex)
            return rex

    else:
        raise Exception('numbers are of unequal lenght')
