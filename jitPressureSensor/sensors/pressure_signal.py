from datetime import datetime
import re

from ubiGATE.ubigate.utils.logger import logger


def matches(signal):
    """
    Analyse the inputs and write them a standard way
    """

    #Chair,2014-05-06 12:55:09.101,0,0,0,0,0,0,0,0
    logger.debug('Checking pressure for signal "%s"' % signal)

    pattern = (r'^Chair,(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})\s'
               '(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2}).'
               '(?P<msecond>\d{3}),(?P<D0>\d+),(?P<D1>\d+),(?P<D2>\d+),'
               '(?P<D3>\d+),(?P<D4>\d+),(?P<D5>\d+),(?P<D6>\d+)'
               ',(?P<D7>\d+)$\n*')
    regexp = re.compile(pattern)

    match = regexp.match(signal)

    if match:
        logger.info('Pressure detected:')

        try:
            date = datetime(datetime.now().year,
                            int(match.group('month')),
                            int(match.group('day')),
                            int(match.group('hour')),
                            int(match.group('minute')),
                            int(match.group('second')))

        except ValueError:
            logger.warn('Invalid date: %s-%s-%s %s:%s:%s, event skipped'
                        % (datetime.datetime.now().year, match.group('month'),
                           match.group('day'), match.group('hour'),
                           match.group('minute'), match.group('second')))
            return None

        logger.info('value of the sensors:\nD0:"%s", D1:"%s", D2:"%s", D3:"%s", D4:"%s", D5:"%s", D6:"%s", D7:"%s", date: "%s"' %
                    (match.group('D0'), match.group('D1'), match.group('D2'), match.group('D3'), match.group('D4'), match.group('D5'), match.group('D6'), match.group('D7'), date))

        data = {}
        data['D0'] = {'value': match.group('D0'),
                      'sensor': 'D0',
                      'date': date.strftime('%Y-%m-%d %H:%M:%S')}
        data['D1'] = {'value': match.group('D1'),
                      'sensor': 'D1',
                      'date': date.strftime('%Y-%m-%d %H:%M:%S')}
        data['D2'] = {'value': match.group('D2'),
                      'sensor': 'D2',
                      'date': date.strftime('%Y-%m-%d %H:%M:%S')}
        data['D3'] = {'value': match.group('D3'),
                      'sensor': 'D3',
                      'date': date.strftime('%Y-%m-%d %H:%M:%S')}
        data['D4'] = {'value': match.group('D4'),
                      'sensor': 'D4',
                      'date': date.strftime('%Y-%m-%d %H:%M:%S')}
        data['D5'] = {'value': match.group('D5'),
                      'sensor': 'D5',
                      'date': date.strftime('%Y-%m-%d %H:%M:%S')}
        data['D6'] = {'value': match.group('D6'),
                      'sensor': 'D6',
                      'date': date.strftime('%Y-%m-%d %H:%M:%S')}
        data['D7'] = {'value': match.group('D7'),
                      'sensor': 'D7',
                      'date': date.strftime('%Y-%m-%d %H:%M:%S')}

        return data

    return None
