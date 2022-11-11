# TODO решить с помощью list comprehension и распечатать его

import pprint
pprint.pprint([{'bin': bin(n), 'dec': n, 'hex': hex(n), 'oct': oct(n)} for n in range(16)])