import re


def parse_date(date):
   # regex = re.compile(r'^(?P<day>[1-31]|0[0-9])(\/|\.|\,)(?P<month>1[0-9]|2[0-9]|3[0-1]|0[1-9]|)(\/|\.|\,)(?P<year>\d{4})$')

    regex = re.compile(r'^(?P<day>\d\d)[/.,](?P<month>\d\d)[/.,](?P<year>\d{4})$')

    matches = regex.search(date)
    if matches:
        return {
            'd': matches.group('day'), 'm': matches.group('month'), 'y': matches.group('year')
        }
    return None


a = parse_date('12/11/1988')
b = parse_date('12,11,2003')
c = parse_date('12.11.2003')
d = parse_date('12.11.184848')
print(a, b, c, d)
