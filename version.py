
class Version:
    def __init__(self, version_str: str, ignore_trailing_zero: bool=False):
        self.version = list(int(i) for i in version_str.split('.'))
        self.ignore_trailing_zero = ignore_trailing_zero
    def __sub__(self, other):
        for i in range(min(len(self.version), len(other.version))):
            if self.version[i] > other.version[i]:
                return 1
            elif self.version[i] < other.version[i]:
                return -1
        if not self.ignore_trailing_zero:
            if len(self.version) > len(other.version):
                return 1
            elif len(self.version) < len(other.version):
                return -1
            else:
                return 0
        else:
            if len(self.version) > len(other.version):
                return next((i for i in self.version[len(other.version):] if i != 0), 0)
            elif len(self.version) < len(other.version):
                return - next((i for i in other.version[len(self.version):] if i != 0), 0)
            else:
                return 0
    def __eq__(self, other):
        return self - other == 0
    def __ne__(self, other):
        return self - other != 0
    def __le__(self, other):
        return self - other <= 0
    def __ge__(self, other):
        return self - other >= 0
    def __gt__(self, other):
        return self - other > 0
    def __lt__(self, other):
        return self - other < 0

__all__ = ['Version']
if __name__ == '__main__':
    print(sorted([
        '6.2.7',
        '6.2.5',
        '5.3',
        '6.2.2',
        '6.2',
        '6.2.0',
        '6.2',
        '6.2.1',
        '5.2',
        '6.2.8',
    ], key=lambda v: Version(v, ignore_trailing_zero=True)))